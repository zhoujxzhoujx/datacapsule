# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framwork.logger import MyLog
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from tools.oper_ini import OperIni
import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, url, file_path):

        self._driver = driver
        self._url = url
        self._log = MyLog().get_log('myAutoTest')
        self._oper_ini = OperIni(file_path)
        self._actions = ActionChains(self._driver)

    # 打开指定url
    def get_url(self):
        self._driver.get(self._url)
        self._log.info("打开url %s" % self._url)
        return self._driver

    def find_element(self, section, key):
        """
        定位单个元素
        :param section: ini文件里的section，即用例名称
        :param key: ini文件里的key，即定位方式
        :return: 返回定位到的元素
        """
        element = ''
        ele = self._oper_ini.get_section(section, key)
        select = ele.split('=>')
        select_by = select[0].strip()
        select_value = select[1].strip()
        if select_by == 'xpath':
            try:
                element = self._driver.find_element_by_xpath(select_value)
                self._log.info("通过xpath定位元素 %s" % select_value)
            except NoSuchElementException:
                self._log.error("定位%s失败" % select_value)
                raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(select_value))
        elif select_by == 'link_text':
            try:
                element = self._driver.find_element_by_link_text(select_value)
                self._log.info("通过link_text定位元素 %s" % select_value)
            except NoSuchElementException:
                self._log.error("定位%s失败" % select_value)
                raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(select_value))
        elif select_by == 'class_name':
            try:
                element = self._driver.find_element_by_class_name(select_value)
                self._log.info("通过class_name定位元素 %s" % select_value)
            except NoSuchElementException:
                self._log.error("定位%s失败" % select_value)
                raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(select_value))
        elif select_by == 'css_selector':
            try:
                element = self._driver.find_element_by_css_selector(select_value)
                self._log.info("通过css_selector定位元素 %s" % select_value)
            except NoSuchElementException:
                self._log.error("定位%s失败" % select_value)
                raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(select_value))
        return element

    def wait_find_element(self, section, key, wait_type="visibility",time_out=10):
        """
        定位元素加上等待支持三种
        :param section: ini文件里的section，即用例名称
        :param key: ini文件里的key，即定位方式
        :param time_out: 超时时间
        :param wait_type: 等待方式
        :return: 返回元素
        """
        element = ''
        ele = self._oper_ini.get_section(section, key)
        select = ele.split('=>')
        select_by = select[0].strip()
        select_value = select[1].strip()
        if select_by == 'xpath':
            select_by = By.XPATH
        elif select_by == 'link_text':
            select_by = By.LINK_TEXT
        elif select_by == 'class_name':
            select_by = By.CLASS_NAME
        elif select_by == 'css_selector':
            select_by = By.CSS_SELECTOR
        locate = (select_by,select_value)
        try:
            if wait_type == "visibility": # 判断元素是否可见，如果可见就返回这个元素
                element = WebDriverWait(self._driver,time_out).until(EC.visibility_of_element_located(locator=(By.XPATH,select_value)))
            elif wait_type == "presence_of_element":
                element = WebDriverWait(self._driver,time_out).until(EC.presence_of_element_located(locator=locate))
            elif wait_type == "clickable":
                element = WebDriverWait(self._driver, time_out).until(EC.element_to_be_clickable(locator=locate))
        except TimeoutException:
            raise TimeoutException(msg="定位元素失败,定位方式是:{}".format(locate))
        except NoSuchElementException:
            raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(locate))
        return element

    def wait_find_elements(self, section, key, wait_type="visibility",time_out=10):
        """
        定位一组元素加上等待支持两种
        :param section: ini文件里的section，即用例名称
        :param key: ini文件里的key，即定位方式
        :param time_out: 超时时间
        :param wait_type: 等待方式
        :return: 返回元素
        """
        element = []
        ele = self._oper_ini.get_section(section, key)
        select = ele.split('=>')
        select_by = select[0].strip()
        select_value = select[1].strip()
        if select_by == 'xpath':
            select_by = By.XPATH
        elif select_by == 'link_text':
            select_by = By.LINK_TEXT
        elif select_by == 'class_name':
            select_by = By.CLASS_NAME
        elif select_by == 'css_selector':
            select_by = By.CSS_SELECTOR
        locate = (select_by,select_value)
        try:
            if wait_type == "visibility": # 判断元素是否可见，如果可见就返回这个元素
                element = WebDriverWait(self._driver,time_out).until(EC.visibility_of_all_elements_located(locator=(By.XPATH,select_value)))
            elif wait_type == "presence_of_element":
                element = WebDriverWait(self._driver,time_out).until(EC.presence_of_all_elements_located(locator=locate))
        except TimeoutException:
            raise TimeoutException(msg="定位元素失败,定位方式是:{}".format(locate))
        except NoSuchElementException:
            raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(locate))
        return element

    def find_elements(self,section, key):
        """
        定位一组元素
        :param section: ini文件里的section，即用例名称
        :param key: ini文件里的key，即定位方式
        :return: 返回定位到的元素
        """
        element = []
        ele = self._oper_ini.get_section(section, key)
        select = ele.split('=>')
        select_by = select[0].strip()
        select_value = select[1].strip()
        if select_by == 'xpath':
            try:
                element = self._driver.find_elements_by_xpath(select_value)
                self._log.info("通过xpath定位元素 %s" % select_value)
            except NoSuchElementException:
                self._log.error("定位%s失败" % select_value)
                raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(select_value))
        elif select_by == 'link_text':
            try:
                element = self._driver.find_elements_by_link_text(select_value)
                self._log.info("通过link_text定位元素 %s" % select_value)
            except NoSuchElementException:
                self._log.error("定位%s失败" % select_value)
                raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(select_value))
        elif select_by == 'class_name':
            try:
                element = self._driver.find_elements_by_class_name(select_value)
                self._log.info("通过class_name定位元素 %s" % select_value)
            except NoSuchElementException:
                self._log.error("定位%s失败" % select_value)
                raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(select_value))
        elif select_by == 'css_selector':
            try:
                element = self._driver.find_elements_by_css_selector(select_value)
                self._log.info("通过css_selector定位元素 %s" % select_value)
            except NoSuchElementException:
                self._log.error("定位%s失败" % select_value)
                raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(select_value))

        return element

    def wait_title(self, title):  # 判断title,返回布尔值
        WebDriverWait(self._driver, 10).until(EC.title_is(title))

    def wait_url(self, url):
        WebDriverWait(self._driver, 10).until(EC.url_to_be(url))

    def web_ready(self): # 判断页面是否加载完成
        web_state = ''
        start_time = time.time()
        while web_state != 'complete':
            time.sleep(10)
            web_state = self._driver.execute_script('return document.readyState')
            end_time = time.time()
            if int(end_time - start_time) > 60:
                self._log.error("页面加载超时")
                raise Exception
        return True




if __name__ == '__main__':
    driver = webdriver.Chrome()
    # opr = OperIni(r'E:\datacapsule\config\locate.ini')
    # ele1 = opr.get_section('login', 'login_name')
    # select = ele1.split('=>')
    # select_by = select[0].strip()
    # select_value = select[1].strip()
    # print("select_value"+select_value)
    base = BasePage(driver,'http://data.airlook.com/',r'E:\datacapsule\config\locate.ini')
    base.get_url()
    driver.maximize_window()
    print(base.web_ready())
    # ele = opr.get_section('login','link_text')

    name = base.wait_find_element('login', 'login_name')
    name.clear()
    name.send_keys("18520836299")
    pw = base.wait_find_element('login', 'login_password')
    pw.clear()
    pw.send_keys("airlook1234")
    base.wait_find_element('login', 'login', wait_type='clickable').click()
    if base.web_ready():
        try:
            ele = driver.find_element_by_class_name("active")
            print(ele)
            base._log.info("登录成功")
            print("登录成功")
        except Exception as e:
            base._log.error("登录失败")
            print(format(e))
            raise Exception






