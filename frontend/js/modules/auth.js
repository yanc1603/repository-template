import { ApiClient } from '../api/client.js';

export async function initAuth() {
    console.log('Initializing Auth Module');
    const api = new ApiClient();

    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const dashboard = document.getElementById('user-dashboard');
    const authForms = document.getElementById('auth-forms-container');
    const userDisplayName = document.getElementById('user-display-name');
    const btnIdentify = document.getElementById('btn-identify-me');
    const btnLogout = document.getElementById('btn-logout-main');

    // --- UI State Management ---
    const updateUI = (user) => {
        if (user) {
            // Logged In
            if (authForms) authForms.classList.add('hidden');
            if (dashboard) dashboard.classList.remove('hidden');
            if (userDisplayName) userDisplayName.textContent = user.username || 'User';
        } else {
            // Logged Out
            if (authForms) authForms.classList.remove('hidden');
            if (dashboard) dashboard.classList.add('hidden');
            if (userDisplayName) userDisplayName.textContent = 'User';
        }
    };

    // --- Initial Check ---
    try {
        const res = await api.get('/me');
        if (res && res.authenticated) {
            console.log("User is authenticated", res.user);
            updateUI(res.user);
        } else {
            updateUI(null);
        }
    } catch (err) {
        console.warn("Auth check failed", err);
        updateUI(null);
    }

    // --- Button Actions ---
    if (btnIdentify) {
        btnIdentify.addEventListener('click', async () => {
            try {
                const res = await api.get('/me');
                if (res && res.authenticated) {
                    alert(`ID: ${res.user.id}\nUsername: ${res.user.username}`);
                } else {
                    alert("Not authenticated.");
                    updateUI(null);
                }
            } catch (err) {
                alert("Error identifying user: " + err.message);
            }
        });
    }

    if (btnLogout) {
        btnLogout.addEventListener('click', async () => {
            console.log("Logging out...");
            try {
                await api.post('/logout');
                updateUI(null);
                window.location.reload(); // Reload to ensure clean state
            } catch (err) {
                console.error("Logout failed", err);
            }
        });
    }

    // --- Form Handlers ---
    const getFormData = (form) => {
        const formData = new FormData(form);
        return Object.fromEntries(formData.entries());
    };

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const messageEl = document.getElementById('login-message');
            messageEl.textContent = 'Logging in...';
            messageEl.className = 'message';

            const data = getFormData(loginForm);

            try {
                const res = await api.post('/login', data);

                if (res && res.success) {
                    messageEl.textContent = 'Login successful!';
                    messageEl.classList.add('success');
                    // Refresh to trigger initial check
                    setTimeout(() => {
                        window.location.reload();
                    }, 500);
                } else {
                    messageEl.textContent = (res && res.detail) || 'Login failed';
                    messageEl.classList.add('error');
                }
            } catch (err) {
                console.error(err);
                messageEl.textContent = 'An error occurred';
                messageEl.classList.add('error');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const messageEl = document.getElementById('register-message');
            messageEl.textContent = 'Registering...';
            messageEl.className = 'message';

            const data = getFormData(registerForm);

            try {
                const res = await api.post('/register', data);

                if (res && res.username) {
                    messageEl.textContent = 'Registration successful! You can now login.';
                    messageEl.classList.add('success');
                    registerForm.reset();
                } else if (res && res.detail) {
                    messageEl.textContent = res.detail;
                    messageEl.classList.add('error');
                } else {
                    messageEl.textContent = 'Registration failed';
                    messageEl.classList.add('error');
                }
            } catch (err) {
                console.error(err);
                messageEl.textContent = 'An error occurred';
                messageEl.classList.add('error');
            }
        });
    }
}
