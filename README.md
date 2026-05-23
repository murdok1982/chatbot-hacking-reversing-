<div align="center">

# 🧠⚔️ H4CK-BOT

### *Tu copiloto de ciberseguridad, hacking ético y reversing con IA local*

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000?logo=llama&logoColor=white)](https://ollama.com)
[![LangChain](https://img.shields.io/badge/LangChain-v0.1+-orange?logo=chainlink&logoColor=white)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/murdok1982/chatbot-hacking-reversing-/actions/workflows/ci.yml/badge.svg)](https://github.com/murdok1982/chatbot-hacking-reversing-/actions)

**100% local · 100% privado · 100% educativo**

</div>

---

## 🔥 ¿Qué es H4CK-BOT?

Un asistente conversacional potenciado por **LLMs locales** (Ollama) especializado en:

```
┌──────────────────────────────────────────────┐
│   🎯  PENTESTING        🔬  REVERSE ENGINEERING │
│   🛡️  EXPLOIT DEV        🌐  SEGURIDAD WEB    │
│   🔐  CRIPTOGRAFÍA       📡  OSINT & RECON    │
│   🏁  CTF SOLVER         💻  SECURE CODING     │
└──────────────────────────────────────────────┘
```

Todo gira en **tu máquina**. Cero datos a la nube. Cero dependencias externas de API. Solo tú, el modelo local, y el conocimiento.

---

## ✨ Características

| Capacidad | 🔧 Descripción |
|---|---|
| **🤖 LLM Local 100% offline** | Corre con Ollama — nada sube a Internet, latencia cero |
| **💬 Memoria conversacional** | El bot recuerda el hilo de la conversación |
| **🔍 Análisis de vulnerabilidades** | SQLi, XSS, buffer overflows, ROP — explicaciones paso a paso |
| **💣 Desarrollo de exploits educativo** | Técnicas de explotación con énfasis en legalidad |
| **🔬 Reversing de binarios** | Estrategias con Ghidra, IDA Pro, GDB, radare2 |
| **🌐 Pentesting web** | Metodologías, herramientas, evasión de WAF |
| **📡 OSINT & Reconocimiento** | Enumeración, DNS, subdominios, footprinting |
| **🔐 Criptoanálisis** | Identificación de hashes, análisis de algoritmos |
| **🛠️ Herramientas integradas** | Nmap wrapper, codificador/decodificador de payloads, buscador de CVEs |
| **🎮 Modos especializados** | `/recon` para escaneos, `/exploit` para payloads |

---

## 📥 Instalación

### Requisitos

| | Mínimo | Recomendado |
|---|---|---|
| **Python** | 3.8 | 3.10+ |
| **RAM** | 8 GB | 16 GB |
| **Disco** | 5 GB libres | 10 GB libres |
| **Ollama** | ✓ | ✓ |
| **Nmap** | — | Opcional (para escaneos) |

### Paso a paso

```bash
# 1. Clona el repositorio
git clone https://github.com/murdok1982/chatbot-hacking-reversing-.git
cd chatbot-hacking-reversing-

# 2. Descarga un modelo local con Ollama
ollama pull llama3.1        # ~4.7 GB — mejor balance calidad/rendimiento
# ollama pull codellama      # alternativa: especializado en código
# ollama pull llama3.2:3b    # alternativa: más ligero

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Copia y configura el entorno (opcional)
cp .env.example .env
# Edita .env si quieres cambiar el modelo o la temperatura

# 5. ¡Ejecuta!
python run.py
```

> **💡 También puedes instalarlo como comando global:**
> ```bash
> pip install -e .
> h4ckbot
> ```

---

## 🎮 Uso

### Modo interactivo

```bash
python run.py
```

```
╔══════════════════════════════════════════════════════════╗
║   🧠⚔️  H4CK-BOT — Asistente de Hacking Ético & RE      ║
║   LLM local · Ollama · Siempre legal y educativo        ║
╚══════════════════════════════════════════════════════════╝

Comandos especiales:
  /chat    → Modo conversación general (por defecto)
  /recon   → Modo reconocimiento — escanea puertos, enumera subdominios
  /exploit → Modo desarrollo de exploits — genera payloads y analiza CVEs
  /tools   → Lista herramientas integradas
  /help    → Ayuda rápida
  salir    → Terminar

[chat] Tú: >
```

### Consultas de ejemplo

```
Tú: > Explica el ataque de tipo SQL injection con ejemplos en código
Tú: > Cómo funciona un buffer overflow en C? Dame un ejemplo práctico
Tú: > Pasos para analizar un binario con Ghidra desde cero
Tú: > Qué comandos de Nmap usarías para un pentest completo?
Tú: > Dame una guía de hardening para servidores Linux
Tú: > Cómo evadir un WAF con técnicas de encoding?
```

### Modo Reconocimiento (`/recon`)

Modo interactivo para tareas de reconocimiento:

```
[recon] $ scan 192.168.1.1 22,80,443
[recon] $ dns google.com
[recon] $ subdomain example.com
[recon] $ back
```

### Modo Exploit Dev (`/exploit`)

Modo interactivo para trabajar con payloads y vulnerabilidades:

```
[exploit] $ encode base64 <script>alert('xss')</script>
[exploit] $ decode hex 48656c6c6f20576f726c64
[exploit] $ hash 5d41402abc4b2a76b9719d911017c592
[exploit] $ cve log4shell
[exploit] $ back
```

### Herramientas integradas (`/tools`)

```
🔧 Herramientas integradas:
  - nmap <target> <puertos>  : Escanea puertos vía Nmap
  - encode <tipo> <texto>    : Codifica payload (base64|hex|url)
  - decode <tipo> <texto>    : Decodifica payload
  - cve <término>            : Busca CVEs relacionados
```

---

## 🧪 Casos de Uso

### 🎓 Estudiante de Ciberseguridad

> *"Estoy preparando la certificación OSCP/eJPT."*

Usa H4CK-BOT como tutor personal. Pregunta sobre cualquier tema de pentesting, desde reconocimiento hasta post-explotación. El bot te guiará con metodología, ejemplos de código y buenas prácticas.

```bash
[chat] Tú: > Dame la metodología completa de un pentest web
[chat] Tú: > Explica la diferencia entre evaluación de vulnerabilidades y pentest
```

### 🏁 CTF Player

> *"Estoy atascado en un desafío de reversing."*

Durante una competición, H4CK-BOT te ayuda a analizar binarios, entender protectores, descifrar strings ofuscados y planificar tu estrategia de ataque.

```bash
[chat] Tú: > Tengo un binario que usa anti-debugging con ptrace, cómo lo bypasseo?
[chat] Tú: > Dame técnicas para analizar un ransomware en sandbox
```

### 🔬 Pentester Profesional

> *"Necesito hacer un reconocimiento rápido de un target."*

Activa el modo `/recon` para escanear puertos, resolver DNS y enumerar subdominios sin salir de la terminal.

```bash
[/recon] $ scan target.com 1-1000
[/recon] $ subdomain target.com
```

### 🛡️ Blue Team / Defensor

> *"Cómo detecto si mi red fue comprometida?"*

Usa el chatbot para entender técnicas de detección, análisis de logs, hardening y respuestas a incidentes.

```bash
[chat] Tú: > Qué patrones debo buscar en logs de Apache para detectar SQLi?
[chat] Tú: > Dame un checklist de hardening para un servidor Ubuntu
```

### 💻 Desarrollador Seguro

> *"Necesito revisar el código de mi app web."*

Pide al bot que audite snippets de código, identifique vulnerabilidades y sugiera parches.

```bash
[chat] Tú: > Este código PHP es vulnerable? [pega código]
[chat] Tú: > Cómo implementar autenticación segura con JWT en Python?
```

### 🔍 Reversing Engineer

> *"Estoy analizando un binario y necesito identificar funciones criptográficas."*

El bot te guía en el uso de Ghidra, IDA Pro, GDB y técnicas de análisis dinámico y estático.

```bash
[chat] Tú: > Cómo identifico una función de cifrado AES en un binario con Ghidra?
[chat] Tú: > Técnicas de unpacking de binarios empaquetados con UPX
```

---

## 🧪 Tests

```bash
# Instalar en modo desarrollo
pip install -e .
pip install pytest-cov

# Ejecutar tests
pytest tests/ -v --cov=src
```

```
tests/test_chatbot.py  ... ✓
tests/test_utils.py    ... ✓
tests/test_tools.py    ... ✓
```

---

## 🗺️ Estructura del proyecto

```
chatbot-hacking-reversing/
├── run.py                      # Entry point principal
├── setup.py                    # Configuración del paquete
├── requirements.txt            # Dependencias
├── .env.example                # Template de configuración
├── ci.yml                      # GitHub Actions CI
│
├── src/
│   └── chatbot/
│       ├── __init__.py
│       ├── main.py              # Bucle principal del chatbot
│       ├── config.py            # Configuración (Ollama, prompt)
│       ├── llm_chain.py         # Cadena LangChain con memoria
│       ├── utils.py             # Logger, validación de input
│       ├── hispan_shield_guardian.py
│       │
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── nmap_wrapper.py  # Escaneo de puertos vía Nmap
│       │   ├── cve_search.py    # Búsqueda de CVEs (API CIRCL)
│       │   ├── payload_tools.py # Encode/decode, hash identifier
│       │   └── osint_tools.py   # DNS, subdominios
│       │
│       └── modes/
│           ├── __init__.py
│           ├── recon.py         # Modo reconocimiento interactivo
│           └── exploit_dev.py   # Modo exploit dev interactivo
│
├── tests/
│   ├── __init__.py
│   ├── test_chatbot.py          # Tests del chain LLM
│   ├── test_utils.py            # Tests de utilidades
│   └── test_tools.py            # Tests de herramientas
│
└── docs/
    ├── installation.md
    └── usage.md
```

---

## 🧠 Roadmap

| Estado | Funcionalidad |
|---|---|
| ✅ | Prompt experto en hacking ético y reversing |
| ✅ | Memoria conversacional con LangChain |
| ✅ | Modos interactivos: chat, recon, exploit |
| ✅ | Herramientas: Nmap wrapper, payload tools, CVE search, OSINT |
| ✅ | Integración con Ollama (modelos locales) |
| 🔜 | Integración con Metasploit RPC |
| 🔜 | Analizador de tráfico de red (packet capture) |
| 🔜 | Interfaz web con Gradio |
| 🔜 | Generación automática de reportes de pentesting |
| 🔜 | Soporte multi-modelo (OpenAI API, Claude API como alternativa) |
| 🔜 | Modo agente autónomo para tareas guiadas |

---

## ⚖️ Ética y Responsabilidad Legal

### ✅ Usos autorizados

| Escenario | ¿Válido? |
|---|---|
| Laboratorios personales (VMs, Docker) | ✅ Sí |
| Bug Bounty en programas autorizados | ✅ Sí |
| Pentesting profesional con contrato | ✅ Sí |
| CTF y competiciones | ✅ Sí |
| Educación e investigación | ✅ Sí |

### ❌ Usos prohibidos

- Acceso no autorizado a sistemas ajenos
- Robo de datos, ransomware o destrucción de información
- Ataques a infraestructura crítica sin autorización
- Cualquier actividad ilegal según leyes locales

> ⚠️ **AVISO LEGAL:** Este software es **exclusivamente para fines educativos y de investigación autorizada**. El autor **no se responsabiliza** por el uso indebido que terceros puedan darle. Conoce las leyes de tu país: la mayoría penaliza severamente el acceso no autorizado a sistemas informáticos.

---

## 🤝 Contribuir

¿Encontraste un bug? ¿Tienes una idea para un nuevo modo o herramienta?

1. **Fork** el repositorio
2. **Crea una rama**: `git checkout -b feature/mi-idea`
3. **Commit**: `git commit -m 'feat: agrega X funcionalidad'`
4. **Push**: `git push origin feature/mi-idea`
5. **Abre un Pull Request**

También puedes reportar issues directamente en [GitHub Issues](https://github.com/murdok1982/chatbot-hacking-reversing-/issues).

---

## 👤 Autor

<div align="center">

### Gustavo Lobato Clara — *murdok1982*

[![GitHub](https://img.shields.io/badge/GitHub-murdok1982-181717?logo=github&logoColor=white)](https://github.com/murdok1982)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gustavo%20Lobato%20Clara-0A66C2?logo=linkedin)](https://www.linkedin.com/in/gustavo-lobato-clara-2b446b102/)
[![Email](https://img.shields.io/badge/Email-gustavolobatoclara@gmail.com-EA4335?logo=gmail)](mailto:gustavolobatoclara@gmail.com)

</div>

---

## 📄 Licencia

**MIT License** — ver [LICENSE](LICENSE) para términos completos.

*Uso educativo permitido. El autor no se responsabiliza por mal uso.*

---

<div align="center">

### ⭐ Si te sirve, deja una estrella

**Hack the planet... legally! 🔐**

</div>
