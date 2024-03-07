document.addEventListener('DOMContentLoaded', function() {
    const registrationForm = document.querySelector('.registration-form');

    registrationForm.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        // Extract form data
        const formData = new FormData(registrationForm);
        const userData = {
            email: formData.get('email'),
            password: formData.get('password'),
            first_name: formData.get('first_name'),
            last_name: formData.get('last_name'),
            phone_number: formData.get('phone_number'),
            user_type: formData.get('user_type'),
            service_preferences: formData.get('service_preferences'),
        };

        // API call to register the user
        fetch('http://0.0.0.0:5001/api/v1/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
        })
        .then(response => {
            if (response.ok) {
                return response.json(); // or handle redirect to another page
            } else {
                throw new Error('Something went wrong with registration');
            }
        })
        .then(data => {
            console.log(data);
            // Display a success message or redirect the user
            alert('Registration successful!');
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Registration failed. Please try again.');
        });
    });
});
