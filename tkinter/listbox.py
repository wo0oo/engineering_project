from tkinter import *


root=Tk()
root.title("info") 
root.geometry("680x480+400+150") 

listbox=Listbox(root, selectmode="extended", height=0) #리스트박스 생성 extended는 여러개 선택, single은 하나 선택, height는 몇개 보여줄 것인지: 3이면 바나나까지만 보여줌. 0은 다보여줌
listbox.insert(0,"사과")     # 0번째에 사과라고 적음
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")  #END는 가장 마지막에 추가
listbox.insert(END,"포도")
listbox.pack()


def btncmd():
    #삭제
    #listbox.delete(END) #맨 뒤에 항목을 삭제 0이면 맨 앞 항목을 삭제
    
    #갯수 확인
    #print("리스트에는", listbox.size(),"개가 있어요")
    
    #항목 확인 (시작 idx, 끝 idx)
    #print("1번재부터 3번째까지의 항목 :", listbox.get(0,2))
    
    #선택된 항목 확인 (위치로 반환 ex(1, 2, 3))
    print("선택된 항목 : ", listbox.curselection())
     
    

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()