'''
@File    :   抖音-version-Android-下载.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/28 17:08   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def download():
    driver = DouYin.driver
    try:
        el = driver.find_element(By.XPATH, '//android.widget.Button[@text="我知道了"]')
        el.click()
        time.sleep(2)
    except:
        pass
    finally:
        TouchAction(driver).tap(x=600, y=1268).perform().release()
    time.sleep(3)
    el1 = driver.find_element(By.XPATH, '//android.widget.LinearLayout[contains(@content-desc,"分享")]')
    el1.click()
    time.sleep(3)
    el2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="保存本地"]')
    el2.click()
    time.sleep(10)


download()