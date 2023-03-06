# from typing import Tuple
from motor.motor_asyncio import AsyncIOMotorClient

class ApplicationDbContext:
    client: AsyncIOMotorClient
    database: str

    def __init__(self) -> None:
        self.client = AsyncIOMotorClient()
        self.database = str()

context = ApplicationDbContext()

async def getDbContext() -> tuple[AsyncIOMotorClient, str]:
    return (context.client, context.database)