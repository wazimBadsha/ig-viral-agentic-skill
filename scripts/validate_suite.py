#!/usr/bin/env python3
"""Validate that all 13 skill folders contain valid SKILL.md frontmatter."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".claude" / "skills"
NAME = re.compile(r"^[a-z0-9-]{1,64}$")


def main():
    errors = []
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if len(skill_files) != 13:
        errors.append(f"Expected 13 specialist skills, found {len(skill_files)}")
    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
            continue
        parts = text.split("---", 2)
        if len(parts) != 3:
            errors.append(f"{path.relative_to(ROOT)}: malformed frontmatter")
            continue
        front = parts[1]
        name = re.search(r"(?m)^name:\s*([^\s]+)\s*$", front)
        desc = re.search(r"(?m)^description:\s*(.+)$", front)
        if not name or not NAME.fullmatch(name.group(1)):
            errors.append(f"{path.relative_to(ROOT)}: invalid skill name")
        if not desc or len(desc.group(1)) > 1024:
            errors.append(f"{path.relative_to(ROOT)}: missing/oversized description")
    required = [
        ROOT / "SKILL.md",
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "references" / "platform-capabilities.md",
        ROOT / "references" / "safety-and-approvals.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(skill_files)} specialist skills and required suite files validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
