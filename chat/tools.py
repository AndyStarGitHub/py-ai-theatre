from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from booking.models import Event, Booking
from django.utils.timezone import now

from constants import VALID_ROWS, VALID_SEATS


def get_upcoming_events() -> list[str]:
    events = Event.objects.filter(date__gte=now()).order_by("date")[:20]
    return [
        f"{e.id}: {e.title} ({e.date.strftime('%Y-%m-%d')})"
        for e in events
    ]


def cancel_booking(booking_id: int, user_id: int = None) -> str:
    qs = Booking.objects.filter(id=booking_id, user_id=user_id)
    if not qs.exists():
        return "⚠️ Booking not found."
    qs.delete()
    return "✅ Booking canceled."


def get_event_details(event_id: int) -> str:
    from booking.models import Event

    try:
        event = Event.objects.get(id=event_id)
        return (
            f"{event.title} ({event.date.strftime('%Y-%m-%d')})\n"
            f"Author: {event.author}\n"
            f"Actors: {event.actors}"
        )
    except Event.DoesNotExist:
        return "🚫 Event not found."


def book_ticket(user_id: int, event_name: str, seat: str) -> str:

    print(f"👉 Booking request: user_id={user_id}, "
          f"event_name={event_name}, seat={seat}")

    try:
        event = Event.objects.filter(
            title__iexact=event_name,
            date__gte=now()).order_by('date').first()
        if not event:
            return (f"❌ Event with name '{event_name}' not "
                    f"found or already took place.")

        try:
            row_str, letter = seat.split('-')
            row = int(row_str)
        except ValueError:
            return ("❌ Incorrect seat format. "
                    "Please use format 'row-seat', "
                    "e.g. '12-A'.")

        if row not in VALID_ROWS or letter not in VALID_SEATS:
            return ("❌ The seat doesn't exist. "
                    "Correct rows: 1–20, seats: A–Q.")

        if Booking.objects.filter(event=event, seat=seat).exists():
            return (f"❌ Seat {seat} for the "
                    f"event '{event.title}' has been "
                    f"booked already.")

        User = get_user_model()
        user = User.objects.get(id=user_id)

        Booking.objects.create(event=event, user=user, seat=seat)
        return (f"✅ The seat {seat} successfully "
                f"booked for the event '{event.title}' ({event.date})")

    except ObjectDoesNotExist:
        return "❌ User not found."

    except Exception as e:
        print(f"[ERROR in book_ticket] {e}")
        raise

        return (f"❌ Unpredicted error while ticket "
                f"booking: {str(e)}")


def get_user_bookings(user_id: int) -> str:
    bookings = (Booking.objects.
                filter(user_id=user_id).
                select_related("event").
                order_by("event__date")
                )

    if not bookings.exists():
        return "You haven't any active bookings."

    response = "Your bookings:\n"
    for booking in bookings:
        response += (f"🎭 {booking.event.title} "
                     f"({booking.event.date}) – seat {booking.seat}\n")

    return response


def cancel_booking_by_event_and_seat(
        user_id: int,
        event_title: str,
        seat: str
        ) -> str:
    try:
        event = Event.objects.get(title__iexact=event_title)
    except Event.DoesNotExist:
        return (f"❌ Event with the title '{event_title}' "
                f"not found.")

    try:
        booking = Booking.objects.get(
            user_id=user_id,
            event=event,
            seat=seat)
        booking_id = booking.id
        booking.delete()
        return (f"✅ Booking {event_title}, seat {seat} "
                f"(ID {booking_id}) cancelled.")
    except Booking.DoesNotExist:
        return (f"❌ You don't have a booking for the event "
                f"with title {event_title}, seat {seat}.")
