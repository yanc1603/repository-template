/**
 * API Client for handling HTTP requests.
 */
export class ApiClient {
    constructor() {
        this.baseUrl = "http://localhost:8000";
    }

    /**
     * Sends an HTTP request to the API.
     * @param {string} endpoint - The API endpoint (e.g., "/login").
     * @param {string} method - The HTTP method (GET, POST, etc.).
     * @param {object|null} body - The request body data (optional).
     * @returns {Promise<any>} The JSON response from the API.
     */
    async request(endpoint, method, body = null) {
        const headers = { 'Content-Type': 'application/json' };

        // Add Auth Token if it exists
        const token = localStorage.getItem('access_token');
        if (token) headers['Authorization'] = `Bearer ${token}`;

        const options = { method, headers, credentials: 'include' };
        if (body) options.body = JSON.stringify(body);

        try {
            const res = await fetch(`${this.baseUrl}${endpoint}`, options);
            return await res.json();
        } catch (err) {
            console.error("API Error", err);
        }
    }

    /**
     * Sends a GET request.
     * @param {string} url - The URL endpoint.
     */
    get(url) { return this.request(url, 'GET'); }

    /**
     * Sends a POST request.
     * @param {string} url - The URL endpoint.
     * @param {object} data - The data to send.
     */
    post(url, data) { return this.request(url, 'POST', data); }

    /**
     * Sends a PATCH request.
     * @param {string} url - The URL endpoint.
     */
    patch(url) { return this.request(url, 'PATCH'); }
}