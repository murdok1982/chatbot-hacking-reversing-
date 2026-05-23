from . import hispan_shield_guardian  # noqa: F401
from .llm_chain import create_chain
from .utils import validate_input, logger
from .modes.recon import recon_mode
from .modes.exploit_dev import exploit_dev_mode

MODES = {
    "chat": "Modo conversación general (por defecto)",
    "recon": "Modo reconocimiento — escanea puertos, enumera subdominios",
    "exploit": "Modo desarrollo de exploits — genera payloads y analiza vulnerabilidades",
}

SESSION_ID = "h4ckbot-default"

def chat_loop():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   H4CK-BOT — Asistente de Hacking Ético & RE           ║")
    print("║   LLM local · Ollama · Siempre legal y educativo        ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    print("Comandos especiales:")
    for cmd, desc in MODES.items():
        print(f"  /{cmd}  -> {desc}")
    print("  /tools -> Lista herramientas integradas")
    print("  /help  -> Ayuda rapida")
    print("  salir  -> Terminar")
    print()

    mode = "chat"
    chain = create_chain()

    while True:
        user_input = input(f"[{mode}] Tu: ").strip()
        if user_input.lower() == 'salir':
            print("Adios! Recuerda: usa el conocimiento eticamente.")
            break

        if user_input.lower().startswith('/'):
            cmd = user_input[1:].lower()
            if cmd in MODES:
                mode = cmd
                print(f"Modo '{cmd}' activado.")
                if cmd == "recon":
                    recon_mode(chain)
                elif cmd == "exploit":
                    exploit_dev_mode(chain)
                continue
            elif cmd == "tools":
                print("Herramientas integradas:")
                print("  - nmap <target> <puertos>  : Escanea puertos via Nmap")
                print("  - encode <tipo> <texto>    : Codifica payload (base64|hex|url)")
                print("  - decode <tipo> <texto>    : Decodifica payload")
                print("  - cve <termino>            : Busca CVEs relacionados")
                continue
            elif cmd == "help":
                print("Comandos: /chat, /recon, /exploit, /tools, /help, salir")
                continue
            else:
                print(f"Comando desconocido: /{cmd}. Usa /help")
                continue

        if not validate_input(user_input):
            print("Input demasiado largo (max 1000 chars). Intenta de nuevo.")
            continue

        response = chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": SESSION_ID}}
        )
        print(f"Bot: {response}\n")
        logger.info(f"User: {user_input[:50]}... | Bot responded.")

if __name__ == "__main__":
    chat_loop()
