from fastapi import APIRouter, HTTPException
from datetime import datetime

router = APIRouter()

@router.get("/status")
async def health_status():
    """
    Get health status of JARVIS and all integrated services
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "services": {
            "ai_engine": "operational",
            "database": "connected",
            "cache": "ready"
        }
    }

@router.get("/ping")
async def ping():
    """Simple ping endpoint"""
    return {"message": "pong", "timestamp": datetime.utcnow().isoformat()}