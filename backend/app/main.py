from fastapi import FastAPI
from .routers import health, ingest, admin, tasks
from .db import init_db

app = FastAPI(title="ITC API", version="0.1.0")

app.include_router(health.router)
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.on_event("startup")
async def startup_event():
    init_db()
