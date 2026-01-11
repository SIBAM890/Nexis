from app.intelligence.graph import IntelligenceGraph
from app.intelligence.memory import IntelligenceMemory
from app.intelligence.risk import RiskEngine
from app.agent.brain import IntelligenceBrain


class Orchestrator:
    def __init__(self):
        self.graph = IntelligenceGraph()
        self.memory = IntelligenceMemory()
        self.risk_engine = RiskEngine()
        self.brain = IntelligenceBrain(
            self.graph,
            self.memory,
            self.risk_engine
        )

    def run_scan(self, payload: dict):
        if payload.get("query"):
            self.brain.process_text(payload["query"])

        if payload.get("image"):
            self.brain.process_image(payload["image"])

        return {
            "intelligence": self.brain.intelligence_summary()
        }