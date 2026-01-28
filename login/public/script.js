document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const loginMessage = document.getElementById('login-message');
    const registerMessage = document.getElementById('register-message');

    function showMessage(element, message, isError = true) {
        element.textContent = message;
        element.style.color = isError ? 'red' : 'green';
        element.style.marginBottom = '10px';
    }

    async function handleFormSubmit(event, url, messageElement) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const jsonData = Object.fromEntries(formData.entries());

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            });

            const result = await response.json();

            if (response.ok) {
                if (result.redirect) {
                    window.location.href = result.redirect;
                } else {
                    showMessage(messageElement, result.message || 'Success!', false);
                    event.target.reset();
                }
            } else {
                showMessage(messageElement, result.error || 'An error occurred.');
            }
        } catch (error) {
            showMessage(messageElement, 'Network error. Please try again.');
        }
    }

    if (loginForm) {
        loginForm.addEventListener('submit', (e) => handleFormSubmit(e, '/login', loginMessage));
    }

    if (registerForm) {
        registerForm.addEventListener('submit', (e) => handleFormSubmit(e, '/register', registerMessage));
    }
});
