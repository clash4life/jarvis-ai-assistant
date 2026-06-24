# JARVIS AI Assistant - API Documentation

## Overview

The JARVIS API provides endpoints for natural language command processing and service integration management.

## Base URL

```
http://localhost:8000/api
```

## Endpoints

### Health Check

#### GET /health/status

Get the health status of JARVIS and all services.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00",
  "version": "1.0.0",
  "services": {
    "ai_engine": "operational",
    "database": "connected",
    "cache": "ready"
  }
}
```

### Chat/Commands

#### POST /chat/message

Send a natural language command to JARVIS.

**Request:**
```json
{
  "message": "Send an email to john@example.com saying I'll be late",
  "user_id": "user123"
}
```

**Response:**
```json
{
  "response": "✓ Email sent to john@example.com",
  "actions_taken": ["Email sent to john@example.com"],
  "context": {
    "type": "email",
    "recipient": "john@example.com",
    "subject": "I'll be late",
    "body": "Send an email to john@example.com saying I'll be late"
  }
}
```

**Example Commands:**
- "Send an email to john@example.com saying hello"
- "Schedule a meeting tomorrow at 2pm"
- "Create a task: Buy groceries"
- "Send a text to 555-1234 saying I'm on my way"
- "Post a message to #general channel"

### Integrations

#### GET /integrations/status

Get status of all integrated services.

**Response:**
```json
{
  "integrations": [
    {
      "name": "Gmail",
      "status": "connected",
      "connected": true,
      "last_sync": "2024-01-01T12:00:00"
    },
    {
      "name": "Slack",
      "status": "connected",
      "connected": true
    }
  ]
}
```

#### POST /integrations/reconnect/{service}

Reconnect to a specific service.

**Parameters:**
- `service` (path): Service name (gmail, slack, sms, calendar, tasks)

**Response:**
```json
{
  "message": "Gmail reconnection initiated"
}
```

## Error Handling

All endpoints return appropriate HTTP status codes:

- `200` - Success
- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found
- `500` - Internal Server Error
- `503` - Service Unavailable

**Error Response:**
```json
{
  "detail": "Error message here"
}
```

## Authentication

Currently, the API is open. In production, implement:
- JWT tokens
- API keys
- OAuth2 flows

## Rate Limiting

To be implemented in production.

## Webhooks

For Slack and other services that support webhooks, JARVIS will receive and process events automatically.