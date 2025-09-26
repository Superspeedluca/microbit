# Imports go at the top
from microbit import *
import music
import speech

speech.say('Hello, world. How are you? I will beep to the light!')
vol = 128



# Code in a 'while True:' loop repeats forever
while True:
    lichtniveau = display.read_light_level()
    print(lichtniveau)
    print("Volume "+ str(vol))
    
    music.pitch(2 * lichtniveau + 100)

    if button_a.was_pressed():
        vol = vol + 10
    if button_b.was_pressed():
        vol = vol - 10


    set_volume(vol)