from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateTimeField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class CreateSessionForm(FlaskForm):
    title = StringField('Session Title', validators=[DataRequired()])
    session_type = SelectField('Session Type', choices=[('in-person', 'In-Person'), ('remote', 'Remote')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    meeting_link = StringField('Meeting Link (for remote sessions)', validators=[DataRequired()])
    date_time = DateTimeField('Date and Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Create Session')

class RSVPForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    submit = SubmitField('RSVP')