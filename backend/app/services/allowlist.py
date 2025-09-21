from ..config import settings

def is_allowed(recipient: str) -> bool:
    return recipient.lower() in [a.lower() for a in settings.allowlist_inboxes]
