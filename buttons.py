from machine import Pin
from sound_manager import play_sound
import stats_screen
import utime
import gc
import sys
import _thread
import objects
import animations
from stats_screen import increase_stat

SELECT_PIN = 21
ENTER_PIN = 18
EXIT_PIN = 19
  
  
def check_button():
    while True:
        # SELECT
        if not select_handler.value():
            play_sound('select')
            stats_screen.select_from_menu()
      
        # ENTER
        if not enter_handler.value():
            #play_sound('enter')
    
            # CLEANING POO IF NOTHING IS SELECTED
            if stats_screen.CURRENT_STAT == -1:
                if objects.POO:
                    objects.clean_poo()
            
            elif stats_screen.CURRENT_STAT == 0:
                increase_stat("health")
                animations.injection()
                
            elif stats_screen.CURRENT_STAT == 1:
                increase_stat("drink")
                animations.drinking()
                
            elif stats_screen.CURRENT_STAT == 2:
                increase_stat("food")
                animations.eating()
            
            elif stats_screen.CURRENT_STAT == 3:
                increase_stat("sweets")
                animations.eating()
                
            elif stats_screen.CURRENT_STAT == 4:
                increase_stat("fun")
                animations.fun()
             
            elif stats_screen.CURRENT_STAT == 5:
                increase_stat("book")
                animations.reading()
            
            elif stats_screen.CURRENT_STAT == 6:
                increase_stat("wash")
                animations.shower()
            
            elif stats_screen.CURRENT_STAT == 7:
                # SLEEP MODE (start timer)
                animations.sleeping()
                
            stats_screen.reset_highlight(1)
            
        # EXIT
        if not exit_handler.value():
            stats_screen.reset_highlight(1)
            #play_sound('enter')
        
        utime.sleep(0.05)
    
select_handler = Pin(SELECT_PIN, Pin.IN, Pin.PULL_UP)
enter_handler = Pin(ENTER_PIN, Pin.IN, Pin.PULL_UP)
exit_handler = Pin(EXIT_PIN, Pin.IN, Pin.PULL_UP)

