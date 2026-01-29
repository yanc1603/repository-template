from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Any, Dict
import datetime

router = APIRouter(prefix="/interactions", tags=["Interactions"])

class InteractionData(BaseModel):
    type: str
    value: Any = None
    extra: Dict[str, Any] = None

@router.post("/echo")
async def echo_interaction(data: InteractionData):
    """
    Echoes back the received interaction data with a timestamp.
    """
    return {
        "received_at": datetime.datetime.now().isoformat(),
        "data": data.dict(),
        "message": f"Server processed {data.type} interaction."
    }
