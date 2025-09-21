from sqlalchemy.orm import Session
from ..models import Job
from typing import Optional

def resolve_job(db: Session, payload, entities) -> Optional[Job]:
    # Exact match by candidate
    cand = entities.get("job_number_candidate")
    if cand:
        job = db.query(Job).filter(Job.number == cand).first()
        if job:
            return job
    # TODO: alias/address/title fuzzy match (v1 simple: first job by name in subject)
    subj = (payload.subject or '')
    job = db.query(Job).filter(Job.name.ilike(f"%{subj[:15]}%")).first()
    return job
