import builtins
from os import O_WRONLY
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *
from typing import get_origin
import random

infostat=int(0) #캐릭터 정보랑 캐릭터 스텟이랑 버튼을 공유하기 때문에 어느 버튼을 눌러서 들어왔는지 구분하기 위해
def working():
    whatto=random.randrange(0,3)
    if whatto==0:
        messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")
    elif whatto==1:
        messagebox.showerror("종려","이곳이 무엇을 하는 곳인 가에 대해서는 \n아쉽게도 까먹었어")
    elif whatto==2:
        messagebox.showerror("타르탈리아","나 타르탈리아는 매 순간 강해지고 있지.\n이깟 공백도 금방 채우겠어")

def main_set():#메인화면으로 설정. 메인화면 버튼을 숨기지 않고 탭전환 시 사용
    global infostat
    protitle.configure(text="원신 도우미")
    infostat=0
    charactor_info.configure(text="캐릭터 정보", fg="black", command=charactor_info_set, image="")
    charactor_stat.configure(text="캐릭터 스텟", fg="black", command=charactor_stat_set, image="")
    weapon.configure(text="무기 정보", fg="black", command=weapon_set, image="")
    artifact.configure(text="성유물 정보", fg="black", command=artifact_set, image="")
    unknown.configure(text="업데이트 예정", fg="black", command=unknown_set, image="")
    setting_section.configure(text="설정", fg="black", command=setting_set, image="")
    elemental_forget()
    fire_forget()
    water_forget()
    wind_forget()
    lightening_forget()
    ice_forget()
    rock_forget()
    main_place()
    ender.configure(text="종료", fg="red", command=window.destroy)

def main_place():#메인화면 버튼 생성
    protitle.place(x=387.5, y=0)
    charactor_info.place(x=0, y=90)
    charactor_stat.place(x=335, y=90)
    weapon.place(x=670,y=90)
    artifact.place(x=0,y=300)
    unknown.place(x=335, y=300)
    setting_section.place(x=670,y=300)

def main_forget():#메인화면 버튼 숨기기
    charactor_info.place_forget()
    charactor_stat.place_forget()
    weapon.place_forget()
    artifact.place_forget()
    unknown.place_forget()
    setting_section.place_forget()

def elemental_place(): #속성 버튼 생성
    fire_dis.place(x=0, y=180)
    water_dis.place(x=142, y=180)
    ice_dis.place(x=284, y=180)
    wind_dis.place(x=426, y=180)
    lightening_dis.place(x=568, y=180)
    rock_dis.place(x=710, y=180)
    grass_dis.place(x=852,y=180)  

def elemental_forget(): #속성 버튼 숨기기
    fire_dis.place_forget()
    water_dis.place_forget()
    ice_dis.place_forget()
    wind_dis.place_forget()
    lightening_dis.place_forget()
    rock_dis.place_forget()
    grass_dis.place_forget()  

#탭 함수
def charactor_info_set(): #캐릭터 메인 탭
    global infostat
    protitle.configure(text="캐릭터 정보")
    infostat=1
    elemental_place()
    main_forget()
    ender.configure(text="메인으로 돌아가기", fg="black", command=main_set)

def charactor_stat_set(): #캐릭터 스텟 탭
    global infostat
    protitle.configure(text="캐릭터 스텟")
    infostat=2
    elemental_place()
    main_forget()
    ender.configure(text="메인으로 돌아가기", fg="black", command=main_set)


def weapon_set(): #무기탭
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

def artifact_set():#성유물탭
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

def unknown_set():#업데이트 예정 탭
    working()

def setting_set():#설정탭
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

#속성별 버튼 생성 삭제  일단 캐릭터정보(infostat==1)부터 작업. 이거랑은 관련 없음
#불
def fire_place():
    elemental_forget()
    amber_dis.place(x=0,y=50)
    hyanglng_dis.place(x=250,y=50)
    benet_dis.place(x=500,y=50)
    dieluk_dis.place(x=750,y=50)
    kle_dis.place(x=0,y=310)
    sinyam_dis.place(x=250,y=310)
    hudo_dis.place(x=500,y=310)
    yawnbi_dis.place(x=750,y=310)

def fire_forget():
    amber_dis.place_forget()
    hyanglng_dis.place_forget()
    benet_dis.place_forget()
    dieluk_dis.place_forget()
    kle_dis.place_forget()
    sinyam_dis.place_forget()
    hudo_dis.place_forget()
    yawnbi_dis.place_forget()

#물
def water_place():
    elemental_forget()
    babara_dis.place(x=0, y=180)
    hangchu_dis.place(x=250, y=180)
    mona_dis.place(x=500, y=180)
    tartalia_dis.place(x=750, y=180)

def water_forget():
    babara_dis.place_forget()
    hangchu_dis.place_forget()
    mona_dis.place_forget()
    tartalia_dis.place_forget()

