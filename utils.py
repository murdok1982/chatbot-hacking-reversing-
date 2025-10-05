import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(user_input: str) -> bool:
    # Ejemplo: Evita inputs maliciosos (básico)
    if len(user_input) > 1000:
        return False
    return True
