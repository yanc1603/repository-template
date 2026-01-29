import { ApiClient } from '../api/client.js';

const api = new ApiClient();

export async function initAuth() {
    console.log("Initializing Auth Module...");

    const loginModule = document.getElementById('login-module');
    const playgroundModule = document.getElementById('playground-module');

    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const loginMessage = document.getElementById('login-message');
    const registerMessage = document.getElementById('register-message');
    const btnLogout = document.getElementById('btn-logout');

    // Helper: Show Message
    function showMessage(element, message, isError = true) {
        element.textContent = message;
        element.style.color = isError ? 'red' : 'green';
        setTimeout(() => element.textContent = '', 3000);
    }

    // Helper: Toggle Views
    function setAuthenticated(isAuthenticated) {
        if (isAuthenticated) {
            loginModule.style.display = 'none';
            playgroundModule.style.display = 'block';
        } else {
            loginModule.style.display = 'block';
            playgroundModule.style.display = 'none';
        }
    }

    // 1. Check Session on Load
    try {
        const res = await api.get('/me');
        console.log("Session Check:", res);
        setAuthenticated(res && res.authenticated);
    } catch (e) {
        console.error("Auth check failed", e);
        setAuthenticated(false);
    }

    // 2. Handle Login
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData.entries());

            const res = await api.post('/login', data);
            if (res && res.success) {
                showMessage(loginMessage, "Login Successful!", false);
                setAuthenticated(true);
                e.target.reset();
            } else {
                showMessage(loginMessage, (res && res.detail) || "Login failed");
            }
        });
    }

    // 3. Handle Register
    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData.entries());

            const res = await api.post('/register', data);
            if (res && res.username) { // User schema returned
                showMessage(registerMessage, "Registered! Please login.", false);
                e.target.reset();
            } else {
                showMessage(registerMessage, (res && res.detail) || "Registration failed");
            }
        });
    }

    // 4. Handle Logout
    if (btnLogout) {
        btnLogout.addEventListener('click', async () => {
            await api.post('/logout');
            setAuthenticated(false);
        });
    }
}
