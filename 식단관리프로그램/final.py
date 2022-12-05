from tkinter import*

root=Tk()
root.title("project")
root.geometry("420x500") 
root.option_add("*Font","고딕 20")
life_style=''
finish=False
def main():
    def conceal():
        lab1.place_forget()
        ent1.place_forget()
        lab2.place_forget()
        ent2.place_forget()
        btn.place_forget()
    #키 라벨 
    lab1=Label(root)
    lab1.config(text="키")
    lab1.place(x=180,y=22)
    #키 입력창
    ent1=Entry(root)
    ent1.place(x=40,y=70)

    #몸무게 라벨
    lab2=Label(root)
    lab2.config(text="몸무게")
    lab2.place(x=155,y=120)
    #몸무게 입력창
    ent2=Entry(root)
    ent2.place(x=40,y=170)


    #확인 버튼
    btn=Button(root)
    btn.config(text="확인")
    def confirm():
        global life_style
        global finish
        height=ent1.get()
        weight=ent2.get()
        conceal()
        project1()
      
    btn.config(command=confirm)
    btn.place(x=160,y=210)
    
def project1():
    global life_style
    def conceal():
        lab1.place_forget()
        btn1.place_forget()
        btn2.place_forget()
        btn3.place_forget()
   
    lab1=Label(root)
    lab1.config(text="당신이 추구하는 관리 방식은?")
    lab1.place(x=20,y=22)


    btn1= Button(root)
    btn1.config(text='체중감량')
    def click1():
        global life_style
        life_style='minus' 
        conceal() 
        project2()
        return life_style
    btn1.config(command=click1)
    btn1.place(x=5,y=100)

    btn2= Button(root)
    btn2.config(text='체중유지')
    def click2():
        global life_style
        life_style='zero' 
        conceal() 
        project2()
        return life_style
    btn2.config(command=click2)
    btn2.place(x=145,y=100)

    btn3= Button(root)
    btn3.config(text='체중증가')
    def click3():
        global life_style
        life_style='plus'
        conceal()
        project2()
        return life_style
    btn3.config(command=click3)
    btn3.place(x=285,y=100)
    print(f"{life_style}")
 
