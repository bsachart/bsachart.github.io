# Codex CLI + Spec Kit integration

This repository includes GitHub Spec Kit prompt commands for Codex CLI under `.codex/prompts/`.

## Use in Codex CLI

From repo root:

```bash
codex
```

Then invoke prompts as:

- `/prompts:speckit.constitution`
- `/prompts:speckit.specify`
- `/prompts:speckit.plan`
- `/prompts:speckit.tasks`
- `/prompts:speckit.analyze`
- `/prompts:speckit.implement`
- `/prompts:speckit.checklist`
- `/prompts:speckit.clarify`
- `/prompts:speckit.taskstoissues`

## Notes

- Existing Antigravity integration remains unchanged.
- Codex context updates are available via `.specify/integrations/codex/scripts/update-context.sh`.
