import re
import time
from PIL import Image


class Entity:
    @staticmethod
    def from_text(text: str):
        text = text.strip()

        if re.match(r"[^@]+@[^@]+\.[^@]+", text):
            etype = "email"
            sensitivity = "high"
        elif re.match(r"\+?\d[\d\s]{7,}", text):
            etype = "phone"
            sensitivity = "high"
        else:
            etype = "username"
            sensitivity = "medium"

        return {
            "id": f"{etype}:{text}",
            "type": etype,
            "identifier": text,
            "attributes": {
                "length": len(text),
                "contains_number": any(c.isdigit() for c in text),
                "contains_special": any(not c.isalnum() for c in text),
                "sensitivity": sensitivity
            },
            "sources": {"user_input"}
        }

    @staticmethod
    def from_image(image):
        try:
            img = Image.open(image)
            w, h = img.size
            return {
                "id": f"image_meta:{w}x{h}",
                "type": "image_meta",
                "identifier": f"{w}x{h}",
                "attributes": {
                    "length": len(f"{w}x{h}"),
                    "contains_number": True,
                    "contains_special": False,
                    "sensitivity": "medium"
                },
                "sources": {"image_upload"}
            }
        except Exception:
            return None