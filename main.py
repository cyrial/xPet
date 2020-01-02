import exit_prompt
from display_manager import tft, init_display
import stats_screen
import utime
import animations
import actions
import buttons
import _thread

from database import populate_first_time

ANIMATION_TIME = 0.2

populate_first_time()
init_display()

# ENABLE BUTTONS IN DIFFERENT THREADS
_thread.start_new_thread("SELECT", buttons.button_select, ())
_thread.start_new_thread("ENTER", buttons.button_enter, ())
_thread.start_new_thread("EXIT", buttons.button_exit, ())

#animations.hatching(2)
stats_screen.generate_images()
stats_screen.show_stripe("all")

actions.generate_poo()

while True:
  animations.animate_walk()
  
  if actions.POO == 1:
    animations.animate_poo(animations.POO_ANIM_STEP)

  utime.sleep(ANIMATION_TIME)
    
#0,25 -> 0, 78

#grow()
  
#tft.clear(tft.WHITE)
#tft.image(13, 20, "images/newborn/normal.jpg")
#utime.sleep(10)




