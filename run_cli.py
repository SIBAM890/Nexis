import sys
import json
from app.agent.brain import IntelligenceBrain

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_cli.py <username>")
        print("Example: python run_cli.py jdoe99")
        sys.exit(1)

    target = sys.argv[1]
    
    print(f"[*] Initializing Nexis Agent for target: {target}...")
    brain = IntelligenceBrain()
    
    print("[*] Running Investigation Pipeline...")
    result = brain.investigate(target)
    
    print("\n" + "="*50)
    print("REPORT OUTPUT")
    print("="*50)
    print(json.dumps(result, indent=2))
    print("="*50)

if __name__ == "__main__":
    main()
