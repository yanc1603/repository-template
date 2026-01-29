from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings


# Create Async Engine (SQLite)
# The engine is the starting point for any SQLAlchemy application.
engine = create_async_engine(settings.database['url'], connect_args={"check_same_thread": False})

# Create a configured "Session" class
# This factory will generate new Session objects when called.
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy declarative models.
    """
    pass

# Dependency for Routes
async def get_db():
    """
    Dependency that provides a database session for a request.
    
    Yields:
        AsyncSession: The database session.
        
    Ensures the session is closed after the request is finished.
    """
    async with AsyncSessionLocal() as session:
        yield session