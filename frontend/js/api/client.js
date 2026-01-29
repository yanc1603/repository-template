export class ApiClient {
    constructor() {
        this.baseUrl = "http://localhost:8000";
    }

    async request(endpoint, method, body = null) {
        const headers = { 'Content-Type': 'application/json' };

        // Add Auth Token if it exists
        const token = localStorage.getItem('access_token');
        if (token) headers['Authorization'] = `Bearer ${token}`;

        const options = { method, headers };
        if (body) options.body = JSON.stringify(body);

        try {
            const res = await fetch(`${this.baseUrl}${endpoint}`, options);
            return await res.json();
        } catch (err) {
            console.error("API Error", err);
        }
    }

    get(url) { return this.request(url, 'GET'); }
    post(url, data) { return this.request(url, 'POST', data); }
    patch(url) { return this.request(url, 'PATCH'); }
}