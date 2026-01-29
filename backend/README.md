# Backend - FastAPI Modular Core

The backend is built with **FastAPI** and **SQLAlchemy**. It features a dynamic router loader that allows for true "Plug-and-Play" development.

## 🏃 Running the Backend

```bash
# From the backend/ directory
uvicorn app.main:app --reload
```

## 🧩 Dynamic Modularity

The `app/main.py` file is designed to **automatically scan** the `app/core/modules/` directory.

### How to Add a Module
1. Create a new folder: `app/core/modules/my_feature/`
2. Add a `router.py` file inside it.
3. Ensure `router.py` defines a `router = APIRouter(...)` object.
   
**That's it!** The server will automatically detect and register your new endpoints.

### How to Remove a Module
1. Simply delete (or rename) the module folder.
2. The server will restart (if reloading) and the routes will vanish. The rest of the app continues to work perfectly.

## 🔐 Auth & Security
- **Authentication**: `modules/auth`. Uses Session Middleware + bcrypt.
- **Database**: `app.db` (SQLite). Managed by `core/database.py`.
- **Config**: `core/config.py` loads `settings.yaml`.

## 📦 Core Modules Provided
- **Auth**: Login, Register, Logout, `/me` check.
- **Playground**: Example CRUD module to demonstrate database interactions.
