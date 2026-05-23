import pytest

def test_validate_input():
    from src.chatbot.utils import validate_input
    assert validate_input("test corto") == True
    assert validate_input("x" * 1001) == False
    assert validate_input("x" * 1000) == True

def test_logger():
    from src.chatbot.utils import logger
    assert logger is not None
    assert logger.name == "src.chatbot.utils"
