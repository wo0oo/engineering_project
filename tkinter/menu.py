from tkinter import *


root=Tk()
root.title("info") 
root.geometry("680x480+400+150") 

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

#File 메뉴
menu_file =Menu(menu, tearoff=0) #root가 아닌 menu에 집어넣음
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator()  #줄로 구분
menu_file.add_command(label="Open file...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) #프로그램 종료

menu.add_cascade(label="file", menu=menu_file)

#Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가 ( radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(labe="Python")
menu_lang.add_radiobutton(labe="Java")
menu_lang.add_radiobutton(labe="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu) #root에 포함하기 위해 menu=menu
root.mainloop()