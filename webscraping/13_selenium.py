from selenium import webdriver
from selenium.webdriver.common.by import By


import time
option=webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging'])
# browser = webdriver.Chrome(options=option,service=Service(ChromeDriverManager().install()))
browser=webdriver.Chrome(options=option)

while(1):
    # 1.네이버 이동
    browser.get("http://naver.com")


    # 2. 로그인 버튼 클릭
    elem = browser.find_element(By.NAME,"link_login")
    elem.click()

    # 3. id, pw 입력
    browser.find_element(By.ID,"id").send_keys("naver_id")
    browser.find_element(By.ID,"pw").send_keys("naver_pw") 

    # 4. 로그인 버튼 클릭
    browser.find_element(By.ID,"log.login").click()