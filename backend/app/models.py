from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, JSON, Index
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True)
    gc = Column(String)
    phase = Column(String, default="Pre")
    aliases = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String)
    role = Column(String)  # Exec, Manager, TeamMember, Estimating, Admin
    team = Column(String, nullable=True)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    title = Column(String, nullable=False)
    intent = Column(String, nullable=True)
    owner_primary_id = Column(Integer, ForeignKey("people.id"), nullable=True)
    owner_secondary_id = Column(Integer, ForeignKey("people.id"), nullable=True)
    due_at = Column(DateTime, nullable=True)
    status = Column(String, default="open")
    confidence = Column(Integer, default=100)
    source_email_id = Column(Integer, ForeignKey("emails.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    job = relationship("Job")
    owner_primary = relationship("Person", foreign_keys=[owner_primary_id])
    owner_secondary = relationship("Person", foreign_keys=[owner_secondary_id])

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True)
    message_id = Column(String, unique=True, index=True)
    subject = Column(String)
    sender = Column(String, index=True)
    to = Column(JSON, default=list)
    cc = Column(JSON, default=list)
    sent_at = Column(DateTime, nullable=True)
    body_preview = Column(String)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=True)
    parsed = Column(JSON, default=dict)  # extracted entities

class Activity(Base):
    __tablename__ = "activity"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    event = Column(String)
    meta = Column(JSON, default=dict)
    at = Column(DateTime, default=datetime.utcnow)

Index("idx_email_message", Email.message_id)
