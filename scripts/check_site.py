"""Check local HTML links/assets without accessing the network.

Usage: python scripts/check_site.py [site] [--base-path /upskilling/]
"""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class LocalReferences(HTMLParser):
    """Collect navigable links and resources that must exist in the build."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attribute = {
            "a": "href",
            "img": "src",
            "script": "src",
            "link": "href",
            "source": "src",
            "video": "poster",
        }.get(tag)
        if attribute:
            value = dict(attrs).get(attribute)
            if value:
                self.references.add(value)


def check_site(site_dir: Path, base_path: str) -> tuple[int, list[str]]:
    root = site_dir.resolve()
    if not (root / "index.html").is_file():
        return 0, [f"Site entry not found: {root / 'index.html'}"]

    base_path = "/" + base_path.strip("/") + "/" if base_path.strip("/") else "/"
    checked = 0
    failures: list[str] = []
    for page in sorted(root.rglob("*.html")):
        parser = LocalReferences()
        parser.feed(page.read_text(encoding="utf-8"))
        for reference in sorted(parser.references):
            parsed = urlsplit(reference)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            local_path = unquote(parsed.path)
            page_name = page.relative_to(root).as_posix()
            if local_path.startswith("/"):
                if not local_path.startswith(base_path):
                    failures.append(
                        f"{page_name}: {reference} omits the project prefix {base_path}"
                    )
                    continue
                target = root / local_path[len(base_path):]
            else:
                target = page.parent / local_path
            target = target.resolve()
            if not target.is_relative_to(root):
                failures.append(f"{page_name}: {reference} leaves the built site")
                continue
            if target.is_dir():
                target = target / "index.html"
            checked += 1
            if not target.is_file():
                failures.append(f"{page_name}: missing {reference}")
    return checked, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "site_dir", nargs="?", type=Path,
        default=Path(__file__).resolve().parents[1] / "site",
    )
    parser.add_argument("--base-path", default="/upskilling/")
    args = parser.parse_args()
    checked, failures = check_site(args.site_dir, args.base_path)
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        print(f"Failed: {len(failures)} broken local references.")
        return 1
    print(f"Checked {checked} local links/assets; all targets exist.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
