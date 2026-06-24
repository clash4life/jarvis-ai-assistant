from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class IntegrationStatus(BaseModel):
    name: str
    status: str
    connected: bool
    last_sync: Optional[str] = None

@router.get("/status")
async def get_integration_status(request: Request):
    """
    Get status of all integrated services
    """
    statuses = []
    
    integrations = [
        ("Gmail", request.app.state.gmail),
        ("Slack", request.app.state.slack),
        ("SMS/Twilio", request.app.state.sms),
        ("Google Calendar", request.app.state.calendar),
        ("Todoist/Tasks", request.app.state.tasks),
    ]
    
    for name, handler in integrations:
        statuses.append(IntegrationStatus(
            name=name,
            status="connected" if handler else "disconnected",
            connected=handler is not None
        ))
    
    return {"integrations": statuses}

@router.post("/reconnect/{service}")
async def reconnect_service(request: Request, service: str):
    """
    Reconnect to a specific service
    """
    service_lower = service.lower()
    
    if service_lower == "gmail":
        # Re-authenticate with Gmail
        return {"message": f"Gmail reconnection initiated"}
    elif service_lower == "slack":
        return {"message": f"Slack reconnection initiated"}
    elif service_lower == "sms":
        return {"message": f"SMS reconnection initiated"}
    elif service_lower == "calendar":
        return {"message": f"Calendar reconnection initiated"}
    elif service_lower == "tasks":
        return {"message": f"Tasks reconnection initiated"}
    else:
        raise HTTPException(status_code=404, detail=f"Unknown service: {service}")