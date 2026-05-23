import subprocess
import re
from ..utils import logger

def scan_port(target: str, ports: str = "1-1000") -> str:
    try:
        result = subprocess.run(
            ["nmap", "-sV", "-p", ports, "-T4", target],
            capture_output=True, text=True, timeout=300
        )
        output = result.stdout
        logger.info(f"Nmap scan completed for {target}:{ports}")
        return output
    except FileNotFoundError:
        return "❌ Nmap no está instalado. Instálalo desde https://nmap.org"
    except subprocess.TimeoutExpired:
        return "⏱️  Escaneo agotó el tiempo de espera (5 min)."
    except Exception as e:
        logger.error(f"Nmap error: {e}")
        return f"❌ Error ejecutando Nmap: {e}"

def quick_scan(target: str) -> str:
    return scan_port(target, "22,80,443,8080,8443")
