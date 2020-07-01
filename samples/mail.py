import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os


current_path=os.path.dirname(__file__)
reprt_path=os.path.join(current_path,'../screen/UItest2020_05_07_13_41_42.png')


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

#邮件附件
smtp_file=reprt_path


#发送附件
msg=MIMEMultipart()
with open(smtp_file,'rb') as f:
    mime=MIMEBase('zip','zip',filename=smtp_file.split('/')[-1])
    mime.add_header('Content-Disposition','attachment',filename=('gb2312','',smtp_file.split('/')[-1]))
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

# 邮件正文信息对象
msg.attach(MIMEText(smtp_body,'html','utf-8'))
msg['from']=smtp_sender
msg['to']=smtp_receiver
msg['Cc']=smtp_cc
msg['subject']=smtp_subject


# 发送邮件
smtp=smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender,password=smtp_senderpassword)
smtp.sendmail(smtp_sender,smtp_receiver.split(',')+smtp_cc.split(','),msg.as_string())