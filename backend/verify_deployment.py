import asyncio
import httpx
import sys

BASE_URL = "http://localhost:8000"

async def verify():
    async with httpx.AsyncClient(follow_redirects=False) as client:
        # 1. Check health/root (static file)
        try:
            resp = await client.get(BASE_URL)
            if resp.status_code == 200:
                print("✅ Frontend is serving at /")
            else:
                print(f"❌ Frontend check failed: {resp.status_code}")
                sys.exit(1)
        except Exception as e:
             print(f"❌ Connection failed: {e}")
             sys.exit(1)

        # 2. Register
        username = "testuser_modular"
        password = "password123"
        reg_data = {"username": username, "password": password}
        
        print("Attempting registration...")
        resp = await client.post(f"{BASE_URL}/register", json=reg_data)
        if resp.status_code == 200:
            print("✅ Registration successful")
        elif resp.status_code == 400 and "already exists" in resp.text:
             print("⚠️ User already exists, proceeding to login")
        else:
            print(f"❌ Registration failed: {resp.status_code} {resp.text}")
            sys.exit(1)

        # 3. Login
        print("Attempting login...")
        login_data = {"username": username, "password": password}
        resp = await client.post(f"{BASE_URL}/login", json=login_data)
        
        if resp.status_code == 200:
            data = resp.json()
            if data.get("success") and data.get("user"):
                 print("✅ Login successful")
            else:
                 print(f"❌ Login response unexpected: {data}")
                 sys.exit(1)
        else:
            print(f"❌ Login failed: {resp.status_code} {resp.text}")
            sys.exit(1)

        # 4. Check Session /me
        print("Checking session /me...")
        resp = await client.get(f"{BASE_URL}/me")
        if resp.status_code == 200 and resp.json().get("authenticated"):
             print("✅ Session /me verified")
        else:
             print(f"❌ Session check failed: {resp.status_code} {resp.text}")
             sys.exit(1)

        # 5. Logout
        print("Logging out...")
        resp = await client.post(f"{BASE_URL}/logout")
        if resp.status_code == 200 and resp.json().get("success"):
             print("✅ Logout successful")
        else:
             print(f"⚠️ Logout failed: {resp.status_code}")

if __name__ == "__main__":
    asyncio.run(verify())
