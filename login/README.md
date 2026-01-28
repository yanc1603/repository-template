# Python Login System with Flask, SQLAlchemy, and bcrypt

A secure login system built with Python, Flask, SQLAlchemy, and bcrypt. This project replicates the features of the original Node.js version but uses a Python stack.

## Features

- **User Registration**: Securely create new accounts.
- **Password Hashing**: Uses `bcrypt` to salt and hash passwords.
- **Session Management**: Uses Flask's signed sessions.
- **Protected Routes**: Dashboard is accessible only after login.
- **SQLite Database**: Lightweight database using SQLAlchemy ORM.
- **Swagger Documentation**: Interactive API documentation via Flasgger.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1.  Clone the repository or navigate to the project directory.

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Start the application:
    ```bash
    python3 app.py
    ```
    The server will start on `http://localhost:5000`.

2.  Open your browser and visit:
    - **App**: [http://localhost:5000](http://localhost:5000)
    - **API Docs**: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

## API Endpoints

- `POST /register`: Register a new user (`username`, `password`).
- `POST /login`: Login (`username`, `password`).
- `GET /dashboard`: Protected route (requires login).
- `GET /logout`: Logout user.
- `GET /apidocs`: Swagger UI.
