import os
import time
from selenium import webdriver
from framwork.base_page import BasePage
from framwork.logger import MyLog
from pageobject.datacapsule import DataCapsule
from pageobject.login import Login
from sendemail.SendEmail import SendEmail
from sendemail.ShrinkPic import process_image

class Monitor(BasePage,SendEmail):
    URL = 'http://data.airlook.com/'
    File_Path = os.path.dirname(os.path.dirname(__file__)) + '/config/locate.ini'
    driver = webdriver.Chrome()
    mail_smtpserver = 'smtp.qq.com'
    mail_port = 587
    mail_sender = '495945370@qq.com'
    mail_pwd = 'qstysmnqlzgvbghg'
    mail_receiverList = ['1012099550@qq.com']
    mail_subject = u'数据胶囊自动化测试报告'


    def __init__(self):
        super().__init__(self.driver, url=self.URL, file_path=self.File_Path)


    def loopMonitor(self):

       while True:

          loginResult = Login.login(self, '18520836299', 'airlook1234')
          if (loginResult == True):
              dataRusult = DataCapsule.data(self)
              if (dataRusult == True):
                SendEmail.normalMessage(self)
              else:
                  SendEmail.screen_alarm(self)
          else:
              SendEmail.login_alarm(self)
           #2h检查一次
          time.sleep(2*60*60)
          self.loopMonitor()

if __name__ == "__main__":
          monitor=Monitor()
          monitor.loopMonitor()