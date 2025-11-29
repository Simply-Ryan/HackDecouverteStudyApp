// form handling and UI interactions
document.addEventListener('DOMContentLoaded', function() {
    // prevent creating sessions in the past
    const sessionDateInput = document.getElementById('session_date_input');
    if (sessionDateInput) {
        const today = new Date().toISOString().split('T')[0];
        sessionDateInput.min = today;
    }
    
    // merge date and time fields before submitting
    const createForm = document.getElementById('createForm');
    if (createForm) {
        createForm.addEventListener('submit', function(e) {
            const dateInput = document.getElementById('session_date_input');
            const timeInput = document.getElementById('session_time_input');
            const hiddenDatetime = document.getElementById('session_date');
            
            if (dateInput && timeInput && hiddenDatetime) {
                // combine into single datetime value
                hiddenDatetime.value = dateInput.value + ' ' + timeInput.value;
            }
        });
    }
    
    const sessionTypeSelect = document.getElementById('session_type');
    const meetingLinkGroup = document.getElementById('meetingLinkGroup');
    const locationGroup = document.getElementById('locationGroup');
    const meetingLinkInput = document.getElementById('meeting_link');
    const locationInput = document.getElementById('location');
    
    if (sessionTypeSelect) {
        sessionTypeSelect.addEventListener('change', function() {
            if (this.value === 'remote') {
                meetingLinkGroup.style.display = 'block';
                locationGroup.style.display = 'none';
                if (meetingLinkInput) meetingLinkInput.required = true;
                if (locationInput) locationInput.required = false;
            } else if (this.value === 'in-person') {
                meetingLinkGroup.style.display = 'none';
                locationGroup.style.display = 'block';
                if (meetingLinkInput) meetingLinkInput.required = false;
                if (locationInput) locationInput.required = true;
            } else {
                meetingLinkGroup.style.display = 'none';
                locationGroup.style.display = 'none';
                if (meetingLinkInput) meetingLinkInput.required = false;
                if (locationInput) locationInput.required = false;
            }
        });
    }
    
    // reminder test button (if it exists)
    const testReminderBtn = document.getElementById('testReminder');
    const reminderNotification = document.getElementById('reminderNotification');
    
    if (testReminderBtn && reminderNotification) {
        testReminderBtn.addEventListener('click', function() {
            // show test notification
            reminderNotification.innerHTML = `
                <strong>🔔 Reminder Sent!</strong><br>
                "Don't forget your study session is coming up soon!"<br>
                <small>Sent at ${new Date().toLocaleTimeString()}</small>
            `;
            reminderNotification.style.display = 'block';
            
            // auto-hide after 5 seconds
            setTimeout(() => {
                reminderNotification.style.display = 'none';
            }, 5000);
        });
    }
    
    // fade out flash messages
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
    
    // chat area file upload button
    const quickFileUpload = document.getElementById('quick-file-upload');
    if (quickFileUpload) {
        quickFileUpload.addEventListener('change', function(e) {
            if (this.files && this.files[0]) {
                const file = this.files[0];
                const sessionId = window.location.pathname.split('/').pop();
                
                // prepare file for upload
                const formData = new FormData();
                formData.append('file', file);
                
                // show loading state
                const uploadBtn = document.querySelector('.file-upload-btn');
                const originalContent = uploadBtn.innerHTML;
                uploadBtn.innerHTML = '⏳';
                uploadBtn.style.pointerEvents = 'none';
                
                // send to server
                fetch(`/session/${sessionId}/upload`, {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // refresh to show uploaded file
                        window.location.reload();
                    } else {
                        alert(data.error || 'Failed to upload file');
                        uploadBtn.innerHTML = originalContent;
                        uploadBtn.style.pointerEvents = 'auto';
                    }
                })
                .catch(error => {
                    alert('Error uploading file: ' + error);
                    uploadBtn.innerHTML = originalContent;
                    uploadBtn.style.pointerEvents = 'auto';
                });
                
                // clear input for next file
                this.value = '';
            }
        });
    }
    
    // real-time session filtering
    const searchInput = document.querySelector('.search-input');
    const subjectFilter = document.querySelector('.subject-filter');
    const sessionCards = document.querySelectorAll('.session-card');
    
    function filterSessions() {
        const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
        const selectedSubject = subjectFilter ? subjectFilter.value : '';
        
        let visibleCount = 0;
        
        sessionCards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const subject = card.querySelector('.subject-badge').textContent;
            
            const matchesSearch = !searchTerm || title.includes(searchTerm);
            const matchesSubject = !selectedSubject || subject === selectedSubject;
            
            if (matchesSearch && matchesSubject) {
                card.style.display = 'block';
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });
        
        // handle no results message
        const sessionGrid = document.querySelector('.session-grid');
        const emptyState = document.querySelector('.empty-state');
        
        if (sessionGrid && visibleCount === 0 && sessionCards.length > 0) {
            if (!emptyState) {
                const noResults = document.createElement('p');
                noResults.className = 'empty-state filter-empty';
                noResults.textContent = 'No sessions match your filters. Try adjusting your search criteria.';
                sessionGrid.insertAdjacentElement('afterend', noResults);
            }
            sessionGrid.style.display = 'none';
        } else if (sessionGrid) {
            sessionGrid.style.display = 'grid';
            const filterEmpty = document.querySelector('.filter-empty');
            if (filterEmpty) filterEmpty.remove();
        }
    }
    
    // attach filter event handlers
    if (searchInput) {
        searchInput.addEventListener('input', filterSessions);
    }
    
    if (subjectFilter) {
        subjectFilter.addEventListener('change', filterSessions);
    }
});