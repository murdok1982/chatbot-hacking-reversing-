import urllib.request
import urllib.error
import urllib.parse
import json
from ..utils import logger

CIRCL_API = "https://cve.circl.lu/api/cve"

def search_cve(keyword: str, limit: int = 5) -> str:
    try:
        url = f"{CIRCL_API}/search/{urllib.parse.quote(keyword)}"
        req = urllib.request.Request(url, headers={"User-Agent": "H4CK-BOT/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        logger.warning(f"CVE API HTTP {e.code}")
        return f"⚠️  API CVE no disponible (HTTP {e.code})."
    except Exception as e:
        logger.error(f"CVE search error: {e}")
        return f"❌ Error buscando CVEs: {e}"

    if not data:
        return f"🔍 No se encontraron CVEs para '{keyword}'."
    
    results = data[:limit]
    lines = [f"🔍 CVEs encontrados para '{keyword}':"]
    for cve in results:
        cve_id = cve.get("id", "N/A")
        summary = cve.get("summary", "Sin descripción")[:120]
        score = cve.get("cvss", "N/A")
        lines.append(f"  • {cve_id} | CVSS: {score} | {summary}")
    return "\n".join(lines)
