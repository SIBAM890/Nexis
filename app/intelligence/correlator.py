from typing import List, Dict
from app.core.schema import UnifiedSignal
from difflib import SequenceMatcher

class IdentityCorrelator:
    """
    Probabilistic correlation engine.
    Links disparate data points to the same identity.
    """
    
    def correlate(self, signals: List[UnifiedSignal]) -> List[Dict]:
        """
        Returns a list of 'Linked Identities' with explanation.
        """
        # Simple O(N^2) comparison for demo purposes
        # In prod, this would be a graph query
        
        links = []
        
        processed_indices = set()
        
        for i, s1 in enumerate(signals):
            if i in processed_indices:
                continue
                
            related_group = {
                "primary": s1.to_dict(),
                "related": []
            }
            
            for j, s2 in enumerate(signals):
                if i == j: continue
                
                confidence, reason = self._calculate_similarity(s1, s2)
                
                if confidence > 0.7:  # Threshold
                    strength_label = "STRONG" if confidence > 0.85 else "MEDIUM"
                    logic_detail = f"Probabilistic Distance (Levenshtein ratio {confidence:.2f})" if "similarity" in reason else "Exact String Match"
                    
                    related_group["related"].append({
                        "signal": s2.to_dict(),
                        "confidence": confidence,
                        "strength": strength_label,
                        "reason": reason,
                        "logic_method": logic_detail
                    })
                    processed_indices.add(j)
            
            if related_group["related"]:
                links.append(related_group)
                
        return links

    def _calculate_similarity(self, s1: UnifiedSignal, s2: UnifiedSignal) -> (float, str):
        # 1. Exact Match
        if s1.value == s2.value:
            return 1.0, "Exact match of value"
            
        # 2. Username Similarity (e.g. jdoe99 vs jdoe_99)
        if s1.type == "username" and s2.type == "username":
            ratio = SequenceMatcher(None, s1.value, s2.value).ratio()
            if ratio > 0.8:
                return ratio, f"High username similarity ({int(ratio*100)}%)"
                
        # 3. Handle reuse (e.g. username matches email prefix)
        if s1.type == "username" and s2.type == "email":
            if s1.value in s2.value:
                return 0.9, "Username found in email address"
                
        return 0.0, ""
