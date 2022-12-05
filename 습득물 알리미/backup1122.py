'''
Lost 112 알림이 (gui)
만든이 : 구교현
instagram : @khxxn_9 문의 : DM
'''

from pathlib import Path
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.service import Service#셀레니움 4부터 사용하기위한 클래스
# from webdriver_manager.chrome import ChromeDriverManager #셀레니움 4부터 사용하기위한 클래스
import time 
import datetime
import re
import random
import smtplib
from email.mime.text import MIMEText

'''
중요 변수들
user_name 사용자 이름
user_email 사용자 이메일
category_value 카테고리 분류 코드
convert_value 카테고리 한글 명
'''
#===================================================================
#모든 사진들 관리 부분
#===================================================================
# 사진 불러오기 위한 변수
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\gongsul\Lost 112\build\assets\frame0") #사진 모아놓은 폴더 경로

# 사진 불러오는 함수
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
#===================================================================
#===================================================================

name=str(input("입력: "))



window = Tk()
window.title("Lost 112 알림이")
main_icon = PhotoImage(file=relative_to_assets("main_icon.png")) #메인아이콘 변경
window.iconphoto(False, main_icon)
#===================================================================

def find_info(category_value,convert_value,SN):
    global Id
    global Start_Ymd
    global End_Ymd


    

    url="https://www.lost112.go.kr/find/findDetail.do?"
    info=f"pageIndex=1&PRDT_CL_NM={convert_value}&PRDT_CL_CD01={category_value}&PRDT_CL_CD02=&START_YMD={Start_Ymd}&END_YMD={End_Ymd}&PRDT_NM=&DEP_PLACE=&SITE=&PLACE_SE_CD=&FD_LCT_CD=&IN_NM=&MDCD=&SRNO=&IMEI_NO=&F_ATC_ID=&ATC_ID={Id}&FD_SN={SN}&MENU_NO="
    info=url+info
    
    return info


def search_data(category_value,convert_value, user_email):
    global idxxx
    global Start_Ymd
    global End_Ymd
    global Id
    global url
    def mail(user_email, arr):
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
        s.sendmail("lostarticle07@gmail.com",user_email,msg.as_string())   #(보내는 메일, 받는 메일)
        s.quit()
    Start_Ymd=datetime.datetime.now()
    year=Start_Ymd.year
    month=Start_Ymd.month-2
    if month<10:
        month="0"+str(month)
    else:
        month=str(month)
    

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

    url='https://www.lost112.go.kr/find/findList.do?'
    url=url+f"PRDT_CL_NM={convert_value}&PRDT_CL_CD01={category_value}&PRDT_CL_CD02=&START_YMD={Start_Ymd}&END_YMD={End_Ymd}&PRDT_NM=&DEP_PLACE=&SITE=&PLACE_SE_CD=&FD_LCT_CD=&IN_NM=&MDCD=&SRNO=&IMEI_NO=&F_ATC_ID=&pageIndex=1&MENU_NO="


    option=webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches',['enable-logging'])
    # browser = webdriver.Chrome(options=option,service=Service(ChromeDriverManager().install()))
    browser=webdriver.Chrome(options=option)
    browser.minimize_window()# 전체화면


    def while_hamsu():
        # 트래픽 방지


        #같은 경로가 아닐경우 안에 파일경로를 입력해주어야한다.

        global idxxx
        global Start_Ymd
        global End_Ymd
        global Id
        global url
        
        def search_signum(url,temp):
            #head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            res=requests.get(url)
            res.raise_for_status()
            soup=BeautifulSoup(res.text,"lxml")
            signum= soup.find_all("tr")[temp+1]
            signum=signum.a["href"]
            return signum[-3:-2]

        SN=search_signum(url,idxxx)
        browser.get(url)# 주소안으로 접속
        Id=browser.find_elements(By.TAG_NAME,"tr")[idxxx+1]
        Id=Id.find_element(By.TAG_NAME,'a').text
        print(Id)
        browser.get(find_info(category_value,convert_value,SN))#새로운 유실물창 접속

        elem=browser.find_element(By.CLASS_NAME,"find_info").text

        arr=elem.split("\n")
        

        target1=re.compile("x")# 물품이름 타겟
        target2=re.compile("y")# 물품 분류 타겟
        
        p=re.compile(name)
        m=p.search(arr[0])
        
        if target2.search(arr[5])!='':# 물품분류가 맞는지 확인
            if target1.search(arr[0])!='': # 습득물 명이 맞는지 확인
                if m!=None:
                    mail(user_email, arr)
            if (idxxx < 5):
                idxxx = idxxx + 1
                window.after(2000,while_hamsu)
            elif (idxxx>=5):
                idxxx = 0
                window.after(2000,while_hamsu)


    window.after(2000,while_hamsu)
            
