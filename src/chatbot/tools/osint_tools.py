import socket
import subprocess
from ..utils import logger

def dns_lookup(domain: str) -> str:
    try:
        ip = socket.gethostbyname(domain)
        return f"🌐 {domain} → {ip}"
    except socket.gaierror:
        return f"❌ No se pudo resolver {domain}"

def reverse_dns(ip: str) -> str:
    try:
        host = socket.gethostbyaddr(ip)
        return f"🔁 {ip} → {host[0]}"
    except socket.herror:
        return f"❌ No se pudo resolver IP {ip}"

def subdomain_enum(domain: str, wordlist_path: str = None) -> str:
    if not wordlist_path:
        wordlist = ["www", "mail", "admin", "ftp", "ssh", "dev", "api", "vpn", "webmail", "blog"]
    else:
        try:
            with open(wordlist_path) as f:
                wordlist = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            return f"❌ Wordlist no encontrada: {wordlist_path}"

    found = []
    for sub in wordlist:
        target = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(target)
            found.append(f"  {target} → {ip}")
        except socket.gaierror:
            continue

    if found:
        return f"🔍 Subdominios encontrados para {domain}:\n" + "\n".join(found[:20])
    return f"🔍 No se encontraron subdominios comunes para {domain}"
