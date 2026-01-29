import { ApiClient } from '../api/client.js';

const api = new ApiClient();

export function initPlayground() {
    console.log("Initializing Playground Module...");

    const playgroundModule = document.getElementById('playground-module');
    // Ideally use classList.add('hidden') initially in CSS, or set here
    if (playgroundModule) playgroundModule.classList.add('hidden');

    const btnAdd = document.getElementById('btn-add');
    const inputTitle = document.getElementById('input-title');
    const list = document.getElementById('task-list');

    // State
    let isMounted = false;

    // Listen for Auth Changes
    window.addEventListener('app:auth-change', (e) => {
        const { authenticated } = e.detail;
        if (playgroundModule) {
            if (authenticated) {
                playgroundModule.classList.remove('hidden');
                loadTasks();
            } else {
                playgroundModule.classList.add('hidden');
                list.innerHTML = '';
            }
        }
    });

    // 1. Button: Send Data
    if (btnAdd) {
        btnAdd.addEventListener('click', async () => {
            if (!inputTitle.value) return;
            await api.post('/playground/', { title: inputTitle.value });
            inputTitle.value = ''; // Clear input
            loadTasks(); // Refresh list
        });
    }

    // 2. Function: Read Data & Render
    async function loadTasks() {
        try {
            const tasks = await api.get('/playground/');
            if (!tasks || !Array.isArray(tasks)) return;

            list.innerHTML = ''; // Clear current list

            tasks.forEach(task => {
                const li = document.createElement('li');
                li.style.display = "flex";
                li.style.justifyContent = "space-between";
                li.style.padding = "5px";
                li.style.borderBottom = "1px solid #ccc";

                // Dynamic Text based on State
                const statusText = task.is_completed ? "✅ Completed" : "⏳ Pending";
                const btnText = task.is_completed ? "Undo" : "Complete";

                li.innerHTML = `
                    <span>${task.title} - <strong>${statusText}</strong></span>
                    <button class="btn-toggle" data-id="${task.id}">${btnText}</button>
                `;
                list.appendChild(li);
            });

            // 3. Button: Change State (Dynamic Binding)
            document.querySelectorAll('.btn-toggle').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    const id = e.target.getAttribute('data-id');
                    await api.patch(`/playground/${id}/toggle`);
                    loadTasks(); // Refresh UI to show new state
                });
            });
        } catch (err) {
            console.error("Failed to load tasks", err);
        }
    }
}