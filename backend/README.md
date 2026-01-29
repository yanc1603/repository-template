# Backend Module Template

Built with **FastAPI**, **SQLAlchemy (Async)**, and **Pydantic**.

## Structure

```
app/
├── core/
│   ├── config.py       # Pydantic Settings
│   ├── database.py     # DB Engine & Session
│   └── modules/        # Feature Modules
│       ├── auth/       # Authentication Logic
│       └── playground/ # Example CRUD Logic
└── main.py             # Entry Point
```

## functionality

- **Auth Module**: Handles Registration, Login (Sessions), and Logout.
- **Playground Module**: Demonstrates database interactions (CRUD).

## Requirements

See [requirements.txt](./requirements.txt).
