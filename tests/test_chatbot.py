from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup


def make_bot():
    """Build a fresh chatbot with its own tool for each test"""
    orders = {"A100": "shipped", "A101": "processing"}
    stock_tool = StockLookup({"rain jacket": 12, "day pack": 0})
    return SupportChatbot("Sunny", "Be friendly", OrderLookup(orders), stock_tool)


def test_finds_known_status():
    tool = OrderLookup({"A100": "shipped", "A101": "processing"})
    assert tool.find_status("A100") == "shipped"


def test_tool_returns_none_for_unknown_order():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_order_id("Where is order A999") == None


def test_respond_records_both_messages():
    bot = make_bot()
    bot.respond("Hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_order_question_uses_tool():
    bot = make_bot()
    assert bot.respond("Where is order A100") == "Order A100 is shipped"


def test_order_question_without_id_asks_for_one():
    bot = make_bot()
    assert "order ID" in bot.respond("Where is my order")


def test_address_change_goes_to_human():
    bot = make_bot()
    assert "human" in bot.respond("I want to change my shipping address")


def test_unknown_request_gets_a_safe_reply():
    bot = make_bot()
    assert "not sure" in bot.respond("What is the weather today")


def test_two_chat_bots_get_two_seperate_histories():
    first = make_bot()
    second = make_bot()
    first.respond("Hello")
    assert len(first.history) == 2
    assert len(second.history) == 0


def test_count_user_message():
    bot = make_bot()
    bot.respond("hello")
    bot.respond("where is order A100?")
    assert bot.count_user_messages() == 2


def test_stock_question_uses_stock_tool():
    bot = make_bot()
    assert "12" in bot.respond("Is the rain jacket in stock?")
