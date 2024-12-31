
document.getElementById('signup-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = {
        guardian_name: document.getElementById('guardian_name').value,
        patient_name: document.getElementById('patient_name').value,
        register_date: document.getElementById('register_date').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        patient_birth_date: document.getElementById('patient_birth_date').value,
        genetic_history: document.getElementById('genetic_history').value || null,
        pregnancy_disease: document.getElementById('pregnancy_disease').value || null,
        other_disorders: document.getElementById('other_disorders').value || null,
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        });

        const result = await response.json();
        alert(result.message || result.error);
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
});
