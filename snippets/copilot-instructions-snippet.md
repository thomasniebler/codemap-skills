## Default navigation workflow

- For repository navigation, start with the root `CODEMAP.md` and then follow the nearest child `CODEMAP.md` for the area you are changing.
- Use the skill in `.github/skills/analyze-submodule-map/` as the default way to understand a submodule before doing broader ad-hoc searching.
- Only fall back to wider repository searches when the relevant code map is missing, stale, or insufficient for the task.

## Keeping code maps useful

- Update the affected `CODEMAP.md` in the same change whenever packages, entry points, routes, pages, or jobs are added, removed, or renamed.
- Follow `.github/skills/maintain-codemap/`: maps are navigation aids only, stay within the size budget, split into child maps instead of growing, and link to docs for behavior.
- Run the codemap check script as part of the normal check task.
