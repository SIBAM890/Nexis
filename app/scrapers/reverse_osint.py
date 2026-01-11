class ReverseOSINT:
    def lookup(self, identifier_type: str, identifier: str):
        signals = []

        if identifier_type == "email":
            domain = identifier.split("@")[-1]
            signals.append({
                "type": "email_domain",
                "value": domain,
                "confidence": 0.7
            })

        if identifier_type == "phone":
            country_code = identifier[:3]
            signals.append({
                "type": "country_code",
                "value": country_code,
                "confidence": 0.8
            })

        return signals