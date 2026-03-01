# detect_nbsp.py
from pathlib import Path

p = Path("spam.py")
s = p.read_text(encoding="utf-8")

found = False
for lineno, line in enumerate(s.splitlines(), 1):
    if "\u00A0" in line or "\u202F" in line:
        found = True
        print(f"Linje {lineno}: {repr(line)}")

if not found:
    print("Ingen NBSP (U+00A0) eller smal NBSP (U+202F) funnet i main.py.")