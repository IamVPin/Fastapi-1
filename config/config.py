from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from models.user import User
from models.student import Student


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = "mongodb://127.0.0.1:27017/testpass"

    # JWT
    print ("1")
    secret_key: str = "62a707a32f174a25acb892cd"
    algorithm: str = "HS256"
    print("2")

    class Config:
        env_file = ".env.dev"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.get_default_database(),
                      document_models=[User, Student])
