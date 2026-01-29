# Frontend Module Template

Built with **HTML5**, **CSS3**, and **Vanilla JavaScript (ES6 Modules)**.

## Structure

```
frontend/
├── index.html          # Main SPA Entry
├── css/style.css       # Global Styles
└── js/
    ├── api/client.js   # API Wrapper (Fetch)
    └── modules/
        ├── auth.js     # Auth Logic (UI & State)
        └── playground.js # Example Module Logic
```

## Functionality

- **Modules**: Each feature is self-contained in `js/modules`.
- **API Client**: Handles JSON content-type and Credentials (Cookies) automatically.
