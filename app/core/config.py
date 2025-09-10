import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REDIS_HOST: str = "wordcloud-redis"
    REDIS_PORT: int = 6379
    MODEL_URL: str = "http://inference-service:8001"

    class Config:
        env_file = ".env"

settings = Settings()
