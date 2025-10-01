
// Form submission handler
document.getElementById('registrationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    try
    {
        // Get form data
        const formData = {
            id: Date.now(), // Simple ID generation
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            additionalGuests: parseInt(document.getElementById('additionalGuests').value),
            dietaryRestrictions: document.getElementById('dietaryRestrictions').value,
            timestamp: new Date().toISOString(),
            status: 'attending'
        };

        // send formData to server
        sendRegistrationDataToServer(formData);

        // Show success message
        document.getElementById('successMessage').style.display = 'block';
        document.getElementById('declineMessage').style.display = 'none';

        // Clear form
        document.getElementById('registrationForm').reset();

        // Scroll to success message
        document.getElementById('successMessage').scrollIntoView({ 
            behavior: 'smooth', 
            block: 'center' 
        });

        // Hide success message after 5 seconds
        setTimeout(() => {
            document.getElementById('successMessage').style.display = 'none';
        }, 5000);
    }
    catch (error)
    {
        console.error('Error during form submission:', error);
        alert('An error occurred while submitting the form. Please try again.');
    }
});

// Decline submission handler
function submitDecline() {
    try
    {
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const groupSize = parseInt(document.getElementById('additionalGuests').value) || 0;
        const dietaryRestrictions = document.getElementById('dietaryRestrictions').value;

        if (!name || !email || !groupSize) {
            alert('Please fill in your name and email to let us know you cannot make it.');
            return;
        }

        const declineData = {
            id: Date.now(), // Simple ID generation
            name: name,
            email: email,
            additionalGuests: groupSize,
            dietaryRestrictions: dietaryRestrictions,
            timestamp: new Date().toISOString(),
            status: 'declined'
        };

        // send declineData to server
        sendRegistrationDataToServer(declineData);

        // Show decline message
        document.getElementById('declineMessage').style.display = 'block';
        document.getElementById('successMessage').style.display = 'none';
        // Clear form
        document.getElementById('registrationForm').reset();

        // Scroll to decline message
        document.getElementById('declineMessage').scrollIntoView({ 
            behavior: 'smooth', 
            block: 'center' 
        });

        // Hide decline message after 5 seconds
        setTimeout(() => {
            document.getElementById('declineMessage').style.display = 'none';
        }, 5000);
    }
    catch (error)
    {
        console.error('Error during decline submission:', error);
        alert('An error occurred while submitting your decline. Please try again.');
    }
}

// Add some visual enhancements
document.addEventListener('DOMContentLoaded', function() {
    // Add floating animation to the flyer
    const flyer = document.querySelector('.flyer');
    let floatDirection = 1;
    
    setInterval(() => {
        floatDirection *= -1;
        flyer.style.transform = `rotate(${floatDirection * 0.5}deg) translateY(${floatDirection * 2}px)`;
    }, 3000);
});

// Console log for demonstration (in real implementation, this would be sent to server)
function sendRegistrationDataToServer(action) {
    console.log('current action:', action);
}