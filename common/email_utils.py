import os
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


class EmilUtils():
    def __init__(self,smtp_subject,smtp_body,smtp_file=None):

        self.smtp_server='smtp.qq.com' # 邮件服务器地址
        self.smtp_sender='505349085@qq.com' # 邮箱名
        self.smtp_senderpassword='dajhtkkzrtrdbhfb' # 授权码
        self.smtp_receiver='505349085@qq.com,1986812570@qq.com'  #收件人
        self.smtp_cc='582434039@qq.com'  #抄送人
        self.smtp_subject=smtp_subject  #邮件主题
        self.smtp_body=smtp_body  #邮件正文
        self.smtp_file=smtp_file #邮件附件路径

    def mail_content(self):
        if self.smtp_file!=None:
            msg = MIMEMultipart()
            with open(self.smtp_file, 'rb') as f:
                mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
                mime.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', self.smtp_file.split('/')[-1]))
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)
            # 邮件正文信息对象
            msg.attach(MIMEText(self.smtp_body, 'html', 'utf-8'))
            msg['from'] = self.smtp_sender
            msg['to'] = self.smtp_receiver
            msg['Cc'] = self.smtp_cc
            msg['subject'] = self.smtp_subject
            return msg
        else:
            msg=MIMEText(self.smtp_body, 'html', 'utf-8')
            msg['from'] = self.smtp_sender
            msg['to'] = self.smtp_receiver
            msg['Cc'] = self.smtp_cc
            msg['subject'] = self.smtp_subject
            return msg

    def send_mial(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        except:
            smtp=smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)

        mail_content=self.mail_content()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',') + self.smtp_cc.split(','),
                          mail_content.as_string())
        except Exception as e:
            print("发送失败，未知错误")
        smtp.quit()


if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    reprt_path = os.path.join(current_path, '../screen/UItest2020_05_07_13_41_42.png')
    send_email=EmilUtils('自动化测试报告（测试版本）','来自Python邮件测试',reprt_path).send_mial()

