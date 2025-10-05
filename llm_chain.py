from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from .config import OLLAMA_MODEL, TEMPERATURE, PROMPT_SYSTEM

def create_chain():
    llm = OllamaLLM(model=OLLAMA_MODEL, temperature=TEMPERATURE, num_predict=512)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", PROMPT_SYSTEM),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
    
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    return LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)
