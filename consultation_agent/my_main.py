# appointment_main.py
# Author: Rahim Rozani

from my_assistant import AppointmentHelper
from my_tool import ConsultationBook

OPEN_TIMES = {
    "monday": "9:00 am and 2:30 pm",
    "wednesday": "11:00 am",
    "friday": "none",
}

consultation_book = ConsultationBook(OPEN_TIMES)
helper = AppointmentHelper(
    "Timmy",
    "You help patients of Bayside Hospital find consultation timings",
    consultation_book,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")
