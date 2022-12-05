''' <<<변수 이름 설명>>>
Basal: 기초대사량에 대한 변수 이름
actMeta 또는 actM: 활동대사량에 대한 변수 이름
macro: 매크로에 대한 변수 이름
btn: 버튼
label: 라벨(글씨 또는 사진)
frame: 프레임

ex)btnbasal 또는 btn_basal은 기초대사량 파트에서 사용할 버튼
   frame_macro 또는 framemacro는 매크로 파트에서 사용할 프레임
'''


from tkinter import *


root=Tk()
root.title("정우성") 
root.geometry("960x600+400+150") 


#신체정보 입력받기 (임시. 1번에서 받아옴.)
user_height = int(input("키:"))
user_weight = int(input("몸무게:"))
user_age = int(input("나이:"))
user_gender = int(input("1.남자, 2.여자:"))

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

    
    #elif macro_var.get()==2:
    #3번으로 넘어감


btnmacro = Button(frame_macro, text="매크로 입력", command=get_macro) 
btnmacro.pack()






root.mainloop()




