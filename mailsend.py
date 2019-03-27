#_*_ coding:utf-8 _*_
import  smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
class Sendmail:
 
    local_hostname = ['xxxx']
    msg = MIMEMultipart('related')
 
    def __init__(self,smtp_server,mail_user,mail_pass):
        self.smtp_server = smtp_server
        self.mail_user = mail_user
        self.mail_pass = mail_pass
 
    def mess(self,theme,message):
        Sendmail.msg['Subject'] = theme  # 邮件主题
        html_msg = '''
                <html><head><body>
                <p>%s</p>
                </body></head></html>
            ''' % message
        html = MIMEText(html_msg, 'html', 'utf-8')
        Sendmail.msg.attach(html)
 
    def files(self,path=None,filenames=None):
        if path == None and filenames == None:
            pass
        else:
            files = path + filenames
            att = MIMEText(open(files, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'p_w_upload; filename=%s' % filenames
            Sendmail.msg.attach(att)
 
    def send(self,receiver):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.ehlo(self.local_hostname)  # 使用ehlo指令向smtp服务器确认身份
        smtp.starttls()  # smtp连接传输加密
        smtp.login(self.mail_user, self.mail_pass)
        smtp.sendmail(self.mail_user, receiver, Sendmail.msg.as_string())
        smtp.quit()

if __name__ == "__main__":
    pass
