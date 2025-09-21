# EmailGod

Magic Task Creator — an intelligent task creation system for Peninsulators.

- Source of Truth: Postgres
- Task UI: Trello (synced)
- ChatOps: Zoom Team Chat (slash commands)
- Attachments: S3
- Events: Email + BuildingConnected (bids@ invites/docs)

## Quick Start (Dev)

1. Copy `.env.example` to `.env` and fill in secrets.
2. Run `docker compose up -d --build`.
3. Initialize and seed the database: `docker compose exec api python -m app.scripts.dev_seed`.
4. Hit the health check: http://localhost:8080/health.
5. Try the example request: `POST /ingest/email` with the payload in `examples/ingest_email.json`.

## Services

- **api**: FastAPI + SQLAlchemy
- **worker**: background queue (RQ) for heavy jobs (plan indexing)
- **db**: Postgres
- **redis**: queues & caching

## Repo Layout

```
backend/app
  ├─ routers/        # HTTP endpoints
  ├─ services/       # BC, Trello, Zoom, S3, classifier, router
  ├─ models.py       # SQLAlchemy tables
  ├─ schemas.py      # Pydantic I/O
  ├─ config.py       # Settings (.env)
  ├─ db.py           # Engine/session, migrate on boot (simple)
  └─ scripts/        # seeding, utilities
config/
  ├─ role_matrix.yaml
  ├─ rbac_policies.yaml
  ├─ job_patterns.yaml
  └─ vocabulary.yaml
n8n/
  └─ README.md
```
