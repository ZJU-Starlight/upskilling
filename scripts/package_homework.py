"""Build the deterministic, UTF-8 Markdown worksheet download using stdlib only."""

from __future__ import annotations

import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "homework" / "session-03"
OUTPUT = ROOT / "docs" / "assets" / "downloads" / "session-03-homework.zip"
PREFIX = "session-03-homework"
TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def main() -> None:
    sources = {
        "README.md": SOURCE / "README.md",
        "worksheet.md": SOURCE / "worksheet.md",
        "reference/answers.md": SOURCE / "answers.md",
        "images/study-desk.png": ROOT / "docs" / "assets" / "images" / "study-desk.png",
    }
    missing = [str(path.relative_to(ROOT)) for path in sources.values() if not path.is_file()]
    if missing:
        raise SystemExit("Cannot package homework; missing files: " + ", ".join(missing))

    worksheet = sources["worksheet.md"].read_text(encoding="utf-8")
    questions = re.findall(r"<!-- Q(\d{2})：", worksheet)
    expected = [f"{number:02}" for number in range(1, 13)]
    if questions != expected:
        raise SystemExit("Worksheet must contain Q01 through Q12 exactly once, in order.")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for archive_name, path in sorted(sources.items()):
            data = path.read_bytes()
            if path.suffix == ".md":
                data = data.decode("utf-8").replace("\r\n", "\n").encode("utf-8")
            info = zipfile.ZipInfo(f"{PREFIX}/{archive_name}", date_time=TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    with zipfile.ZipFile(OUTPUT) as archive:
        if archive.testzip() is not None:
            raise SystemExit("Homework ZIP failed integrity check.")
    print(f"Built {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size:,} bytes, 12 questions)")


if __name__ == "__main__":
    main()
