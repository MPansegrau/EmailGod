from fastapi import APIRouter
from pydantic import BaseModel
from ..services import rbac

router = APIRouter()

class AdminCommand(BaseModel):
    command: str
    args: list = []

@router.post("/command")
def admin_command(cmd: AdminCommand):
    return rbac.execute(cmd.command, cmd.args)
