import openai
from django.conf import settings

from .tools import (
    get_upcoming_events,
    book_ticket,
    get_user_bookings,
    cancel_booking, get_event_details, cancel_booking_by_event_and_seat,
)

openai.api_key = settings.OPENAI_API_KEY

FUNCTION_MAP = {
    "get_upcoming_events": get_upcoming_events,
    "book_ticket": book_ticket,
    "get_user_bookings": get_user_bookings,
    "cancel_booking": cancel_booking,
    "get_event_details": get_event_details,
    "cancel_booking_by_event_and_seat": cancel_booking_by_event_and_seat,
}


def call_ai_agent(messages: str, user_id: int) -> str:
    thread = openai.beta.threads.create(messages=messages)

    run = openai.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=settings.OPENAI_ASSISTANT_ID,
        tool_choice="auto",
        metadata={"user_id": str(user_id)},
    )

    while run.status not in ["completed", "requires_action"]:
        run = openai.beta.threads.runs.retrieve(run.id, thread_id=thread.id)

    if run.status == "requires_action":
        tool_outputs = []

        for call in run.required_action.submit_tool_outputs.tool_calls:
            name = call.function.name
            arguments = call.function.arguments
            fn = FUNCTION_MAP.get(name)

            if fn:
                try:
                    import json
                    args = json.loads(arguments)
                    result = fn(user_id=user_id, **args)
                except Exception as e:
                    result = f"❌ Error executing function {name}: {e}"
            else:
                result = f"❌ Function {name} not found."

            tool_outputs.append({
                "tool_call_id": call.id,
                "output": str(result),
            })

        run = openai.beta.threads.runs.submit_tool_outputs(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs,
        )

        while run.status != "completed":
            run = openai.beta.threads.runs.retrieve(
                run.id,
                thread_id=thread.id
            )

    result = openai.beta.threads.messages.list(thread_id=thread.id)
    latest = result.data[0].content[0].text.value
    return latest
