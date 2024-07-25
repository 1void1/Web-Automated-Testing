import unittest
from parameterized import parameterized
from page.page_login import PageLogin
from base.get_driver import  GetDriver
from tools.read_json import read_json
from time import  sleep

global_error_info = 0

def get_data_login():
    datas = read_json("login.json")
    # print(datas)
    arrs = []
    for data in datas.values():
       arrs.append((data['username'],data['password'],data['success'],data['expect_result']))
    return arrs

# 测试登录
class Test_Login(unittest.TestCase):
    driver = None

    # 初始化方法
    @classmethod
    def setUpClass(cls):
         cls.driver  = GetDriver().get_driver()
         cls.login= PageLogin(cls.driver)

    # 结束方法
    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    @parameterized.expand(get_data_login())
    def test_login(self,username,password,success = None,expect_result =None,driver=driver):
        '''
        账号为空和密码为空以及勾选协议为空都不行，第一次都是用户名或密码错误，之后每次点击都是登录失败,所以为了验证，先验证三个基本信息
        检查合格？
        '''
        global global_error_info
        #  账号、密码不为空并且点击了协议
        self.login.page_login(username,password,self.driver)
        if success:
            try:
                # 判断安全退出是否存在,判断是否登录成功
                print(self.login.page_is_login_success)
                self.assertTrue(self.login.page_is_login_success)
                # 点击退出
                self.login.page_click_logout()

                try:
                    # 判断是否退出成功
                    self.assertTrue(self.login.page_is_logout_success)
                except:
                    self.login.base_screenshot()
                    # 截图
                # 为下一次错误做准备
                global_error_info = 0
                #退出成功之后，为下次做准备
                # 点击登录链接
                self.login.page_click_login()
                # 点击 账号密码登录
                self.login.page_click_pwd_login()
            except:
                self.login.base_screenshot()
                # 截图
        else:

            if global_error_info == 0:
                # 如果是错误的
                msg = self.login.page_get_error_info()
                global_error_info = 1
            else:
                msg = self.login.page_get_error_info1()
                global_error_info = 1

            # print(msg)
            try:
                # 进行断言，判断预期结果和真实结果是否相同
                self.assertEqual(msg,expect_result)
            except AssertionError:
                # 截图  将错误信息保存
                self.login.base_screenshot()

        # 刷新页面，主要就是为了刷新已经填写的协议
        self.driver.refresh()
        sleep(2)
        # 点击 账号密码登录
        self.login.page_click_pwd_login()










