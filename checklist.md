# Django Relationship Mission Checklist

- [x] Extract mission requirements from the LIKELION PBL page.
- [x] Inspect existing `lions` models, views, URLs, templates, admin, and tests.
- [x] Add failing tests for `Task`, `LionProfile`, `Tag`, admin registration, and creation transaction behavior.
- [x] Implement relationship models and admin configuration.
- [x] Add model migration.
- [x] Add tests for detail page task/profile/tag display and actions.
- [x] Implement task completion toggle, profile edit, and tag toggle views.
- [x] Expand templates under `lions/templates/lions/` without moving the directory structure.
- [ ] Apply migration against MySQL.
- [ ] Run the relevant Django test suite and report exact verification output.

## Django Project Wrap-Up Checklist

- [x] Extract week 10 project wrap-up requirements from the LIKELION PBL page.
- [x] Inspect existing `lions` implementation after week 9 changes.
- [x] Add failing tests for model ordering, 404 behavior, POST-only actions, Task creation, and README coverage.
- [x] Refactor object lookup to `get_object_or_404`.
- [x] Add `Meta.ordering` to relationship models.
- [x] Implement Task creation from the detail page with empty-title validation.
- [x] Keep all mutation views POST-only.
- [x] Write `README.md` with introduction, stack, setup, ERD, design rationale, transaction testing, and MVT notes.
- [x] Run verification commands and record any environment blockers.
