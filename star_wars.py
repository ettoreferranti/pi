import sys
import RPi.GPIO as GPIO
from time import sleep

#define the frequency of the notes
c = 261
d = 294
e = 329
f = 349
g = 391
gS = 415
a = 440
aS = 455
b = 466
cH = 523
cSH = 554
dH = 587
dSH = 622
eH = 659
fH = 698
fSH = 740
gH = 784
gSH = 830
aH = 880

#configuration
duty = 10
triggerPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN,GPIO.OUT)

#helper functions to play notes
def playNote(freq, time):
    buzzer.stop()
    buzzer.ChangeFrequency(freq)
    sleep(0.05)
    buzzer.start(duty)
    sleep(time)

def pause(time):
    buzzer.stop()
    sleep(time)
    buzzer.start(duty)

def firstSection():
    playNote(a, 0.500)
    playNote(a, 0.500)    
    playNote(a, 0.500)
    playNote(f, 0.350)
    playNote(cH, 0.150)  
    playNote(a, 0.500)
    playNote(f, 0.350)
    playNote(cH, 0.150)
    playNote(a, 0.650)

    pause(0.5)

    playNote(eH, 0.500)
    playNote(eH, 0.500)
    playNote(eH, 0.500)  
    playNote(fH, 0.350)
    playNote(cH, 0.150)
    playNote(gS, 0.500)
    playNote(f, 0.350)
    playNote(cH, 0.150)
    playNote(a, 0.650)

def secondSection():
    playNote(aH, 0.500)
    playNote(a, 0.300)    
    playNote(a, 0.150)
    playNote(aH, 0.500)
    playNote(gSH, 0.325)
    playNote(gH, 0.175)
    playNote(fSH, 0.125)
    playNote(fH, 0.125)    
    playNote(fSH, 0.250)

    pause(0.325)

    playNote(aS, 0.250)
    playNote(dSH, 0.500)
    playNote(dH, 0.325)  
    playNote(cSH, 0.175)  
    playNote(cH, 0.125)  
    playNote(b, 0.125) 
    playNote(cH, 0.250)  

    pause(0.350)

# define PWM signal and start it on trigger PIN
buzzer = GPIO.PWM(triggerPIN, c)
buzzer.start(duty)

#execute music
firstSection()

secondSection()

playNote(f, 0.250)
playNote(gS, 0.500)  
playNote(f, 0.350)  
playNote(a, 0.125)
playNote(cH, 0.500)
playNote(a, 0.375)  
playNote(cH, 0.125)
playNote(eH, 0.650)

pause(0.500)

secondSection()

playNote(f, 0.250)  
playNote(gS, 0.500)  
playNote(f, 0.375)  
playNote(cH, 0.125)
playNote(a, 0.500)  
playNote(f, 0.375)  
playNote(cH, 0.125)
playNote(a, 0.650)  

pause(0.650)

GPIO.cleanup()
sys.exit()
