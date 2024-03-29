from machine import Pin, PWM
from rtttl import RTTTL
import time
import _thread

SOUND_PIN = 25

SOUNDS = [
    'hatched:d=8,o=5,b=63:16b,16d6,b,16b,16d6,b,16b,16d6,4f6',
    'alert:d=8,o=6,b=140:d,4f,d,d',
    'success:d=4,o=5,b=63:32c,32e,32g,8b',
    'poo:d=4,o=5,b=63:8b4,8g4,8e4,c4',
    'select:d=8,o=6,b=140:16g',
    'enter:d=8,o=6,b=140:16g5'
]


def find_sound(name):
    for sound in SOUNDS:
        sound_name = sound.split(':')[0]
        if sound_name == name:
            return sound
            
def play_tone(freq, msec):
  
  if freq > 0:
    tone = PWM(Pin(SOUND_PIN, Pin.OUT), freq=int(freq), duty=90)
    time.sleep(msec*0.001) # Play for a number of msec
    
    tone.deinit()
    pin = Pin(SOUND_PIN, Pin.OUT)
    pin.value(1)
    time.sleep(0.05) # Delay 50 ms between notes
  
def play_sound(snd):
  tune = RTTTL(find_sound(snd))
  
  for freq, msec in tune.notes():
    play_tone(freq, msec)
    
def play_sound_thread(sound_name):
    _thread.start_new_thread("SOUND_" + sound_name, play_sound, (sound_name,))
    