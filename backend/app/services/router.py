from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from ..models import Task, Person, Job
from ..config import settings

ROLE_MATRIX = {
    "Pre": {"default_owner_role": "Estimating"},
    "Post": {"default_owner_role": "PMPE"},
}

def pick_owners(db: Session, job: Job, intent: str):
    if job and job.phase == "Post":
        # Simple: choose PM/PE by job.team in future; for now pick Team A members
        pm = db.query(Person).filter(Person.team=="A", Person.role.in_(["Manager","TeamMember"])).first()
        pe = db.query(Person).filter(Person.team=="A").offset(1).first()
        return (pm, pe)
    else:
        est = db.query(Person).filter(Person.role=="Estimating").first()
        return (est, None)

def create_tasks_from_email(db: Session, payload, intent, entities, job: Job):
    owner1, owner2 = pick_owners(db, job, intent or "")
    due = None
    if intent in ("rfi","submittal","change_order","invoice","schedule"):
        days = {"rfi":2,"submittal":5,"change_order":3,"invoice":3,"schedule":2}[intent]
        due = datetime.now(timezone.utc) + timedelta(days=days)
    t = Task(job_id=job.id if job else None, title=payload.subject[:140] or "Email-derived task",
             intent=intent, owner_primary_id=owner1.id if owner1 else None,
             owner_secondary_id=owner2.id if owner2 else None, due_at=due,
             confidence=80 if job else 50)
    db.add(t); db.commit()
    # TODO: sync Trello
    return {"task_ids":[t.id], "confidence": t.confidence}
