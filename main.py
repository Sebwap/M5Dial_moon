import os, sys, io
import M5
from M5 import *
import time
from hardware import *

image = None

def display_image():
    global planet
    if planet=='moon':
        image = Widgets.Image('res/img/moon/moon ('+str(i)+').jpg', 0, 0)
    else:
        image = Widgets.Image('res/img/earth/earth ('+str(i)+').jpg', 0, 0)

#source des images: https://svs.gsfc.nasa.gov/4310/
# earth https://svs.gsfc.nasa.gov/3639/
# redimensionner en 240 avec Gimp et recadrées (BIMP pour faire du Gimp en rafale)
# échantilloné en prenant seulement 48 images (xx1 et xx6)

i=1

i_max_moon=48
i_max_earth=50
mode_manuel=-1 # automatique par défaut

# on commence avec la lune
planet='moon'
i_max=48

rotary = Rotary()
r_count=0
Speaker.setVolumePercentage(0.3)
Lcd.setBrightness(5)

while True:
    M5.update()
    
    if BtnA.wasSingleClicked():
        # on change de planète
        if planet=='moon':
            planet='earth'
            i_max=i_max_earth
        else:
            planet='moon'
            i_max=i_max_moon
    
    if M5.Touch.getCount()>0 and M5.Touch.getDetail()[4]==True:
        time.sleep_ms(100)
        M5.update()
        mode_manuel*=-1
        r_count=rotary.get_rotary_value()
    
    if mode_manuel==1:
        rot_temp=rotary.get_rotary_value()
        if rot_temp<r_count:
            Speaker.tone(3000, 50)
            i-=1
            if i<1:
                i=i_max
            display_image()
            r_count=rot_temp
        elif rot_temp>r_count:
            Speaker.tone(4000, 50)
            i+=1
            if i>i_max:
                i=1
            display_image()
            r_count=rot_temp
    else:
        display_image()
        i+=1;
        if i>i_max:
            i=1
        time.sleep_ms(20)
