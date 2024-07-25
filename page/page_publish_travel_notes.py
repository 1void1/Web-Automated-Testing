import page
from base.base import  Base
from selenium.webdriver.common.by import  By
from  time import  sleep

global_var = 0

class PagePublish(Base):
    # 点击攻略
    def page_click_strategy(self):
        self.base_click(page.publish_click_travel)
    # 点击发表游记
    def page_click_publish_travel_notes(self):
        self.base_click(page.publish_click_travel_notes)

    #  切换主窗口到游记界面
    def page_publish_change_window(self,driver):
        self.base_change_window(driver)



    # 输入游记名称
    def page_input_travel_name(self,name):
        self.base_click(page.publish_click_travel_name_before)
        self.base_input(page.publish_click_travel_name,name,1)

    # 输入游记开头
    def page_input_traval_title(self,title):
        self.base_click(page.publish_click_travel_title)
        self.base_input(page.publish_click_travel_title,title,1)

    # 为游记添加目录
    def page_input_travel_first_table(self):
        pass


    # 输入游记内容
    def page_input_content(self,content):
        self.base_click(page.publish_click_travel_place)
        self.base_input(page.publish_click_travel_place,content,1)

    # 点击发表游记
    def page_click_publish(self):
        self.base_click(page.publish_click_publish)

    # 点击发表之后 错误信息
    def page_publish_get_error_info(self):
        return self.base_get_text(page.publish_error_info)

    # 发表成功
    def page_publish_success(self):
        return self.base_if_exist(page.publish_success)

    # 退出成功 确认
    def page_publish_logout(self):
        return self.base_if_exist(page.publish_click_travel_notes)

    # 发表成功确认
    def page_publish_success_button_ok(self):
        self.base_click(page.publish_success_button_ok)

    def page_publish(self,name,title,content):

        global global_var
        if global_var == 0:
            self.page_click_strategy()
            global_var = 1
        self.page_click_publish_travel_notes()
        self.page_publish_change_window(self.driver)
        sleep(5)
        self.page_input_travel_name(name)
        sleep(2)
        self.page_input_traval_title(title)
        sleep(2)
        self.page_input_content(content)
        sleep(2)
        self.page_click_publish()





