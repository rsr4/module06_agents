from consultation_agent.my_assistant import AppointmentHelper
from consultation_agent.my_tool import ConsultationBook
from mock_model import MockModel


class SlientModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_helper():
    """Build a new helper everytime a test is ran with its own history and data"""
    book = ConsultationBook({"monday": "9:00 am and 2:30 pm", "friday": "none"})
    return AppointmentHelper("Timmy", "Be informative", book, MockModel())


def test_open_times_question_uses_the_tool():
    helper = make_helper()
    reply = helper.respond("What are the open times on Monday?")
    assert reply == "Open times on monday: 9:00 am and 2:30 pm."


def test_question_without_a_known_day_asks_for_one():
    helper = make_helper()
    assert "Which day?" in helper.respond("What times are open on Sunday?")


def test_booking_request_goes_to_a_human():
    helper = make_helper()
    assert "front desk" in helper.respond("PLease book me for Monday at 9")


def test_unkown_request_gets_a_safe_reply():
    helper = make_helper()
    assert "not sure" in helper.respond("What is your favorite day?")


def test_list_available_days_when_asked():
    helper = make_helper()
    assert "Which day" in helper.respond("Which days are open?")


def test_history_grows_by_two_each_time():
    helper = make_helper()
    helper.respond("Hello")
    helper.respond("Which days are open?")
    helper.respond("what is open for Monday?")
    assert len(helper.history) == 6


def test_unkown_request_gets_safe_reply():
    book = ConsultationBook({"monday": "9:00 am and 2:30 pm"})
    helper = AppointmentHelper("Timmy", "Be Clear", book, SlientModel())
    assert "try again" in helper.respond("What is your favorite color?")


def test_other_messages_go_to_the_model():
    helper = make_helper()
    assert helper.respond("hello") == "Hello how can I help you today?"
