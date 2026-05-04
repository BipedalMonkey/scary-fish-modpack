import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path("./mods")

url_pattern = re.compile(r'url\s*=\s*["\'](.*?)["\']')

def fix_url(url: str) -> str:
    # Only encode spaces, not full re-encoding
    return url.replace(" ", "%20")

for file in ROOT.rglob("*.toml"):
    text = file.read_text(encoding="utf-8")
    new_text = url_pattern.sub(
        lambda m: f'url = "{fix_url(m.group(1))}"',
        text
    )

    if new_text != text:
        file.write_text(new_text, encoding="utf-8")
        print("Fixed:", file)