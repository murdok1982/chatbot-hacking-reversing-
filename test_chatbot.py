import pytest
from unittest.mock import patch
from src.chatbot.llm_chain import create_chain

@patch('langchain_ollama.OllamaLLM')
def test_chain_creation(mock_llm):
    chain = create_chain()
    assert chain is not None
