import itertools
from collections import defaultdict
from typing import Dict, List

from app.intelligence.memory import IntelligenceMemory


class SelfLearningEngine:
    """
    Autonomous learning layer.
    Evolves scanning strategy based on historical exposure patterns.
    """

    def __init__(self):
        self.memory = IntelligenceMemory()
        self.source_weights = defaultdict(lambda: 1.0)
        self.username_patterns = set()

    def learn_from_snapshot(self):
        """
        Called after every scan cycle.
        """
        snapshot = self.memory.latest()
        if not snapshot:
            return

        self._learn_sources(snapshot)
        self._learn_username_patterns(snapshot)

    def _learn_sources(self, snapshot: Dict):
        """
        Increase weight of consistently leaking platforms.
        """
        exposure_counts = defaultdict(int)

        for entity in snapshot["entities"]:
            for src in entity.get("sources", []):
                exposure_counts[src] += 1

        for source, count in exposure_counts.items():
            if count > 2:
                self.source_weights[source] *= 1.2

    def _learn_username_patterns(self, snapshot: Dict):
        """
        Discover username mutation logic.
        """
        usernames = [
            e["identifier"]
            for e in snapshot["entities"]
            if e["type"] == "username"
        ]

        for u in usernames:
            if "_" in u or "." in u:
                self.username_patterns.add(u)

    def predict_new_usernames(self, base_username: str) -> List[str]:
        """
        Requirement 3 example: Predict unseen usernames.
        """
        mutations = [
            "{}_dev",
            "{}_private",
            "real_{}",
            "{}.official",
            "git.{}"
        ]

        return list(
            set(fmt.format(base_username) for fmt in mutations)
        )

    def adaptive_scan_plan(self) -> Dict[str, float]:
        """
        Returns platform priority map.
        Used by scheduler / agent.
        """
        return dict(self.source_weights)