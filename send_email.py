from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
#update it with your gmail
app.config['MAIL_USERNAME'] = 'opusfarm4@gmail.com'
#update it with your password
app.config['MAIL_PASSWORD'] = 'ixbh zejs urpy ncfh'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/api/send_email', methods=["POST"])
def send_email():
    # Gets email data from the request body
    email_data = request.get_json()

    # Code to send the email
    msg = Message(
        sender ='opusfarm4@gmail.com',
        subject=email_data["subject"],
        recipients=email_data["recipients"],
        body=email_data["body"]
    )
    mail.send(msg)

    return {"email_success":"Email sent successfully"}


if __name__ == "__main__":
    app.run(debug=True, port=5003)
