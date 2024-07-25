'''
这个文件主要是对Web自动化测试时，经常使用的操作进行封装
'''
# 导入相关的包
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import ActionChains
class Base:
    '''
    将常用的函数封装在一个类中，方便调用
    '''
    # 初始化函数
    def __init__(self,driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # 查找元素的操作
    def base_find_element(self,loc,timeout=30,poll=0.5):
        '''
        :param loc: 
        :param timeout: 隐式等待的时间,默認參數為30
        :param poll: 轮询的时间间隔
        :return: 
        '''
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击操作
    def base_click(self,loc):
        '''
        :param loc: 定位路径
        :return: None
        '''
        self.base_find_element(loc).click()

    # 切换窗口
    def base_change_window(self, driver):
        cur_window = driver.current_window_handle
        handles = driver.window_handles
        if len(handles)>2:
            # print(cur_window)
            # print(handles)
            driver.switch_to.window(handles[0])
            driver.close()
            handles = handles[1:]
            # print(handles)
        # 获取不是当前窗口的句柄，并切换
        for handle in handles:
            if handle != cur_window:
                driver.switch_to.window(handle)



    # 输入
    def base_input(self,loc,value,default_para = 0):
         el = self.base_find_element(loc)  # 先找到元素
         # print(self.base_find_element(loc) )
         if default_para == 0:
             el.clear() # 清除可能的内容
         el.send_keys(value)  # 输入数据


    # 获取文本
    def base_get_text(self,loc):
        return self.base_find_element(loc).text


    # 获取Value属性
    def base_get_value(self,loc):
        '''
        :param loc:
        :return:
        '''
        # 使用get
        return self.base_find_element(loc).get_attribute("value")

    # 截图操作
    def base_screenshot(self):
        '''
        :return: None
        '''
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    # 拖动滑块方法
    def base_move(self, loca, locb):
        loc1 = self.base_find_element(loca)
        loc2 = self.base_find_element(locb)
        self.action.drag_and_drop_by_offset(loc1, loc2.size['width'], -loc2.size['height'])
        self.action.move_by_offset(10, 10)
        self.action.perform()
        time.sleep(1)

    # 移动到空白处
    def base_move_to_empty_space(self):
        self.action.move_by_offset(0, 0)
        self.action.click()
        self.action.perform()
        time.sleep(1)

    # 封装判断元素是否存在
    def base_if_exist(self,loc):
        try:
            self.base_find_element(loc,timeout=5)
            print(True)
            return True
        except:
            print(False)
            return  False

    # 判断框是否为空
    def base_get_text_rect(self, loc):
        return self.base_find_element(loc).get_attribute('value')

    def base_is_input_empty(self, loc):
        input_text = self.base_get_text_rect(loc)
        return len(input_text.strip()) == 0

    # 判断复选框是否为空
    def base_is_checkbox_checked(self, loc):
        element = self.base_find_element(loc)
        return element.is_selected()