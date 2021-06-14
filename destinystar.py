from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *

def star1(character_number, starinput):
    if character_number==10:
        starinput.configure(text="무지개의 노래:바바라는 10초마다 원소에너지를 1pt(궁극기는 80pt요구함) 채워줍니다", font=("Comic Sans MS",18))