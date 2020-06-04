import time
from pageobject.datacapsule import DataCapsule
from sendemail.SendEmail import SendEmail
from sendemail.ShrinkPic import process_image
import os

def loopMonitor():
       while True:
         datacapsule = DataCapsule()
         loginResult=datacapsule.data('18520836299', 'airlook1234')
         File_Path = os.path.dirname(os.path.dirname(__file__))
         mail_smtpserver = 'smtp.qq.com'
         mail_port = 587
         mail_sender = '495945370@qq.com'
         mail_pwd = 'qstysmnqlzgvbghg'
         mail_receiverList = ['1012099550@qq.com','xulingna@airlook.com','zhoujingxian@airlook.com']
         if(loginResult==True):
            mail_subject = u'数据胶囊自动化测试报告'
            SendEmail.normalMessage(File_Path ,mail_smtpserver, mail_port, mail_sender, mail_pwd, mail_receiverList, mail_subject)
         else:
           print("sdsfdsf")
           mail_subject1 = u'数据胶囊错误警告，请注意！！'
           SendEmail.alarm(File_Path ,mail_smtpserver, mail_port, mail_sender, mail_pwd, mail_receiverList, mail_subject1)
         #2h检查一次
         time.sleep(2*60*60)
         loopMonitor()

if __name__ == "__main__":
          loopMonitor()