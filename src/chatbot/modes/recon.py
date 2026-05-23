from ..tools.nmap_wrapper import scan_port, quick_scan
from ..tools.osint_tools import dns_lookup, reverse_dns, subdomain_enum
from ..utils import logger

def recon_mode(chain=None):
    print("🕵️  Modo Reconocimiento activado.")
    print("  Comandos: scan <target> [ports], dns <domain>, subdomain <domain>, back")
    while True:
        cmd = input("  [recon] $ ").strip().lower()
        if cmd == "back":
            break
        parts = cmd.split()
        if not parts:
            continue
        if parts[0] == "scan":
            target = parts[1] if len(parts) > 1 else input("Target: ")
            ports = parts[2] if len(parts) > 2 else "22,80,443,8080,8443"
            print(f"🔎 Escaneando {target} (puertos: {ports})...")
            print(scan_port(target, ports))
        elif parts[0] == "dns":
            domain = parts[1] if len(parts) > 1 else input("Dominio: ")
            print(dns_lookup(domain))
            print(reverse_dns(domain))
        elif parts[0] == "subdomain":
            domain = parts[1] if len(parts) > 1 else input("Dominio: ")
            print(subdomain_enum(domain))
        else:
            print("❓ Comando: scan, dns, subdomain, back")
    print("↩️  Volviendo al chat principal.")
