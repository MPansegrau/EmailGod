from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models import Task

router = APIRouter()

@router.get("/overdue")
def overdue():
    db: Session = SessionLocal()
    try:
        # v1 placeholder: everything open with due date in past
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        q = db.query(Task).filter(Task.status=="open", Task.due_at != None, Task.due_at < now).all()
        return [{"id":t.id,"title":t.title,"due_at":str(t.due_at),"job_id":t.job_id} for t in q]
    finally:
        db.close()
