# Frontend - Modular UI Kit

The frontend is a Single Page Application (SPA) structure built with **Vanilla JS Modules** and a custom **CSS UI Kit**.

## 🏃 Running the Frontend
The frontend is served statically by the Backend.
- Run the backend: `uvicorn app.main:app`
- Visit: `http://localhost:8000`

## 🧩 Modularity & Event Architecture

Modules are loosely coupled using an **Event-Driven Architecture**.

### Dynamic Loading
`index.html` uses a helper function `loadModule(path, initFn)`. 
- **Resilient**: If a module file is missing, it logs a warning but **does not break** the rest of the app.
- ** decoupled**: You can remove a `<script>` line or delete a `.js` file safely.

### Event Bus
Modules communicate via `window` events, not direct calls.
- **Auth Module**: Dispatches `app:auth-change`.
- **Feature Modules**: Listen for `app:auth-change` to toggle visibility or fetch data.

### How to Add a Module
1. Create `js/modules/my_feature.js`.
2. Export an `initMyFeature` function.
3. In `index.html`, add:
   ```javascript
   loadModule('./js/modules/my_feature.js', 'initMyFeature');
   ```

## 🎨 UI Kit

A robust CSS system is included in `css/style.css`.

### Components
- **Containers**: `.container-fluid`, `.card`, `.module`
- **Typography**: `.title`, `.subtitle`
- **Buttons**: 
  - `.btn .btn-primary` (Blue)
  - `.btn .btn-secondary` (Gray)
  - `.btn .btn-danger` (Red)
  - `.btn .btn-outline` (Border only)
- **Forms**: 
  - `.slider` (Range input)
  - `.toggle-switch` (iOS style toggle)
