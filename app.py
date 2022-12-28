from flask import Flask,render_template,request
import smtplib
from email.message import EmailMessage
import pickle

app=Flask(__name__)

@app.route('/')
def email():
    return render_template('email.html')

@app.route('/email_send',methods=['POST'])
def mail_alert():
    msg=EmailMessage()
    content=request.form['c']
    msg.set_content(content)
    msg['subject']=request.form['b']
    msg['to']=request.form['a']
    msg['image']=request.form['d']
    user='pythontest565@gmail.com'
    msg['from']=user
    password='sxizrcgniauglqlq'
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

    return ("email sent")



    



if __name__=="__main__":
    app.run(debug=True)

