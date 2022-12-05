from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service#셀레니움 4부터 사용하기위한 클래스
# from webdriver_manager.chrome import ChromeDriverManager #셀레니움 4부터 사용하기위한 클래스
import time 
import datetime
import re
import random
import smtplib
from email.mime.text import MIMEText
# from datetime import datetime, timedelta

user_mail=str(input("이메일 입력:"))

def test():
    global Id
    def mail(user_mail, arr):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('lostarticle07@gmail.com','blnlfnaaieegbola')
        a0=arr[0].replace("습득물명 :", " :")
        a1=arr[1].replace("관리번호", "관리번호: ")
        a2=arr[2].replace("습득일", "습득일: ")
        a3=arr[3].replace("습득장소 ", "습득장소: ")
        a5=arr[5].replace("접수장소", "접수장소: ")
        a6=arr[6].replace("보관장소", "보관장소: ")
        a8=arr[8].replace("보관장소연락처", "보관장소 연락처: ")
        

        #본문
        msg=MIMEText(arr[0]+"\n"+    
                    a1+"\n"+
                    a2+"\n"+
                    a3+"\n"+
                    a5+"\n"+
                    a6+"\n"+
                    a8)   

        #제목
        msg['Subject']='습득물 알리미 (7조)'+a0
        s.sendmail("lostarticle07@gmail.com",user_mail,msg.as_string())   #(보내는 메일, 받는 메일)
        s.quit()
        
        

    def find_info():
        global Id
        Start_Ymd=datetime.datetime.now()
        year=Start_Ymd.year
        month=Start_Ymd.month-2
        day="01"
        Start_Ymd=str(year)+str(month)+day

        End_Ymd=datetime.datetime.now()
        year=End_Ymd.year
        month=End_Ymd.month
        day=End_Ymd.day

        if day<10:
            day="0"+str(day)
        else:
            day=str(day)

        End_Ymd=str(year)+str(month)+day

        a=''
        b=''# 물품 분류 코드 

        url="https://www.lost112.go.kr/find/findDetail.do?"
        info=f"pageIndex=1&PRDT_CL_NM=&PRDT_CL_CD01={a}&PRDT_CL_CD02={b}&START_YMD={Start_Ymd}&END_YMD={End_Ymd}&PRDT_NM=&DEP_PLACE=&SITE=&PLACE_SE_CD=&FD_LCT_CD=&IN_NM=&MDCD=&SRNO=&IMEI_NO=&F_ATC_ID=&ATC_ID={Id}&FD_SN=1&MENU_NO="
        info=url+info
        
        return info



    url='https://www.lost112.go.kr/find/findList.do'

    option=webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches',['enable-logging'])
    # browser = webdriver.Chrome(options=option,service=Service(ChromeDriverManager().install()))
    browser=webdriver.Chrome(options=option)
    browser.minimize_window()# 전체화면



    while(1):
        time.sleep(random.randint(1,3))# 트래픽 방지


        #같은 경로가 아닐경우 안에 파일경로를 입력해주어야한다.

        for temp in range(5):
            browser.get(url)# 주소안으로 접속
            Id=browser.find_elements(By.TAG_NAME,"tr")[temp+1]
            Id=Id.find_element(By.TAG_NAME,'a').text
            print(Id)
            browser.get(find_info())#새로운 유실물창 접속

            elem=browser.find_element(By.CLASS_NAME,"find_info").text

            arr=elem.split("\n")
            print(arr[4])
            target1=re.compile("x")# 물품이름 타겟
            target2=re.compile("y")# 물품 분류 타겟

            if target2.search(arr[5])!='':# 물품분류가 맞는지 확인
                if target1.search(arr[0])!='': # 습득물 명이 맞는지 확인
                    mail(user_mail, arr)




            time.sleep(random.randint(1,3))# 트래픽 방지
if user_mail!="":
    test()
    