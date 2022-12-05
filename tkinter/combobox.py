import tkinter.ttk as ttk
from tkinter import *


root=Tk()
root.title("info") 
root.geometry("680x480+400+150") 


values = [str(i) + "일" for i in range(1,32)] #1~31 까지의 숫자
combobox=ttk.Combobox(root, height=5, values=values) #사용자가 입력도 가능
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정

redonly_combobox=ttk.Combobox(root, height=10, values=values, stat="readonly") #읽기 전용, 사용자가 입력 불가능
redonly_combobox.current(0) #0번째 인덱스 값 선택
redonly_combobox.pack()


def btncmd():
    print(combobox.get()) #선택된 값 표시
    print(redonly_combobox.get())
    

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()