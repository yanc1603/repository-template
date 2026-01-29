from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from app.core.database import engine, Base
# Corrected path based on file system structure analysis
from app.core.modules.playground.router import router as playground_router
from app.core.modules.auth.router import router as auth_router
from app.core.config import settings
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Session Middleware for Auth
# Fallback secret key if not set (for safety in dev)
secret_key = settings.security.get('secret_key', 'REPLACE_THIS_SECRET_KEY')
app.add_middleware(SessionMiddleware, secret_key=secret_key)

#Initialize Database
@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(playground_router)
app.include_router(auth_router)

# Mount static files
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend'))
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")
