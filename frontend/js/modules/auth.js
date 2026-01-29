import { ApiClient } from '../api/client.js';

const api = new ApiClient();

export async function initAuth() {
    console.log("Initializing Auth Module...");

    // Auth Module Elements (Self-contained)
    const loginModule = document.getElementById('login-module');

    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const loginMessage = document.getElementById('login-message');
    const registerMessage = document.getElementById('register-message');

    // Helper: Show Message
    function showMessage(element, message, isError = true) {
        element.textContent = message;
        element.style.color = isError ? 'red' : 'green';
        setTimeout(() => element.textContent = '', 3000);
    }

    // Broadcast Auth State
    function setAuthenticated(isAuthenticated, user = null) {
        // 1. Update own UI (Login Form)
        if (loginModule) {
            if (isAuthenticated) loginModule.classList.add('hidden');
            else loginModule.classList.remove('hidden');
        }

        // 2. Dispatch Event for other modules
        window.dispatchEvent(new CustomEvent('app:auth-change', {
            detail: { authenticated: isAuthenticated, user: user }
        }));
    }

    // 1. Check Session on Load
    try {
        const res = await api.get('/me');
        setAuthenticated(res && res.authenticated, res.user);
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
                setAuthenticated(true, res.user);
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
            if (res && res.username) {
                showMessage(registerMessage, "Registered! Please login.", false);
                e.target.reset();
            } else {
                showMessage(registerMessage, (res && res.detail) || "Registration failed");
            }
        });
    }

    // 4. Handle Logout
    // We listen to body delegation or specific button if it exists
    document.addEventListener('click', async (e) => {
        if (e.target && e.target.id === 'btn-logout') {
            await api.post('/logout');
            setAuthenticated(false);
        }
    });
}
