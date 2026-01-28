import requests
import time
import sys

BASE_URL = "http://localhost:5000"

def test_registration():
    print("Testing Registration...")
    payload = {"username": "testuser", "password": "password123"}
    try:
        response = requests.post(f"{BASE_URL}/register", json=payload)
        if response.status_code == 200:
            print("Registration Successful")
            return True
        else:
            print(f"Registration Failed: {response.text}")
            return False
    except Exception as e:
        print(f"Registration Error: {e}")
        return False

def test_login():
    print("Testing Login...")
    payload = {"username": "testuser", "password": "password123"}
    session = requests.Session()
    try:
        response = session.post(f"{BASE_URL}/login", json=payload)
        if response.status_code == 200:
            print("Login Successful")
            return session
        else:
            print(f"Login Failed: {response.text}")
            return None
    except Exception as e:
        print(f"Login Error: {e}")
        return None

def test_dashboard(session):
    print("Testing Dashboard...")
    try:
        response = session.get(f"{BASE_URL}/dashboard")
        if "Welcome, testuser!" in response.text:
            print("Dashboard Access Successful")
            return True
        else:
            print(f"Dashboard Access Failed: {response.text}")
            return False
    except Exception as e:
        print(f"Dashboard Error: {e}")
        return False

def test_swagger():
    print("Testing Swagger UI...")
    try:
        response = requests.get(f"{BASE_URL}/apidocs/")
        if response.status_code == 200:
            print("Swagger UI Access Successful")
            return True
        else:
            print(f"Swagger UI Access Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"Swagger UI Error: {e}")
        return False

if __name__ == "__main__":
    # Wait for server to start
    print("Waiting for server to start...")
    time.sleep(5)
    
    if not test_swagger():
        sys.exit(1)

    if not test_registration():
        sys.exit(1)
        
    session = test_login()
    if not session:
        sys.exit(1)
        
    if not test_dashboard(session):
        sys.exit(1)
        
    print("All tests passed!")