def project2():
    root.geometry("960x600+400+150")
    root.option_add("*Font","고딕 10")
    user_height=178
    user_weight=70
    user_age=20
    user_gender=1
    #기초대사량 계산
    def BasalMetabolism():
        if user_gender==1:
            basal_Meta = 66.47 + (13.75*user_weight) + (5*user_height) - (6.76*user_age)
        elif user_gender==2:
            basal_Meta = 65.51 + (9.56*user_weight) + (1.85*user_height) - (4.68*user_age)
                                                                                            
        return basal_Meta

    #기초대사량 표시
    frame_basal=LabelFrame(root,text="기초대사량" )  #기초대사량 LabelFrame 생성, 프레임 제목은 "기초대사량"으로
    frame_basal.pack(side="left",fill="both") #side는 어디에 배치할지, fill은 위아래로 크기를 얼마나 할지. both는 가득채움
    label_basal=Label(frame_basal, text=BasalMetabolism()) #기초대사량을 알려주는 Label을 frame_basal 안에 생성, 기초대사량을 계산하는 함수를 호출하여 text로 보여줌
    label_basal.pack() 

    #활동대사량 계산
    frame_actMeta=LabelFrame(root, text="활동량 선택")  
    frame_actMeta.pack(side="left",fill="both")
    actMeta_var=IntVar() #여기에 int 형으로 값을 저장
    btn_actM1= Radiobutton(frame_actMeta, text="활동이 적거나 운동을 안 하는 경우", value=1, variable=actMeta_var) #라디오버튼 생성, value는 이 라디오버튼을 선택했을때 저장할 변수
    btn_actM2= Radiobutton(frame_actMeta, text="가벼운 활동 및 운동을 하는 경우(1~3일/1주)", value=2, variable=actMeta_var)
    btn_actM3= Radiobutton(frame_actMeta, text="보통의 활동 및 운동을 하는 경우(3~5일/1주)", value=3, variable=actMeta_var)
    btn_actM4= Radiobutton(frame_actMeta, text="적극적인 활동 및 운동을 하는 경우(6~7일/1주", value=4, variable=actMeta_var)
    btn_actM5= Radiobutton(frame_actMeta, text="매우 적극적인 활동 및 운동, 운동선수", value=5, variable=actMeta_var)


    btn_actM1.pack()
    btn_actM2.pack()
    btn_actM3.pack()
    btn_actM4.pack()
    btn_actM5.pack()

    #활동대사량 계산 함수
    def actM():
        
        if actMeta_var.get()==1:
            actMeta=BasalMetabolism()*0.375
        elif actMeta_var.get()==2:
            actMeta=BasalMetabolism()*0.375
        elif actMeta_var.get()==3:
            actMeta=BasalMetabolism()*0.555
        elif actMeta_var.get()==4:
            actMeta=BasalMetabolism()*0.725
        elif actMeta_var.get()==5:
            actMeta=BasalMetabolism()*0.9
        
        label_actMeta=Label(frame_actMeta, text=actMeta) 
        label_actMeta.pack()
        
        return actMeta
        
    #활동량 선택 후 버튼 클릭하면 계산
    btnactMeta = Button(frame_actMeta, text="활동대사량 계산", command=actM) 
    btnactMeta.pack()

    #매크로 측정 유무 제시
    frame_macro=LabelFrame(root, text="본인의 매크로 측정을 하셨습니까?")
    frame_macro.pack(side="left",fill="both")

    macro_var=IntVar() 
    macro_yes= Radiobutton(frame_macro, text="예", value=1, variable=macro_var).pack()
    macro_no= Radiobutton(frame_macro, text="아니오", value=2, variable=macro_var).pack()

    #식단 제시 함수
    def recommend():
        #전에 사용했던 위젯들 전부 삭제
        frame_actMeta.destroy()
        frame_basal.destroy()
        frame_macro.destroy()
            
        global photo1 #사진을 함수 안에서 사용하려면 전역변수 처리해야함.
        
        photo1=PhotoImage(file="C:\\Users\\ij594\\engineering\\chiken.png",master=root)  #사진 저장 후 파일 경로 바꿔야함.
        label_food=Label(root, image=photo1,width=500, height=500)
        label_food.pack()
        
        def next():
            global photo2
            photo2=PhotoImage(file="C:\\Users\\ij594\\engineering\\pizza.png", master=root)  #사진 저장 후 파일 경로 바꿔야함.
            label_food.config(image=photo2)
            
        nextfood = Button(root, text="다음", command=next) 
        nextfood.pack()
        

        

        

    #매크로를 입력받는 함수
    def get_macro():
        
        if macro_var.get()==1:
        
            e_protein = Entry(frame_macro, width=30)   #텍스트 위젯 생성 한 줄로 입력받을때 사용
            e_protein.pack()
            e_protein.insert(0, "단백질") #글자가 미리 들어가있음
        
            e_carbohydrate = Entry(frame_macro, width=30)   #텍스트 위젯 생성 한 줄로 입력받을때 사용
            e_carbohydrate.pack()
            e_carbohydrate.insert(0, "탄수화물") #글자가 미리 들어가있음
        
            e_fat = Entry(frame_macro, width=30)   #텍스트 위젯 생성 한 줄로 입력받을때 사용
            e_fat.pack()
            e_fat.insert(0, "지방")  
            
            
            
        
            btn_diet = Button(frame_macro, text="식단 제시", command=recommend) 
            btn_diet.pack()

        
        elif macro_var.get()==2:
            project3()
        


    btnmacro = Button(frame_macro, text="매크로 입력", command=get_macro) 
    btnmacro.pack()

