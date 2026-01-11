import os

class Config:
    SCAN_INTERVAL_SECONDS = int(os.getenv("SCAN_INTERVAL", 300))
    ENABLE_REVERSE_OSINT = True
    ENABLE_REPO_SCANNING = True
    ENABLE_IMAGE_ANALYSIS = True

    USER_AGENT = "OSINT-Chakra/1.0"