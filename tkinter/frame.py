from tkinter import *


root=Tk()
root.title("info") 
root.geometry("680x480+400+150") 

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

#메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1) #bd는 외곽선
frame_burger.pack(side="left", fill="both",expand=True) #side는 프레임 위치, fill은 위치에서 위아래로 채우는거, expand는 옆으로 채우는거

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()


#음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()
