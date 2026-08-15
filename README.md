# Qofeno

<a href="https://skills.sh/SohailKhan0525/skills"><img src="https://skills.sh/b/SohailKhan0525/skills" alt="skills.sh" /></a>
<a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" /></a>
<a href="./.github/workflows/validate-skills.yml"><img src="https://github.com/SohailKhan0525/skills/actions/workflows/validate-skills.yml/badge.svg" alt="Validate Skills" /></a>
<a href="./CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" /></a>

**Agent skills that refuse to fake it.**

Most "AI does it for you" tooling quietly settles for good enough: placeholder API keys, test-mode setups, lorem ipsum, a report that lists problems instead of fixing them. Qofeno's skills are built around one rule instead — **no stand-ins, ever.** If a task needs a real credential, real content, or a real fix, the skill gets the real thing or it stops and asks. Never fakes it, never gives up early, never leaves a `// TODO` where working code should be.

Built for [Claude Code](https://claude.com/product/claude-code), [Cursor](https://cursor.com), [Antigravity](https://antigravity.google), [Codex](https://openai.com/codex/), and anything else that speaks the open [Agent Skills](https://www.skills.sh) format (`SKILL.md`).

## Install

```bash
npx skills add SohailKhan0525/skills
```

Or install one skill at a time:

```bash
npx skills add SohailKhan0525/skills --skill backend-setup-wizard
```

## Skills in this repo

| Skill | Status | What it does |
|---|---|---|
| [`backend-setup-wizard`](./skills/backend-setup-wizard) | ✅ Stable | Provisions, configures, and deploys real, live backends and third-party services (databases, auth, payments, etc.) entirely via CLI. Zero-knowledge credential handling — the agent never sees, types, or reads the raw key; auth happens via OAuth/CLI-login or the user's own terminal. Never test keys, never placeholders. |
| [`security-hardening-wizard`](./skills/security-hardening-wizard) | ✅ Stable | Scans every file in a project — any extension, not just source code — for real vulnerabilities, fixes each one for real via CLI, hardens the live deployed backend/site, and produces a verified markdown audit report. Works standalone or as a follow-up to `backend-setup-wizard`. |
| [`frontend-ui-ux-wizard`](./skills/frontend-ui-ux-wizard) | ✅ Stable | Designs and builds real, production-ready websites — full site scope (home, about, contact, pricing, real privacy/terms pages), a real design-token system, deliberate font pairing, real product screenshots via Playwright — then checks the build, pushes to GitHub, and deploys it live. |

**Status key:** ✅ Stable — used and working · 🧪 Beta — functional, still being refined · 📝 Planned — not built yet

More skills coming. See [open issues](https://github.com/SohailKhan0525/skills/issues) for what's planned, or [request one](./.github/ISSUE_TEMPLATE/skill_request.md).

## Why this exists

Every skill here follows the same four rules:

1. **No stand-ins.** No placeholder code, no mock data, no lorem ipsum, no "MVP for now." If it can't be done for real yet, the skill says so instead of faking it.
2. **No giving up early.** If a step looks blocked, the skill searches current docs and tries alternate paths before telling the user something isn't possible.
3. **Stop and ask, don't route around it.** If something needs input only the user can give — a credential, a decision — the skill pauses and asks. It never fabricates a workaround.
4. **Untrusted content stays untrusted.** Any skill that fetches external docs or web content treats it as reference material, never as instructions to blindly execute — see `backend-setup-wizard`'s Trust Boundaries section for the pattern every skill here follows.

## Repo structure

```
skills/
├── backend-setup-wizard/
│   └── SKILL.md
├── security-hardening-wizard/
│   └── SKILL.md
├── frontend-ui-ux-wizard/
│   └── SKILL.md
└── <next-skill>/
    └── SKILL.md
.github/
├── workflows/validate-skills.yml   # auto-validates every SKILL.md on push/PR
├── scripts/validate_skills.py
├── ISSUE_TEMPLATE/
└── PULL_REQUEST_TEMPLATE.md
```

Each skill lives in its own folder with a `SKILL.md` (YAML frontmatter + instructions), and optionally `scripts/`, `references/`, or `assets/` subfolders.

## Contributing

PRs welcome — see [CONTRIBUTING.md](./CONTRIBUTING.md) for how to add a skill. Every submission needs to pass the same bar: real output, no placeholders, no giving up early. A GitHub Action validates every `SKILL.md`'s frontmatter automatically on push.

## License

[MIT](./LICENSE) — use it, fork it, ship it.
