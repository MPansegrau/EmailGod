from typing import Tuple, Dict, Any
import re

KEY_INTENTS = ['rfi','submittal','change order','invoice','schedule']

def classify_email(payload) -> Tuple[str, Dict[str, Any], int]:
    subj = (payload.subject or '').lower()
    body = (payload.body_text or '').lower()
    text = subj + ' ' + body
    intent = None
    for key in KEY_INTENTS:
        if key in text:
            intent = key.replace(' ','_')
            break
    # Extract candidate job number (simple regex; exact mapping comes from BC)
    m = re.search(r'\b\d{2}-\d{4}\b', text)
    entities = {"job_number_candidate": m.group(0) if m else None}
    has_attach = bool(payload.attachments)
    priority = (100 if entities["job_number_candidate"] else 0) + (30 if has_attach else 0) + (40 if intent else 0)
    return intent, entities, priority
