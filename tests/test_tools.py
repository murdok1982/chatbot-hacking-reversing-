import pytest

class TestPayloadTools:
    def test_encode_base64(self):
        from src.chatbot.tools.payload_tools import encode_payload
        result = encode_payload("base64", "test")
        assert result == "dGVzdA=="

    def test_encode_hex(self):
        from src.chatbot.tools.payload_tools import encode_payload
        result = encode_payload("hex", "test")
        assert result == "74657374"

    def test_decode_base64(self):
        from src.chatbot.tools.payload_tools import decode_payload
        result = decode_payload("base64", "dGVzdA==")
        assert result == "test"

    def test_identify_hash(self):
        from src.chatbot.tools.payload_tools import identify_hash
        assert "MD5" in identify_hash("a" * 32)
        assert "SHA1" in identify_hash("a" * 40)
        assert "SHA256" in identify_hash("a" * 64)

class TestOsintTools:
    def test_dns_lookup_invalid(self):
        from src.chatbot.tools.osint_tools import dns_lookup
        result = dns_lookup("invalid-domain-that-definitely-does-not-exist-12345.xyz")
        assert "No se pudo resolver" in result

class TestCveSearch:
    def test_search_cve_returns_message(self):
        from src.chatbot.tools.cve_search import search_cve
        result = search_cve("test")
        assert isinstance(result, str)
