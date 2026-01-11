from typing import List, Dict
from app.core.schema import UnifiedSignal, RiskLevel
from app.core.ethics import EthicsGuardian

class RiskAssessor:
    """
    transparent, logic-based risk assessment.
    NO MAGIC NUMBERS.
    """
    
    def assess(self, signals: List[UnifiedSignal]) -> Dict:
        risk_score = RiskLevel.LOW
        reasons = []
        
        # 1. Analyze Individual Signals
        for signal in signals:
            if signal.type == "email":
                risk_score = self._max_risk(risk_score, RiskLevel.MEDIUM)
                reasons.append(f"Exposed Email address found: {signal.value}")
                
            if signal.type == "password_hash":
                risk_score = RiskLevel.HIGH
                reasons.append("HIGH RISK: Simulated credential-like pattern detected in mock public-style data.")
                
            if signal.source == "github_public":
                 if "api_key" in signal.context.lower():
                     risk_score = RiskLevel.MEDIUM
                     reasons.append(f"Simulated API Key pattern observed in public code comment: {signal.value}")

        # 2. Analyze Cross-Platform Exposure (Aggregation)
        sources = {s.source for s in signals}
        if len(sources) >= 3:
            risk_score = self._max_risk(risk_score, RiskLevel.MEDIUM)
            reasons.append(f"Broad digital footprint detected ({len(sources)} platforms).")
            reasons.append("Aggregation Risk: High visibility across multiple service providers.")

        return {
            "level": risk_score.value,
            "score_logic": reasons if reasons else ["No significant exposure detected (Risk Score: 0/100)."],
            "quantitative_score": self._get_numeric_score(risk_score)
        }

    def _get_numeric_score(self, level: RiskLevel) -> int:
        mapping = {
            RiskLevel.LOW: 10,
            RiskLevel.MEDIUM: 50,
            RiskLevel.HIGH: 80,
            RiskLevel.CRITICAL: 100
        }
        return mapping.get(level, 0)

    def _max_risk(self, current: RiskLevel, new: RiskLevel) -> RiskLevel:
        # Simple hierarchy comparison
        order = [RiskLevel.LOW, RiskLevel.MEDIUM, RiskLevel.HIGH, RiskLevel.CRITICAL]
        if order.index(new) > order.index(current):
            return new
        return current