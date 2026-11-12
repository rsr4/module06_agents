# appointment_main.py
# Author: Rahim Rozani

from my_assistant import AppointmentHelper
from my_tool import ConsultationBook
from ollama_model import OllamaModel

OPEN_TIMES = {
    "monday": "9:00 am and 2:30 pm",
    "wednesday": "11:00 am",
    "friday": "none",
}

INSTRUCTIONS = """You are Timmy, consultation helper for Bayside Hospital.
Asnwer in one short sentence.
The hospital is at 40 Harbor Street, patient parking at the front.
Bring your ID and other health records related to the consultation.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the patient to the front desk."""


consultation_book = ConsultationBook(OPEN_TIMES)
model = OllamaModel("granite4.1:3b")
helper = AppointmentHelper(
    "Timmy",
    "You help patients of Bayside Hospital find consultation timings",
    consultation_book,
    model,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")
