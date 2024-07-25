import page
from base.base import  Base
from selenium.webdriver.common.by import  By
from  time import  sleep


class BuyLogin(Base):
    # 点击购买火车票
    def page_click_buy_tickets(self):
        self.base_click(page.buy_click_tickets)

    # 选择出发站
    def page_input_start_station(self,start_station):
        self.base_input(page.buy_start_station,start_station)

    # 选择到达站
    def page_input_arrive_station(self,arrive_station):
        self.base_input(page.buy_arrive_station,arrive_station)

    # 选择日期
    def page_input_time(self,time):
        date_input = self.base_find_element(page.buy_start_time)  # "//input[@name='date']"
        self.driver.execute_script("arguments[0].value = arguments[1];", date_input,time)

    # 选择搜索
    def page_click_find(self):
        self.base_click(page.buy_click_find)

    # 点击购买
    def page_click_buy_ticket(self):
        self.base_click(page.but_click_buy_ticket)

    # 输入购票人姓名
    def page_input_buy_ticket_name(self,name):
        self.base_input(page.buy_input_name,name)

    # 输入购票人身份证信息
    def page_input_buy_ticket_board(self,board):
        self.base_input(page.buy_input_boardcard,board)

    # 输入取票人姓名
    def page_input_contact_name(self,name):
        self.base_input(page.buy_input_contact_name,name)

    # 输入取票人电话
    def page_input_contact_phone(self,phone):
        self.base_input(page.buy_input_contact_phone,phone)

    # 点击提交订单
    def page_click_submit(self):
        self.base_click(page.buy_click_submit)

    # 提交订单成功
    def page_submit_access(self):
        self.base_if_exist(page.buy_submit_success)

    # 获取异常提示信息
    def page_buy_get_error_info(self):
        return self.base_get_text(page.buy_submit_fail_info)
    # 点击错误提示信息的确认框
    def page_buy_click_button_OK(self):
        self.base_click(page.buy_submit_click_OK)
    # 退出成功
    def page_buy_is_logout_success(self):
        self.base_if_exist(page.buy_click_tickets)

    # 购票业务
    def page_buy_tickets(self,start_station,arrive_station,time,name,board,phone):
        self.page_click_buy_tickets()
        self.page_input_start_station(start_station)
        self.page_input_arrive_station(arrive_station)

        self.page_input_time(time)

        self.page_click_find()
        self.page_click_buy_ticket()
        self.page_input_buy_ticket_name(name)
        self.page_input_buy_ticket_board(board)
        self.page_input_contact_name(name)
        self.page_input_contact_phone(phone)
        self.page_click_submit()






