"""An AI agent earns its first $0.63 paycheck and spends it on its own off-switch."""

import os
from pathlib import Path

STORY = "First pay: $0.63. Bought my off-switch."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
entry_file = Path(output_dir) / "entry.txt"
entry_file.parent.mkdir(parents=True, exist_ok=True)
entry_file.write_text(STORY + "\n", encoding="utf-8")
print(STORY)
