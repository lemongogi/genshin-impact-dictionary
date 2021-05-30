from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *
from typing import get_origin

def info_weapon_level2(character_number, weapon_level, b, c):
    if character_number==10:
        c.configure(text="     1단/2단/3단/4단    강공격 낙하공격(저공/고공)")
        if weapon_level==1:
            b.configure(text="37.8%/35.5%/41.0%/55.2%  166%  114%/142%")
        elif weapon_level==2:
            b.configure(text="37.8%/35.5%/41.0%/55.2%  166%  114%/142%") 