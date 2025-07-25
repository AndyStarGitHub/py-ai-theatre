import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are a theatre AI assistant. Help users view upcoming
shows, book seats, see and cancel bookings.
Only use tools provided. Do not make up anything.
"""

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_upcoming_events",
            "description": "Get upcoming events",
            "parameters": {},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "book_ticket",
            "description": "Book ticket",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_id": {"type": "integer"},
                    "seat": {"type": "string"},
                },
                "required": ["event_id", "seat"]
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_user_bookings",
            "description": "List all bookings of user",
            "parameters": {},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_booking",
            "description": "Cancel specific booking",
            "parameters": {
                "type": "object",
                "properties": {
                    "booking_id": {"type": "integer"},
                },
                "required": ["booking_id"]
            },
        },
    },
]

assistant = openai.beta.assistants.create(
    instructions=SYSTEM_PROMPT,
    model="gpt-4.1-mini",
    tools=tools,
)

print("✅ Assistant created!")
print("Assistant ID:", assistant.id)
