from flask_wtf import FlaskForm,Form
from wtforms import TextField,TextAreaField, SubmitField
    
class ContactForm(Form):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")