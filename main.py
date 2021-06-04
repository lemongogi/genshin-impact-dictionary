import builtins
from os import O_WRONLY
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *
import random
import infomultiply


infostat=int(0) #캐릭터 정보랑 캐릭터 스텟이랑 버튼을 공유하기 때문에 어느 버튼을 눌러서 들어왔는지 구분하기 위해
character_number=int(0) #캐릭터 정보와 캐릭터 스텟에서 어떤 캐릭터를 선택한 상황인지 알기 위하여
def working():
    whatto=random.randrange(0,3)
    if whatto==0:
        messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")
    elif whatto==1:
        messagebox.showerror("종려","이곳이 무엇을 하는 곳인 가에 대해서는 \n아쉽게도 까먹었어")
    elif whatto==2:
        messagebox.showerror("타르탈리아","나 타르탈리아는 매 순간 강해지고 있지.\n이깟 공백도 금방 채우겠어")

def main_set():#메인화면으로 설정. 메인화면 버튼을 숨기지 않고 탭전환 시 사용
    global infostat, character_number
    protitle.configure(text="원신 도우미", fg="deep sky blue")
    infostat=0
    character_number=0
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
    character_info_forget()
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
    main_forget()
    ender.configure(text="메인으로 돌아가기", fg="black", command=main_set)

def setting_set():#설정탭
    messagebox.showerror("페이몬","이쪽은 다음에 다시 탐색하러 오자")

def test_set():
    protitle.configure(text="오류", fg="red")

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

#기존의 탭 입장이 아니라 캐릭터까지 들어가는 것과 캐릭터에서 나오는 것
def charcater_info_place():
    global character_number
    character_image.place(x=0, y=50)
    character_name.place(x=260,y=50)
    character_eletype.place(x=530, y=50)
    character_weapon.place(x=750,y=50)
    character_weapon_image.place(x=240, y=130)
    character_weapon_text.place(x=330, y=130)
    character_skill_image.place(x=0, y=290)
    character_skill_text.place(x=90, y=300)
    character_ult_image.place(x=0, y=420)
    character_ult_text.place(x=90, y=430)
    character_weapon_level.place(x=243, y=210)
    character_weapon_multiply_frame.place(x=330, y=230)
    character_weapon_multiply.place(x=320, y=265)
    character_skill_level.place(x=0, y=370)
    character_skill_multiply.place(x=80, y=415)
    character_skill_multiply_frame.place(x=80,y=390)
    character_ult_level.place(x=0, y=500)
    character_ult_multiply.place(x=80, y=520)
    character_ult_multiply_frame.place(x=80, y=490)
    if character_number==13:
        tartalia_skill_convert.place(x=800, y=370)

def character_info_forget():
    global character_number
    character_image.place_forget()
    character_name.place_forget()
    character_eletype.place_forget()
    character_weapon.place_forget()
    character_weapon_image.place_forget()
    character_weapon_text.place_forget()
    character_skill_image.place_forget()
    character_skill_text.place_forget()
    character_ult_image.place_forget()
    character_ult_text.place_forget()
    character_weapon_level.place_forget()
    character_weapon_multiply_frame.place_forget()
    character_weapon_multiply.place_forget()
    character_skill_level.place_forget()
    character_skill_multiply_frame.place_forget()
    character_skill_multiply.place_forget()
    character_ult_level.place_forget()
    character_ult_multiply.place_forget()
    character_ult_multiply_frame.place_forget()
    tartalia_skill_convert.place_forget()

#레벨 전환기  이거 미완성임. 숫자는 올라가는데 보이는 수치를 조정하지 않으며 place하지 않음

def tartalia_info_convert():
    global tartalia_entry, tartalia_mode
    tartalia_entry=1
    if tartalia_mode=="bow":
        tartalia_mode="broadsword"
    else:
        tartalia_mode="bow"
    tartalia_info()




