from time import sleep

from selenium import webdriver
from framwork.base_page import BasePage
from framwork.logger import MyLog
import os

class DataCapsule(BasePage):
    URL = 'http://data.airlook.com/'
    File_Path = os.path.dirname(os.path.dirname(__file__)) + '/config/locate.ini'
    driver = webdriver.Chrome()

    def __init__(self):
        super().__init__(self.driver, url=self.URL, file_path=self.File_Path)


    def data(self, user_name, password):
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

                ele = self.find_element('login', 'alldata')
                self._log.info("登录成功")
                print("登录成功")
                scree_File_Path = os.path.dirname(os.path.dirname(__file__)) + '/screenshot/'+'全国数据.png'
                self.driver.get_screenshot_as_file(scree_File_Path)

                # 全国数据总面积十佳排行map
                target_map = self.find_element('data','Allmap')
                self.driver.execute_script("arguments[0].scrollIntoView();", target_map)
                scree_File_Path1 = os.path.dirname(os.path.dirname(__file__)) + '/screenshot/' + '全国数据十佳排行map.png'
                self.driver.get_screenshot_as_file(scree_File_Path1)

                # 全国数据总面积十佳排行三维数据
                target_three = self.find_element('data', 'ThreeDime')
                target_three.click()
                # 全国数据总面积十佳排行增长三维数据
                target2 = self.find_element('data', 'ThreeDimeIncrese')
                target2.click()
                sleep(1)
                scree_File_Path2 = os.path.dirname(os.path.dirname(__file__)) + '/screenshot/' + '全国数据十佳排行三维数据.png'
                self.driver.get_screenshot_as_file(scree_File_Path2)


                # 全国数据总面积十佳排行二维数据
                target_two = self.find_element('data', 'TwoDime')
                target_two.click()
                # 全国数据总面积十佳排行增长二维数据
                target3 = self.find_element('data', 'TwoDimeIncrese')
                target3.click()
                sleep(1)
                scree_File_Path3= os.path.dirname(os.path.dirname(__file__)) + '/screenshot/' + '全国数据十佳排行二维数据.png'
                self.driver.get_screenshot_as_file(scree_File_Path3)

                # 全国数据总面积十佳排行原始数据
                target = self.find_element('data', 'Alldata')
                target.click()
                # 全国数据总面积十佳排行增长原始数据
                target4 = self.find_element('data', 'AlldataIncrese')
                target4.click()
                sleep(1)
                scree_File_Path4 = os.path.dirname(os.path.dirname(__file__)) + '/screenshot/' + '全国数据十佳排行原始数据.png'
                self.driver.get_screenshot_as_file(scree_File_Path4)

                target3 = self.find_element('data', 'data')
                target3.click()
                sleep(3)
                scree_File_Path3 = os.path.dirname(os.path.dirname(__file__)) + '/screenshot/' + '数据管理.png'
                self.driver.get_screenshot_as_file(scree_File_Path3)
                return True
            except Exception as e:
                self._log.error("登录失败")
                print(format(e))
                # raise Exception
                return False


if __name__ == '__main__':
            datacapsule = DataCapsule()
            datacapsule.data('18520836297','airlook1234')
