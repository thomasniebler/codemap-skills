# CODEMAP Skills

Reusable GitHub Copilot assets for a hierarchical repository navigation workflow built around `CODEMAP.md` files.

![Illustration of a developer using a repository map to guide coding-assistant navigation](assets/codemap-workflow.png)

## What this repo contains

- `skills/analyze-submodule-map/SKILL.md` - a skill that tells Copilot to read the root `CODEMAP.md`, then the nearest child map, then only the relevant source files
- `skills/maintain-codemap/SKILL.md` - guidance (and `scripts/check_codemaps.py`) for keeping maps lean: size budgets, structure-over-behavior, hierarchical splitting, drift checks
- `.github/prompts/setup-codemap.prompt.md` - a reusable prompt for setting up the CODEMAP hierarchy in another repository
- `snippets/copilot-instructions-snippet.md` - the instruction snippet to add to a target repository's `.github/copilot-instructions.md`

## Install

```bash
# any agent (Copilot, Claude Code, Cursor, ...) via the Agent Skills CLI
npx skills add thomasniebler/codemap-skills

# Claude Code plugin marketplace
/plugin marketplace add thomasniebler/codemap-skills
/plugin install codemap@codemap-skills
```

Skills live in `skills/<name>/SKILL.md` (open Agent Skills format). `.github/skills/` contains symlinks so the skills are also active in this repository itself.

## How to reuse it (manual)

1. Copy both skill folders (`analyze-submodule-map`, `maintain-codemap`) into `.github/skills/` in the target repository.
2. Copy the setup prompt into `.github/prompts/setup-codemap.prompt.md` in the target repository.
3. Add the instruction snippet from `snippets/copilot-instructions-snippet.md` to the target repository's `.github/copilot-instructions.md`.
4. Run `python .github/skills/maintain-codemap/scripts/check_codemaps.py` from your check task or pre-commit.
5. Run the setup prompt to generate the repository's root and child `CODEMAP.md` files.

## Notes

This repository is the reusable source of truth for the skill assets. Copilot only treats the skill as active inside repositories that actually include the skill files under `.github/skills/` locally.

## License

MIT, see [LICENSE](LICENSE).
