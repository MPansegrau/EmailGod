# n8n Flows (stubs)
- Gmail/Workspace Trigger → HTTP Request to `POST /ingest/email`
- BuildingConnected Webhook → HTTP Request to `POST /ingest/bc` (placeholder)
- Daily cron → GET /tasks/overdue → send Zoom message (future)

Import Gmail trigger credentials and point to `http://api:8080/ingest/email` inside docker network.
