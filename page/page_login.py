import page
from base.base import  Base
from selenium.webdriver.common.by import  By
from  time import  sleep

global_variable = 0
class PageLogin(Base):

    # 切换到登录界面
    def page_click_please_login(self):
        self.base_click(page.login_please_login)

    #  切换主窗口到登录界面
    def page_change_window(self,driver):
        self.base_change_window(driver)

    # 点击 登录按钮
    def  page_click_login(self):
        self.base_click(page.login_login)

    # 点击 密码登录
    def page_click_pwd_login(self):
        self.base_click(page.login_click_pwd_login)

    # 输入账号
    def page_input_account(self,username):
        self.base_input(page.login_input_account,username)
    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.login_input_password,password)
    # 点击协议
    def page_click_protocol(self):
        self.base_click(page.login_click_protocol)

    # 登录
    def page_click_login_button(self):
        self.base_click(page.login_click_login_button)

    # 判断是否登录成功
    def page_is_login_success(self):
        self.base_if_exist(page.login_logout)

    # 判断是否退出成功
    def page_is_logout_success(self):
        self.base_if_exist(page.login_login)

    # 安全退出
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 在登陆前获取异常信息
    def page_get_error_info_before(self):
        #判断是否输入输入用户名
        if self.base_is_input_empty(page.login_input_account):
            # 返回用户名为空
            return self.base_get_text(page.login_phone_lack)
        # 判断是否输入密码
        elif self.base_is_input_empty(page.login_input_password):
            # 返回密码为空
            return  self.base_get_text(page.login_pwd_lack)
        # 判断协议是否勾选
        elif self.base_is_checkbox_checked(page.login_click_protocol):
            # 返回协议未勾选
            return self.base_get_text(page.login_protocol_fail)
        # 否则就是账号 或者密码格式不对 或者是账号不对 密码不对等等
        # else:
        #     return self.base_get_text(page.login_login_fail)

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_account_or_pwd_error)

    def page_get_error_info1(self):
        return self.base_get_text(page.login_login_fail)


    # 移动滑块
    def page_moving_vertify_code(self):
        self.base_move(page.login_moving_btn,page.login_moving_area)


    # 登录业务
    def page_login(self,username,password,driver):
        # 点击去哪切换到登录界面-切换窗口-点击登录-点击账号密码登录-输入账号-输入密码-同意协议-点击登录-移动滑块-点击空白区域
        global global_variable
        if global_variable == 0:
            global_variable = 1
            self.page_click_please_login()
            self.page_change_window(driver)
            self.page_click_login()
            self.page_click_pwd_login()

        self.page_input_account(username)
        self.page_input_password(password)
        self.page_click_protocol()
        self.page_click_login_button()
        # 首先判断是否输入了账号 密码 以及点击协议

        # 点击了之后，就执行
        self.page_moving_vertify_code()
        self.base_move_to_empty_space()





