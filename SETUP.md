# 🔧 JARVIS Setup Guide

## Prerequisites

- Python 3.9+
- pip or conda
- Git
- API keys for services (see below)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/clash4life/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
```

### 5. Configure API Keys

You'll need API keys for:

- **OpenAI/Claude** - For AI engine
- **Gmail** - Google Cloud Console OAuth2
- **Slack** - Slack App credentials
- **Twilio** - For SMS capabilities
- **Google Calendar** - Google Cloud Console
- **Todoist** - Todoist API token

### 6. Run the server

```bash
python main.py
```

Server will start at `http://localhost:8000`

## API Key Setup

### Gmail Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Gmail API
4. Create OAuth2 credentials (Desktop application)
5. Download JSON and add to `.env`

### Slack Setup
1. Go to [Slack App Directory](https://api.slack.com/apps)
2. Create new app
3. Enable Socket Mode
4. Copy Bot Token and add to `.env`

### Twilio Setup
1. Sign up at [Twilio](https://www.twilio.com/)
2. Get your Account SID and Auth Token
3. Get a Twilio phone number
4. Add to `.env`

### Google Calendar Setup
1. Same Google Cloud Console project as Gmail
2. Enable Google Calendar API
3. Use same OAuth2 credentials

## Docker Setup

```bash
docker-compose up
```

## Running Tests

```bash
pytest tests/
```

## Documentation

See `/docs` folder for detailed API documentation.