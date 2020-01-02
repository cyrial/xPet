from machine import Pin
from sound_manager import play_sound
from stats_screen import select_from_menu, reset_highlight, CURRENT_STAT
import utime
import gc
import sys

SELECT_PIN = 21
ENTER_PIN = 18
EXIT_PIN = 19
  
def button_select():
  while True:
    if not select_handler.value():
      play_sound('select')
      select_from_menu()
      
    utime.sleep(0.1)
    
def button_enter():
  while True:
    if not enter_handler.value():
      play_sound('enter')
    
  utime.sleep(0.1)
  
def button_exit():
  while True:
    if not exit_handler.value():
      reset_highlight(1)
      play_sound('enter')
    
select_handler = Pin(SELECT_PIN, Pin.IN, Pin.PULL_UP)
enter_handler = Pin(ENTER_PIN, Pin.IN, Pin.PULL_UP)
exit_handler = Pin(EXIT_PIN, Pin.IN, Pin.PULL_UP)









