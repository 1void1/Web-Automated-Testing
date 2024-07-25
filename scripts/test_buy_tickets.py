import unittest
from parameterized import parameterized
from page.page_buy_tickets import BuyLogin
from base.get_driver import  GetDriver
from page.page_login import PageLogin
from tools.read_json import read_json
from time import  sleep

global_var = 0

def get_data_login():
    data = read_json("buy_tickets.json")
    arrs = []
    for data in data.values():
        arrs.append((data['start_station'],data['arrive_station'],data['time'],data['name'],data['boardcard'],data['phone'],data['success'],data['except_result']))
    return arrs
# 测试登录
class Test_Login(unittest.TestCase):

    driver = None
    # 初始化方法
    @classmethod
    def setUpClass(cls):
         cls.driver  = GetDriver().get_driver()
         cls.buy_tickets = BuyLogin(cls.driver)
         cls.login = PageLogin(cls.driver)
    # 结束方法
    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    #("北京","上海","2024-07-25","孙海森","142725199908224856","15135976034","True","None")
    @parameterized.expand(get_data_login())

    def test_buy_tickets(self,start_station,arrive_station,time,name,boardcard,phone,success= None,expect_result=None,driver=driver):
        global global_var

        if global_var == 0:
            # 登录成功
            self.login.page_login("15135976034", "shs092121", self.driver)
            global_var = 1
        # 购票
        self.buy_tickets.page_buy_tickets(start_station,arrive_station,time,name,boardcard,phone)
        # 如果购票成功，判断购票成功
        if success:
            try:
                # 标志购票成功
                self.assertTrue(self.buy_tickets.page_submit_access)
                # 四次回退到回退选择购票信息页面
                for _ in range(3):
                    self.driver.back()
                try:
                    # 判断是否在选票界面
                    self.assertTrue(self.buy_tickets.page_buy_is_logout_success)
                except:
                    # 记录错误信息
                    self.buy_tickets.base_screenshot()
                # 已经为下一次测试用例做好准备
            except:
                self.buy_tickets.base_screenshot()
        # 如果信息错误
        else:
            msg = self.buy_tickets.page_buy_get_error_info()
            try:
                self.assertEqual(msg,expect_result)
                sleep(10)
                # 点击确认框
                self.buy_tickets.page_buy_click_button_OK()
                # 回退三次到火车票界面
                for _ in range(3):
                    self.driver.back()
                try:
                    # 判断是否在选票界面
                    self.assertTrue(self.buy_tickets.page_buy_is_logout_success)
                except:
                    # 记录错误信息
                    self.buy_tickets.base_screenshot()

            except AssertionError:
                self.buy_tickets.base_screenshot()


















