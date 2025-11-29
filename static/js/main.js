// This file contains JavaScript code for client-side functionality, such as handling form submissions, displaying reminders, and managing session interactions.

document.addEventListener('DOMContentLoaded', function() {
    const rsvpForms = document.querySelectorAll('.rsvp-form');
    
    rsvpForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const sessionId = this.dataset.sessionId;
            const rsvpStatus = this.querySelector('input[name="rsvp"]:checked').value;

            fetch(`/rsvp/${sessionId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ rsvp: rsvpStatus }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('RSVP submitted successfully!');
                } else {
                    alert('Error submitting RSVP. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    const reminderButtons = document.querySelectorAll('.set-reminder');
    
    reminderButtons.forEach(button => {
        button.addEventListener('click', function() {
            const sessionId = this.dataset.sessionId;
            const reminderTime = this.dataset.reminderTime;

            // Simulate setting a reminder
            alert(`Reminder set for session ID ${sessionId} at ${reminderTime}`);
        });
    });
});