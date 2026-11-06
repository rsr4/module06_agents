# my_assistant.py
# Authoer: Rahim Rozani

HANDOFF_WORDS = ["book", "cancel", "reschedule"]


class AppointmentHelper:
    """A mock appointment helper, its replies come from simple rules not AI."""

    def __init__(self, name, instructions, consultation_book):
        """Set up one helper with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.consultation_book = consultation_book
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keywords rules, this is the mock part."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't change the schedule. Im passing you to the front desk"
        if "open" in text or "available" in text:
            return self.time_reply(user_message)
        if "hello" in text:
            return f"Hello! Im {self.name}. Ask me which times are open for the day."
        return "I'm not sure how to help with that. I can list open times."

    def needs_human(self, text):
        """Return True if the message asks to change the schedule."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def time_reply(self, user_message):
        """Use the appointment book to answer a question about open times."""
        day = self.consultation_book.find_day(user_message)
        if day is None:
            return "Which day? I can check Monday, Wednesday, or Friday."
        times = self.consultation_book.times_for(day)
        return f"Open times on {day}: {times}."
