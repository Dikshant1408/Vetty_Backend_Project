from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Vetty Crypto API"
    APP_VERSION: str = "1.0.0"
    JWT_SECRET: str = "supersecret"  # or load from .env
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 60
    COINGECKO_BASE_URL: str = "https://api.coingecko.com/api/v3"

    class Config:
        env_file = ".env"

settings = Settings()
