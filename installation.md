## Instalación completa

### 1. Prerequisitos

| Paquete | Instalación |
|---|---|
| **Python 3.8+** | [python.org/downloads](https://python.org/downloads) |
| **Ollama** | [ollama.com/download](https://ollama.com/download) |
| **Nmap** (opcional) | [nmap.org/download](https://nmap.org/download) — para escaneos |

### 2. Clonar

```bash
git clone https://github.com/murdok1982/chatbot-hacking-reversing-.git
cd chatbot-hacking-reversing-
```

### 3. Descargar modelo LLM

```bash
ollama pull llama3.1
```

También puedes usar `codellama` (especializado en código) o `llama3.2` (más ligero).

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

O instalar como paquete editable:

```bash
pip install -e .
```

### 5. Configurar entorno

```bash
cp .env.example .env
# Edita .env si quieres cambiar modelo o temperatura
```

### 6. Ejecutar

```bash
python run.py
# O si instalaste como paquete:
h4ckbot
```
