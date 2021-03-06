# 爬取指定微博
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://weibo.com/2264713730/KgDR23sSX?ref=feedsdk&type=comment#_rnd1621736455489')
try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'WB_feed_detail'))) #使用expected_conditions自带验证函数
    for title in driver.find_elements_by_css_selector('.WB_detail > .W_f14'):
        print(title.text)
finally:
    driver.close() # close the driver