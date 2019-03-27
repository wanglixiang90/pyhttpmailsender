#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from flask import Flask,request
from flask import make_response, jsonify
from flask_httpauth import HTTPBasicAuth
import json
from mailsend import Sendmail

app = Flask(__name__)
auth = HTTPBasicAuth()

users = [
    {'username': 'test', 'password': 'itsok'},
    {'username': 'ok', 'password': 'ojbk'}
]

@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None

@app.route('/sendmail' , methods=['GET', 'POST'])
@auth.login_required
def index():
    if request.method == 'POST':
        jsondata = request.get_data()
        data = json.loads(jsondata)
        s,e,f,r= data['smtpserver'],data['emailsubject'],data['filepath'],data['receivesuser']
        email = Sendmail(s['server'],s['mailuser'],s['mailpasswd'])
        email.mess(e['subject'],e['mess'])
        email.files(f['path'],f['files'])
        print '邮件正在发送...'
        email.send(r['receiver'])
        return '邮件发送成功'
    else:
        return '<h1>只接受post请求！</h1>'

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

if __name__ =='__main__':
    app.run(
      host='0.0.0.0',
      port= 5000,
      debug=True
    )