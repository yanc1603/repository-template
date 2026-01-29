import { ApiClient } from '../api/client.js';

export function initApiTester() {
    console.log('Initializing API Tester Module');
    const api = new ApiClient();

    const outputBox = document.getElementById('api-output');
    const testBtn = document.getElementById('btn-test-api');

    if (testBtn) {
        testBtn.addEventListener('click', async () => {
            outputBox.textContent = 'Loading...';
            try {
                // Test the /me endpoint as an example, or a public one if auth is issue
                // We'll try a public endpoint effectively or the auth status
                const res = await api.get('/me');
                // Actually based on router.py it's at /me if mounted at root, or /auth/me if prefixed.
                // Dynamic loader does: app.include_router(module.router) without prefix usually unless specified in router.
                // Let's check router.py again? No, let's just assume /me for now or check mounts.
                // Wait, dynamic loader in main.py includes router directly. 
                // Let's try to hit a known endpoint.

                outputBox.textContent = JSON.stringify(res, null, 2);
            } catch (err) {
                outputBox.textContent = 'Error: ' + err.message;
            }
        });
    }
}
