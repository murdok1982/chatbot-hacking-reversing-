from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from .config import OLLAMA_MODEL, TEMPERATURE, PROMPT_SYSTEM

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def create_chain():
    llm = OllamaLLM(model=OLLAMA_MODEL, temperature=TEMPERATURE, num_predict=512)

    prompt = ChatPromptTemplate.from_messages([
        ("system", PROMPT_SYSTEM),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])

    chain = prompt | llm

    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )

    return chain_with_history
