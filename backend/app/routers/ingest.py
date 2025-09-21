from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..schemas import EmailIn, IngestResult
from ..services import classifier, job_resolver, router as task_router, trello_client
from ..models import Email, Task

router = APIRouter()

@router.post("/email", response_model=IngestResult)
def ingest_email(payload: EmailIn):
    # idempotency
    db: Session = SessionLocal()
    try:
        exists = db.query(Email).filter(Email.message_id == payload.message_id).first()
        if exists:
            return IngestResult(job_number=None, intent=None, created_tasks=[], confidence=100, notes="Duplicate message-id ignored")
        # classify
        intent, entities, priority_score = classifier.classify_email(payload)
        # resolve job
        job = job_resolver.resolve_job(db, payload, entities)
        # route
        result = task_router.create_tasks_from_email(db, payload, intent, entities, job)
        # store email stub
        db_email = Email(message_id=payload.message_id, subject=payload.subject, sender=payload.sender,
                         to=payload.to, cc=payload.cc, sent_at=payload.sent_at, body_preview=(payload.body_text or "")[:500],
                         job_id=job.id if job else None, parsed={"intent": intent, "entities": entities, "score": priority_score})
        db.add(db_email); db.commit()
        return IngestResult(job_number=job.number if job else None, intent=intent, created_tasks=result["task_ids"], confidence=result["confidence"])
    finally:
        db.close()
