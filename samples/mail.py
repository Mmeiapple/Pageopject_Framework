import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 邮件服务器地址
smtp_server='smtp.qq.com'

# 邮箱名
smtp_sender='505349085@qq.com'

# 授权码
smtp_senderpassword='dajhtkkzrtrdbhfb'

#收件人
smtp_receiver='505349085@qq.com,1986812570@qq.com'
#抄送人
smtp_cc='582434039@qq.com'

#邮件主题
smtp_subject='自动化测试报告（测试版本）'

#邮件正文
smtp_body='来自Python邮件测试'


# 邮件信息对象
msg=MIMEText(smtp_body,'html','utf-8')
msg['from']=smtp_sender
msg['to']=smtp_receiver
msg['Cc']=smtp_cc
msg['subject']=smtp_subject

# 发送邮件
smtp=smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender,password='P@SSHM.214W0RD')
smtp.sendmail(smtp_sender,smtp_receiver.split(',')+smtp_cc.split(','),msg.as_string())