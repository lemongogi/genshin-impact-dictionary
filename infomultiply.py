from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *
from typing import get_origin

def not_written(b):
    b.configure(text="\t제대로 레벨을 입력하라구  \t-페이몬-")

def info_weapon_level2(character_number, weapon_level, b, c):
    if character_number==10: #바바라
        c.configure(text="    [1단/2단/3단/4단]  [강공격]    [낙하공격(저공/고공)]")
        if weapon_level==1:
            b.configure(text="[37.8% / 35.5% / 41.0% / 55.2%]   [166%]   [114% / 142%]")
        elif weapon_level==2:
            b.configure(text="[40.7% / 38.2% / 44.1% / 59.3%]  [179%]  [123%/153%]")
        elif weapon_level==3:
            b.configure(text="[43.5% / 40.8% / 47.2% / 63.5%]   [191%]   [132% / 165%]") 
        elif weapon_level==4:
            b.configure(text="[47.3% / 44.4% / 51.3% / 69.0%]   [208%]   [145% / 182%]")
        elif weapon_level==5:
            b.configure(text="[50.1% / 47.1% / 54.4% / 73.1%]   [220%]   [155% / 193%]")
        elif weapon_level==6:
            b.configure(text="[53.0% / 49.7% / 57.5% / 77.3%]   [233%]   [165% / 206%]")
        elif weapon_level==7:
            b.configure(text="[56.8% / 53.3% / 64.6% / 82.8%]   [249%]   [180% / 224%]")
        elif weapon_level==8:
            b.configure(text="[60.5% / 56.8% / 65.7% / 88.3%]   [266%]   [194% / 243%]")
        elif weapon_level==9:
            b.configure(text="[64.3% / 60.4% / 69.8% / 93.8%]   [283%]   [209% / 261%]")
        elif weapon_level==10:
            b.configure(text="[68.1% / 63.9% / 73.9% / 99.4%]   [299%]   [225% / 281%]")
        elif weapon_level==11:
            b.configure(text="[72.1% / 67.6% / 78.1% / 105.1%]   [317%]   [240% / 300%]")
        elif weapon_level==12:
            b.configure(text="[77.2% / 72.5% / 83.7% / 112.6%]  [339%]  [256% / 320%]")
        elif weapon_level==13:
            b.configure(text="[82.3% / 77.3% / 89.3% / 120.1%]  [362%]  [272% / 340%]")
        elif weapon_level==14:
            b.configure(text="[87.5% / 82.1% / 94.9% / 127.6%]  [384%]  [288% / 360%]")
        elif weapon_level==15:
            b.configure(text="[92.6% / 87.0% / 100.5% / 135.1%]  [407%]  [304% / 380%]")
        else :
            not_written(b)

def info_skill_level2(character_number, skill_level, b, c):
    if character_number==10: #바바라
        c.configure(text="[치유량(공격 시 회복/자동회복)] [피해량] [지속시간] [쿨타임]")
        if skill_level==1:
            b.configure(text="[0.0075 x hp + 72/0.04 x hp + 385]   [58.4%]   [15초] [32초]")
        elif skill_level==2:
            b.configure(text="[0.0081 x hp + 79/0.043 x hp + 424]   [62.8%]   [15초] [32초]")
        elif skill_level==3:
            b.configure(text="[0.0086 x hp + 87/0.046 x hp + 465]   [67.2%]   [15초] [32초]") 
        elif skill_level==4:
            b.configure(text="[0.0094 x hp + 96/0.05 x hp + 510]   [73%]   [15초] [32초]")
        elif skill_level==5:
            b.configure(text="[0.0099 x hp + 105/0.053 x hp + 559]   [77.4%]   [15초] [32초]")
        elif skill_level==6:
            b.configure(text="[0.0105 x hp + 114/0.056 x hp + 610]   [81.8%]   [15초] [32초]")
        elif skill_level==7:
            b.configure(text="[0.0113 x hp + 125/0.06 x hp + 664]   [87.6%]   [15초] [32초]")
        elif skill_level==8:
            b.configure(text="[0.012 x hp + 135/0.064 x hp + 722]   [93.4%]   [15초] [32초]")
        elif skill_level==9:
            b.configure(text="[0.0128 x hp + 147/0.068 x hp + 783]   [99.3%]   [15초] [32초]")
        elif skill_level==10:
            b.configure(text="[0.0135 x hp + 159/0.072 x hp + 847]   [105.1%]   [15초] [32초]")
        elif skill_level==11:
            b.configure(text="[0.0143 x hp + 172/0.076 x hp + 915]   [111%]   [15초] [32초]")
        elif skill_level==12:
            b.configure(text="[0.015 x hp + 185/0.08 x hp + 986]   [116.8%]   [15초] [32초]")
        elif skill_level==13:
            b.configure(text="[0.0159 x hp + 199/0.085 x hp + 1059]   [124.1%]   [15초] [32초]")
        elif skill_level==14:
            b.configure(text="[0.0169 x hp + 213/0.09 x hp + 1136]   [131.4%]   [15초] [32초]")
        elif skill_level==15:
            b.configure(text="[0.0178 x hp + 228/0.095 x hp + 1217]   [138.7%]   [15초] [32초]")
        else :
            not_written(b)

def info_ult_level2(character_number, skill_level, b, c):
    if character_number==10:  #바바라
        c.configure(text="\t[치유량] \t\t[쿨타임]")
        if skill_level==1:
            b.configure(text="[0.0176 x hp + 1694] \t\t[20초]")
        elif skill_level==2:
            b.configure(text="[0.0189 x hp + 1864] \t\t[20초]")
        elif skill_level==3:
            b.configure(text="[0.0202 x hp + 2047] \t[20초]") 
        elif skill_level==4:
            b.configure(text="[0.022 x hp + 2245] \t\t[20초]")
        elif skill_level==5:
            b.configure(text="[0.0233 x hp + 2457] \t[20초]")
        elif skill_level==6:
            b.configure(text="[0.0246 x hp + 2683] \t[20초]")
        elif skill_level==7:
            b.configure(text="[0.0264 x hp + 2923] \t[20초]")
        elif skill_level==8:
            b.configure(text="[0.0282 x hp + 3177] \t[20초]")
        elif skill_level==9:
            b.configure(text="[0.0299 x hp + 3445] \t[20초]")
        elif skill_level==10:
            b.configure(text="[0.0317 x hp + 3728] \t[20초]")
        elif skill_level==11:
            b.configure(text="[0.0334 x hp + 4024] \t[20초]")
        elif skill_level==12:
            b.configure(text="[0.0352 x hp + 4335] \t[20초]")
        elif skill_level==13:
            b.configure(text="[0.0374 x hp + 4660] \t[20초]")
        elif skill_level==14:
            b.configure(text="[0.0396 x hp + 4999] \t[20초]")
        elif skill_level==15:
            b.configure(text="[0.0418 x hp + 5352] \t[20초]")
        else :
            not_written(b)