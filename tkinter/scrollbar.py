from tkinter import *


root=Tk()
root.title("info") 
root.geometry("680x480+400+150") 

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y") #fill="y"를 하면 스크롤이 길어짐

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10,yscrollcommand=scrollbar.set)
for i in range(1,32): #1~31일
    listbox.insert(END, str(i)+"일") # 1일, 2일, ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) #스크롤바를 잡아서 리스트박스를 움직이게 할 수 있음

root.mainloop()
