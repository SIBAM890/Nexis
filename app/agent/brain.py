from typing import Dict
from app.core.ethics import EthicsGuardian
from app.scrapers.social_scraper import SocialScraper
from app.intelligence.risk import RiskAssessor
from app.intelligence.correlator import IdentityCorrelator
from app.intelligence.reverse_osint import ReverseOSINT

class IntelligenceBrain:
    """
    Coordinator / Pipeline Manager.
    Input -> Ethics -> Collect -> Correlate -> Risk -> Output
    """
    
    def __init__(self):
        self.scraper = SocialScraper(simulation_mode=True)
        self.correlator = IdentityCorrelator()
        self.risk_engine = RiskAssessor()
        self.reverse_engine = ReverseOSINT()

    def investigate(self, target: str) -> Dict:
        """
        Main entry point for the agent.
        """
        
        # Step 1: Ethics Gate
        is_safe, reason = EthicsGuardian.validate_target(target)
        if not is_safe:
            return {
                "status": "blocked",
                "error": reason
            }
            
        # Step 2: Collection
        raw_signals = self.scraper.scan(target)
        
        # Step 3: Correlation
        # self-correlate (find links within the gathered data)
        correlated_identities = self.correlator.correlate(raw_signals)
        
        # Step 4: Risk Assessment
        risk_report = self.risk_engine.assess(raw_signals)

        # Step 5: Reverse OSINT (Surveillance Awareness)
        reverse_report = self.reverse_engine.analyze(raw_signals)
        
        # Step 6: Output Formatting
        return {
            "status": "success",
            "target": target,
            "ethics_verified": True,
            "signal_count": len(raw_signals),
            "signals": [s.to_dict() for s in raw_signals],
            "correlations": correlated_identities,
            "risk_assessment": risk_report,
            "reverse_osint": reverse_report
        }