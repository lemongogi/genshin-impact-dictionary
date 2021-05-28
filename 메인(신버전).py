import builtins
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *

def charactor_info_set():
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

def charactor_stat_set():
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

def weapon_set():
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

def artifact_set():
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

def unknown_set():
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

def setting_set():
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

window=Tk()
window.iconbitmap(default='바바라.ico')
window.configure(bg="light steel blue")
window.title("Genshin Impact Supporter")
window.geometry("1000x600+450+200") #창 사이즈 결정(400x100크기에 x좌표 100, y좌표 200에 소환)
window.resizable(width=FALSE, height=FALSE) #창의 너비, 높이 조절 가능여부 조정(현제:불가능)

menus=Menu(window)  #이건 뭐고
window.config(menu=menus)
menu1=Menu(menus) #메뉴탭 1호
menus.add_cascade(label="설정", menu=menu1)
menu1.add_command(label="종료", command=window.destroy)
protitle=Label(text="원신 도우미", font=("굴림체", 30), fg="deep sky blue",bg="light steel blue")
charactor_info=Button(window, text="캐릭터 정보", command=charactor_info_set, width= 40,height=10)
charactor_stat=Button(window, text="캐릭터 스텟", command=charactor_stat_set, width= 40,height=10)
weapon=Button(window, text="무기 정보", command=weapon_set, width= 40,height=10)
artifact=Button(window, text="성유물 세트 정보", command=artifact_set, width= 40,height=10)
unknown=Button(window, text="업데이트 예정", command=unknown_set, width= 40,height=10)
setting_section=Button(window, text="설정", command=setting_set, width= 40,height=10)
ender=Button(window, text="종료", command=window.destroy, height=2, fg="red")

protitle.place(x=387.5, y=0)
charactor_info.place(x=0, y=100)
charactor_stat.place(x=335, y=100)
weapon.place(x=670,y=100)
artifact.place(x=0,y=310)
unknown.place(x=335, y=310)
setting_section.place(x=670,y=310)

ender.pack(side=BOTTOM, fill=X)



window.mainloop()
