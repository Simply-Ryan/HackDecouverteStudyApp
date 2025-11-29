// Dynamic form handling for session type
document.addEventListener('DOMContentLoaded', function() {
    const sessionTypeSelect = document.getElementById('session_type');
    const meetingLinkGroup = document.getElementById('meetingLinkGroup');
    const locationGroup = document.getElementById('locationGroup');
    
    if (sessionTypeSelect) {
        sessionTypeSelect.addEventListener('change', function() {
            if (this.value === 'remote') {
                meetingLinkGroup.style.display = 'block';
                locationGroup.style.display = 'none';
            } else if (this.value === 'in-person') {
                meetingLinkGroup.style.display = 'none';
                locationGroup.style.display = 'block';
            } else {
                meetingLinkGroup.style.display = 'none';
                locationGroup.style.display = 'none';
            }
        });
    }
    
    // Test reminder button
    const testReminderBtn = document.getElementById('testReminder');
    const reminderNotification = document.getElementById('reminderNotification');
    
    if (testReminderBtn && reminderNotification) {
        testReminderBtn.addEventListener('click', function() {
            // Simulate a reminder notification
            reminderNotification.innerHTML = `
                <strong>🔔 Reminder Sent!</strong><br>
                "Don't forget your study session is coming up soon!"<br>
                <small>Sent at ${new Date().toLocaleTimeString()}</small>
            `;
            reminderNotification.style.display = 'block';
            
            // Hide after 5 seconds
            setTimeout(() => {
                reminderNotification.style.display = 'none';
            }, 5000);
        });
    }
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});