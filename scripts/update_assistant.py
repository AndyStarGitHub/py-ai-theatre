import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

assistant_id = os.getenv("OPENAI_ASSISTANT_ID")

updated_tools = [
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
            "description": "Book a seat for a specific event",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_name": {"type": "string"},
                    "seat": {"type": "string"},
                },
                "required": ["event_name", "seat"]
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_user_bookings",
            "description": "Get user's bookings",
            "parameters": {},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_booking",
            "description": "Cancel a booking",
            "parameters": {
                "type": "object",
                "properties": {
                    "booking_id": {"type": "integer"},
                },
                "required": ["booking_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_event_details",
            "description": "Get details of a specific event including actors",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_id": {"type": "integer"},
                },
                "required": ["event_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_booking_by_event_and_seat",
            "description": "Cancel booking by event title and seat",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_title": {"type": "string"},
                    "seat": {"type": "string"},
                },
                "required": ["event_title", "seat"]
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_event_author",
            "description": "Get author of the play by title",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                },
                "required": ["title"]
            }
        }
    },
]

response = openai.beta.assistants.update(
    assistant_id=assistant_id,
    tools=updated_tools,
)

print("✅ Assistant updated:")
print(f"Name: {response.name}")
print(f"Tools: {[tool.function.name for tool in response.tools]}")
