from time import sleep

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    # 初始化 WebDriver
    driver = webdriver.Chrome()

    try:
        # 打开目标网站
        driver.get("https://www.qunar.com/")  # 请将此行替换为你的目标网站 URL

        # 等待元素可见
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '关于去哪儿')]")))

        # 确保元素可见和可点击
        if element.is_displayed() and element.is_enabled():
            # 滚动到元素可见位置
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)  # 确保滚动完成

            # 使用 JavaScript 点击元素
            driver.execute_script("arguments[0].click();", element)
        else:
            print("元素不可见或不可点击")
        time.sleep(10)
        # 其他操作...

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭浏览器
        driver.quit()


