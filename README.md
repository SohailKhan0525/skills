# Qofeno Skills

<a href="https://skills.sh/SohailKhan0525/skills"><img src="https://skills.sh/b/SohailKhan0525/skills" alt="skills.sh" /></a>

A collection of agent skills by Qofeno — reusable, real-world workflows for AI coding agents (Claude Code, Cursor, Antigravity, Codex, and more), following the open [Agent Skills](https://www.skills.sh) format.

## Install a skill

```bash
npx skills add SohailKhan0525/skills
```

Or install a specific skill from this repo once packs/scoped installs are set up.

## Skills in this repo

| Skill | Description |
|---|---|
| [`backend-setup-wizard`](./skills/backend-setup-wizard) | Provisions, configures, and deploys real, live backends and third-party services (databases, auth, payments, etc.) entirely via CLI — collects live API credentials safely into `.env`, pushes them into the deployment platform's own secret store, and gets the backend actually live in production. Never test keys, never placeholders, never stub code — if a required credential is missing, it stops and asks rather than faking anything. Always pulls current official docs before setting anything up. |
| [`security-hardening-wizard`](./skills/security-hardening-wizard) | Scans every file in a project — any extension, not just source code — for real vulnerabilities (secrets, injection risks, weak auth, insecure config), fixes each one for real via CLI, hardens the live deployed backend/site against actual attacks, and produces a markdown audit report. Works standalone on any codebase, or as a follow-up to `backend-setup-wizard`. |

More skills coming soon.

## Structure

```
skills/
├── backend-setup-wizard/
│   └── SKILL.md
├── security-hardening-wizard/
│   └── SKILL.md
└── <next-skill>/
    └── SKILL.md
```

Each skill lives in its own folder with a `SKILL.md` (YAML frontmatter + instructions), and optionally `scripts/`, `references/`, or `assets/` subfolders.

## Contributing / Adding a new skill

1. Create a new folder under `skills/<skill-name>/`.
2. Add a `SKILL.md` with `name` and `description` frontmatter.
3. Update the table above.
4. Commit and push — `npx skills add SohailKhan0525/skills` picks up all skills in the repo automatically.
