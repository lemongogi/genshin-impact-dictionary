from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *

def not_written(multiply):
    multiply.configure(text="\t제대로 레벨을 입력하라구  \t-페이몬-")

def reposition(x_pos, frame_y, content_y, multiply, multiply_frame):
    multiply.place_forget()
    multiply_frame.place_forget()
    multiply_frame.place(x=x_pos,y=frame_y)
    multiply.place(x=x_pos,y=content_y)

def info_weapon_level2(character_number, weapon_level, multiply, multiply_frame, tartalia_mode="", skill_level=0):
    if character_number==10: #바바라
        multiply_frame.configure(text="    [1단/2단/3단/4단]  [강공격]    [낙하공격(저공/고공)]", font=("Comic Sans MS", 12))
        multiply.configure(font=("Comic Sans MS",10))
        if weapon_level==1:
            multiply.configure(text="[37.8% / 35.5% / 41.0% / 55.2%]   [166%]   [114% / 142%]")
        elif weapon_level==2:
            multiply.configure(text="[40.7% / 38.2% / 44.1% / 59.3%]  [179%]  [123%/153%]")
        elif weapon_level==3:
            multiply.configure(text="[43.5% / 40.8% / 47.2% / 63.5%]   [191%]   [132% / 165%]") 
        elif weapon_level==4:
            multiply.configure(text="[47.3% / 44.4% / 51.3% / 69.0%]   [208%]   [145% / 182%]")
        elif weapon_level==5:
            multiply.configure(text="[50.1% / 47.1% / 54.4% / 73.1%]   [220%]   [155% / 193%]")
        elif weapon_level==6:
            multiply.configure(text="[53.0% / 49.7% / 57.5% / 77.3%]   [233%]   [165% / 206%]")
        elif weapon_level==7:
            multiply.configure(text="[56.8% / 53.3% / 64.6% / 82.8%]   [249%]   [180% / 224%]")
        elif weapon_level==8:
            multiply.configure(text="[60.5% / 56.8% / 65.7% / 88.3%]   [266%]   [194% / 243%]")
        elif weapon_level==9:
            multiply.configure(text="[64.3% / 60.4% / 69.8% / 93.8%]   [283%]   [209% / 261%]")
        elif weapon_level==10:
            multiply.configure(text="[68.1% / 63.9% / 73.9% / 99.4%]   [299%]   [225% / 281%]")
        elif weapon_level==11:
            multiply.configure(text="[72.1% / 67.6% / 78.1% / 105.1%]   [317%]   [240% / 300%]")
        elif weapon_level==12:
            multiply.configure(text="[77.2% / 72.5% / 83.7% / 112.6%]  [339%]  [256% / 320%]")
        elif weapon_level==13:
            multiply.configure(text="[82.3% / 77.3% / 89.3% / 120.1%]  [362%]  [272% / 340%]")
        elif weapon_level==14:
            multiply.configure(text="[87.5% / 82.1% / 94.9% / 127.6%]  [384%]  [288% / 360%]")
        elif weapon_level==15:
            multiply.configure(text="[92.6% / 87.0% / 100.5% / 135.1%]  [407%]  [304% / 380%]")
        else :
            not_written(multiply)

    elif character_number==11:  #행추
        multiply_frame.configure(text="  [1단/2단/3단/4단/5단]  [강공격]    [낙하공격(저공/고공)]", font=("Comic Sans MS", 12))
        multiply.configure(font=("Comic Sans MS", 11))
        if weapon_level==1:
            multiply.configure(text="[46.6% / 47.6% / 28.6+28.6% / 56.0% / 35.9%+35.9%]   [47.3%+56.2%]   [128% / 160%]")#전부 수정
        elif weapon_level==2:
            multiply.configure(text="[50.4% / 51.5% / 30.9%+30.9% / 60.5% / 38.8%+38.8%]  [51.2%+60.7%]  [138% / 173%]")
        elif weapon_level==3:
            multiply.configure(text="[54.2% / 55.4% / 33.2%+33.2% / 65.1% / 41.7%+41.7%]   [55.0%+65.3%]   [149% / 186%]") 
        elif weapon_level==4:
            multiply.configure(text="[59.6% / 60.9% / 36.5%+36.5% / 71.6% / 45.9%+45.9%]   [60.5%+71.8%]   [164% / 204%]")
        elif weapon_level==5:
            multiply.configure(text="[63.4% / 64.8% / 38.8%+38.8% / 76.2% / 48.8%+48.8%]   [64.4%+76.4%]   [174% / 217%]")
        elif weapon_level==6:
            multiply.configure(text="[67.8% / 69.3% / 41.5%+41.5% / 81.4% / 52.1%+52.1%]   [68.8%+81.6%]   [186% / 232%]")
        elif weapon_level==7:
            multiply.configure(text="[73.7% / 75.3% / 45.2%+45.2% / 88.5% / 56.7%+56.7%]   [74.8%+88.8%]   [202% / 253%]")
        elif weapon_level==8:
            multiply.configure(text="[79.7% / 81.4% / 48.8%+48.8% / 95.7% / 61.3%+61.3%]   [80.9%+96.0%]   [219% / 273%]")
        elif weapon_level==9:
            multiply.configure(text="[85.6% / 87.5% / 52.5%+52.5% / 102.9% / 65.9%+65.9%]   [86.9%+103.2%]   [235% / 293%]")
        elif weapon_level==10:
            multiply.configure(text="[92.1% / 94.2% / 56.4%+56.4% / 110.7% / 70.9%+70.9%]   [93.5%+111.0%]   [253% / 316%]")
        elif weapon_level==11:
            multiply.configure(text="[99.6% / 102% / 61.0%+61.0% / 119.6% / 76.6%+76.6%]   [101.1%+120.0%]   [271% / 338%]")
        elif weapon_level==12:
            multiply.configure(text="[108.4% / 110.8% / 66.4%+66.4% / 130.2% / 83.4%+83.4%]  [110.0%+130.6%]  [289% / 360%]")
        elif weapon_level==13:
            multiply.configure(text="[117.1% / 120.0% / 71.7%+71.7% / 140.7% / 90.1%+90.1%]  [118.9%+141.1%]  [306% / 382%]")
        elif weapon_level==14:
            multiply.configure(text="[125.9% / 128.7% / 77.1%+77.1% / 151.2% / 96.9%+96.9%]  [127.7%+151.7%]  [324% / 405%]")
        elif weapon_level==15:
            multiply.configure(text="[135.5% / 138.4% / 83.0%+83.0% / 162.7% / 104.2%+104.2%]  [137.5%+163.2%]  [342% / 427%]")
        else :
            not_written(multiply)

    elif character_number==12: #모나
        multiply_frame.configure(text="    [1단/2단/3단/4단]  [강공격]    [낙하공격(저공/고공)]", font=("Comic Sans MS", 12))
        multiply.configure(font=("Comic Sans MS",11))
        if weapon_level==1:
            multiply.configure(text="[37.6% / 36.0% / 44.8% / 56.2%]   [150%]   [114% / 142%]")
        elif weapon_level==2:
            multiply.configure(text="[40.4% / 38.7% / 48.1% / 60.3%]  [161%]  [123%/153%]")
        elif weapon_level==3:
            multiply.configure(text="[43.2% / 41.4% / 51.5% / 64.6%]   [172%]   [132% / 165%]") 
        elif weapon_level==4:
            multiply.configure(text="[47.0% / 45.0% / 56.0% / 70.2%]   [186%]   [145% / 182%]")
        elif weapon_level==5:
            multiply.configure(text="[49.8% / 47.7% / 59.4% / 74.4%]   [198%]   [155% / 193%]")
        elif weapon_level==6:
            multiply.configure(text="[52.6% / 50.4% / 62.7% / 78.6%]   [210%]   [165% / 206%]")
        elif weapon_level==7:
            multiply.configure(text="[56.4% / 54.0% / 67.2% / 84.2%]   [225%]   [180% / 224%]")
        elif weapon_level==8:
            multiply.configure(text="[60.2% / 57.6% / 71.7% / 89.9%]   [240%]   [194% / 243%]")
        elif weapon_level==9:
            multiply.configure(text="[63.9% / 61.2% / 76.2% / 95.5%]   [255%]   [209% / 261%]")
        elif weapon_level==10:
            multiply.configure(text="[67.7% / 64.8% / 80.6% / 101.1%]   [270%]   [225% / 281%]")
        elif weapon_level==11:
            multiply.configure(text="[71.4% / 68.4% / 85.1% / 106.7%]   [285%]   [240% / 300%]")
        elif weapon_level==12:
            multiply.configure(text="[75.2% / 72.0% / 89.6% / 112.3%]  [305%]  [256% / 320%]")
        elif weapon_level==13:
            multiply.configure(text="[79.9% / 76.5% / 95.2% / 119.3%]  [325%]  [272% / 340%]")
        elif weapon_level==14:
            multiply.configure(text="[84.6% / 81.0% / 100.8% / 126.4%]  [346%]  [288% / 360%]")
        elif weapon_level==15:
            multiply.configure(text="[89.3% / 85.5% / 106.4% / 133.4%]  [367%]  [304% / 380%]")
        else :
            not_written(multiply)

    elif character_number==13: #타르탈리아

        multiply.configure(font=("Comic Sans MS",10))
        if tartalia_mode=="bow":
            multiply_frame.configure(text="[1단/2단/3단/4단/5단/6단] [조준공격/풀차징] [단류섬] [단류파] [단류지속] [낙하공격(저공/고공)]", font=("Comic Sans MS", 10))
            if weapon_level==1:
                multiply.configure(text="[41.3% / 46.3% / 55.4% / 57.0% / 60.9% / 72.8%]   [43.9%/124%] [12.4%] [62%] [10초] [114% / 142%]")
            elif weapon_level==2:
                multiply.configure(text="[44.6% / 50.0% / 59.9% / 61.7% / 65.8% / 78.7%]  [47.4%/133%] [13.3%] [66.7%] [10초] [123%/153%]")
            elif weapon_level==3:
                multiply.configure(text="[48.0% / 53.8% / 64.4% / 66.3% / 70.8% / 84.6%]   [51%/143%] [14.3%] [71.3%] [10초] [132% / 165%]") 
            elif weapon_level==4:
                multiply.configure(text="[52.8% / 59.2% / 70.8% / 73.0% / 77.9% / 93.0%]   [56.1%/155%] [15.5%] [77.5%] [10초] [145% / 182%]")
            elif weapon_level==5:
                multiply.configure(text="[56.2% / 63.0% / 75.4% / 77.6% / 82.8% / 99.0%]   [59.7%/164%] [16.4%] [82.2%] [10초] [155% / 193%]")
            elif weapon_level==6:
                multiply.configure(text="[60.0% / 67.3% / 80.5% / 82.9% / 88.5% / 105.8%]   [63.8%/174%] [17.4%] [86.8%] [10초] [165% / 206%]")
            elif weapon_level==7:
                multiply.configure(text="[65.3% / 73.2% / 87.6% / 90.2% / 96.3% / 115.1%]   [69.4%/186%] [18.6%] [93%] [10초] [180% / 224%]")
            elif weapon_level==8:
                multiply.configure(text="[70.6% / 79.1% / 94.7% / 97.5% / 104.1% / 124.4%]   [75%/198%] [19.8%] [99.2%] [10초] [194% / 243%]")
            elif weapon_level==9:
                multiply.configure(text="[75.8% / 85.0% / 101.8% / 104.8% / 111.9% / 133.7%]   [80.6%/211%] [21.1%] [105%] [10초] [209% / 261%]")
            elif weapon_level==10:
               multiply.configure(text="[81.6% / 91.5% / 109.5% / 112.7% / 120.4% / 143.8%]   [86.7%/223%] [22.3%] [112%] [10초] [225% / 281%]")
            elif weapon_level==11:
                multiply.configure(text="[87.4% / 98.0% / 117.2% / 120.7% / 128.9% / 154%]   [92.8%/236%] [23.6%] [118%] [10초] [240% / 300%]")
            elif weapon_level==12:
                multiply.configure(text="[93.1% / 104.4% / 125% / 128.6% / 137.4% / 164.1%]  [98.9%/248%] [24.8%] [124%] [10초] [256% / 320%]")
            elif weapon_level==13:
                multiply.configure(text="[98.9% / 110.8% / 132.7% / 136.6% / 145.9% / 174.3%]  [105.1%/264%] [26.4%] [132%] [10초] [272% / 340%]")
            elif weapon_level==14:
                multiply.configure(text="[104.6% / 117.3% / 140.4% / 144.5% / 154.3% / 184.4%]  [111.2%/279%] [27.9%] [140%] [10초] [288% / 360%]")
            elif weapon_level==15:
                multiply.configure(text="[110.4% / 123.7% / 148.1% / 152.5% / 162.8% / 194.6%]  [117.3%/295%] [29.5%] [147%] [10초] [304% / 380%]")
            else :
                not_written(multiply)
        else:
                multiply_frame.configure(text="[1단/2단/3단/4단/5단/6단] [강공격] [단류참] [단류지속]", font=("Comic Sans MS", 10))
                if skill_level==1:
                    multiply.configure(text="[38.9% / 41.6% / 56.3% / 59.9% / 55.3% / 35.4%+37.7%]   [60.2%+72.0%] [12.4%] [10초]")
                elif skill_level==2:
                    multiply.configure(text="[42.0% / 45.0% / 60.9% / 64.8% / 59.8% / 38.3%+40.7%]   [65.1%+77.8%] [12.4%] [10초]")
                elif skill_level==3:
                    multiply.configure(text="[45.1% / 48.4% / 65.5% / 69.7% / 64.3% / 41.2%+43.7%]   [70.0%+83.6%] [12.4%] [10초]")
                elif skill_level==4:
                    multiply.configure(text="[49.7% / 53.2% / 72.1% / 76.7% / 70.7% / 45.3%+48.2%]   [77.0%+92.1%] [12.4%] [10초]")
                elif skill_level==5:
                    multiply.configure(text="[52.9% / 56.6% / 76.6% / 81.5% / 75.2% / 48.2%+51.2%]   [81.9%+97.9%] [12.4%] [10초]")
                elif skill_level==6:
                    multiply.configure(text="[56.1% / 60.0% / 81.1% / 86.3% / 79.7% / 51.1%+54.2%]   [86.8%+103%] [12.4%] [10초]")
                elif skill_level==7:
                    multiply.configure(text="[61.5% / 65.8% / 89.1% / 94.8% / 87.5% / 56.0%+59.6%]   [95.2%+114%] [12.4%] [10초]")
                elif skill_level==8:
                    multiply.configure(text="[66.4% / 71.2% / 96.3% / 102.5% / 94.5% / 60.6%+64.4%]   [103%+123%] [12.4%] [10초]")
                elif skill_level==9:
                    multiply.configure(text="[71.4% / 76.5% / 103.5% / 110.1% / 101.6% / 65.1%+69.2%]   [110.6%+132.2%] [12.4%] [10초]")
                elif skill_level==10:
                    multiply.configure(text="[76.8% / 82.3% / 111.4% / 118.5% / 109.3% / 70.0%+74.5%]   [119.0%+142.3%] [12.4%] [10초]")
                elif skill_level==11:
                    multiply.configure(text="[82.3% / 88.1% / 119.2% / 126.9% / 117.0% / 75.0%+79.7%]   [127.4%+152.3%] [12.4%] [10초]")
                elif skill_level==12:
                    multiply.configure(text="[87.7% / 93.9% / 127.1% / 135.2% / 124.7% / 79.9%+85.0%]   [135.8%+162.4%] [12.4%] [10초]")
                elif skill_level==13:
                    multiply.configure(text="[93.1% / 99.7% / 134.9% / 143.6% / 132.5% / 84.9%+90.2%]   [144.2%+172.4%] [12.4%] [10초]")
                elif skill_level==14:
                    multiply.configure(text="[98.5% / 105.5% / 142.8% / 152.0% / 140.2% / 89.8%+95.5%]   [152.6%+182.5%] [12.4%] [10초]")
                elif skill_level==15:
                    multiply.configure(text="[104.0% / 111.3% / 150.7% / 160.3% / 147.9% / 94.8%+100.7%]   [161%+192.5%] [12.4%] [10초]")
                else :
                    not_written(multiply)

