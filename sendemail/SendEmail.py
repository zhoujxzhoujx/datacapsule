import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from sendemail.ShrinkPic import process_image


class SendEmail:
    mail_smtpserver = 'smtp.qq.com'
    mail_port = 587
    mail_sender = '495945370@qq.com'
    mail_pwd = 'qstysmnqlzgvbghg'
    mail_receiverList = ['1012099550@qq.com']
    mail_subject = u'数据胶囊自动化测试报告'
    mail_subject_alarm = u'数据胶囊错误警告，请注意！！'

    # def __init__(self, smtpServer, mailPort, mailSender, mailPwd, mailtoList, mailSubject):
    #     self._smtpServer =  smtpServer
    #     self._mailPor = mailPort
    #     self._mailSender = mailSender
    #     self._mailPwd = mailPwd
    #     self._mail_receiverList = mailtoList
    #     self._mail_subject=mailSubject

    '''
    发送邮件模块封装，属性均从config.ini文件获得
    '''
    def normalMessage(self):

        # 构建根容器
        msgRoot = MIMEMultipart('related')

        msgRoot['Subject']=self.mail_subject
        # msgRoot['From'] = Header("自动化测试服务", 'utf-8')
        # msgRoot['To'] =Header("测试", 'utf-8')
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
        now = time.strftime('%Y-%m-%d_%H:%M:%S')
        process_image("E:/datacapsule/screenshot/全国数据.png")
        process_image("E:/datacapsule/screenshot/全国数据十佳排行map.png")
        process_image("E:/datacapsule/screenshot/全国数据十佳排行三维数据.png")
        process_image("E:/datacapsule/screenshot/全国数据十佳排行二维数据.png")
        process_image("E:/datacapsule/screenshot/全国数据十佳排行原始数据.png")
        process_image("E:/datacapsule/screenshot/数据管理.png")
        mail_msg = """
                      <p>以下是自动化测试脚本发送，数据胶囊当前页面截图...</p>
                      <p>时间："""+now+"""</p>
                      <p>全国数据：</p>
                      <p><img src="cid:image1"></p>
                      <p>全国数据十佳总面积排行——map数据：</p>
                      <p><img src="cid:image2"></p>
                      <p>全国数据十佳总面积排行——三维数据：</p>
                      <p><img src="cid:image3"></p>
                      <p>全国数据十佳总面积排行——二维数据：</p>
                      <p><img src="cid:image4"></p>
                      <p>全国数据十佳总面积排行——原始数据：</p>
                      <p><img src="cid:image5"></p>
                      <p>数据管理页面</p>
                      <p><img src="cid:image6"></p>
                      """
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        # 指定图片为当前目录
        fp1 = open('E:/datacapsule/screenshot/全国数据.png', 'rb')
        fp2 = open('E:/datacapsule/screenshot/全国数据十佳排行map.png', 'rb')
        fp3 = open('E:/datacapsule/screenshot/全国数据十佳排行三维数据.png', 'rb')
        fp4 = open('E:/datacapsule/screenshot/全国数据十佳排行二维数据.png', 'rb')
        fp5 = open('E:/datacapsule/screenshot/全国数据十佳排行原始数据.png', 'rb')
        fp6 = open('E:/datacapsule/screenshot/数据管理.png', 'rb')


        msgImage1 = MIMEImage(fp1.read())
        msgImage2 = MIMEImage(fp2.read())
        msgImage3 = MIMEImage(fp3.read())
        msgImage4 = MIMEImage(fp4.read())
        msgImage5 = MIMEImage(fp5.read())
        msgImage6 = MIMEImage(fp6.read())


        fp1.close()
        fp2.close()
        fp3.close()
        fp4.close()
        fp5.close()
        fp6.close()
        # 定义图片 ID，在 HTML 文本中引用
        msgImage1.add_header('Content-ID', '<image1>')
        msgImage2.add_header('Content-ID', '<image2>')
        msgImage3.add_header('Content-ID', '<image3>')
        msgImage4.add_header('Content-ID', '<image4>')
        msgImage5.add_header('Content-ID', '<image5>')
        msgImage6.add_header('Content-ID', '<image6>')

        msgRoot.attach(msgImage1)
        msgRoot.attach(msgImage2)
        msgRoot.attach(msgImage3)
        msgRoot.attach(msgImage4)
        msgRoot.attach(msgImage5)
        msgRoot.attach(msgImage6)

        try:
            smtp = smtplib.SMTP_SSL(host=self.mail_smtpserver, port=self.mail_port)  # 继承自SMTP
        except:
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_smtpserver, self.mail_port)

        # 登录邮箱，用户名和密码
        smtp.login(user=self.mail_sender, password=self.mail_pwd)

        # 函数：sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[]):
        smtp.sendmail(self.mail_sender, self.mail_receiverList, msgRoot.as_string())
        smtp.quit()

    def  login_alarm(self):
        # 构建根容器
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject']=self.mail_subject_alarm
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
        now = time.strftime('%Y-%m-%d_%H:%M:%S')
        process_image("E:/datacapsule/image/timg.jfif")

        mail_msg = """
                              <p>这里是自动化测试脚本发送的警报信息：数据胶囊登录错误，请留意！</p>
                              <p>时间：""" + now + """</p>
                              <p><img src="cid:image1"></p>
                              """
        fp1 = open('E:/datacapsule/image/timg.jfif', 'rb')
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
        msgImage1 = MIMEImage(fp1.read())
        msgImage1.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage1)
        fp1.close()
        try:
            smtp = smtplib.SMTP_SSL(host=self.mail_smtpserver, port=self.mail_port)  # 继承自SMTP
        except:
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_smtpserver, self.mail_port)

        # 登录邮箱，用户名和密码
        smtp.login(user=self.mail_sender, password=self.mail_pwd)

        # 函数：sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[]):
        smtp.sendmail(self.mail_sender, self.mail_receiverList, msgRoot.as_string())
        smtp.quit()
    def  screen_alarm(self):
        # 构建根容器
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject']=self.mail_subject_alarm
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
        now = time.strftime('%Y-%m-%d_%H:%M:%S')
        process_image("E:/datacapsule/image/timg.jfif")

        mail_msg = """
                              <p>这里是自动化测试脚本发送的警报信息：数据胶囊截图失败，请留意！</p>
                              <p>时间：""" + now + """</p>
                              <p><img src="cid:image1"></p>
                              """
        fp1 = open('E:/datacapsule/image/timg.jfif', 'rb')
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
        msgImage1 = MIMEImage(fp1.read())
        msgImage1.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage1)
        fp1.close()
        try:
            smtp = smtplib.SMTP_SSL(host=self.mail_smtpserver, port=self.mail_port)  # 继承自SMTP
        except:
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_smtpserver, self.mail_port)

        # 登录邮箱，用户名和密码
        smtp.login(user=self.mail_sender, password=self.mail_pwd)

        # 函数：sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[]):
        smtp.sendmail(self.mail_sender, self.mail_receiverList, msgRoot.as_string())
        smtp.quit()
    # 调试代码
if __name__ == "__main__":
       ss=SendEmail();
       ss.alarm()
       print('--- test end --- ')