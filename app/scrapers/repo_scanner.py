class RepoScanner:
    def scan(self, username: str):
        if len(username) < 4:
            return []

        return [{
            "platform": "github",
            "indicator": "possible_public_repos",
            "confidence": 0.5
        }]