
from selenium.webdriver.common.by import By

# 以下是服务器域名配置地址
# 测试的地址
url = 'https://www.qunar.com/'

# 登录测试
##################################################################################################################
# 关于去哪儿
login_please_login = By.XPATH, "//div[contains(text(), '关于去哪儿')]"
# 登录按钮
login_login = By.XPATH,"//a[text()='登录']"
# 点击密码登录
login_click_pwd_login = By.XPATH,"//div[text()='密码登录']"

# 账号
login_input_account = By.XPATH,"//input[@placeholder='手机/邮箱/用户名']"

# 密码
login_input_password = By.XPATH,"//input[@placeholder='密码']"

# 协议
login_click_protocol = By.XPATH,"//input[@id='agreement']"

# 登录按钮
login_click_login_button = By.XPATH,"//div[@class='button' and @role='button']/span[text()='登录']"

# 滑动按钮
login_moving_btn =By.CSS_SELECTOR, ".OQphwVk_QrhLuedI5-Jme"
# 拖动区域
login_moving_area = By.CSS_SELECTOR, ".NrgjHeg7YBdiFd3U9T_j_"

# 退出按钮
login_logout = By.XPATH,"//a[text()='退出']"  #"//a[text()='退出']"

# 请输入手机号
login_phone_lack =  By.XPATH,"//span[text()='请输入手机/邮箱/用户名']"
# 请输入验证码
login_pwd_lack = By.XPATH,"//span[text()='请输入密码']"
# 登录失败
login_login_fail = By.XPATH,"//span[text()='登录失败']"
# 未勾选协议
login_protocol_fail = By.XPATH,"//span[text()='请阅读并勾选用户协议']"

# 用户名或者密码错误
login_account_or_pwd_error = By.XPATH,"//span[text()='用户名或密码错误']"
#################################################################################################################
# 点击购买火车票
buy_click_tickets = By.XPATH, "//b[text()='火车票']"

# 出发站
buy_start_station = By.XPATH, "//input[@name='fromStation']"

# 到达站
buy_arrive_station = By.XPATH,"//input[@name='toStation']"

# 日期
buy_start_time = By.XPATH,"//input[@name='date']"
# buy_start_time = By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[1]/input"
# 点击空白 确保日期填写正确
# buy_click_space = By.XPATH,"//a[@class='banner-bglink' and @id='banner-camel']"
# 查找
buy_click_find = By.XPATH, "//button[@name='stsSearch']"

# 点击购买
but_click_buy_ticket = By.XPATH,"//span[text()='购\u00A0\u00A0买']"

# 姓名
buy_input_name = By.XPATH,"//input[@class='inp_txt']"

# 身份证信息
buy_input_boardcard = By.XPATH,"//input[@name='pCertNo_0']"

# 填写取票人姓名
buy_input_contact_name = By.XPATH,"//input[@type='text' and @name='contact_name']"
# 填写电话
buy_input_contact_phone = By.XPATH,"//input[@type='text' and @name='contact_phone']"

# 点击提交订单
buy_click_submit = By.XPATH,"/html/body/form/div[2]/div[2]/div[4]/div[2]/div[3]/button"

# 提交订单成功
buy_submit_success = By.XPATH,"//span[@class='msg-title' and text()='在线支付']"

# 提交订单失败
buy_submit_fail_info = By.XPATH,"//div[@class='retitle']"
# 点击确认
buy_submit_click_OK = By.XPATH,"//b[text()='确定']"
###############################################################################################################
# 点击游记
publish_click_travel = By.XPATH,"//b[text()='攻略']"

# 点击发表游记
publish_click_travel_notes = By.XPATH,"//a[@class='link' and @href='//travel.qunar.com/youji/create']"

# 输入游记名称
publish_click_travel_name_before = By.XPATH,"//*[@id='b_note_hd']/div[2]/a"
publish_click_travel_name = By.XPATH,"//input[contains(@class, 'title_input')]"

# 输入标题
publish_click_travel_title = By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/textarea"

# 输入游玩地点
publish_click_travel_place = By.XPATH,"//textarea[@data-placeholder='添加随记、交通或旅游心得']"

# 点击发表
publish_click_publish = By.XPATH,"//a[@class='finish_note_btn js_finish_note' and @data-beacon='Submit_bottom']"

# 错误信息，标题不能为空
publish_error_info = By.XPATH, "//div[@class='tit_tip' and @style='display: block;']/span" #By.XPATH,"//span[text()='标题不能为空']"

# 发表成功
publish_success = By.XPATH,"/html/body/div[12]/div/div/div[1]/p[1]"

# 发表成功的确认
publish_success_button_ok = By.XPATH,"//*[@id='dlg2']/div/div/div[2]/a"
