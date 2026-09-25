const API_BASE_URL = 'http://127.0.0.1:5000/api';

document.getElementById('test-backend-btn').addEventListener('click', () => {
    const responseBox = document.getElementById('backend-response');
    responseBox.textContent = 'Loading...';
    
    fetch(`${API_BASE_URL}/health`)
        .then(response => response.json())
        .then(data => {
            responseBox.textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            responseBox.textContent = 'Error connecting to backend: ' + error.message;
        });
});

document.getElementById('login-form').addEventListener('submit', (e) => {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const rollNo = document.getElementById('roll-no').value;
    const errorBox = document.getElementById('login-error');
    
    errorBox.textContent = '';
    
    fetch(`${API_BASE_URL}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, roll_no: rollNo })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            localStorage.setItem('demo_user_name', data.name);
            localStorage.setItem('demo_user_roll', data.roll_no);
            window.location.href = 'dashboard.html';
        } else {
            errorBox.textContent = data.message || 'Login failed';
        }
    })
    .catch(error => {
        errorBox.textContent = 'Error connecting to backend: ' + error.message;
    });
});
