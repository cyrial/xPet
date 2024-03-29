import exit_prompt
from display_manager import tft, init_display
import stats_screen
import animations
import buttons
import _thread
import timers
import gc
import utime

from database import populate_first_time

populate_first_time()
init_display()
gc.enable()

# ENABLE BUTTONS IN DIFFERENT THREADS
_thread.start_new_thread("BUTTON", buttons.check_button, ())

#animations.hatching(2)
stats_screen.generate_images()
stats_screen.update_stripe("all")

# POOP TIMER IS MANAGED THROUGH OBJECTS AFTER FIRST POOP
timers.check_timer("TIMER_POOP", timers.timer_poop)

while True:
    
    if animations.STOP_IDLE == 0:
        animations.idle()
    else:
        utime.sleep(0.5)
    
    timers.check_timer("TIMER_FOOD", timers.timer_food)
    gc.collect()
    
#0,25 -> 0, 78

#grow()
  
#tft.clear(tft.WHITE)
#tft.image(13, 20, "images/newborn/normal.jpg")
#utime.sleep(10)