idxxx=0

#===================================================================
#위젯 지우는 함수
def widget_delet():
    for wg in window.place_slaves():
       wg.place_forget()

#위젯 다시 불러오는 함수
def widget_retry():
    Progressbar.stop()
    widget_delet()
    canvas.place(x = 0, y = 0)
    button_1.place(
        x=556.9999999999999,
        y=401.0,    
        width=180.0,
        height=55.0
    )
    entry_user.place(
        x=489.9999999999999,
        y=137.0,
        width=321.0,
        height=59.0
    )
    entry_email.place(
        x=489.9999999999999,
        y=218.0,
        width=321.0,
        height=59.0
    )
    entry_category.place(
        x=489.9999999999999,
        y=299.0,
        width=321.0,
        height=59.0
    )
    button_2.place(
        x=773.9999999999999,
        y=309.0,                             
        width=42.0,
        height=42.0
    )

#====================================================================
#progressbar 디자인
s=ttk.Style()
s.theme_use("clam")
# https://stackoverflow.com/questions/13510882/how-to-change-ttk-progressbar-color-in-python 진행바 색바꾸기 참고
# https://zetcode.com/tkinter/attributes/  색상참고
s.configure("bar.Horizontal.TProgressbar", foreground="#00CC36", background="#00CC36",troughcolor="#E8E8E8")
Progressbar = ttk.Progressbar(window, style="bar.Horizontal.TProgressbar", orient="horizontal",
                length=500, mode="indeterminate", maximum=100)
#=======================================================================
#finding창에 띄우는 위젯들 함수에 저장
new_label=Label(
    text="finding...",
    font=("Yu Gothic Medium", 40 * -1),
    foreground="SlateGray4",
    background="SlateGray3"
    )

def new_btn_1_cmd():
    # print("new button_1 clicked")
    answer = msgbox.askyesno(title="confirmation", message="프로그램을 나가시겠습니까?")
    # print(answer)
    if(answer==1):
        # print("트루")
        window.destroy()         # tkinter 종료
        raise SystemExit         # 전체 스크립트 종료

new_button_1_image = PhotoImage(file=relative_to_assets("new_button_1.png"))
new_button_1=Button(
    image=new_button_1_image,
    borderwidth=0,
    highlightthickness=0,
    command=new_btn_1_cmd,
    background="SlateGray3",
    activebackground="SlateGray3",
    relief="flat"
)

def new_btn_2_cmd():
    # print("new button_2 clicked")
    answer = msgbox.askyesno(title="confirmation", message="정보를 다시 입력하시겠습니까?")
    # print(answer)
    if(answer==1):
        # print("트루")
        window.configure(bg = "#3A7FF6")
        widget_retry()

new_button_2_image = PhotoImage(file=relative_to_assets("new_button_2.png"))
new_button_2=Button(
    image=new_button_2_image,
    borderwidth=0,
    highlightthickness=0,
    command=new_btn_2_cmd,
    background="SlateGray3",
    activebackground="SlateGray3",
    relief="flat"
)

window.geometry("862x519+450+120")
window.configure(bg = "#3A7FF6")

window.wm_attributes("-transparentcolor", "#ab23ff")
#=======================================================================
#캔버스 디자인
#=======================================================================

canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    430.9999999999999,
    0.0,
    861.9999999999999,
    519.0,
    fill="#FCFCFC",
    outline="")
#======================================================================
#새로운 창에 위젯 띄우기
#=======================================================================
def find_screen():
    global user_email
    Progressbar.start(15)
    window.configure(bg = "SlateGray3")
    Progressbar.place(x=185,y=300)
    new_label.place(x=360,y=200)
    new_button_1.place(
    x=485.0,
    y=452.0,
    width=114.0,
    height=40.0
)
    new_button_2.place(
        x=274.0,
        y=452.0,
        width=114.0,
        height=40.0
    )
    
    search_data(category_value,convert_value, user_email)
#=======================================================================
# 새로운 창 띄우기
#=======================================================================
def start_find():
    # print("시작")
    widget_delet()
    find_screen()
  


#=======================================================================
# 에러 메세지 띄우기
#=======================================================================

