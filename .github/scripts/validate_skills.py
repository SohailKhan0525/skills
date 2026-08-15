#!/usr/bin/env python3
"""
Validates every skills/*/SKILL.md in this repo:
- Has YAML frontmatter delimited by ---
- Has a 'name' field matching its folder name
- Has a 'description' field, non-empty and <= 1024 characters
- Folder name is lowercase-with-hyphens
Exits non-zero (fails CI) if any skill is invalid.
"""
import re
import sys
from pathlib import Path

import yaml

MAX_DESCRIPTION_LEN = 1024
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def validate_skill(skill_dir: Path) -> list[str]:
    errors = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return [f"{skill_dir.name}: SKILL.md has no valid YAML frontmatter (must start with '---')"]

    try:
        frontmatter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        return [f"{skill_dir.name}: frontmatter is not valid YAML ({e})"]

    name = frontmatter.get("name")
    description = frontmatter.get("description")

    if not name:
        errors.append(f"{skill_dir.name}: frontmatter missing 'name'")
    elif name != skill_dir.name:
        errors.append(
            f"{skill_dir.name}: frontmatter name '{name}' does not match folder name '{skill_dir.name}'"
        )

    if not description:
        errors.append(f"{skill_dir.name}: frontmatter missing 'description'")
    elif len(description) > MAX_DESCRIPTION_LEN:
        errors.append(
            f"{skill_dir.name}: description is {len(description)} chars, "
            f"max is {MAX_DESCRIPTION_LEN}"
        )

    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", skill_dir.name):
        errors.append(
            f"{skill_dir.name}: folder name should be lowercase-with-hyphens"
        )

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    skills_dir = repo_root / "skills"

    if not skills_dir.exists():
        print("No skills/ directory found — nothing to validate.")
        return 0

    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not skill_dirs:
        print("skills/ directory is empty — nothing to validate.")
        return 0

    all_errors = []
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            all_errors.extend(errors)
        else:
            print(f"✅ {skill_dir.name}")

    if all_errors:
        print("\n❌ Validation failed:\n")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(f"\nAll {len(skill_dirs)} skill(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