#바람
def wind_place():
    elemental_forget()
    suger_dis.place(x=0, y=50)
    jean_dis.place(x=250, y=50)
    venti_dis.place(x=500, y=50)
    so_dis.place(x=750,y=50)
    kazha_dis.place(x=0, y=310)
    lumine_wind_dis.place(x=250, y=310)

def wind_forget():
    suger_dis.place_forget()
    jean_dis.place_forget()
    venti_dis.place_forget()
    so_dis.place_forget()
    kazha_dis.place_forget()
    lumine_wind_dis.place_forget()

#번개
def lightening_place():
    elemental_forget()
    lisa_dis.place(x=0, y=50)
    razor_dis.place(x=250, y=50)
    bukdu_dis.place(x=500, y=50)
    fisl_dis.place(x=750, y=50)
    gakchuwng_dis.place(x=0, y=310)

def lightening_forget():
    lisa_dis.place_forget()
    razor_dis.place_forget()
    bukdu_dis.place_forget()
    fisl_dis.place_forget()
    gakchuwng_dis.place_forget()

#얼음
def ice_place():
    elemental_forget()
    keiya_dis.place(x=0, y=50)
    jungun_dis.place(x=250, y=50)
    chichi_dis.place(x=500, y=50)
    diona_dis.place(x=750, y=50)
    gamwoo_dis.place(x=0,y=310)
    rosaria_dis.place(x=250, y=310)
    uera_dis.place(x=500,y=310)
    ayaka_dis.place(x=750, y=310)

def ice_forget():
    keiya_dis.place_forget()
    jungun_dis.place_forget()
    chichi_dis.place_forget()
    diona_dis.place_forget()
    gamwoo_dis.place_forget()
    rosaria_dis.place_forget()
    uera_dis.place_forget()
    ayaka_dis.place_forget()

#바위
def rock_place():
    elemental_forget()
    nggwang_dis.place(x=0,y=50)
    noel_dis.place(x=250, y=50)
    zongliya_dis.place(x=500, y=50)
    albedo_dis.place(x=750, y=50)
    lumine_rock_dis.place(x=0,y=310)

def rock_forget():
    nggwang_dis.place_forget()
    noel_dis.place_forget()
    zongliya_dis.place_forget()
    albedo_dis.place_forget()
    lumine_rock_dis.place_forget()
  

#메인코드
window=Tk()
window.iconbitmap(default='barbara.ico')
window.configure(bg="light steel blue")
window.title("Genshin Impact Supporter")
window.geometry("1000x600+450+200") 
window.resizable(width=FALSE, height=FALSE)
version="alpha 5.29"
version_dis=Label(window, text=version, fg="white", bg="light steel blue")
version_dis.place(x=0,y=0)
menus=Menu(window)  #이건 뭐고
window.config(menu=menus)
menu1=Menu(menus) #메뉴탭 1호
menus.add_cascade(label="설정", menu=menu1)
menu1.add_command(label="종료", command=window.destroy)
protitle=Label(text="원신 도우미", font=("굴림체", 30), fg="deep sky blue",bg="light steel blue")

#탭 생성
charactor_info=Button(window, text="캐릭터 정보", command=charactor_info_set, width= 40,height=10)
charactor_stat=Button(window, text="캐릭터 스텟", command=charactor_stat_set, width= 40,height=10)
weapon=Button(window, text="무기 정보", command=weapon_set, width= 40,height=10)
artifact=Button(window, text="성유물 정보", command=artifact_set, width= 40,height=10)
unknown=Button(window, text="업데이트 예정", command=unknown_set, width= 40,height=10)
setting_section=Button(window, text="설정", command=setting_set, width= 40,height=10)
ender=Button(window, text="종료", command=window.destroy, height=2, fg="red")

#속성 이미지 생성
fire=PhotoImage(file="gid/elemental/fire2.png")
water=PhotoImage(file="gid/elemental/water.png")
ice=PhotoImage(file="gid/elemental/ice.png")
lightening=PhotoImage(file="gid/elemental/lightening.png")
grass=PhotoImage(file="gid/elemental/grass.png")
wind=PhotoImage(file="gid/elemental/wind.png")
rock=PhotoImage(file="gid/elemental/rock.png")

#속성 버튼
fire_dis=Button(window, image=fire, command=fire_place)
water_dis=Button(window, image=water, command=water_place)
ice_dis=Button(window, image=ice, command=ice_place)
wind_dis=Button(window, image=wind, command=wind_place)
lightening_dis=Button(window, image=lightening, command=lightening_place)
rock_dis=Button(window, image=rock, command=rock_place)
grass_dis=Button(window,image=grass, command=working)


#메인화면 버튼
protitle.place(x=387.5, y=0)
charactor_info.place(x=0, y=90)
charactor_stat.place(x=335, y=90)
weapon.place(x=670,y=90)
artifact.place(x=0,y=300)
unknown.place(x=335, y=300)
setting_section.place(x=670,y=300)

