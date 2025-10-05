from .llm_chain import create_chain
from .utils import validate_input, logger

def chat_loop():
    print("¡Bienvenido al Chatbot Local Experto en Hacking y Reversing!")
    print("Ejecutando con LLM local (Ollama). Escribe 'salir' para terminar.\n")
    
    chain = create_chain()
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            print("¡Adiós! Recuerda: usa el conocimiento éticamente.")
            break
        
        if not validate_input(user_input):
            print("Input demasiado largo. Intenta de nuevo.")
            continue
        
        response = chain.invoke({"input": user_input})
        print(f"Bot: {response['text']}\n")
        logger.info(f"User: {user_input[:50]}... | Bot responded.")

if __name__ == "__main__":
    chat_loop()
