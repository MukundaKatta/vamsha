"""CLI for vamsha."""
import sys, json, argparse
from .core import Vamsha

def main():
    parser = argparse.ArgumentParser(description="Vamsha — Indian Genealogy Tracker. Family tree builder with AI-powered ancestral research.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Vamsha()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.generate(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"vamsha v0.1.0 — Vamsha — Indian Genealogy Tracker. Family tree builder with AI-powered ancestral research.")

if __name__ == "__main__":
    main()
