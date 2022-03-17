'''
@File    :   Taobao-10.10.5-Android-私聊发语音.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/17 14:50   xyhu       10.10.5     None
'''
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def send_voice():
    driver = Taobao.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="消息"]')
            el1.click()
            time.sleep(2)
            break
        except:
            el2 = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            el2.click()
            time.sleep(2)
            el1_times += 1
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="联系人"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="A测试"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="发消息"]')
    el5.click()
    time.sleep(2)
    el6_times = 0
    while el6_times < 3:
        try:
            el6 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="语音"]')
            el6.click()
            time.sleep(2)
            el7 = driver.find_element(By.XPATH, '//android.widget.Button[@text="按住 说话"]')
            TouchAction(driver).long_press(el7, duration=3000).wait(3000).perform()
            time.sleep(5)
            break
        except:
            el6_times += 1


send_voice()
