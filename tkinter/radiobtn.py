from tkinter import *


root=Tk()
root.title("info") 
root.geometry("680x480+400+150") 

label1 = Label(root, text="메뉴를 선택하세요").pack() #이렇게 해도 됨

burger_var=IntVar() #여기에 int 형으로 값을 저장
btn_burger1= Radiobutton(root, text="햄버거", value=1, variable=burger_var) #라디오버튼 생성
btn_burger1.select() #첫번째 버튼이 선택 되어있음
btn_burger2= Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3= Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label1 = Label(root, text="음료를 선택하세요").pack()

drink_var=StringVar()
btn_drink1 = Radiobutton(root, text="콜라",value="콜라",variable=drink_var)
btn_drink1.select() #기본값 선택
btn_drink2 = Radiobutton(root, text="사이다",value="사이다",variable=drink_var)



btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get()) #햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())  #음료 중 선택된 값을 출력

btn = Button(root, text="주문", command=btncmd) 
btn.pack()

root.mainloop()