# appointment_tool.py
# Author: Rahim Rozani


class ConsultationBook:
    """A tool that knows which appointment times are open"""

    def __init__(self, open_times):
        """Store the open appointment times this tool can look up."""
        self.open_times = open_times

    def find_day(self, text):
        """Return the first known day in text, or None."""
        for day in self.open_times:
            if day in text.lower():
                return day
        return None

    def times_for(self, day):
        """Return open times for one day, or None if the day is unknown."""
        if day in self.open_times:
            return self.open_times[day]
        return None
