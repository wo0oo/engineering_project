from tkinter import * #gui라이브러리 tkinter 불러오기

root=Tk()
root.title("info") #창 제목 설정
#root.geometry("680x480") #창 크기 설정 가로*세로
root.geometry("680x480+400+150")  #가로*세로+x좌표+좌표
#root.resizable(False,False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

btn1=Button(root,text="버튼") #버튼 만들기
btn1.pack() #main윈도우에 포함되게 함

btn2 = Button(root, width=5, height=10,text="버튼2") #width는 가로 조절, height는 상하 조절
btn2.pack()
btn3 = Button(root, fg="red", bg="yellow", text="버튼5")
btn3.pack()


def btncmd():
    print("버튼이 클릭되었어요")

btn4 = Button(root, text="동작하는 버튼", command=btncmd) #버튼에 동작 추가 btncmd함수를 호출함
btn4.pack()

label1=Label(root, text="안녕하세요") #레이블 생성 (텍스트)
label1.pack()

def change():
    label1.config(text="반가워요") #config로 속성을 바꿈

btn5 = Button(root, text="클릭", comman=change)


txt = Text(root, width=30, height=5) #텍스트 위젯 생성
txt.pack()

txt.insert(END, "글자를 입력하세요") #글자가 미리 들어가있음

e = Entry(root, width=30)   #텍스트 위젯 생성 한 줄로 입력받을때 사용
e.pack()
e.insert(0, "한 줄만 입력해요") #글자가 미리 들어가있음

def btn6cmd():
    #내용 출력
    print(txt.get("1.0", END)) #1.0부터 끝까지 가져와서 출력 (1:첫번재 라인, 0: 0번째 columc 위치)
    print(e.get())  #엔트리 가져와서 출력
    
    #내용 삭제
    txt.delete("1.0", END) #1부터 끝까지 삭제
    e.delete(0,END) #삭제(0부터 끝까지)
    
btn6 = Button(root, text="버튼6", command=btn6cmd)
btn6.pack()






 
 
 





root.mainloop()  #창 실행

