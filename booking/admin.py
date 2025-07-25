from django.contrib import admin

from booking.models import Event, Booking


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author', 'actors')
    list_filter = ('date',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'seat', 'created_at')
    search_fields = ('user__username', 'event__title', 'seat')
    list_filter = ('event', 'created_at')
