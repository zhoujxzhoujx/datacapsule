from time import sleep
from selenium import webdriver
from framwork.base_page import BasePage
from framwork.logger import MyLog
import os
from tools.oper_ini import OperIni

class Login(BasePage):
    URL = 'http://data.airlook.com/'
    File_Path = os.path.dirname(os.path.dirname(__file__)) + '/config/locate.ini'
    driver = webdriver.Chrome()

    def __init__(self):
        super().__init__(self.driver, url=self.URL, file_path=self.File_Path)

    def login(self, user_name, password):
         self._log.info("测试登录")
         self.get_url()
         self.driver.maximize_window()
         name = self.wait_find_element('login', 'login_name')
         name.clear()
         name.send_keys(user_name)
         pw = self.wait_find_element('login', 'login_password')
         pw.clear()
         pw.send_keys(password)
         self.wait_find_element('login', 'login', wait_type='clickable').click()
         if self.web_ready():
            try:
                # ele=self.wait_find_element('login', 'alldata')
                ele = self.find_element('login', 'alldata')
                print(ele)
            except Exception as e:
                self._log.error("登录失败")
                print(format(e))
                # raise Exception
                return False
            else:
                self._log.info("登录成功")
                print("登录成功")
                scree_File_Path = os.path.dirname(os.path.dirname(__file__)) + '/screenshot/' + '全国数据.png'
                self.driver.get_screenshot_as_file(scree_File_Path)
                return True

if __name__ == '__main__':
            dd = Login()
            dd.login('18520836299','airlook1234')
