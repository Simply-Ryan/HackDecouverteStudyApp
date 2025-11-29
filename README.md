# Study Session App

This project is a web application designed for students and study groups to create and manage study sessions. It offers features for both remote and in-person study options, RSVP functionality, and simulated reminders.

## Features

- **Create Study Sessions**: Users can create study sessions by providing details such as title, type (remote or in-person), location, and meeting link.
- **RSVP Functionality**: Users can RSVP to sessions, allowing session creators to see who will attend.
- **Session Management**: Users can view, edit, and delete their created sessions.
- **Reminders**: The application simulates reminders for upcoming sessions.
- **User Authentication**: Users can log in to manage their sessions securely.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, an ORM for database interactions.
- **Flask-WTF**: An extension that integrates WTForms with Flask, providing form handling and validation.
- **SQLite**: A lightweight database engine used for storing session and user data.
- **HTML/CSS/JavaScript**: For front-end development and user interface design.

## Project Structure

```
study-session-app
├── app.py
├── models.py
├── forms.py
├── config.py
├── requirements.txt
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── main.js
├── templates
│   ├── base.html
│   ├── index.html
│   ├── create_session.html
│   ├── session_detail.html
│   ├── my_sessions.html
│   └── login.html
├── database
│   └── schema.sql
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd study-session-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Run the SQL commands in `database/schema.sql` to create the necessary tables.

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage Guidelines

- Users must log in to create or manage study sessions.
- When creating a session, ensure to fill in all required fields.
- Users can RSVP to sessions they wish to attend.
- Reminders will be simulated based on the session's scheduled time.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.