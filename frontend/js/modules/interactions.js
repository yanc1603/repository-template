import { ApiClient } from '../api/client.js';

export function initInteractions() {
    console.log('Initializing Interactions Module');
    const api = new ApiClient();

    // UI Elements
    const terminal = document.getElementById('browser-terminal');
    const btnClear = document.getElementById('btn-clear-terminal');
    const sliderValueDisplay = document.getElementById('slider-value-display');

    if (!terminal) return;

    // --- Helper for Logging ---
    const log = (msg, isServer = false) => {
        const line = document.createElement('div');
        line.textContent = isServer ? `> Server: ${msg}` : `$ ${msg}`;
        if (isServer) line.style.color = '#00ffff';
        terminal.appendChild(line);
        terminal.scrollTop = terminal.scrollHeight;
    };

    // --- API Call Helper ---
    const sendInteraction = async (type, value = null, extra = {}) => {
        const payload = { type, value, extra };
        // Show what is being sent (restore functionality)
        log(`Sending: ${JSON.stringify(payload)}`);
        try {
            const res = await api.post('/interactions/echo', payload);
            if (res) {
                log(JSON.stringify(res, null, 2), true);
            }
        } catch (err) {
            // Different error message for mistakes
            log(`⚠️ Oops! Interaction Failed: ${err.message}`);
        }
    };

    // --- Event Listeners ---

    // Buttons
    ['primary', 'secondary', 'outline', 'danger'].forEach(type => {
        const btn = document.getElementById(`btn-interaction-${type}`);
        if (btn) {
            btn.addEventListener('click', () => {
                sendInteraction('button_click', type);
            });
        }
    });

    // Slider
    const slider = document.getElementById('input-interaction-slider');
    if (slider) {
        slider.addEventListener('change', (e) => {
            const val = e.target.value;
            if (sliderValueDisplay) sliderValueDisplay.textContent = val;
            sendInteraction('slider_change', parseInt(val));
        });

        // Update display while dragging (input event)
        slider.addEventListener('input', (e) => {
            if (sliderValueDisplay) sliderValueDisplay.textContent = e.target.value;
        });
    }

    // Toggle
    const toggle = document.getElementById('input-interaction-toggle');
    if (toggle) {
        toggle.addEventListener('change', (e) => {
            sendInteraction('toggle_switch', e.target.checked);
        });
    }

    // Clear Terminal
    if (btnClear) {
        btnClear.addEventListener('click', () => {
            terminal.innerHTML = '<div>$ Terminal cleared.</div>';
        });
    }
}
