from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

class EmailIn(BaseModel):
    message_id: str
    subject: str
    sender: str
    to: List[str]
    cc: List[str] = []
    sent_at: Optional[datetime] = None
    body_text: Optional[str] = ""
    attachments: List[dict] = []  # {filename, content_type, size_bytes, s3_key?}

class IngestResult(BaseModel):
    job_number: Optional[str]
    intent: Optional[str]
    created_tasks: List[int]
    confidence: int
    notes: Optional[str] = None
