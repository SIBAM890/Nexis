class IntelligenceMemory:
    def __init__(self):
        self.seen = set()

    def remember(self, entity_id: str):
        self.seen.add(entity_id)

    def export(self):
        return {
            "seen_entities": list(self.seen)
        }