def ErrorMsg_2():
    result = user_email.find("@")
    if (result == -1):
        msgbox.showerror("error","올바른 이메일을 입력해주세요.")
    else:
        start_find()
     
def ErrorMsg_1():
    if (entry_category.get() == "분실물 분류명 찾기....." or user_name == "사용자 이름" or user_email == "이메일"):
        # print("오류")
        msgbox.showerror("error","입력창을 모두 입력해주세요.")
    else:
        ErrorMsg_2()
        

#=======================================================================
# register 버튼
#=======================================================================
def btn_1_cmd():
    global user_name
    global user_email
    user_name=entry_user.get()
    # print(entry_user.get())
    user_email=entry_email.get()
    # print(entry_email.get())
    ErrorMsg_1()
 
    # if (entry_category.get() != "분실물 분류명 찾기....."):
    #     print(category_value)
    


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_1_cmd,
    relief="flat"
)
button_1.place(
    x=556.9999999999999,
    y=401.0,    
    width=180.0,
    height=55.0
)
#=======================================================================
# 메인 화면 디자인
#=======================================================================
canvas.create_text(
    39.999999999999886,
    115.0,
    anchor="nw",
    text="Lost 112 알림이",
    fill="#FFFFFF",
    font=("배달의민족 한나체 Pro OTF", 24 * -1)
)

canvas.create_text(
    481.9999999999999,
    74.0,
    anchor="nw",
    text="Enter the details.",
    fill="#505485",
    font=("맑은 고딕", 24 * -1)
)

canvas.create_rectangle(
    39.999999999999886,
    160.0,
    99.99999999999989,
    165.0,
    fill="#FCFCFC",
    outline="")

def on_enter_user(e):
    name_blank=entry_user.get()
    if name_blank=="사용자 이름":
        entry_user.delete(0,"end")

def on_leave_user(e):
    name_blank=entry_user.get()
    if name_blank=="":
        entry_user.insert(0,"사용자 이름")


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    650.4999999999999,
    167.5,
    image=entry_image_1
)
entry_user = Entry(
    font=("맑은 고딕", 12),
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_user.place(
    x=489.9999999999999,
    y=137.0,
    width=321.0,
    height=59.0
)
entry_user.insert(0,"사용자 이름")
entry_user.bind("<FocusIn>",on_enter_user)
entry_user.bind("<FocusOut>",on_leave_user)

def on_enter_email(e):
    email_blank=entry_email.get()
    if email_blank=="이메일":
        entry_email.delete(0,"end")

def on_leave_email(e):
    email_blank=entry_email.get()
    if email_blank=="":
        entry_email.insert(0,"이메일")


entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    650.4999999999999,
    248.5,
    image=entry_image_2
)
entry_email = Entry(
    font=("맑은 고딕", 12),
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_email.place(
    x=489.9999999999999,
    y=218.0,
    width=321.0,
    height=59.0
)
entry_email.insert(0,"이메일")
entry_email.bind("<FocusIn>",on_enter_email)
entry_email.bind("<FocusOut>",on_leave_email)

def switch(key):
    global convert_value
    convert_value={"PRA000" : "가방",
    "PRO000" : "귀금속",
    "PRB000" : "도서용품",
    "PRC000" : "서류",
    "PRD000" : "산업용품",
    "PRQ000" : "쇼핑백",
    "PRE000" : "스포츠용품",
    "PRR000" : "악기",
    "PRM000" : "유가증권",
    "PRK000" : "의류",
    "PRF000" : "자동차",
    "PRG000" : "전자기기",
    "PRH000" : "지갑",
    "PRN000" : "증명서",
    "PRI000" : "컴퓨터",
    "PRP000" : "카드",
    "PRL000" : "현금",
    "PRJ000" : "휴대폰",
    "PRZ000" : "기타물품",
    "PRX000" : "유류품"
    }.get(key,"분실물 분류명 찾기.....")
    #print(convert_value)


'''
def on_enter_category(e):
    category_blank=entry_category.get()
    if category_blank=="분실물 분류명 찾기.....":
        entry_category.delete(0,"end")

def on_leave_category(e):
    category_blank=entry_category.get()
    if category_blank=="":
        entry_category.insert(0,"분실물 분류명 찾기.....")
'''

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    650.4999999999999,
    329.5,
    image=entry_image_3
)