def project3():
    def widget_delet():
        for wg in root.pack_slaves():    #[bun1,btn2,btn3,btn_choice]
            wg.destroy()
   
    #사진 다음 버튼 함수
    def next_img():
        global img_num
        img_num+=1
        if img_num>=len(img_list):
            img_num=0
        canvas.itemconfig(food_img,image=img_list[img_num])
    
    #사진 이전 버튼 함수
    def pre_img():
        global img_num
        img_num-=1
        if img_num<0:
            img_num=len(img_list)-1
        canvas.itemconfig(food_img,image=img_list[img_num])


    var_lifestyle=IntVar() #어떤 체크 버튼을 선택했는지 value값 저장
    btn1=Radiobutton(root,text="체중 감소",font=("돋움",15),value=1,variable=var_lifestyle) #체중 감소 체크버튼
    btn1.select() #1번 선택되서 실행
    btn2=Radiobutton(root,text="체중 유지",font=("돋움",15),value=2,variable=var_lifestyle) #체중 유지 체크버튼
    btn3=Radiobutton(root,text="체중 증가",font=("돋움",15),value=3,variable=var_lifestyle) #체중 증가 체크버튼


    def show_photo(): #사진을 캔버스에 띄우는 함수
        global img_num
        global food_img
        img_num=0
        food_img= canvas.create_image(310,200,image=img_list[img_num])
    
    def photo_upload(): #사용자에 체크에 따라 어떤 사진을 나타낼지 사진 리스트에 저장
        global img
        global img_list
        if lifestyle_num == 1:
            img_list=[]
            for i in range(8):
                img=PhotoImage(file=f"C:/사진/foods/gamso/img{i}.png")
                img_list.append(img)
        if lifestyle_num == 2:
            img_list=[]
            for i in range(8):
                img=PhotoImage(file=f"C:/사진/foods/uzi/img{i}.png")
                img_list.append(img)
        if lifestyle_num == 3:
            img_list=[]
            for i in range(8):
                img=PhotoImage(file=f"C:/사진/foods/jeungga/img{i}.png")
                img_list.append(img)

        show_photo()


    #음식 사진 띄울 위젯과 버튼 위젯 생성
    def foods():
        #이전버튼
        global next_btn
        global pre_btn
        global canvas
        pre_btn = Button(root, text="◀이전",font=("돋움",15),bg="light steel blue",command=pre_img)
        pre_btn.grid(column=0,row=0)
        #다음버튼
        next_btn = Button(root, text="다음▶",font=("돋움",15),bg="light steel blue",command=next_img)
        next_btn.grid(column=1,row=0)
        #캔버스 생성
        canvas=Canvas(root,height=480,width=640)
        canvas.grid(column=0,row=1,columnspan=2)
        photo_upload()

    #추천 음식 보기 버튼 눌렀을 때 실행되는 함수
    def recommendation_button():
        widget_delet() 
        root.geometry("645x520")
        foods()

    #탄단지 비율 알려주는거 띄우는 함수
    def nutrient_rate():
        
        if lifestyle_num == 1:
            Label(root,text="추천 탄단지 비율",font=("돋움",20)).pack()
            Label(root,text="탄수화물 X% Y% Z%",font=("돋움",15)).pack()
            Button(root,text="추천 음식 보기",font=("돋움",15),bg="misty rose",command=recommendation_button).pack()
            
        if lifestyle_num == 2:
            Label(root,text="추천 탄단지 비율",font=("돋움",20)).pack()
            Label(root,text="탄수화물 X% Y% Z%",font=("돋움",15)).pack()
            Button(root,text="추천 음식 보기",font=("돋움",15),bg="misty rose",command=recommendation_button).pack()
            
        if lifestyle_num == 3:
            Label(root,text="추천 탄단지 비율",font=("돋움",20)).pack()
            Label(root,text="탄수화물 X% Y% Z%",font=("돋움",15)).pack()
            Button(root,text="추천 음식 보기",font=("돋움",15),bg="misty rose",command=recommendation_button).pack()
            

    #선택 버튼 눌렀을 때 함수
    def btn_choice_cmd():
        global lifestyle_num
        lifestyle_num=int(var_lifestyle.get()) #사용자가 어떤 체크박스에 체크했는지 value값 함수에 저장
        widget_delet()  
        #print(lifestyle_num)
        nutrient_rate()
        



    btn_choice=Button(root,text="선택",bg="linen",command=btn_choice_cmd) #선택버튼 
    #버튼생성
    btn1.pack() 
    btn2.pack()
    btn3.pack()
    btn_choice.pack()


if __name__=="__main__":
    main()

root.mainloop()