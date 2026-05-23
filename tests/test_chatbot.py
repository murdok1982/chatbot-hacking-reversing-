import pytest
from unittest.mock import patch, MagicMock

def test_chain_creation():
    with patch('src.chatbot.llm_chain.OllamaLLM') as mock:
        mock.return_value = MagicMock()
        from src.chatbot.llm_chain import create_chain
        chain = create_chain()
        assert chain is not None

def test_chain_has_invoke():
    with patch('src.chatbot.llm_chain.OllamaLLM') as mock:
        mock.return_value = MagicMock()
        from src.chatbot.llm_chain import create_chain
        chain = create_chain()
        assert hasattr(chain, 'invoke')
