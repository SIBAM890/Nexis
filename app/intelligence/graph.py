import time
from collections import defaultdict


class IntelligenceGraph:
    def __init__(self):
        self.entities = {}
        self.relationships = []
        self.timeline = []

    def add_entity(self, entity: dict):
        eid = entity["id"]
        now = int(time.time())

        if eid not in self.entities:
            entity["first_seen"] = now
            entity["last_seen"] = now
            entity["sources"] = set(entity.get("sources", []))
            self.entities[eid] = entity
        else:
            self.entities[eid]["last_seen"] = now
            self.entities[eid]["sources"].update(entity.get("sources", []))

        self._snapshot()

    def add_relationship(self, src: str, dst: str, relation: str, confidence: float = 0.6):
        self.relationships.append({
            "src": src,
            "dst": dst,
            "relation": relation,
            "confidence": confidence
        })

    def _snapshot(self):
        high_risk = sum(
            1 for e in self.entities.values()
            if e.get("attributes", {}).get("sensitivity") == "high"
        )
        self.timeline.append({
            "timestamp": int(time.time()),
            "entity_count": len(self.entities),
            "high_risk": high_risk
        })

    def export_entities(self):
        output = []
        for e in self.entities.values():
            clean = dict(e)
            clean["sources"] = sorted(list(clean.get("sources", [])))
            output.append(clean)
        return output

    def export_relationships(self):
        return list(self.relationships)

    def export_timeline(self):
        return list(self.timeline)