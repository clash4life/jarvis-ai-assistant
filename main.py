#!/usr/bin/env python3
"""
JARVIS - AI Assistant Multi-App Integration
Main entry point for the application
"""

import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as uvicorn_run

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import routers
try:
    from backend.routes import health, chat, integrations
    from core.ai_engine import AIEngine
    from integrations.gmail_handler import GmailHandler
    from integrations.slack_handler import SlackHandler
    from integrations.sms_handler import SMSHandler
    from integrations.calendar_handler import CalendarHandler
    from integrations.tasks_handler import TasksHandler
except ImportError as e:
    logger.warning(f"Import warning: {e}")

# Initialize FastAPI app
app = FastAPI(
    title="JARVIS AI Assistant",
    description="Multi-app AI integration platform",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
logger.info("Initializing JARVIS services...")

try:
    ai_engine = AIEngine()
    logger.info("✓ AI Engine initialized")
except Exception as e:
    logger.error(f"✗ Failed to initialize AI Engine: {e}")
    ai_engine = None

try:
    gmail = GmailHandler()
    logger.info("✓ Gmail Handler initialized")
except Exception as e:
    logger.warning(f"⚠ Gmail Handler not available: {e}")
    gmail = None

try:
    slack = SlackHandler()
    logger.info("✓ Slack Handler initialized")
except Exception as e:
    logger.warning(f"⚠ Slack Handler not available: {e}")
    slack = None

try:
    sms = SMSHandler()
    logger.info("✓ SMS Handler initialized")
except Exception as e:
    logger.warning(f"⚠ SMS Handler not available: {e}")
    sms = None

try:
    calendar = CalendarHandler()
    logger.info("✓ Calendar Handler initialized")
except Exception as e:
    logger.warning(f"⚠ Calendar Handler not available: {e}")
    calendar = None

try:
    tasks = TasksHandler()
    logger.info("✓ Tasks Handler initialized")
except Exception as e:
    logger.warning(f"⚠ Tasks Handler not available: {e}")
    tasks = None

# Store handlers in app state
app.state.ai_engine = ai_engine
app.state.gmail = gmail
app.state.slack = slack
app.state.sms = sms
app.state.calendar = calendar
app.state.tasks = tasks

# Include routers
logger.info("Loading API routes...")

try:
    app.include_router(health.router, prefix="/api/health", tags=["health"])
    app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
    app.include_router(integrations.router, prefix="/api/integrations", tags=["integrations"])
    logger.info("✓ All routes loaded successfully")
except Exception as e:
    logger.warning(f"⚠ Some routes could not be loaded: {e}")

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "🤖 JARVIS AI Assistant is running!",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/health/status"
    }

if __name__ == "__main__":
    host = os.getenv("SERVER_HOST", "0.0.0.0")
    port = int(os.getenv("SERVER_PORT", 8000))
    debug = os.getenv("DEBUG", "True") == "True"
    
    logger.info(f"🚀 Starting JARVIS Server on {host}:{port}")
    logger.info(f"📚 API Docs available at http://{host}:{port}/docs")
    
    uvicorn_run(
        "main:app",
        host=host,
        port=port,
        reload=debug
    )