import requests
from typing import List
from app.core.schema import UnifiedSignal
from app.core.ethics import EthicsGuardian

class SocialScraper:
    """
    Collects public footprints.
    Defaults to SAFE MOCK DATA for Hackathon stability/Safety.
    """
    
    def __init__(self, simulation_mode=True):
        self.simulation = simulation_mode
        self.platforms = ["github", "twitter", "linkedin", "instagram"]

    def scan(self, target: str) -> List[UnifiedSignal]:
        # 1. Ethics Check (Redundant but safe)
        is_safe, reason = EthicsGuardian.validate_target(target)
        if not is_safe:
            return []

        if self.simulation:
            return self._mock_scan(target)
        else:
            return self._live_scan(target)

    def _mock_scan(self, username: str) -> List[UnifiedSignal]:
        """
        Returns realistic-looking data for the demo.
        """
        signals = []
        
        # Simulate GitHub
        signals.append(UnifiedSignal(
            source="github",
            type="username",
            value=username,
            context="Active developer account found. \n- 12 Public Repositories \n- Account created 2020",
            evidence=f"https://github.com/{username} (HTTP 200 OK)",
            detection_method="Direct URL Verification: Validated username against GitHub User API pattern.",
            confidence=1.0
        ))
        
        # Simulate Leak (if username has 'test' or specific pattern)
        if "test" in username or "admin" in username:
             signals.append(UnifiedSignal(
                source="pastebin_dump",
                type="email",
                value=f"{username}@gmail.com",
                context="Email structure detected in mock public breach dataset. \n- Date: 2024-05-12 \n- Type: Simulated Credential Exposure",
                evidence="dump_v2_2024.txt: Line 4022 (Simulated Public Paste)",
                detection_method="Pattern Match: Simulated RegEx search for email format in public datasets.",
                confidence=0.8
            ))

        # Simulate Twitter
        signals.append(UnifiedSignal(
            source="twitter",
            type="username",
            value=f"@{username}_official",
            context="Profile public metadata matches target. \n- Bio contains 'Developer' \n- Location matches",
            evidence=f"https://twitter.com/{username}_official/status/123",
            detection_method="Cross-Referencing: Public bio keyword match & username similarity.",
            confidence=0.7
        ))
        
        return signals

    def _live_scan(self, username: str) -> List[UnifiedSignal]:
        # Real HTTP HEAD implementation would go here.
        # For now, return empty to prevent IP bans during dev.
        return []