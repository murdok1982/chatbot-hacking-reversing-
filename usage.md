## Uso del H4CK-BOT

### Modo Chat (por defecto)

Solo escribe tu pregunta:

```
Tú: > Explica cómo funciona un ataque de tipo SQL injection
Tú: > Dame pasos para reverse-engineering con Ghidra
Tú: > Cómo mitigar un buffer overflow en C?
```

### Modos especiales

| Comando | Modo | Descripción |
|---|---|---|
| `/chat` | Chat general | Consultas de seguridad, hacking, reversing |
| `/recon` | Reconocimiento | Escanea puertos, DNS, subdominios |
| `/exploit` | Exploit dev | Codifica payloads, busca CVEs, identifica hashes |
| `/tools` | Lista herramientas | Muestra herramientas integradas disponibles |

### Modo Reconocimiento

```
[recon] $ scan 192.168.1.1
[recon] $ dns example.com
[recon] $ subdomain example.com
[recon] $ back
```

### Modo Exploit Dev

```
[exploit] $ encode base64 <script>alert(1)</script>
[exploit] $ decode hex 48656c6c6f
[exploit] $ hash e99a18c428cb38d5f260853678922e03
[exploit] $ cve apache log4j
[exploit] $ back
```
