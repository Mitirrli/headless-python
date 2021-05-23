# 查找百度热搜
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'s-hotsearch-title'))) #使用expected_conditions自带验证函数
    for title in driver.find_elements_by_css_selector('.title-content'):
        print(title.find_element_by_css_selector('.title-content-title').text)
finally:
    driver.close() # close the driver