entry_category = Entry(
    font=("맑은 고딕", 12),
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0,
    state="disable",
    disabledbackground="#F1F5FF",
    disabledforeground="#000716"
)
entry_category.place(
    x=489.9999999999999,
    y=299.0,
    width=321.0,
    height=59.0
)
entry_category.config(state="normal")
entry_category.insert(0,"분실물 분류명 찾기.....")
entry_category.config(state="disable")
# entry_category.bind("<FocusIn>",on_enter_category)
# entry_category.bind("<FocusOut>",on_leave_category)

def btn_2_cmd():
    #print("button_2 clicked")
    createCategoryWindow()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_2_cmd,
    relief="flat"
)
button_2.place(
    x=773.9999999999999,
    y=309.0,                             
    width=42.0,
    height=42.0
)


canvas.create_text(
    39.999999999999886,
    184.0,
    anchor="nw",
    text="이 프로그램은 lost 112에 올라오는 분실물을 자동적으로  \n파악하여 이메일로 알림을 보내주는 프로그램입니다.",
    fill="#FFFFFF",
    font=("맑은 고딕", 15 * -1)
)

#=======================================================================
#=======================================================================
def AfterChoose():
    switch(category_value)
    entry_category.config(state="normal")
    entry_category.delete(0,"end")
    entry_category.insert(0,convert_value)
    

