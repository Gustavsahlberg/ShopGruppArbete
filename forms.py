from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(),Length(min=2,max=50)])
    email = EmailField("Email", validators=[DataRequired(),Length(max=50, message="maximum 50 char")])
    contact_msg = StringField("Contact message", validators=[DataRequired(),Length(max=255, message="Maximum 255 chars")], widget=TextArea())
    submit = SubmitField("Contact")



class NewsLetterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(),Length(max=50, message="maximum 50 char")])
    submit = SubmitField("Sign up")