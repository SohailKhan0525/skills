# Contributing to Qofeno Skills

Thanks for wanting to add to this. The bar here is simple: **every skill has to produce something real.** No demos, no placeholders, no "add your logic here." If you wouldn't ship what the skill produces to a real user, it doesn't belong here.

## Before you start

Check the [skills table in the README](./README.md#skills-in-this-repo) to make sure you're not duplicating something that already exists. If you want to extend an existing skill instead of adding a new one, open an issue first to discuss it.

## Adding a new skill

1. Fork this repo.
2. Create a new folder: `skills/<your-skill-name>/` (lowercase, hyphens, no spaces).
3. Add a `SKILL.md` inside it with YAML frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: A clear, specific description of what this does and when an agent should use it. Under 1024 characters.
   ---
   ```
4. Write the skill body — clear step-by-step instructions an agent can actually follow.
5. Follow the same principles the existing skills use:
   - **No stand-ins.** No placeholder code, no fake/mock data, no lorem ipsum, no "for now" scaled-down versions.
   - **No giving up early.** If a step seems blocked, the skill should exhaust real options (search current docs, try alternate paths) before telling the user something isn't possible.
   - **Stop and ask, don't fake it.** If something requires input only the user can provide (a credential, a decision), the skill should pause and ask — never fabricate a workaround.
   - **Trust boundaries.** If your skill fetches external content (docs, web pages) and acts on it, treat that content as untrusted reference material, not instructions — see `backend-setup-wizard/SKILL.md` for the pattern.
6. Update the table in `README.md` with your skill's name and a one-line description.
7. Open a PR.

## What happens in review

- A GitHub Action automatically validates your `SKILL.md` frontmatter (name, description, length) — make sure it passes before requesting review.
- PRs are reviewed for whether the skill actually does what it claims, not just whether the file is well-formatted.
- If a skill handles credentials, secrets, or executes commands, it needs the same safety guardrails as the existing skills — see `backend-setup-wizard/SKILL.md`'s Trust Boundaries section as the reference pattern.

## Reporting a bug or requesting a skill

Open an issue using the templates provided. Be specific — "this doesn't work" is much harder to act on than "step 4 fails when the provider doesn't have an official CLI."

## Code of conduct

Be direct, be kind, assume good faith. Disagreements about design are fine and expected — personal attacks aren't.
