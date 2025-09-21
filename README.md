<<<<<<< HEAD
# EmailGod
Magic Task Creator
=======
# Intelligent Task Creation (ITC) — MVP

Cloud-first task creation system for Peninsulators.
- Source of Truth: Postgres
- Task UI: Trello (synced)
- ChatOps: Zoom Team Chat (slash commands)
- Attachments: S3
- Events: Email + BuildingConnected (bids@ invites/docs)

## Quick Start (Dev)

1) Copy `.env.example` to `.env` and fill secrets.
2) `docker compose up -d --build`
3) Initialize DB and seed: `docker compose exec api python -m app.scripts.dev_seed`
4) Hit health: http://localhost:8080/health
5) Try example: `POST /ingest/email` with `examples/ingest_email.json`

## Services
- api: FastAPI + SQLAlchemy
- worker: background queue (RQ) for heavy jobs (plan indexing)
- db: Postgres
- redis: queues & caching

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
>>>>>>> 4a68e49 (Initial commit)