def info_skill_level2(character_number, skill_level, multiply, multiply_frame):
    if character_number==10: #바바라
        reposition(80, 390, 415, multiply, multiply_frame)
        multiply_frame.configure(text="[치유량(공격 시 회복/자동회복)] [피해량] [지속시간] [쿨타임]")
        if skill_level==1:
            multiply.configure(text="[0.0075 x hp + 72/0.04 x hp + 385]   [58.4%]   [15초] [32초]")
        elif skill_level==2:
            multiply.configure(text="[0.0081 x hp + 79/0.043 x hp + 424]   [62.8%]   [15초] [32초]")
        elif skill_level==3:
            multiply.configure(text="[0.0086 x hp + 87/0.046 x hp + 465]   [67.2%]   [15초] [32초]") 
        elif skill_level==4:
            multiply.configure(text="[0.0094 x hp + 96/0.05 x hp + 510]   [73%]   [15초] [32초]")
        elif skill_level==5:
            multiply.configure(text="[0.0099 x hp + 105/0.053 x hp + 559]   [77.4%]   [15초] [32초]")
        elif skill_level==6:
            multiply.configure(text="[0.0105 x hp + 114/0.056 x hp + 610]   [81.8%]   [15초] [32초]")
        elif skill_level==7:
            multiply.configure(text="[0.0113 x hp + 125/0.06 x hp + 664]   [87.6%]   [15초] [32초]")
        elif skill_level==8:
            multiply.configure(text="[0.012 x hp + 135/0.064 x hp + 722]   [93.4%]   [15초] [32초]")
        elif skill_level==9:
            multiply.configure(text="[0.0128 x hp + 147/0.068 x hp + 783]   [99.3%]   [15초] [32초]")
        elif skill_level==10:
            multiply.configure(text="[0.0135 x hp + 159/0.072 x hp + 847]   [105.1%]   [15초] [32초]")
        elif skill_level==11:
            multiply.configure(text="[0.0143 x hp + 172/0.076 x hp + 915]   [111%]   [15초] [32초]")
        elif skill_level==12:
            multiply.configure(text="[0.015 x hp + 185/0.08 x hp + 986]   [116.8%]   [15초] [32초]")
        elif skill_level==13:
            multiply.configure(text="[0.0159 x hp + 199/0.085 x hp + 1059]   [124.1%]   [15초] [32초]")
        elif skill_level==14:
            multiply.configure(text="[0.0169 x hp + 213/0.09 x hp + 1136]   [131.4%]   [15초] [32초]")
        elif skill_level==15:
            multiply.configure(text="[0.0178 x hp + 228/0.095 x hp + 1217]   [138.7%]   [15초] [32초]")
        else :
            not_written(multiply)

    elif character_number==11: #행추
        reposition(80, 380, 405, multiply, multiply_frame)
        multiply_frame.configure(text="[스킬피해량] [피해감소량] [지속시간] [쿨타임]")
        multiply.configure(font=("Comic Sans MS",14))
        if skill_level==1:
            multiply.configure(text="[168%+191%]   [20%]   [15초] [21초]")
        elif skill_level==2:
            multiply.configure(text="[181%+206%]   [21%]   [15초] [21초]")
        elif skill_level==3:
            multiply.configure(text="[193%+221%]   [22%]   [15초] [21초]") 
        elif skill_level==4:
            multiply.configure(text="[210%+239%]   [23%]   [15초] [21초]")
        elif skill_level==5:
            multiply.configure(text="[223%+253%]   [24%]   [15초] [21초]")
        elif skill_level==6:
            multiply.configure(text="[235%+268%]   [25%]   [15초] [21초]")
        elif skill_level==7:
            multiply.configure(text="[252%+287%]   [26%]   [15초] [21초]")
        elif skill_level==8:
            multiply.configure(text="[269%+306%]   [27%]   [15초] [21초]")
        elif skill_level==9:
            multiply.configure(text="[286%+325%]   [28%]   [15초] [21초]")
        elif skill_level==10:
            multiply.configure(text="[302%+344%]   [29%]   [15초] [21초]")
        elif skill_level==11:
            multiply.configure(text="[319%+363%]   [29%]   [15초] [21초]")
        elif skill_level==12:
            multiply.configure(text="[336%+382%]   [29%]   [15초] [21초]")
        elif skill_level==13:
            multiply.configure(text="[357%+406%]   [29%]   [15초] [21초]")
        elif skill_level==14:
            multiply.configure(text="[378%+430%]   [29%]   [15초] [21초]")
        elif skill_level==15:
            multiply.configure(text="[399%+454%]   [29%]   [15초] [21초]")
        else :
            not_written(multiply)
    
    elif character_number==12: #모나
        reposition(80, 380, 405, multiply, multiply_frame)
        multiply_frame.configure(text="[지속피해량] [파열피해량] [지속시간] [쿨타임]")
        multiply.configure(font=("Comic Sans MS",14))
        if skill_level==1:
            multiply.configure(text="[32.0%]   [133%]   [5초] [21초]")
        elif skill_level==2:
            multiply.configure(text="[34.4%]   [143%]   [5초] [21초]")
        elif skill_level==3:
            multiply.configure(text="[36.8%]   [153%]   [5초] [21초]") 
        elif skill_level==4:
            multiply.configure(text="[40%]   [166%]   [5초] [21초]")
        elif skill_level==5:
            multiply.configure(text="[42.4%]   [176%]   [5초] [21초]")
        elif skill_level==6:
            multiply.configure(text="[44.8%]   [186%]   [5초] [21초]")
        elif skill_level==7:
            multiply.configure(text="[48%]   [199%]   [5초] [21초]")
        elif skill_level==8:
            multiply.configure(text="[51.2%]   [212%]   [5초] [21초]")
        elif skill_level==9:
            multiply.configure(text="[54.4%]   [226%]   [5초] [21초]")
        elif skill_level==10:
            multiply.configure(text="[57.6%]   [239%]   [5초] [21초]")
        elif skill_level==11:
            multiply.configure(text="[60.8%]   [252%]   [5초] [21초]")
        elif skill_level==12:
            multiply.configure(text="[64%]   [266%]   [5초] [21초]")
        elif skill_level==13:
            multiply.configure(text="[68%]   [282%]   [5초] [21초]")
        elif skill_level==14:
            multiply.configure(text="[72%]   [299%]   [5초] [21초]")
        elif skill_level==15:
            multiply.configure(text="[76%]   [315%]   [5초] [21초]")
        else :
            not_written(multiply)

    elif character_number==13: #타르탈리아
        reposition(80, 380, 405, multiply, multiply_frame)
        multiply_frame.configure(text="[피해량]")
        multiply_frame.configure(font=("Comic Sans MS",13))
        multiply.configure(font=("Comic Sans MS",13))
        if skill_level==1:
            multiply.configure(text="[72%]")
        elif skill_level==2:
            multiply.configure(text="[77%]")
        elif skill_level==3:
            multiply.configure(text="[82%]") 
        elif skill_level==4:
            multiply.configure(text="[90%]")
        elif skill_level==5:
            multiply.configure(text="[95%]")
        elif skill_level==6:
            multiply.configure(text="[100%]")
        elif skill_level==7:
            multiply.configure(text="[108%]")
        elif skill_level==8:
            multiply.configure(text="[115%]")
        elif skill_level==9:
            multiply.configure(text="[122%]")
        elif skill_level==10:
            multiply.configure(text="[130%]")
        elif skill_level==11:
            multiply.configure(text="[137%]")
        elif skill_level==12:
            multiply.configure(text="[144%]")
        elif skill_level==13:
            multiply.configure(text="[153%]")
        elif skill_level==14:
            multiply.configure(text="[162%]")
        elif skill_level==15:
            multiply.configure(text="[171%]")
        else :
            not_written(multiply)

