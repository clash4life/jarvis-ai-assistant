from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings"""
    
    # Server
    server_host: str = "0.0.0.0"
    server_port: int = 8000
    debug: bool = True
    log_level: str = "INFO"
    
    # Database
    database_url: str = "sqlite:///./jarvis.db"
    
    # Security
    secret_key: str = "your-secret-key-change-this"
    allowed_origins: str = "http://localhost:3000,http://localhost:8000"
    
    # OpenAI/Claude
    openai_api_key: Optional[str] = None
    claude_api_key: Optional[str] = None
    ai_model: str = "claude-3-sonnet"
    
    # Gmail
    gmail_client_id: Optional[str] = None
    gmail_client_secret: Optional[str] = None
    gmail_refresh_token: Optional[str] = None
    
    # Slack
    slack_bot_token: Optional[str] = None
    slack_app_token: Optional[str] = None
    slack_signing_secret: Optional[str] = None
    
    # Twilio
    twilio_account_sid: Optional[str] = None
    twilio_auth_token: Optional[str] = None
    twilio_phone_number: Optional[str] = None
    
    # Google Calendar
    google_calendar_id: Optional[str] = None
    
    # Todoist
    todoist_api_token: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()