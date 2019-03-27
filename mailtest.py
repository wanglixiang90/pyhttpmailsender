#_*_ coding:utf-8 _*_

#POST方式发送邮件数据到smtp http转发接口
import urllib2
import json

def http_post():
    url = 'http://192.168.1.51:5000/sendmail'
    data = {'smtpserver': {'server': 'mail.163.com', 'mailuser': '15201376500@163.com', 'mailpasswd': 'itspasswd'},
            'emailsubject': {'subject': 'easy http mail', 'mess': '来一封HTTP 接口邮件'},
            'filepath': {'path': '/tmp/', 'files': 'test.log'},
            'receivesuser': {'receiver': '1318659588@qq.com'},
			'username':'test','password':'itsok'
			}

    headers = {'Content-Type': 'application/json'}
    req = urllib2.Request(url=url, headers=headers, data=json.dumps(data))
    response = urllib2.urlopen(req)
    return response.read()
resp = http_post()
print resp