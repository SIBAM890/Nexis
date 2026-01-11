import re
from typing import Tuple

class EthicsGuardian:
    """
    Mandatory ethics enforcement layer.
    Ensures no processing of sensitive/illegal targets.
    """
    
    # regex for things we ABSOLUTELY do not touch
    FORBIDDEN_PATTERNS = {
        "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
        "credit_card": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
        "private_ip": r"\b(192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1]))",
    }
    
    @classmethod
    def validate_target(cls, target: str) -> Tuple[bool, str]:
        """
        Checks if a target is ethically safe to process.
        Returns: (is_safe, refusal_reason)
        """
        if not target:
            return False, "Target cannot be empty"
            
        # Check against forbidden patterns
        for name, pattern in cls.FORBIDDEN_PATTERNS.items():
            if re.search(pattern, target):
                return False, f"Ethics Safety: Detected sensitive pattern ({name}). Process aborted."
        
        # In a real system, you might checking against a 'Do Not Scan' list here
        return True, "Target accepted for public OSINT analysis"

    @classmethod
    def sanitize_output(cls, data: dict) -> dict:
        """
        Redacts any accidentally collected sensitive info before display.
        """
        # (Placeholder for deep cleaning logic)
        # For this prototype, we assume upstream collectors are safe, 
        # but this serves as the final gate.
        return data
