🪙 Vetty Backend Project — Cryptocurrency Market API
Built with FastAPI • JWT Auth • CoinGecko API • Docker • CI/CD • Unit Tests
🚀 Overview

This project is a backend API built as part of the Vetty Technical Assessment.
The API fetches real-time cryptocurrency market data using the CoinGecko API and exposes it through clean REST endpoints with JWT-based authentication.

The backend is production-ready with:

FastAPI (ASGI framework)

JWT Authentication

Paginated crypto endpoints

Dockerized deployment

CI pipeline (GitHub Actions)

Pytest-based unit tests with API mocking

Ruff + Black linting & formatting

Modular, scalable folder structure

📁 Project Structure
Vetty_Backend_Project/
│
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── coins.py
│   │   ├── categories.py
│   │   └── health.py
│   │
│   ├── core/
│   │   ├── auth.py
│   │   └── config.py
│   │
│   ├── services/
│   │   └── coingecko.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_coins.py
│   └── test_categories.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── pytest.ini
├── ruff.toml
├── pyproject.toml
└── README.md

🔐 Authentication

All API routes except /health and /auth/token require JWT authentication.

Get Token

POST /auth/token

Request:
{
  "username": "demo"
}

Response:
{
  "access_token": "<jwt>",
  "token_type": "bearer"
}


Use the token in headers:

Authorization: Bearer <token>

🪙 API Endpoints
🔹 List All Coins

GET /coins/?page_num=1&per_page=10

🔹 Get Market Data for Specific Coin

GET /coins/{coin_id}
Returns INR & CAD price.

🔹 List Categories

GET /categories/

🔹 Health Check

GET /health

📦 Running Locally (FastAPI)
uvicorn app.main:app --reload


Swagger UI:

http://localhost:8000/docs

🧪 Running Tests
pytest -v


Mocks are used for API calls so no internet required.

🐳 Docker Deployment
Build:
docker build -t vetty_api .

Run:
docker run -p 8000:8000 vetty_api


or using compose:

docker-compose up

🧹 Code Quality
Run Ruff Linter:
ruff check .

Run Black Formatter:
black .

⚙️ CI/CD — GitHub Actions

Every push triggers:

Linting (Ruff)

Formatting check (Black)

Unit tests (Pytest)

Workflow file: .github/workflows/ci.yml

🌐 Tech Stack
Component	Technology
Backend Framework	FastAPI
Auth	JWT
External API	CoinGecko
Containerization	Docker
Testing	Pytest, respx
CI/CD	GitHub Actions
Linting	Ruff
Formatting	Black
📄 License

This project is developed for the Vetty Internship Technical Exercise.