from display_manager import tft
from sound_manager import play_sound_thread
import animations
import config
import _thread
import timers

POO_WIDTH = 24
POO_HEIGHT = 24
POO = 0

def generate_poo():
  global POO
  
  # Generate POO only when character is on the left side of the screen
  if animations.CH_X < config.MAX_WIDTH - POO_WIDTH:
    POO = 1
    config.MAX_WIDTH -= POO_WIDTH
    draw_poo(animations.POO_ANIM_STEP)
    play_sound_thread("poo")
    
  else:
    _thread.start_new_thread("TIMER_FOOD_RECHECK", timers.timer_poop_recheck, ())
    
def clean_poo():
    global POO
    
    POO = 0
    config.MAX_WIDTH += POO_WIDTH
    
    tft.rect(config.SCREEN_WIDTH - POO_WIDTH, config.GROUND - POO_HEIGHT, POO_WIDTH, POO_HEIGHT, tft.WHITE, tft.WHITE)
    play_sound_thread("success")
    timers.check_timer("TIMER_POOP", timers.timer_poop)

  
def draw_poo(step):
    tft.image(config.SCREEN_WIDTH - POO_WIDTH, config.GROUND - POO_HEIGHT, "images/poo/" + str(step) + ".jpg")
    