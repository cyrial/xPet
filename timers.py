import utime
import database
import random
import config
import _thread
import objects
from stats_screen import decrease_stat

def wait(min_sec,max_sec):
    min_time = int(min_sec / config.GAME_SPEED)
    max_time = int(max_sec / config.GAME_SPEED)
    utime.sleep(random.randint(min_time, max_time))
    
def check_timer(thread_name, function):
    all_threads = _thread.list(False)
    all_thread_names = ""
    
    for thread in all_threads:
        all_thread_names += "," + thread[2]
        
    if thread_name not in all_thread_names:
        _thread.start_new_thread(thread_name, function, ())
        
def timer_food():
    
    # FOOD - 1 every 20-30min
    wait(1200,1800)
    decrease_stat("food")
    
def timer_poop():

    # POOP - every 1-2h
    wait(3600,7200)
    objects.generate_poo()
    decrease_stat("food")
    
# IF CHARACTER IS HOVERING POOP, MAKE CHECKS EVERY 3s
def timer_poop_recheck():
    
    wait(3 * config.GAME_SPEED,3 * config.GAME_SPEED)
    objects.generate_poo()