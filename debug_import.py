import sys
import traceback

try:
    print("Attempting import...")
    from app.agent.brain import IntelligenceBrain
    print("Import successful!")
except Exception:
    with open("import_error.txt", "w") as f:
        f.write(traceback.format_exc())
    print("Import failed. Check import_error.txt")
