import unittest
from parameterized import parameterized
from page.page_login import PageLogin
from base.get_driver import  GetDriver
from page.page_publish_travel_notes import PagePublish
from tools.read_json import read_json

from time import  sleep

global_var = 0

def get_data_publish():
    datas = read_json("publish_travel_notes.json")
    # print(datas)
    arrs = []
    for data in datas.values():
       arrs.append((data['name'],data['title'],data['content'],data['success'],data['except_result']))
    return arrs

# 测试登录
class Test_Publish(unittest.TestCase):
    driver = None

    # 初始化方法
    @classmethod
    def setUpClass(cls):
         cls.driver  = GetDriver().get_driver()
         cls.login = PageLogin(cls.driver)
         cls.publish =PagePublish(cls.driver)
    # 结束方法
    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    @parameterized.expand(get_data_publish())
    def test_publish(self,name,title,content,success=None,except_result=None,driver=driver):
        global global_var

        if global_var == 0:
            global_var = 1
            # 登录成功
            self.login.page_login("15135976034", "shs092121", self.driver)

        # 发表游记
        self.publish.page_publish(name,title,content)

        if success:
            try:
                # 判断是否发表成功
                sleep(2)
                self.assertTrue(self.publish.page_publish_success)
                # 退出 点击确认
                self.publish.page_publish_success_button_ok()


                try:
                    # 判断是否退出成功  判断是否有游记
                    self.assertTrue(self.publish.page_publish_logout)

                except:
                    # 截图
                    self.publish.base_screenshot()

                # 已经为下次测试用例做准备
            except:
                # 截图
                self.publish.base_screenshot()
            sleep(2)
        else:
            sleep(2)
            msg = self.publish.page_publish_get_error_info()
            try:
                self.assertEqual(msg,except_result)

            except AttributeError:
                # 截图
                self.publish.base_screenshot()

            # 退出到游记界面为下次做准备
            # 获取当前页面 和所有界面
            cur_window = self.driver.current_window_handle
            all_window = self.driver.window_handles
            # 关闭当前界面
            self.driver.close()
            # 将句柄切换到之前的界面 为下一次测试用例做准备
            for window in all_window:
                if window != cur_window:
                    self.driver.switch_to.window(window)















