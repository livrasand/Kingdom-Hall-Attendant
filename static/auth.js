const KHA_DOMAIN = 'http://127.0.0.1:5000';
const CLIENT_ID = 'G5qVugP62UqDTzw1BjXIBmhB';
const CLIENT_SECRET = 'gvBI969nQa26DtIbKGa33fkpAkuEuqP5COiCQ2f13mG4Gxxg';

document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const action = params.get('action');
    
    document.getElementById('formTitle').innerText = action === 'register' ? 'Register' : 'Login';
    
    // Show password field only if it's a login action
    if (action === 'login') {
        document.getElementById('passwordField').style.display = 'block';
    }
    
    document.getElementById('authForm').addEventListener('submit', (event) => {
        event.preventDefault();
        
        const email = document.getElementById('email').value;
        const password = document.getElementById('password') ? document.getElementById('password').value : null;
        
        // Redirect to the API login or registration endpoint with email and password
        window.parent.postMessage({ action, email, password }, '*');
        window.close();
    });
});
