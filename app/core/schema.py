from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
import time

class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

@dataclass
class UnifiedSignal:
    """
    Standardized OSINT signal format to normalize data from any source.
    """
    source: str  # e.g., "github", "twitter_mock", "user_input"
    type: str    # e.g., "username", "email", "repo_name"
    value: str   # The actual data found
    timestamp: float = field(default_factory=time.time)
    context: str = "" # Explanation of where/how this was found
    
    # Explainability Fields
    evidence: str = "N/A" # Raw proof (e.g. URL, API Response)
    detection_method: str = "Unknown" # Logic used (e.g. "String Match", "API Lookup")
    
    # Metadata for correlation
    confidence: float = 1.0 
    
    def to_dict(self):
        return {
            "source": self.source,
            "type": self.type,
            "value": self.value,
            "timestamp": self.timestamp,
            "context": self.context,
            "evidence": self.evidence,
            "detection_method": self.detection_method,
            "confidence": self.confidence
        }
