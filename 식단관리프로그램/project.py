from tkinter import*
win=Tk()

win.title("project")
win.geometry("420x500")
win.option_add("*Font","고딕 20")
finish=False
life_style=''
def main():
    global life_style  
    def conceal():
        lab1.place_forget()
        ent1.place_forget()
        lab2.place_forget()
        ent2.place_forget()
        btn.place_forget()
        

    # def callback(event):
    #     win.focus_set()
    #     print(event.x,event.y)

    # win.bind("<Button-1>",callback)

    #배경이미지 
    screen=Canvas(win,width=720,height=800,bg='black')
    screen.pack()
    # screen_img=PhotoImage(file="")
    # screen.create_image(720,800,image=screen_img)


    #키 라벨 
    lab1=Label(win)
    lab1.config(text="키")
    lab1.place(x=180,y=22)
    
    #키 입력창
    ent1=Entry(win)

    ent1.place(x=40,y=70)
    #몸무게 라벨
    lab2=Label(win)
    lab2.config(text="몸무게")
    lab2.place(x=155,y=120)
    #몸무게 입력창
    ent2=Entry(win)
    ent2.place(x=40,y=170)


    #확인 버튼
    btn=Button(win)
    btn.config(text="확인")
    def confirm():
        global life_style
        global finish
        height=ent1.get()
        weight=ent2.get()
        print(height, weight)
        conceal()
        life()
      
    btn.config(command=confirm)
    btn.place(x=160,y=210)
    



def life():
    global life_style
    def conceal():
        lab1.place_forget()
        btn1.place_forget()
        btn2.place_forget()
        btn3.place_forget()

   
    lab1=Label(win)
    lab1.config(text="당신이 추구하는 관리 방식은?")
    lab1.place(x=20,y=22)


    btn1= Button(win)
    btn1.config(text='체중감량')
    def click1():
        global life_style
        life_style='minus' 
        conceal() 
        return life_style
    btn1.config(command=click1)
    btn1.place(x=5,y=100)

    btn2= Button(win)
    btn2.config(text='체중유지')
    def click2():
        global life_style
        life_style='zero' 
        conceal() 

    btn2.config(command=click2)
    btn2.place(x=145,y=100)

    btn3= Button(win)
    btn3.config(text='체중증가')
    def click3():
        global life_style
        life_style='plus'
        conceal()  


    btn3.config(command=click3)
    btn3.place(x=285,y=100)
    print(f"{life_style}")
 

if __name__=="__main__":
    main()
    


win.mainloop()

