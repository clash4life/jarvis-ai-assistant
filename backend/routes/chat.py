from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class ChatMessage(BaseModel):
    message: str
    context: Optional[dict] = None
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    actions_taken: list = []
    context: dict = {}

@router.post("/message", response_model=ChatResponse)
async def send_message(request: Request, chat_msg: ChatMessage):
    """
    Send a natural language message to JARVIS AI
    The AI will parse the intent and take appropriate actions across integrated apps
    
    Example:
    - "Send an email to john@example.com saying I'll be late"
    - "Schedule a meeting tomorrow at 2pm"
    - "Show me my unread emails"
    - "Create a task: Buy groceries"
    """
    
    try:
        ai_engine = request.app.state.ai_engine
        
        if not ai_engine:
            raise HTTPException(status_code=503, detail="AI Engine not available")
        
        # Parse intent from message
        intent = await ai_engine.parse_intent(chat_msg.message)
        
        # Execute actions based on intent
        actions_taken = []
        response_text = ""
        
        if intent["type"] == "email":
            gmail_handler = request.app.state.gmail
            if gmail_handler:
                result = await gmail_handler.send_email(
                    to=intent["recipient"],
                    subject=intent.get("subject", "No subject"),
                    body=intent["body"]
                )
                actions_taken.append(f"Email sent to {intent['recipient']}")
                response_text = f"✓ Email sent to {intent['recipient']}"
        
        elif intent["type"] == "calendar":
            calendar_handler = request.app.state.calendar
            if calendar_handler:
                result = await calendar_handler.create_event(
                    title=intent["title"],
                    start_time=intent["start_time"],
                    end_time=intent["end_time"]
                )
                actions_taken.append(f"Meeting scheduled: {intent['title']}")
                response_text = f"✓ Meeting scheduled: {intent['title']}"
        
        elif intent["type"] == "task":
            tasks_handler = request.app.state.tasks
            if tasks_handler:
                result = await tasks_handler.create_task(
                    title=intent["title"],
                    description=intent.get("description", "")
                )
                actions_taken.append(f"Task created: {intent['title']}")
                response_text = f"✓ Task created: {intent['title']}"
        
        elif intent["type"] == "sms":
            sms_handler = request.app.state.sms
            if sms_handler:
                result = await sms_handler.send_sms(
                    to=intent["phone"],
                    message=intent["body"]
                )
                actions_taken.append(f"SMS sent to {intent['phone']}")
                response_text = f"✓ Text sent to {intent['phone']}"
        
        elif intent["type"] == "slack":
            slack_handler = request.app.state.slack
            if slack_handler:
                result = await slack_handler.send_message(
                    channel=intent["channel"],
                    message=intent["body"]
                )
                actions_taken.append(f"Slack message sent to {intent['channel']}")
                response_text = f"✓ Slack message sent"
        
        else:
            response_text = await ai_engine.generate_response(chat_msg.message)
        
        return ChatResponse(
            response=response_text or "Command processed",
            actions_taken=actions_taken,
            context=intent
        )
    
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history")
async def get_chat_history(request: Request, limit: int = 50):
    """
    Get chat history
    """
    return {
        "history": [],
        "total": 0,
        "limit": limit
    }