'''

'''
from  selenium import  webdriver
import  page


class GetDriver:

    driver  = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)

        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 注意：此处有一个很大的坑
            cls.driver = None