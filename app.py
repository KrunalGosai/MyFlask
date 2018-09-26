from flask import Flask, render_template, request, json
from flask_mail import Mail, Message
from app.contact import ContactForm

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'donotreplysgm@gmail.com'
app.config['MAIL_PASSWORD'] = 'test@1511'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
app.secret_key = 'development test'

@app.route('/')
def appStart():
    return render_template('index.html')

@app.route("/mail",methods=['POST'])
def sendmail():
    msg = Message('Contact Details by Website', sender = 'donotreplysgm@gmail.com', recipients = ['gosai.krunal@yahoo.com'])
    html =str("<!DOCTYPE html><html><body><p>Hi,</p>"+
    "<p>Kindly find new contact details filled by user on Web site</p>"+
    "<p>Name : "+request.form.get('name')+"</p><p>E-Mail : "+request.form.get('email')+"</p>"+
    "<p>Subect : "+request.form.get('subject')+"</p><p>Message : "+request.form.get('message')+"</p>"+
    "<p>Note: dont replay this mail.</p><span>Regards</span><br><span>Python System Generated Mail.</span></body></html>")
    msg.html = html
    mail.send(msg)
    return "details successfully sent."

if __name__== "__main__":
    app.run()