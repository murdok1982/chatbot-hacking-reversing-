import base64
import urllib.parse

def encode_payload(encoding: str, text: str) -> str:
    encoding = encoding.lower()
    if encoding == "base64":
        return base64.b64encode(text.encode()).decode()
    elif encoding == "hex":
        return text.encode().hex()
    elif encoding == "url":
        return urllib.parse.quote(text)
    elif encoding == "double-url":
        return urllib.parse.quote(urllib.parse.quote(text))
    else:
        return f"❌ Codificación no soportada: {encoding}. Usa: base64, hex, url, double-url"

def decode_payload(encoding: str, text: str) -> str:
    encoding = encoding.lower()
    try:
        if encoding == "base64":
            return base64.b64decode(text).decode()
        elif encoding == "hex":
            return bytes.fromhex(text).decode()
        elif encoding == "url":
            return urllib.parse.unquote(text)
        else:
            return f"❌ Codificación no soportada: {encoding}"
    except Exception as e:
        return f"❌ Error decodificando: {e}"

def identify_hash(hash_str: str) -> str:
    lengths = {32: "MD4/MD5/NTLM", 40: "SHA1", 56: "SHA224", 64: "SHA256", 96: "SHA384", 128: "SHA512"}
    hlen = len(hash_str)
    return lengths.get(hlen, f"Longitud {hlen} — hash desconocido o custom")