#바바라 버튼함수
def babara_info():
    global character_image, character_name, character_eletype, character_weapon, babara, infostat, character_number, character_weapon_image, character_weapon_text, character_skill_image, character_skill_text, character_ult_image, character_ult_text
    character_number=10
    if infostat==1:
        water_forget()
        character_image.configure(image=babara)
        character_name.configure(text="바바라", fg="dodgerblue3", font=("Comic Sans MS",40), bg="light steel blue")
        character_eletype.configure(text="물속성", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
        character_weapon.configure(text="법구", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
        charcater_info_place()
        character_weapon_image.configure(image=orb)
        character_weapon_text.configure(text="주기가 4회인 물 원소 공격을 합니다\n강공격:짧은 영창 후 범위 물 원소피해를 가합니다\n낙하공격:착지 시 범위 내 적에게 물 원소 피해를 가합니다", fg="dodgerblue3", font=("Comic Sans MS", 18), bg="light steel blue")
        character_skill_image.configure(image=babara_skill_image)
        character_skill_text.configure(text="자신에게 노래의 고리를 부여하고 주위의 적에게 물 원소 피해를 가합니다.\n노래의 고리는 캐릭터를 전환해도 유지됩니다.\n노래의 고리를 가진 동안 바바라의 공격(강공격은 4배)이 명중 시 파티원 전원을 치유합니다\n노래의 고리가 있는 동안 주기적으로 현제 캐릭터를 치유하며 현제캐릭터와 주위의 적에게 습기를 부여합니다", fg="dodgerblue3", font=("Comic Sans MS", 12), bg="light steel blue")
        character_ult_image.configure(image=babara_ult_image)
        character_ult_text.configure(fg="dodgerblue3", font=("Comic Sans MS", 26), bg="light steel blue", text="주위 아군 및 자신의 파티원 전원이 회복됩니다")
        info_weapon_level(10)
        info_skill_level(10)
        info_ult_level(10)
    else:
        working()

def hangchu_info():
    global character_image, character_name, character_eletype, character_weapon, babara, infostat, character_number, character_weapon_image, character_weapon_text, character_skill_image, character_skill_text, character_ult_image, character_ult_text
    character_number=11
    if infostat==1:
        water_forget()
        character_image.configure(image=hangchu)
        character_name.configure(text="행추", fg="dodgerblue3", font=("Comic Sans MS",40), bg="light steel blue")
        character_eletype.configure(text="물속성", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
        character_weapon.configure(text="한손검", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
        charcater_info_place()
        character_weapon_image.configure(image=broadsword)
        character_weapon_text.configure(text="주기가 5회인 공격을 합니다\n강공격:전방으로 공격 2회 가합니다\n낙하공격:착지 시 범위 내 적에게 피해를 가합니다", fg="dodgerblue3", font=("Comic Sans MS", 18), bg="light steel blue")
        character_skill_image.configure(image=hangchu_skill_image)
        character_skill_text.configure(text="주위의 적에게 물 원소 공격(타격2회)를 가하고 자신을 습기상태로 만든 뒤 3개의 우렴검을 부여합니다.\n우렴검은 캐릭터를 전환해도 유지되며 부여량은 1별이상이면 4개가 됩니다\n우렴검 가진 동안 경직저항이 증가하고, 받는 피해량이 감소하지만 피격마다 1개씩 감소합니다", fg="dodgerblue3", font=("Comic Sans MS", 12), bg="light steel blue")
        character_ult_image.configure(image=hangchu_ult_image)
        character_ult_text.configure(fg="dodgerblue3", font=("Comic Sans MS", 16), bg="light steel blue", text="우렴검의 수가 최대치로 유지되게 되며 일반공격 시행마다 홍검세가 물원소 피해를 같이 가합니다.\n이 효과들은 캐릭터를 전환해도 유지됩니다")
        info_weapon_level(character_number)
        info_skill_level(character_number)
        info_ult_level(character_number)
    else:
        working()

def mona_info():
    global character_image, character_name, character_eletype, character_weapon, babara, infostat, character_number, character_weapon_image, character_weapon_text, character_skill_image, character_skill_text, character_ult_image, character_ult_text
    character_number=12
    if infostat==1:
        water_forget()
        character_image.configure(image=mona)
        character_name.configure(text="모나", fg="dodgerblue3", font=("Comic Sans MS",40), bg="light steel blue")
        character_eletype.configure(text="물속성", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
        character_weapon.configure(text="법구", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
        charcater_info_place()
        character_weapon_image.configure(image=orb)
        character_weapon_text.configure(text="주기가 4회인 물 원소 공격을 합니다\n강공격:짧은 영창 후 범위 물 원소 공격을 가합니다\n낙하공격:착지 시 범위 내 적에게 물 원소 피해를 가합니다", fg="dodgerblue3", font=("Comic Sans MS", 18), bg="light steel blue")
        character_skill_image.configure(image=mona_skill_image)
        character_skill_text.configure(text="길게 눌러 허영을 소환하며 빠르게 후퇴합니다. 허영은 주위 적을 도발하며 지속적으로 물 원소 피해를 가합니다\n지속시간이 종료되면 파열되며 주위 적에게 물 원소 피해를 가합니다\n대시 대신 몸을 숨키고 빠른 속도를 이동할 수 있으며 몸을 드러낼 때 주위 적에게 물 원소 피해를 가합니다", fg="dodgerblue3", font=("Comic Sans MS", 12), bg="light steel blue")
        character_ult_image.configure(image=mona_ult_image)
        character_ult_text.configure(fg="dodgerblue3", font=("Comic Sans MS", 16), bg="light steel blue", text="주위적을 포영,성이, 습기 상태로 만듭니다. 포영 상태의 적 공격 시 추가 물 원소 피해를 가합니다\n 성이상태의 적은 받는 피해가 증가하고 약한 적은 구속당해 아무것도 못하게 합니다")
        info_weapon_level(character_number)
        info_skill_level(character_number)
        info_ult_level(character_number)
    else:
        working()

def tartalia_info():
    global character_image, character_name, character_eletype, character_weapon, babara, infostat, character_number, character_weapon_image, character_weapon_text, character_skill_image, character_skill_text, character_ult_image, character_ult_text, tartalia_mode, tartalia_entry, weapon_level, skill_level_global
    character_number=13
    if infostat==1:
        water_forget()
        charcater_info_place()
        if tartalia_entry==0:
            tartalia_mode="bow"
            info_weapon_level(character_number, tartalia_mode)
            info_skill_level(character_number)
            info_ult_level(character_number)
        else:
            tartalia_entry=0
            infomultiply.info_weapon_level2(character_number, weapon_level_global, character_weapon_multiply, character_weapon_multiply_frame, tartalia_mode, skill_level_global)
            infomultiply.info_ult_level2(character_number, ult_level_global, character_ult_multiply, character_ult_multiply_frame, tartalia_mode)
        character_image.configure(image=tartalia)
        character_name.configure(text="타르탈리아", fg="dodgerblue3", font=("Comic Sans MS",40), bg="light steel blue")
        character_eletype.configure(text="물속성", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
        if tartalia_mode=="bow":
            character_weapon.configure(text="활", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
            character_weapon_text.configure(text="주기가 6회인 공격을 합니다\n강공격:조준하여 피해량이 더 큰공격을 합니다. \n최대차징 시 물 원소 피해를 주며 단류를 부여합니다\n낙하공격:착지 시 범위 내 적에게 물 원소 피해를 가합니다", fg="dodgerblue3", font=("Comic Sans MS", 12), bg="light steel blue")
            character_weapon_image.configure(image=bow)
            character_skill_image.configure(image=tartalia_skill_image)
            character_skill_text.configure(text="주위 적에게 물 원소 피해를 주고 자신의 무장을 마왕무장(한손검)으로 전환합니다\n단류 섬:활 상태에서 풀차징으로 단류 상태의 적 공격 시 그 적 중심으로 3회 범위 물 원소 피해(일반공격)를 가합니다\n단류 파:단류상태인 적을 처치 시 주위 적에게 물 원소 피해(일반공격)를 가하며 단류효과를 부여합니다", fg="dodgerblue3", font=("Comic Sans MS", 12), bg="light steel blue")
            character_ult_text.configure(fg="dodgerblue3", font=("Comic Sans MS", 16), bg="light steel blue", text="전방을 향해 범위 물 원소 피해를 가하며 단류상태를 부여하며 원소에너지를 33%반환합니다")
        else:
            character_weapon.configure(text="한손검", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
            character_weapon_text.configure(text="주기가 6회인 물 원소 공격을 합니다\n강공격:전방으로 2회 물 원소 공격을 합니다\n낙하공격을 할 수 없습니다", fg="dodgerblue3", font=("Comic Sans MS", 18), bg="light steel blue")
            character_weapon_image.configure(image=tartalia_skill_image)
            character_skill_image.configure(image=bow)
            character_skill_text.configure(text="다시 활 상태로 돌아옵니다\n쿨타임은 6초+사용시간이며 지속시간을 전부 소모 시 36초가 아닌 45초가 됩니다\n단류 참:검 상태에서 단류상태의 적 적중 시 그 적 중심 범위 물 원소 피해(스킬피해)를 가하며 1.5초마다 한 번 발동됩니다", fg="dodgerblue3", font=("Comic Sans MS", 12), bg="light steel blue")
            character_ult_text.configure(fg="dodgerblue3", font=("Comic Sans MS", 16), bg="light steel blue", text="근처의 적 전원에게 물 원소 피해를 가합니다.\n 이 공격이 단류상태의 적 적중 시 단류를 제거하고 범위 물 원소 피해(원소폭발)를 가합니다")
        character_ult_image.configure(image=tartalia_ult_image)
    else:
        working()


def info_weapon_level_butten_ver():
    global character_number
    info_weapon_level(character_number, tartalia_mode)

def info_weapon_level(character_number, tartalia_mode=""):
    global weapon_level_global, skill_level_global
    character_weapon_multiply.configure(text="")
    character_weapon_multiply_frame.configure(text="")
    weapon_level=askinteger("일반 공격의 레벨", "일반 공격의 레벨을 설정해주세요", minvalue=1, maxvalue=15)
    weapon_level_global=weapon_level
    character_weapon_level.configure(text=weapon_level)
    infomultiply.info_weapon_level2(character_number, weapon_level, character_weapon_multiply, character_weapon_multiply_frame, tartalia_mode, skill_level_global)

def info_skill_level_button_ver():
    global character_number, weapon_level_global
    info_skill_level(character_number)


def info_skill_level(character_number):
    global skill_level_global
    character_skill_multiply.configure(text="")
    character_skill_multiply_frame.configure(text="")
    skill_level=askinteger("원소 스킬의 레벨","원소 스킬의 레벨을 설정해주세요", minvalue=1, maxvalue=15)
    character_skill_level.configure(text=skill_level)
    skill_level_global=skill_level
    infomultiply.info_skill_level2(character_number, skill_level, character_skill_multiply, character_skill_multiply_frame)
    if character_number==13:
        infomultiply.info_weapon_level2(character_number, weapon_level_global, character_weapon_multiply, character_weapon_multiply_frame, tartalia_mode, skill_level_global)

def info_ult_level_button_ver():
    global character_number
    info_ult_level(character_number)

def info_ult_level(character_number):
    global tartalia_mode, ult_level_global
    character_ult_multiply.configure(text="")
    character_ult_multiply_frame.configure(text="")
    ult_level=askinteger("원소 폭발의 레벨","원소 폭발의 레벨을 설정해주세요", minvalue=1, maxvalue=15)
    character_ult_level.configure(text=ult_level)
    ult_level_global=ult_level
    if character_number==13:
        infomultiply.info_ult_level2(character_number, ult_level, character_ult_multiply, character_ult_multiply_frame, tartalia_mode)
    else:
        infomultiply.info_ult_level2(character_number, ult_level, character_ult_multiply, character_ult_multiply_frame)        
    
#메인코드
window=Tk()
tartalia_mode="bow"
tartalia_entry=int(0)#다른 모든 캐릭터처럼 들어갈 때
weapon_level_global=skill_level_global=ult_level_global=int(1)
window.iconbitmap(default='barbara.ico')
window.configure(bg="light steel blue")
window.title("Genshin Impact Supporter")
window.geometry("1000x600+450+200") 
window.resizable(width=FALSE, height=FALSE)
version="alpha 6.04"
version_dis=Label(window, text=version, fg="white", bg="light steel blue")
version_dis.place(x=0,y=0)
menus=Menu(window)  #이건 뭐고
window.config(menu=menus)
menu1=Menu(menus) #메뉴탭 1호
menus.add_cascade(label="설정", menu=menu1)
menu1.add_command(label="종료", command=window.destroy)
protitle=Label(text="원신 도우미", font=("Comic Sans MS", 30), fg="deep sky blue",bg="light steel blue")

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
babara_dis=Button(window, image=babara, command=babara_info)
hangchu_dis=Button(window, image=hangchu, command=hangchu_info)
mona_dis=Button(window, image=mona, command=mona_info)
tartalia_dis=Button(window, image=tartalia, command=tartalia_info)

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


#캐릭터 정보 ui 코딩
skill_level=ult_level=int(1)

#물=dodgerblue3
#무기 이미지
orb=PhotoImage(file="gid/skill icon/weapon/orb.png")
broadsword=PhotoImage(file="gid/skill icon/weapon/broadsword.png")
bow=PhotoImage(file="gid/skill icon/weapon/bow.png")

#3번째 특성(요리증가, 재련제료 반환 등등)
cooking=PhotoImage(file="gid/skill icon/passive3/cook.png")
ability_ingr_reduce=PhotoImage(file="gid/skill icon/passive3/ability_reduce.png")
weapon_ingr_reduce=PhotoImage(file="gid/skill icon/passive3/weapon_reduce.png")

#바바라 이미지
babara_skill_image=PhotoImage(file="gid/skill icon/barbara/skill.png")
babara_ult_image=PhotoImage(file="gid/skill icon/barbara/ult.png")
babara_passive1_image=PhotoImage(file="gid/skill icon/barbara/passive1.png")
babara_passive2_image=PhotoImage(file="gid/skill icon/barbara/passive2.png")

#행추 이미지
hangchu_skill_image=PhotoImage(file="gid/skill icon/xingqiu/skill.png")
hangchu_ult_image=PhotoImage(file="gid/skill icon/xingqiu/ult.png")
hangchu_passive1_image=PhotoImage(file="gid/skill icon/xingqiu/passive1.png")
hangchu_passive2_image=PhotoImage(file="gid/skill icon/xingqiu/passive2.png")

#모나 이미지
mona_skill_image=PhotoImage(file="gid/skill icon/mona/skill.png")
mona_ult_image=PhotoImage(file="gid/skill icon/mona/ult.png")
mona_passive1_image=PhotoImage(file="gid/skill icon/mona/passive1.png")
mona_passive2_image=PhotoImage(file="gid/skill icon/mona/passive2.png")

#타르탈리아
tartalia_skill_image=PhotoImage(file="gid/skill icon/childe/skill.png")
tartalia_ult_image=PhotoImage(file="gid/skill icon/childe/ult.png")
tartalia_passive1_image=PhotoImage(file="gid/skill icon/childe/passive1.png")
tartalia_passive2_image=PhotoImage(file="gid/skill icon/childe/passive2.png")
tartalia_passive3_image=PhotoImage(file="gid/skill icon/childe/passive3.png")


character_image=Label(window, image=tartalia)
character_name=Label(window, text="타르탈리아", fg="dodgerblue3", font=("Comic Sans MS",40), bg="light steel blue")
character_eletype=Label(window, text="물속성", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")
character_weapon=Label(window, text="활", fg="dodgerblue3", font=("Comic Sans MS", 40), bg="light steel blue")

#누른 버튼에 따라 다를 부분


#1페이지(데폴트-바바라)
character_weapon_image=Label(window, image=bow)
character_weapon_text=Label(window, text="주기가 6회인 공격을 합니다\n강공격:조준하여 피해량이 더 큰공격을 합니다. \n최대차징 시 물 원소 피해를 주며 단류를 부여합니다\n낙하공격:착지 시 범위 내 적에게 물 원소 피해를 가합니다", fg="dodgerblue3", font=("Comic Sans MS", 18), bg="light steel blue")
character_skill_image=Label(window, image=tartalia_skill_image)
character_skill_text=Label(window, text="주위 적에게 물 원소 피해를 주고 자신의 무장을 마왕무장(한손검)으로 전환합니다\n단류 섬:활 상태에서 풀차징으로 단류 상태의 적 공격 시 그 적 중심으로 3회 범위 물 원소 피해(일반공격)를 가합니다\n단류 파:단류상태인 적을 처치 시 주위 적에게 물 원소 피해(일반공격)를 가하며 단류효과를 부여합니다", fg="dodgerblue3", font=("Comic Sans MS", 12), bg="light steel blue")
character_ult_image=Label(window, image=tartalia_ult_image)
character_ult_text=Label(window, fg="dodgerblue3", font=("Comic Sans MS", 26), bg="light steel blue", text="전방을 향해 범위 물 원소 피해를 가하며 단류상태를 부여하며 원소에너지를 33%반환합니다")
character_weapon_multiply_frame=Label(window, text="무기 테두리", bg="light steel blue", fg="dodgerblue3", font=("Comic Sans MS",18))
character_weapon_multiply=Label(window, text="무기내용", bg="light steel blue", fg="dodgerblue3", font=("Comic Sans MS",18))
character_weapon_level=Button(window, text="미설정", command=info_weapon_level_butten_ver, width=8, height=3)
character_skill_multiply_frame=Label(window, text="스킬 테두리", bg="light steel blue", fg="dodgerblue3", font=("Comic Sans MS",11))
character_skill_multiply=Label(window, text="스킬 내용", bg="light steel blue", fg="dodgerblue3", font=("Comic Sans MS",11))
character_skill_level=Button(window, text="미설정", command=info_skill_level_button_ver, width=8, height=2)
character_ult_multiply_frame=Label(window, text="궁 테두뤼", bg="light steel blue", fg="dodgerblue3", font=("Comic Sans MS",12))
character_ult_multiply=Label(window, text="궁 내용", bg="light steel blue", fg="dodgerblue3", font=("Comic Sans MS",12))
character_ult_level=Button(window, text="미설정", command=info_ult_level_button_ver, width=8, height=2)


#타르탈리아용 버튼
tartalia_skill_convert=Button(window, text="스킬시전", command=tartalia_info_convert, width=8, height=2)






window.mainloop()