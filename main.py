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
    timers.check_timer("TIMER_DRINK", timers.timer_drink)
    timers.check_timer("TIMER_SWEETS", timers.timer_sweets)
    timers.check_timer("TIMER_LEARN", timers.timer_learn)
    timers.check_timer("TIMER_FUN", timers.timer_fun)
    timers.check_timer("TIMER_SHOWER", timers.timer_shower)
    timers.check_timer("TIMER_SLEEP", timers.timer_fun)

    # FOOD
    if (int(read_db_value("food")) <= 3 or int(read_db_value("food")) > 10):
        timers.check_timer("TIMER_HEALTH_FOOD", timers.timer_decrease_stat("health", 900))
        
    if (int(read_db_value("food")) >= 9):
        timers.check_timer("TIMER_POO_FOOD", timers.timer_poop_demand(900))
    
    # DRINK
    if (int(read_db_value("drink")) <= 3 or int(read_db_value("drink")) > 10):
        timers.check_timer("TIMER_HEALTH_DRINK", timers.timer_decrease_stat("health", 900))
        
    # SWEETS
    if (int(read_db_value("sweets")) <= 3 or int(read_db_value("sweets")) > 10):
        timers.check_timer("TIMER_MOOD_SWEETS", timers.timer_decrease_stat("mood", 900))
    
    if (int(read_db_value("sweets")) >= 9):
        timers.check_timer("TIMER_HEALTH_SWEETS", timers.timer_decrease_stat("health", 900))
        
    # LEARN
    if (int(read_db_value("book")) <= 3):
        timers.check_timer("TIMER_MOOD_LEARN", timers.timer_decrease_stat("mood", 900))
    
    if (int(read_db_value("book")) > 9):
        timers.check_timer("TIMER_FUN_LEARN", timers.timer_decrease_stat("fun", 900))
    
    # FUN
    if (int(read_db_value("fun")) <= 3):
        timers.check_timer("TIMER_MOOD_FUN", timers.timer_decrease_stat("mood", 900))
    
    if (int(read_db_value("fun")) > 9):
        timers.check_timer("TIMER_SHOWER_FUN", timers.timer_decrease_stat("shower", 900))
        
    if (int(read_db_value("fun")) > 10):
        timers.check_timer("TIMER_BOOK_FUN", timers.timer_decrease_stat("book", 900))
    
    # SHOWER
    if (int(read_db_value("shower")) <= 3):
        timers.check_timer("TIMER_HEALTH_SHOWER", timers.timer_decrease_stat("health", 900))
    
    # SLEEP
    if (int(read_db_value("sleep")) <= 3):
        timers.check_timer("TIMER_HEALTH_SLEEP", timers.timer_decrease_stat("health", 900))
        timers.check_timer("TIMER_HEALTH_MOOD", timers.timer_decrease_stat("mood", 900))

    # HEALTH
    if (int(read_db_value("health")) <= 3):
        timers.check_timer("TIMER_HEALTH_HEALTH", timers.timer_decrease_stat("health", 900))
    
    gc.collect()
    
#0,25 -> 0, 78

#grow()
  
#tft.clear(tft.WHITE)
#tft.image(13, 20, "images/newborn/normal.jpg")
#utime.sleep(10)