#하단 버튼
ender.pack(side=BOTTOM, fill=X)

#불 캐릭터 이미지 생성
amber=PhotoImage(file="gid/character/amber.png")
hyanglng=PhotoImage(file="gid/character/xiangling.png")
benet=PhotoImage(file="gid/character/bennett.png")
dieluk=PhotoImage(file="gid/character/diluc.png")
kle=PhotoImage(file="gid/character/klee.png")
sinyam=PhotoImage(file="gid/character/xinyan.png")
hudo=PhotoImage(file="gid/character/hu tao.png")
yawnbi=PhotoImage(file="gid/character/yanfei.png")

#불 캐릭터 버튼
amber_dis=Button(window, image=amber, command=working)
hyanglng_dis=Button(window, image=hyanglng, command=working)
benet_dis=Button(window, image=benet, command=working)
dieluk_dis=Button(window, image=dieluk, command=working)
kle_dis=Button(window, image=kle, command=working)
sinyam_dis=Button(window, image=sinyam, command=working)
hudo_dis=Button(window, image=hudo, command=working)
yawnbi_dis=Button(window, image=yawnbi, command=working)

#물 캐릭터 이미지 생성
babara=PhotoImage(file="gid/character/barbara.png")
hangchu=PhotoImage(file="gid/character/xingqiu.png")
mona=PhotoImage(file="gid/character/mona.png")
tartalia=PhotoImage(file="gid/character/childe.png")

#물 캐릭터 버튼
babara_dis=Button(window, image=babara, command=working)
hangchu_dis=Button(window, image=hangchu, command=working)
mona_dis=Button(window, image=mona, command=working)
tartalia_dis=Button(window, image=tartalia, command=working)

#바람 캐릭터 이미지 생성
suger=PhotoImage(file="gid/character/sucrose.png")
jean=PhotoImage(file="gid/character/jean.png")
venti=PhotoImage(file="gid/character/venti.png")
so=PhotoImage(file="gid/character/xiao.png")
kazha=PhotoImage(file="gid/character/kazuha.png")
lumine=PhotoImage(file="gid/character/lumine.png")

#바람 캐릭터 버튼
suger_dis=Button(window, image=suger, command=working)
jean_dis=Button(window, image=jean, command=working)
venti_dis=Button(window, image=venti, command=working)
so_dis=Button(window, image=so, command=working)
kazha_dis=Button(window, image=kazha, command=working)
lumine_wind_dis=Button(window, image=lumine, command=working)

#번개 캐릭터 이미지
lisa=PhotoImage(file="gid/character/lisa.png")
razor=PhotoImage(file="gid/character/razor.png")
bukdu=PhotoImage(file="gid/character/beidou.png")
fisl=PhotoImage(file="gid/character/fischl.png")
gakchuwng=PhotoImage(file="gid/character/keqing.png")

#번개 캐릭터 버튼
lisa_dis=Button(window, image=lisa, command=working)
razor_dis=Button(window, image=razor, command=working)
bukdu_dis=Button(window, image=bukdu, command=working)
fisl_dis=Button(window, image=fisl, command=working)
gakchuwng_dis=Button(window, image=gakchuwng, command=working)

#얼음 캐릭터 이미지
keiya=PhotoImage(file="gid/character/kaeya.png")
jungun=PhotoImage(file="gid/character/chongyun.png")
chichi=PhotoImage(file="gid/character/qiqi.png")
diona=PhotoImage(file="gid/character/diona.png")
gamwoo=PhotoImage(file="gid/character/ganyu.png")
rosaria=PhotoImage(file="gid/character/rosaria.png")
uera=PhotoImage(file="gid/character/eula.png")
ayaka=PhotoImage(file="gid/character/ayaka.png")

#얼음 캐릭터 버튼
keiya_dis=Button(window, image=keiya, command=working)
jungun_dis=Button(window, image=jungun, command=working)
chichi_dis=Button(window, image=chichi, command=working)
diona_dis=Button(window, image=diona, command=working)
gamwoo_dis=Button(window, image=gamwoo, command=working)
rosaria_dis=Button(window, image=rosaria, command=working)
uera_dis=Button(window, image=uera, command=working)
ayaka_dis=Button(window, image=ayaka, command=working)

#바위 캐릭터 이미지
nggwang=PhotoImage(file="gid/character/ningguang.png")
noel=PhotoImage(file="gid/character/noelle.png")
zongliya=PhotoImage(file="gid/character/zhongli.png")
albedo=PhotoImage(file="gid/character/albedo.png")

#바위 캐릭터 버튼
nggwang_dis=Button(window, image=nggwang, command=working)
noel_dis=Button(window, image=noel, command=working)
zongliya_dis=Button(window, image=zongliya, command=working)
albedo_dis=Button(window, image=albedo, command=working)
lumine_rock_dis=Button(window, image=lumine, command=working)

window.mainloop()