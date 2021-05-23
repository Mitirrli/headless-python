# 查找新浪热搜
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://weibo.com/a/hot/realtime')
try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'UG_content_row'))) #使用expected_conditions自带验证函数
    for title in driver.find_elements_by_css_selector('.UG_content_row'):
        print(title.find_element_by_css_selector('.UG_list_b > .list_des > .list_title_b > a').text.strip('#'))
finally:
    driver.close() # close the driver