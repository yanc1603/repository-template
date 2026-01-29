# Modular Development Template

A scalable and modular template for full-stack applications using **FastAPI** (Backend) and **Vanilla JS Modules** (Frontend).

## Structure

- **backend/**: FastAPI application structured by modules.
- **frontend/**: SPA-like frontend using ES6 modules.

## Getting Started

1. **Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
2. **Frontend**:
   The backend serves the frontend at `http://localhost:8000`.

## Features

- **Modular Design**: Code organized by feature modules.
- **Authentication**: Secure Session-based Auth with bcrypt hashing.
- **Interactive Playground**: Demo module showcasing CRUD operations.
