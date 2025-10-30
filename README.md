# LLM_API: FastAPI + OpenAI Production-Grade Query Endpoint

Welcome to **LLM_API**! This project lets you send smart questions to a Large Language Model (LLM) like OpenAI’s GPT and get answers, all through a super-fast web API that you can use from anywhere.

***

## What Does This Project Do?

- Lets you ask smart questions to the AI using a simple web link ("endpoint").
- Handles lots of users at once efficiently.
- Keeps safe with logging, caching, and rate limits.
- Makes it easy to add more features later by using good file organization.

***

## How Does the Code Work?

### Project Structure (Folders & Files)

```text
llm_api/
├── app/
│   ├── main.py            # Starts your FastAPI app. Loads middleware and routers.
│   ├── core/
│   │   ├── config.py      # Reads secret keys and settings from the .env file.
│   │   ├── dependencies.py# Shares connections (OpenAI, Redis) across the app.
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── query.py # Handles your LLM queries.
│   ├── middleware/
│   │   ├── correlation.py # Adds a unique Trace ID to every web request.
│   ├── services/
│   │   ├── llm_service.py # Logic to talk to OpenAI and handle caching.
│   ├── tests/             # For testing your code!
├── venv/                  # Your Python environment files (ignore/change nothing here).
├── requirements.txt       # List of libraries your project needs.
├── .env                   # Your personal settings and secrets (never share this!).
├── README.md              # This file :)
```


***

## Code Explained (Simple English)

### 1. **main.py**
- Turns ON your FastAPI server, sets up all the helper pieces ("middleware"), and connects the endpoint for questions.
- It’s like the switchboard for your whole project.

### 2. **core/config.py**
- Reads secret keys (like OpenAI API KEY) and settings from the `.env` file.
- Makes sure settings are correct before your app starts (so you don’t break stuff by accident).

### 3. **core/dependencies.py**
- Creates one master connection to OpenAI and Redis so every user doesn’t make their own (this is much faster and saves computer resources).
- Shares these connections with every function that wants them.

### 4. **middleware/correlation.py**
- Adds a special tracking code (a UUID) to each request and every log message.
- Makes it easy to debug and see who did what, even when hundreds visit your app.

### 5. **api/v1/endpoints/query.py**
- This is your main question-asking endpoint.
- When you send a question, it checks the cache first, then asks OpenAI if it’s a new one.
- Returns the answer and tells you if it was "cached" or fresh.

### 6. **services/llm_service.py**
- This is the smart helper that actually talks to OpenAI and caches answers.
- If OpenAI is slow/times out, will retry a few times automatically ("tenacity").

***

## Step-by-Step Setup Instructions

### 1. **Get Everything Ready**

*Open PowerShell*

```powershell
# Make folders (if you haven't already)
mkdir llm_api
cd llm_api
# (Make subfolders as shown above)
```

### 2. **Setup Python Virtual Environment**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. **Install All Dependencies**

```powershell
pip install fastapi uvicorn openai pydantic-settings aioredis structlog tenacity python-dotenv
pip freeze > requirements.txt
```

### 4. **Create Your `.env` File**

Create `.env` (in the root folder) and add:
```
OPENAI_API_KEY=your_real_openai_key
OPENAI_MODEL=gpt-4-turbo-preview
REDIS_URL=redis://localhost:6379
LOG_LEVEL=INFO
DEBUG=True
```

### 5. **(Optional) Setup Redis for Caching**

If you want performance magic, install Docker and run Redis:
```powershell
docker pull redis
docker run -d -p 6379:6379 --name redis-server redis
```

### 6. **Run Your App!**

```powershell
uvicorn app.main:app --reload
```
- Visit: http://127.0.0.1:8000/docs — Here you can test your question endpoint!

***

## How Does the Endpoint Work?

1. You send a question (prompt) through a POST request.
2. The app first checks if the answer is cached (already stored).
3. If yes, sends cached answer instantly!
4. If no, asks OpenAI for a new answer, then stores that in the cache for next time.
5. Handles errors/retries if OpenAI is slow or busy — you almost never get an ugly crash.

***

## Key Features (Why This Is Super Efficient & Safe)

- **Trace IDs**: Every action is tracked, so bugs are super easy to find.
- **Singleton Connections**: All users share the same OpenAI/Redis connection, so the server is fast!
- **Config Safety**: Change secrets/settings in `.env`, never in code. No mistakes, and keys are always hidden.
- **Structured Logging**: Every log is clear, machine-readable, and easy to search.
- **Async Everything**: Uses Python’s async so it can talk to OpenAI, Redis, and users at the same time—no waiting!
- **Retries**: If OpenAI fails, the app will quietly try again up to 5 times.
- **Caching**: Fast answers for repeat questions, saves cost and makes things snappy.
- **Rate Limiting**: Prevents too many requests at once, so the server stays healthy.

***

## Example Request Through Swagger Docs

- Go to http://127.0.0.1:8000/docs.
- Click POST `/api/v1/query/`
- Send something like:
  ```json
  {
    "query": "What is the capital of France?"
  }
  ```
- Get a smart answer back! If you ask again soon, it'll be instant.

***

## Advanced Deployment (Docker)

- For real production, add a `Dockerfile` (see FastAPI docs) and `.dockerignore` to keep your app secure and scalable.
- Always run as a non-root user in Docker.

***

## Tips for Safety & Scaling

- Never commit your `.env` to Git!
- Document new endpoints in your README.
- Always test new features in `/tests` before deploying live.

***

## Troubleshooting

- If you see import errors, make sure:
  - You installed every library in your virtual environment (`venv`) and it’s activated.
  - VSCode uses the right Python interpreter.
- Can’t connect to Redis? Make sure Docker is running and Redis is started.

***

## Sources & Best Practices
- Modular design inspired by real production blueprints[1]
- FastAPI documentation and expert community tips[2][3]
- Robust error-handling, dependency injection, and structured logging.

***
