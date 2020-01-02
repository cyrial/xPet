from display_manager import tft
import utime
from sound_manager import play_sound

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 128

GROUND = 103
CHARACTER_WIDTH = 48
CHARACTER_HEIGHT = 48

MAX_WIDTH = SCREEN_WIDTH-CHARACTER_WIDTH
MAX_HEIGHT = 25

STEP = 5

CH_X = 5
CH_Y = GROUND - CHARACTER_HEIGHT

POO_ANIM_STEP = 1

def hatching(count):
  tft.clear()
  
  for x in range(0, count):
    tft.image(0, 0, "images/hatch/1-1.jpg")
    utime.sleep(0.5)
    tft.image(0, 0, "images/hatch/1-2.jpg")
    utime.sleep(0.5)
    
  tft.image(0,0, "images/hatch/1-3.jpg")  
  play_sound('hatched')
  tft.image(0,0, "images/hatch/1-4.jpg")
  utime.sleep(2)
  tft.clear(tft.WHITE)

def reset_center():
  tft.rect(0, 25, 160, 53, tft.WHITE, tft.WHITE)
 
def move_right(character_image):
  global CH_X, CH_Y
  
  CH_X += STEP
  if CH_X < MAX_WIDTH:
    tft.image(CH_X, CH_Y, "images/newborn/" + character_image + ".jpg")
    tft.rect(CH_X-STEP, CH_Y, STEP, CHARACTER_HEIGHT, tft.WHITE, tft.WHITE)
  
def animate_walk():
  global CH_X, CH_Y
  
  move_right("normal")
  
def animate_poo(step):
  global POO_ANIM_STEP
  tft.image(SCREEN_WIDTH-24, GROUND-24, "images/poo/" + str(step) + ".jpg")
  
  if POO_ANIM_STEP < 3:
    POO_ANIM_STEP += 1
  else:
    POO_ANIM_STEP = 1
  