icon = PhotoImage(file=relative_to_assets("icon.png"))
#=======================================================================
# 카테고리 선택 창 띄우기
#=======================================================================
def createCategoryWindow():
    #global category
    category = Toplevel(window)
    category.title("분실물 분류명 찾기.....")
    category.iconphoto(False, icon)
    category.geometry("720x480+480+85") #가로X세로+x좌표+y좌표
    Label(
        category,
        text="분류명 선택",
        fg="#2D6BBA",
        font=("배달의민족 한나체 Pro OTF", 18)
        ).place(x=25,y=10)
    Label(category,text="-----------------------------------------------------------------------------------------------------------------------------------------------",
        fg="#ADADAD").place(x=0,y=40)
    global category_var
    category_var=StringVar()
    #==========================================================
    #==========================================================
    global bag_image
    bag_image=PhotoImage(file=relative_to_assets("ico_01.gif"))
    bag_lable_1=Label(category,image=bag_image)
    bag_lable_2=Label(category,text="가방",font=("맑은 고딕", 14 * -1))
    bag_lable_1.place(x=30,y=60)
    bag_lable_2.place(x=35,y=110)
    bag=Radiobutton(
        category,
        value="PRA000",
        variable=category_var
        )
    bag.place(x=40,y=130)
    bag.select()
    #=========================================================
    #=========================================================
    global jewelry_image
    jewelry_image=PhotoImage(file=relative_to_assets("ico_02.gif"))
    jewelry_lable_1=Label(category,image=jewelry_image)
    jewelry_lable_2=Label(category,text="귀금속",font=("맑은 고딕", 14 * -1))
    jewelry_lable_1.place(x=122,y=60)
    jewelry_lable_2.place(x=121,y=110)
    jewelry=Radiobutton(
        category,
        value="PRO000",
        variable=category_var
        )
    jewelry.place(x=134,y=130)
    #========================================================
    #========================================================
    global book_image
    book_image=PhotoImage(file=relative_to_assets("ico_03.gif"))
    book_lable_1=Label(category,image=book_image)
    book_lable_2=Label(category,text="도서용품",font=("맑은 고딕", 14 * -1))
    book_lable_1.place(x=218,y=60)
    book_lable_2.place(x=209,y=110)
    book=Radiobutton(
        category,
        value="PRB000",
        variable=category_var
        )
    book.place(x=229,y=130)
    #=========================================================
    #=========================================================
    global document_image
    document_image=PhotoImage(file=relative_to_assets("ico_04.gif"))
    document_lable_1=Label(category,image=document_image)
    document_lable_2=Label(category,text="문서",font=("맑은 고딕", 14 * -1))
    document_lable_1.place(x=307,y=60)
    document_lable_2.place(x=310,y=110)
    document=Radiobutton(
        category,
        value="PRC000",
        variable=category_var
        )
    document.place(x=317,y=130)
    #===========================================================
    #===========================================================
    global industrial_goods_image
    industrial_goods_image=PhotoImage(file=relative_to_assets("ico_05.gif"))
    industrial_goods_lable_1=Label(category,image=industrial_goods_image)
    industrial_goods_lable_2=Label(category,text="산업용품",font=("맑은 고딕", 14 * -1))
    industrial_goods_lable_1.place(x=401,y=60)
    industrial_goods_lable_2.place(x=390,y=110)
    document=Radiobutton(
        category,
        value="PRD000",
        variable=category_var
        )
    document.place(x=412,y=130)
    #============================================================
    #============================================================
    global shopping_bag_image
    shopping_bag_image=PhotoImage(file=relative_to_assets("ico_06.gif"))
    shopping_bag_label_1=Label(category,image=shopping_bag_image)
    shopping_bag_lable_2=Label(category,text="쇼핑백",font=("맑은 고딕", 14 * -1))
    shopping_bag_label_1.place(x=497,y=60)
    shopping_bag_lable_2.place(x=494,y=110)
    shopping_bag=Radiobutton(
        category,
        value="PRQ000",
        variable=category_var
        )
    shopping_bag.place(x=508,y=130)
    #================================================================
    #================================================================
    global sports_equipment_image
    sports_equipment_image=PhotoImage(file=relative_to_assets("ico_07.gif"))
    sports_equipment_label_1=Label(category,image=sports_equipment_image)
    sports_equipment_lable_2=Label(category,text="스포츠용품",font=("맑은 고딕", 14 * -1))
    sports_equipment_label_1.place(x=593,y=60)
    sports_equipment_lable_2.place(x=578,y=110)
    sports_equipment=Radiobutton(
        category,
        value="PRE000",
        variable=category_var
        )
    sports_equipment.place(x=604,y=130)
    #==================================================================
    #==================================================================
    global instrument_image
    instrument_image=PhotoImage(file=relative_to_assets("ico_08.gif"))
    instrument_label_1=Label(category,image=instrument_image)
    instrument_lable_2=Label(category,text="악기",font=("맑은 고딕", 14 * -1))
    instrument_label_1.place(x=30,y=180)
    instrument_lable_2.place(x=35,y=230)
    instrument=Radiobutton(
        category,
        value="PRR000",
        variable=category_var
        )
    instrument.place(x=40,y=250)
    #==========================================
    #==========================================
    global securities_image
    securities_image=PhotoImage(file=relative_to_assets("ico_09.gif"))
    securities_label_1=Label(category,image=securities_image)
    securities_lable_2=Label(category,text="유가증권",font=("맑은 고딕", 14 * -1))
    securities_label_1.place(x=122,y=180)
    securities_lable_2.place(x=115,y=230)
    securities=Radiobutton(
        category,
        value="PRM000",
        variable=category_var
        )
    securities.place(x=134,y=250)
    #=====================================
    #=====================================
    global clothing_image
    clothing_image=PhotoImage(file=relative_to_assets("ico_10.gif"))
    clothing_label_1=Label(category,image=clothing_image)
    clothing_lable_2=Label(category,text="의류",font=("맑은 고딕", 14 * -1))
    clothing_label_1.place(x=218,y=180)
    clothing_lable_2.place(x=222,y=230)
    clothing=Radiobutton(
        category,
        value="PRK000",
        variable=category_var
        )
    clothing.place(x=229,y=250)
    #=====================================
    #=====================================
    global car_image
    car_image=PhotoImage(file=relative_to_assets("ico_11.gif"))
    car_label_1=Label(category,image=car_image)
    car_lable_2=Label(category,text="자동차",font=("맑은 고딕", 14 * -1))
    car_label_1.place(x=307,y=180)
    car_lable_2.place(x=304,y=230)
    car=Radiobutton(
        category,
        value="PRF000",
        variable=category_var
        )
    car.place(x=317,y=250)
    #=====================================
    #=====================================
    global electronic_equipment_image
    electronic_equipment_image=PhotoImage(file=relative_to_assets("ico_12.gif"))
    electronic_equipment_label_1=Label(category,image=electronic_equipment_image)
    electronic_equipment_lable_2=Label(category,text="전자기기",font=("맑은 고딕", 14 * -1))
    electronic_equipment_label_1.place(x=401,y=180)
    electronic_equipment_lable_2.place(x=390,y=230)
    electronic_equipment=Radiobutton(
        category,
        value="PRG000",
        variable=category_var
        )
    electronic_equipment.place(x=412,y=250)
    #=====================================
    #=====================================
    global wallet_image
    wallet_image=PhotoImage(file=relative_to_assets("ico_13.gif"))
    wallet_label_1=Label(category,image=wallet_image)
    wallet_lable_2=Label(category,text="지갑",font=("맑은 고딕", 14 * -1))
    wallet_label_1.place(x=497,y=180)
    wallet_lable_2.place(x=500,y=230)
    wallet=Radiobutton(
        category,
        value="PRH000",
        variable=category_var
        )
    wallet.place(x=508,y=250)
    #=====================================
    #=====================================
    global certificate_image
    certificate_image=PhotoImage(file=relative_to_assets("ico_14.gif"))
    certificate_label_1=Label(category,image=certificate_image)
    certificate_lable_2=Label(category,text="증명서",font=("맑은 고딕", 14 * -1))
    certificate_label_1.place(x=593,y=180)
    certificate_lable_2.place(x=590,y=230)
    certificate=Radiobutton(
        category,
        value="PRN000",
        variable=category_var
        )
    certificate.place(x=604,y=250)
    #=====================================
    #=====================================
    global computer_image
    computer_image=PhotoImage(file=relative_to_assets("ico_15.gif"))
    computer_label_1=Label(category,image=computer_image)
    computer_lable_2=Label(category,text="컴퓨터",font=("맑은 고딕", 14 * -1))
    computer_label_1.place(x=30,y=300)
    computer_lable_2.place(x=26,y=350)
    computer=Radiobutton(
        category,
        value="PRI000",
        variable=category_var
        )
    computer.place(x=40,y=370)
    #=====================================
    #=====================================
    global card_image
    card_image=PhotoImage(file=relative_to_assets("ico_16.gif"))
    card_label_1=Label(category,image=card_image)
    card_lable_2=Label(category,text="카드",font=("맑은 고딕", 14 * -1))
    card_label_1.place(x=121,y=300)
    card_lable_2.place(x=126,y=350)
    card=Radiobutton(
        category,
        value="PRP000",
        variable=category_var
        )
    card.place(x=133,y=370)
    #=====================================
    #=====================================
    global cash_image
    cash_image=PhotoImage(file=relative_to_assets("ico_17.gif"))
    cash_label_1=Label(category,image=cash_image)
    cash_lable_2=Label(category,text="현금",font=("맑은 고딕", 14 * -1))
    cash_label_1.place(x=218,y=300)
    cash_lable_2.place(x=222,y=350)
    cash=Radiobutton(
        category,
        value="PRL000",
        variable=category_var
        )
    cash.place(x=229,y=370)
    #=====================================
    #=====================================
    global mobile_phone_image
    mobile_phone_image=PhotoImage(file=relative_to_assets("ico_18.gif"))
    mobile_phone_label_1=Label(category,image=mobile_phone_image)
    mobile_phone_lable_2=Label(category,text="휴대폰",font=("맑은 고딕", 14 * -1))
    mobile_phone_label_1.place(x=307,y=300)
    mobile_phone_lable_2.place(x=304,y=350)
    mobile_phone=Radiobutton(
        category,
        value="PRJ000",
        variable=category_var
        )
    mobile_phone.place(x=317,y=370)
    #=====================================
    #=====================================
    global other_item_image
    other_item_image=PhotoImage(file=relative_to_assets("ico_19.gif"))
    other_item_label_1=Label(category,image=other_item_image)
    other_item_lable_2=Label(category,text="기타물품",font=("맑은 고딕", 14 * -1))
    other_item_label_1.place(x=401,y=300)
    other_item_lable_2.place(x=390,y=350)
    other_item=Radiobutton(
        category,
        value="PRZ000",
        variable=category_var
        )
    other_item.place(x=412,y=370)
    #=====================================
    #=====================================
    global lost_articles_image
    lost_articles_image=PhotoImage(file=relative_to_assets("ico_20.gif"))
    lost_articles_label_1=Label(category,image=lost_articles_image)
    lost_articles_lable_2=Label(category,text="유류품",font=("맑은 고딕", 14 * -1))
    lost_articles_label_1.place(x=497,y=300)
    lost_articles_lable_2.place(x=495,y=350)
    lost_articles=Radiobutton(
        category,
        value="PRX000",
        variable=category_var
        )
    lost_articles.place(x=508,y=370)
    #===============
    #==============
    def btn_3_cmd():    
        global category_value
        category_value=category_var.get()
        #print(category_value)
        AfterChoose()
        category.destroy()
    global button_image_3
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        category,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_3_cmd,
        relief="flat"
    )
    button_3.place(
        x=296.0,
        y=423.0,
        width=128.0,
        height=40.0
    )
    category.resizable(False,False)

#=======================================================================
#=======================================================================

window.resizable(False, False)





window.mainloop()