def info_ult_level2(character_number, skill_level, multiply, multiply_frame, tartalia_mode=""):
    if character_number==10:  #바바라
        multiply_frame.configure(text="\t[치유량] \t\t[쿨타임]")
        if skill_level==1:
            multiply.configure(text="[0.0176 x hp + 1694] \t\t[20초]")
        elif skill_level==2:
            multiply.configure(text="[0.0189 x hp + 1864] \t\t[20초]")
        elif skill_level==3:
            multiply.configure(text="[0.0202 x hp + 2047] \t[20초]") 
        elif skill_level==4:
            multiply.configure(text="[0.022 x hp + 2245] \t\t[20초]")
        elif skill_level==5:
            multiply.configure(text="[0.0233 x hp + 2457] \t[20초]")
        elif skill_level==6:
            multiply.configure(text="[0.0246 x hp + 2683] \t[20초]")
        elif skill_level==7:
            multiply.configure(text="[0.0264 x hp + 2923] \t[20초]")
        elif skill_level==8:
            multiply.configure(text="[0.0282 x hp + 3177] \t[20초]")
        elif skill_level==9:
            multiply.configure(text="[0.0299 x hp + 3445] \t[20초]")
        elif skill_level==10:
            multiply.configure(text="[0.0317 x hp + 3728] \t[20초]")
        elif skill_level==11:
            multiply.configure(text="[0.0334 x hp + 4024] \t[20초]")
        elif skill_level==12:
            multiply.configure(text="[0.0352 x hp + 4335] \t[20초]")
        elif skill_level==13:
            multiply.configure(text="[0.0374 x hp + 4660] \t[20초]")
        elif skill_level==14:
            multiply.configure(text="[0.0396 x hp + 4999] \t[20초]")
        elif skill_level==15:
            multiply.configure(text="[0.0418 x hp + 5352] \t[20초]")
        else :
            not_written(multiply)

    elif character_number==11:  #행추
        multiply_frame.configure(text="[피해량] [지속시간] [쿨타임]")
        if skill_level==1:
            multiply.configure(text="[54.3%] [15초] [20초]")
        elif skill_level==2:
            multiply.configure(text="[58.3%] [15초] [20초]")
        elif skill_level==3:
            multiply.configure(text="[62.4%] [15초] [20초]") 
        elif skill_level==4:
            multiply.configure(text="[67.8%] [15초] [20초]")
        elif skill_level==5:
            multiply.configure(text="[71.9%] [15초] [20초]")
        elif skill_level==6:
            multiply.configure(text="[76%] [15초] [20초]")
        elif skill_level==7:
            multiply.configure(text="[81.4%] [15초] [20초]")
        elif skill_level==8:
            multiply.configure(text="[86.8%] [15초] [20초]")
        elif skill_level==9:
            multiply.configure(text="[92.3%] [15초] [20초]")
        elif skill_level==10:
            multiply.configure(text="[97.7%] [15초] [20초]")
        elif skill_level==11:
            multiply.configure(text="[103%] [15초] [20초]")
        elif skill_level==12:
            multiply.configure(text="[109%] [15초] [20초]")
        elif skill_level==13:
            multiply.configure(text="[115%] [15초] [20초]")
        elif skill_level==14:
            multiply.configure(text="[122%] [15초] [20초]")
        elif skill_level==15:
            multiply.configure(text="[129%] [15초] [20초]")
        else :
            not_written(multiply)
    
    elif character_number==12:  #모나
        multiply_frame.configure(text="[피해량] [피해증폭량] [포영지속시간] [성이지속시간] [쿨타임]")
        if skill_level==1:
            multiply.configure(text="[442%] [42%] [8초] [4초] [15초]")
        elif skill_level==2:
            multiply.configure(text="[476%] [44%] [8초] [4초] [15초]")
        elif skill_level==3:
            multiply.configure(text="[509%] [46%] [8초] [4초] [15초]") 
        elif skill_level==4:
            multiply.configure(text="[553%] [48%] [8초] [4.5초] [15초]")
        elif skill_level==5:
            multiply.configure(text="[586%] [50%] [8초] [4.5초] [15초]")
        elif skill_level==6:
            multiply.configure(text="[619%] [52%] [8초] [4.5초] [15초]")
        elif skill_level==7:
            multiply.configure(text="[664%] [54%] [8초] [5초] [15초]")
        elif skill_level==8:
            multiply.configure(text="[708%] [56%] [8초] [5초] [15초]")
        elif skill_level==9:
            multiply.configure(text="[752%] [58%] [8초] [5초] [15초]")
        elif skill_level==10:
            multiply.configure(text="[796%] [60%] [8초] [5초] [15초]")
        elif skill_level==11:
            multiply.configure(text="[841%] [60%] [8초] [5초] [15초]")
        elif skill_level==12:
            multiply.configure(text="[885%] [60%] [8초] [5초] [15초]")
        elif skill_level==13:
            multiply.configure(text="[940%] [60%] [8초] [5초] [15초]")
        elif skill_level==14:   
            multiply.configure(text="[995%] [60%] [8초] [5초] [15초]")
        elif skill_level==15:
            multiply.configure(text="[1051%] [60%] [8초] [5초] [15초]")
        else :
            not_written(multiply)
        
    elif character_number==13:  #타르탈리아
        if tartalia_mode=="bow":
            multiply_frame.configure(text="[피해량] [쿨타임]")
            if skill_level==1:
                multiply.configure(text="[378%] [15초]")
            elif skill_level==2:
                multiply.configure(text="[407%] [15초]")
            elif skill_level==3:
                multiply.configure(text="[435%] [15초]") 
            elif skill_level==4:
                multiply.configure(text="[473%] [15초]")
            elif skill_level==5:
                multiply.configure(text="[501%] [15초]")
            elif skill_level==6:
                multiply.configure(text="[530%] [15초]")
            elif skill_level==7:
                multiply.configure(text="[568%] [15초]")
            elif skill_level==8:
                multiply.configure(text="[605%] [15초]")
            elif skill_level==9:
                multiply.configure(text="[643%] [15초]")
            elif skill_level==10:
                multiply.configure(text="[681%] [15초]")
            elif skill_level==11:
                multiply.configure(text="[719%] [15초]")
            elif skill_level==12:
                multiply.configure(text="[757%] [15초]")
            elif skill_level==13:
                multiply.configure(text="[804%] [15초]")
            elif skill_level==14:   
                multiply.configure(text="[851%] [15초]")
            elif skill_level==15:
                multiply.configure(text="[899%] [15초]")
            else :
                not_written(multiply)
        else:
            multiply_frame.configure(text="[피해량] [단류 폭] [쿨타임]")
            if skill_level==1:
                multiply.configure(text="[464%] [120%] [15초]")
            elif skill_level==2:
                multiply.configure(text="[499%] [129%] [15초]")
            elif skill_level==3:
                multiply.configure(text="[534%] [138%] [15초]") 
            elif skill_level==4:
                multiply.configure(text="[580%] [150%] [15초]")
            elif skill_level==5:
                multiply.configure(text="[615%] [159%] [15초]")
            elif skill_level==6:
                multiply.configure(text="[650%] [168%] [15초]")
            elif skill_level==7:
                multiply.configure(text="[696%] [180%] [15초]")
            elif skill_level==8:
                multiply.configure(text="[742%] [192%] [15초]")
            elif skill_level==9:
                multiply.configure(text="[789%] [204%] [15초]")
            elif skill_level==10:
                multiply.configure(text="[835%] [216%] [15초]")
            elif skill_level==11:
                multiply.configure(text="[882%] [228%] [15초]")
            elif skill_level==12:
                multiply.configure(text="[928%] [240%] [15초]")
            elif skill_level==13:
                multiply.configure(text="[986%] [255%] [15초]")
            elif skill_level==14:   
                multiply.configure(text="[1044%] [270%] [15초]")
            elif skill_level==15:
                multiply.configure(text="[1102%] [285%] [15초]")
            else :
                not_written(multiply)