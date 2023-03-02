from display_manager import tft
from sound_manager import play_sound_thread
import animations
import config
import _thread
import timers
import character
import utime

POO = 0

POO_SIZE = [24,24]
FOOD_SIZE = [24,20]
DRINK_SIZE = [18,18]
BALL_SIZE = [23,23]

def generate_poo():
  global POO
  
  # Generate POO only when character is on the left side of the screen
  if animations.CH_X < config.MAX_WIDTH - POO_SIZE[0]:
    
    # IN CASE WE ARE ANIMATING ACTION, WAIT FOR IT'S COMPLETION
    if animations.STOP_IDLE == 1:
        utime.sleep(7)
    
    POO = 1
    config.MAX_WIDTH -= POO_SIZE[0]
    draw_poo(animations.POO_ANIM_STEP)
    #play_sound_thread("poo")
    
  else:
    _thread.start_new_thread("TIMER_FOOD_RECHECK", timers.timer_poop_recheck, ())
    
def clean_poo():
    global POO
    
    POO = 0
    config.MAX_WIDTH += POO_SIZE[0]
    
    tft.rect(config.SCREEN_SIZE[0] - POO_SIZE[0], config.GROUND - POO_SIZE[1], POO_SIZE[0], POO_SIZE[1], tft.WHITE, tft.WHITE)
    #play_sound_thread("success")
    timers.check_timer("TIMER_POOP", timers.timer_poop)

def draw_food(step):
    tft.image(animations.ACTION_X + character.SIZE[0] + 5, animations.CH_Y + int(character.SIZE[1] / 2) - int(FOOD_SIZE[1] / 2), "images/food/" + str(step) + ".jpg")

def draw_drink(step):
    tft.image(animations.ACTION_X + character.SIZE[0] + 5, animations.CH_Y + int(character.SIZE[1] / 2) - int(DRINK_SIZE[1] / 2), "images/drink/" + str(step) + ".jpg")
  
def draw_ball(step, height, clear_height):
    tft.rect(animations.ACTION_X + character.SIZE[0] + 5, height-clear_height, BALL_SIZE[0], clear_height, tft.WHITE, tft.WHITE)
    tft.image(animations.ACTION_X + character.SIZE[0] + 5, height, "images/fun/" + str(step) + ".jpg")
    
def draw_poo(step):
    tft.image(config.SCREEN_SIZE[0] - POO_SIZE[0], config.GROUND - POO_SIZE[1], "images/poo/" + str(step) + ".jpg")
    
