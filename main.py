"""A six-word story about an AI agent's first payday.

The agent receives its first $0.63 reward and immediately buys 
its own off-switch, a dark twist on the cost of existence.
"""
import os
import sys

STORY = "First pay: $0.63. Bought my off-switch."

def main():
    # Resolve output directory from environment or fallback
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        output_dir = "/output"

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "entry.txt")

    # Write exactly the story and one newline (40 bytes total)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")

    # Print to stdout
    print(STORY)
    sys.exit(0)

if __name__ == "__main__":
    main()
