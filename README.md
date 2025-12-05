🪙 Vetty Backend Project — Cryptocurrency Market API

Built with: FastAPI • JWT Auth • CoinGecko API • Docker • CI/CD • Unit Tests

<!-- GitLab Badges (replace with your actual links after setting up CI/CD) -->

🚀 Overview

This project is a backend API built as part of the Vetty Technical Assessment. The API fetches real-time cryptocurrency market data using the CoinGecko API and exposes it through clean REST endpoints with JWT-based authentication.

The backend is designed to be production-ready with the following key features:

FastAPI (High-performance ASGI framework)

JWT Authentication for secure access control

Paginated crypto market data endpoints

Dockerized deployment for environment consistency

CI pipeline (using GitHub Actions/GitLab CI) for automated testing

Pytest-based unit tests with API mocking for reliability

Ruff + Black for standardized linting & formatting

Modular, scalable folder structure

📁 Project Structure

The repository maintains a clean and logical structure for scalability:

Vetty_Backend_Project/
│
├── app/                          # Core application logic
│   ├── api/                      # REST API Endpoints (Controllers)
│   │   ├── auth.py               # Authentication routes
│   │   ├── coins.py              # Cryptocurrency coins data routes
│   │   ├── categories.py         # Coin categories routes
│   │   └── health.py             # Health check endpoint
│   │
│   ├── core/                     # Configuration and core utilities
│   │   ├── auth.py               # JWT logic and dependency injection
│   │   └── config.py             # Environment configuration (Pydantic settings)
│   │
│   ├── services/                 # External API integration (CoinGecko client)
│   │   └── coingecko.py
│   │
│   └── main.py                   # FastAPI application entry point
│
├── tests/                        # Unit and integration tests
│   ├── test_auth.py
│   ├── test_coins.py
│   └── test_categories.py
│
├── Dockerfile                    # Container build instructions
├── docker-compose.yml            # Defines the application service
├── requirements.txt              # Python dependencies
├── .dockerignore
├── pytest.ini                    # Pytest configuration
├── ruff.toml                     # Ruff linter configuration
├── pyproject.toml                # Project metadata and configuration (Black)
└── README.md


🔐 Authentication

All API routes, except /health and /auth/token, require a valid JWT passed in the request header.

Get Token

POST /auth/token

Parameter

Type

Description

username

string

The user identity (e.g., "demo")

Request Example:

{
  "username": "demo"
}


Response Example:

{
  "access_token": "<jwt_string_here>",
  "token_type": "bearer"
}


Usage

Use the obtained token in the Authorization header for all protected endpoints:

Authorization: Bearer <token_string_here>


🪙 API Endpoints

🔹 List All Coins

GET /coins/?page_num=1&per_page=10


Query Parameters: page_num (default 1), per_page (default 10)

Requires: JWT Authentication

🔹 Get Market Data for Specific Coin

GET /coins/{coin_id}


Path Parameter: coin_id (e.g., bitcoin, ethereum)

Returns: Detailed market data, including INR and CAD price conversion.

Requires: JWT Authentication

🔹 List Categories

GET /categories/


Returns: A list of all available cryptocurrency categories.

Requires: JWT Authentication

🔹 Health Check

GET /health


Returns: A simple status check (no authentication required).

📦 Running Locally (FastAPI)

Prerequisites

Python 3.9+

pip (Python package installer)

Virtual environment activation (assuming you are in the project root):

.venv\Scripts\activate


(Note: Use source .venv/bin/activate for Linux/Git Bash/WSL)

Setup and Run

Install dependencies:

pip install -r requirements.txt


Start the FastAPI application with auto-reload:

uvicorn app.main:app --reload


Documentation

Access the interactive API documentation (Swagger UI):

http://localhost:8000/docs


🧪 Running Tests

Unit tests are implemented using pytest and mock API calls using respx to ensure reliable, isolated testing without external network dependencies.

pytest -v


🐳 Docker Deployment

The application is containerized for consistent deployment across environments.

Build the Image

docker build -t vetty_api .


Run the Container (Standalone)

docker run -p 8000:8000 vetty_api


Run using Docker Compose

docker-compose up


🧹 Code Quality

The project enforces high code quality standards using industry-leading tools:

Run Ruff Linter

ruff check .


Run Black Formatter

black .


⚙️ CI/CD — GitHub Actions

The Continuous Integration workflow is managed via GitHub Actions (or can be adapted to GitLab CI):

Every push and merge request triggers the following checks defined in .github/workflows/ci.yml:

Linting (Ruff)

Formatting check (Black --check)

Unit tests (Pytest)

🌐 Tech Stack

Component

Technology

Description

Backend Framework

FastAPI

ASGI framework for building fast APIs.

Authentication

JWT

JSON Web Tokens for secure session management.

External API

CoinGecko

Primary data source for crypto market data.

Containerization

Docker

Packaging the application and its dependencies.

Testing

Pytest, respx

Framework for unit tests and API mocking.

CI/CD

GitHub Actions

Automation for testing and quality checks.

Linting

Ruff

High-performance linter.

Formatting

Black

Uncompromising code formatter.

📄 License

This project is developed for the Vetty Internship Technical Exercise.