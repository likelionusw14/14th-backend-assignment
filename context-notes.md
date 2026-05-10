# Context Notes

## 2026-05-11

- User requested implementation from `https://likelion-pbl-five.vercel.app/django/2f044860a4f4812b91f5f192355b9d9b` and explicitly forbade commits.
- The workspace at `/Users/keemhoeyune/Desktop/DjangoApi` is not currently inside a Git repository, so no commit operation is available or planned.
- The mission requires extending the existing HTML-based Django app, not DRF or JSON APIs.
- Existing app already has `Lion` CRUD with MySQL configured in `config/settings.py`.
- Keep existing `templates/lions/` structure.
- Required relationship shape is `Lion` to `Task` as 1:N, `Lion` to `LionProfile` as 1:1, and `Lion` to `Tag` as N:M with `related_name` values for reverse access.
- Creation of a `Lion` must also create three default tasks and one empty profile inside a single transaction.
- UI scope is intentionally minimal and follows existing template style.
- `venv/bin/python manage.py test lions.tests.RelationshipModelRegistryTests.test_relationship_models_are_registered` failed before implementation because the relationship models were not registered, then passed after model implementation.
- `venv/bin/python manage.py test lions` could not create the MySQL test database because the local MySQL server is not accepting connections on `127.0.0.1:3306`.
- `venv/bin/python manage.py makemigrations --check --dry-run` reports no pending model changes, but emits the same MySQL connection warning while checking migration history.
- `venv/bin/python manage.py migrate` is blocked for the same MySQL connection reason before migrations can be applied.

## 2026-05-11 Week 10 Wrap-Up

- User requested the same process for `https://likelion-pbl-five.vercel.app/django/2f044860a4f48190af97d846f046c8dc` and still forbids commits.
- The new mission is a project wrap-up: preserve all Lion / Task / LionProfile / Tag behavior, refactor duplicate lookup logic, strengthen exception handling, add default QuerySet ordering, and write a complete README.
- The page explicitly requires `get_object_or_404` for Lion and Task lookups, POST-only mutation views, `LionProfile.objects.get_or_create(lion=lion)`, and `Meta.ordering = ['-created_at']`.
- It also lists Task addition as an expected final behavior, so this pass will add a detail-page Task creation form and view.
- README must explain project purpose, stack, run steps, ERD relationships, design rationale, transaction rollback testing, and conceptual questions about MVT and relationships.
- `venv/bin/python manage.py test lions.tests.ProjectWrapUpContractTests.test_models_define_default_latest_ordering` failed before implementation because model ordering was empty.
- After implementation, `venv/bin/python manage.py test lions.tests.ProjectWrapUpContractTests` passed 4 tests.
- `venv/bin/python manage.py makemigrations lions` generated `lions/migrations/0003_alter_lion_options_alter_task_options.py` for `Lion` and `Task` ordering.
- `venv/bin/python manage.py makemigrations --check --dry-run` reports no pending changes, with a MySQL connection warning while checking migration history.
- `venv/bin/python manage.py check` and `venv/bin/python -m compileall lions` pass.
- `venv/bin/python manage.py migrate` and `venv/bin/python manage.py test lions` remain blocked because MySQL is not accepting connections on `127.0.0.1:3306`.
