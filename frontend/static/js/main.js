// Handle authentication token
document.body.addEventListener('htmx:afterRequest', function(evt) {
    if (evt.detail.pathInfo.requestPath === '/auth/token') {
        const response = JSON.parse(evt.detail.xhr.response);
        if (response.access_token) {
            localStorage.setItem('token', response.access_token);
            updateAuthUI();
            showNotification('Successfully logged in!', 'success');
        }
    }
});

// Update UI based on authentication status
function updateAuthUI() {
    const token = localStorage.getItem('token');
    const authSection = document.getElementById('auth-section');
    
    if (token) {
        authSection.innerHTML = `
            <button onclick="logout()" class="hover:text-blue-600">Logout</button>
        `;
    } else {
        authSection.innerHTML = `
            <a href="/login" class="hover:text-blue-600">Login</a>
            <a href="/register" class="hover:text-blue-600">Register</a>
        `;
    }
}

// Logout function
function logout() {
    localStorage.removeItem('token');
    updateAuthUI();
    showNotification('Successfully logged out!', 'success');
    window.location.href = '/';
}

// Add authentication headers to HTMX requests
document.body.addEventListener('htmx:configRequest', function(evt) {
    const token = localStorage.getItem('token');
    if (token) {
        evt.detail.headers['Authorization'] = `Bearer ${token}`;
    }
});

// Show notifications
function showNotification(message, type = 'success') {
    const notifications = document.getElementById('notifications');
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    notifications.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    updateAuthUI();
});