from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings


# Create Async Engine (SQLite)
engine = create_async_engine(settings.database['url'], connect_args={"check_same_thread": False})
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# Dependency for Routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session