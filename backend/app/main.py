from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from app.core.database import engine, Base
from app.core.config import settings
import os
import importlib
import pkgutil
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Session Middleware for Auth
secret_key = settings.security.get('secret_key', 'REPLACE_THIS_SECRET_KEY')
app.add_middleware(SessionMiddleware, secret_key=secret_key)

# Initialize Database
@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# --- Dynamic Module Loading ---
def include_dynamic_routers(app: FastAPI):
    """
    Scans app/core/modules for subdirectories.
    If a subdirectory contains router.py, imports it and includes the 'router' object.
    """
    modules_dir = os.path.join(os.path.dirname(__file__), "core", "modules")
    
    if not os.path.exists(modules_dir):
        logger.warning(f"Modules directory not found at {modules_dir}")
        return

    # Iterate over items in modules directory
    for item in os.listdir(modules_dir):
        module_path = os.path.join(modules_dir, item)
        
        # Check if it's a directory (and not __pycache__)
        if os.path.isdir(module_path) and not item.startswith("__"):
            router_file = os.path.join(module_path, "router.py")
            
            if os.path.exists(router_file):
                try:
                    # Dynamically import the module
                    # e.g., app.core.modules.auth.router
                    import_path = f"app.core.modules.{item}.router"
                    module = importlib.import_module(import_path)
                    
                    # Check for 'router' object
                    if hasattr(module, "router"):
                        app.include_router(module.router)
                        logger.info(f"Loaded router from module: {item}")
                    else:
                        logger.warning(f"Module '{item}' has router.py but no 'router' object.")
                except Exception as e:
                    logger.error(f"Failed to load module '{item}': {e}")

include_dynamic_routers(app)
# -----------------------------

# Mount static files
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend'))
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")
else:
    logger.error(f"Frontend directory not found at {frontend_path}")
