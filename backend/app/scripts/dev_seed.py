from ..db import SessionLocal, init_db
from ..models import Person, Job

def run():
    init_db()
    db = SessionLocal()
    try:
        # Seed people
        people = [
            Person(email="mpansegrau@peninsulators.com", name="Max Pansegrau", role="Admin", team=None),
            Person(email="ryanh@peninsulators.com", name="Ryan Haisley", role="Manager", team="A"),
            Person(email="jsantos@peninsulators.com", name="Jose Santos", role="TeamMember", team="A"),
            Person(email="klester@peninsulators.com", name="Kristen Lester", role="Manager", team="B"),
            Person(email="jcollins@peninsulators.com", name="Jacob Collins", role="TeamMember", team="B"),
            Person(email="tromo@peninsulators.com", name="Tony Romo", role="Manager", team="C"),
            Person(email="dclevenger@peninsulators.com", name="Dylan Clevenger", role="TeamMember", team="C"),
            Person(email="estimating@peninsulators.com", name="Estimating Team", role="Estimating", team=None),
        ]
        for p in people:
            if not db.query(Person).filter(Person.email==p.email).first():
                db.add(p)
        # Seed example jobs
        jobs = [
            Job(number="23-1987", name="Veterans Home - Yountville", gc="Devcon", phase="Pre", aliases=["Yountville Veterans"]),
            Job(number="24-1234", name="Google Caribbean 100", gc="Google", phase="Post", aliases=["Caribbean 100"]),
        ]
        for j in jobs:
            if not db.query(Job).filter(Job.number==j.number).first():
                db.add(j)
        db.commit()
        print("Seeded initial people and jobs.")
    finally:
        db.close()

if __name__ == "__main__":
    run()
