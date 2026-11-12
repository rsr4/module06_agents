# mock_model.py
# Author: Rahim Rozani


class MockModel:
    """It's a stand in model for the AI model, it gives the same simple replies everytime."""

    def reply(self, instructions, history):
        """Return a fixed reply based on the last message in the history."""
        last_message = history[-1]["content"].lower()
        if "hello" in last_message:
            return "Hello how can I help you!"
        return "I'm not sure how to help with that. I can check an order or a stock for you."
