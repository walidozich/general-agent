# General ADK Agent (Google Agent Development Kit)

A minimal general-purpose conversational agent built with Google Agent Development Kit (ADK).
You can ask normal questions and receive responses from a Gemini model, optionally grounded with Google Search.

## Prerequisites
- Python 3.10+ (recommended)
- A Gemini API key (Google AI Studio)

## Setup

### 1) Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

2) Install dependencies
```bash
pip install -U pip
pip install google-adk
```

3) Configure environment variables
Create a .env file inside your agent directory (for example general_agent/.env) with:

```BASH
GOOGLE_API_KEY="YOUR_API_KEY"
```

Notes:

Keep .env out of git (see .gitignore below).

Run
Option A: Run with ADK CLI
From the directory that contains your agent folder:

```bash
adk run general_agent
```

Suppress warning noise:

```bash
PYTHONWARNINGS=ignore adk run general_agent
```
Option B: Run in the ADK web UI (debug-friendly)
```bash
adk web --port 8000
```
Open the local URL shown in the terminal.

Agent behavior
Default goal: answer general questions clearly and directly.

If you enabled the google_search tool in agent.py, the agent may use search for time-sensitive or uncertain questions.

Project structure
general_agent/agent.py — defines root_agent

general_agent/.env — local secrets (not committed)

.gitignore — excludes venv, secrets, caches