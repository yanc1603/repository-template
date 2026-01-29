# Modular Full-Stack Template

A resilient, "Plug-and-Play" template for rapid development using **FastAPI** (Backend) and **Vanilla JS Modules** (Frontend).

The core goal of this template is **Modularity**. 
- **Decoupled Features**: You can add or remove feature folders without breaking the application.
- **Dynamic Loading**: Use the file system to manage your features. Dropping a folder in the right place automatically registers it.
- **Resilience**: Missing modules are skipped gracefully, they do not crash the app.

## Quick Start

This is a single-repo full-stack application. The Backend serves the Frontend.

1. **Setup Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Open Browser**:
   Visit `http://localhost:8000`.

## Project Structure

```text
repository-template/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── config.py       # Configuration loader
│   │   │   ├── database.py     # Database connection
│   │   │   └── modules/        # Dynamic Feature Modules
│   │   │       ├── auth/       # Authentication Logic
│   │   │       └── playground/ # Example Feature
│   │   └── main.py             # App Entry & Autoloader
│   ├── requirements.txt        # Python Dependencies
│   ├── settings.yaml           # Env Settings
│   └── README.md
├── frontend/
│   ├── css/
│   │   └── style.css           # UI Kit & Global Styles
│   ├── js/
│   │   ├── api/
│   │   │   └── client.js       # API Client (Fetch Wrapper)
│   │   └── modules/            # Feature JS Modules
│   │       ├── auth.js         # Auth Logic
│   │       └── playground.js   # Playground Logic
│   ├── index.html              # SPA Entry & Dynamic Loader
│   └── README.md
├── readme/
│   └── README.md               # Readme template
└── README.md                   # This file
```

## Features

- **Authentication**: Secure session-based login/register (JSON API).
- **Dynamic Modularity**: 
    - **Backend**: Auto-loads routers from `app/core/modules/`.
    - **Frontend**: Helper to safely load JS modules.
- **UI Kit**: Built-in CSS system for Cards, Buttons, and Deep Interactions.
