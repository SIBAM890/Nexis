from typing import List, Dict
from app.core.schema import UnifiedSignal

class ReverseOSINT:
    """
    Analyzes the COLLECTED signals to infer if the target is being
    actively tracked or aggregated by third parties.
    
    PHILOSOPHY:
    - This is INFERENCE, not detection.
    - We look for artifacts that suggest the user's data has been 
      indexed by data brokers or breach monitoring services.
    """
    
    def analyze(self, signals: List[UnifiedSignal]) -> Dict:
        indicators = []
        
        # 1. Check for "Aggregator" patterns in sources
        sources = [s.source for s in signals]
        
        if "pastebin_dump" in sources:
             indicators.append(
                 "Simulated public paste-style exposure pattern. "
                 "Inference: Publicly indexed data *may* create probabilistic correlation risks."
             )
             
        # 2. Check for "Dorking" susceptibility
        # If unique username is found across diverse, unconnected platforms
        unique_platforms = set(sources)
        if len(unique_platforms) > 3:
            indicators.append(
                f"Public Indexability: Identity present on {len(unique_platforms)} unrelated public platforms. "
                "Inference: Increased visibility to automated indexing systems."
            )

        return {
            "module": "Reverse OSINT",
            "status": "Possible Exposure" if indicators else "Low Visibility",
            "inferences": indicators if indicators else ["No specific tracking patterns inferred."],
            "methodology": "Pattern Analysis of Public Indexing"
        }
