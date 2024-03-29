from display_manager import tft
from sound_manager import play_sound
import utime
import random
import config
import character
import objects

ACTION_X = 35
STOP_IDLE = 0

# WE NEED TO DEFINE TOP LEFT POSITION AND BOTTOM RIGHT POSITION SO WE CAN CALCULATE BOUNDARIES
#    x,y,width,height

# CURRENT LEFT
CH_X = 45
# CURRENT TOP
CH_Y = config.GROUND - character.SIZE[1]

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
    if objects.POO == 1:
        tft.rect(0, config.MAX_HEIGHT, config.SCREEN_SIZE[0] - objects.POO_SIZE[0], config.GROUND - config.MAX_HEIGHT, tft.WHITE, tft.WHITE)
    else:
        tft.rect(0, config.MAX_HEIGHT, config.SCREEN_SIZE[0], config.GROUND - config.MAX_HEIGHT, tft.WHITE, tft.WHITE)
        
def idle():
    global STOP_IDLE
    
    number = random.randint(0,1)
    
    if number == 0:
        for x in range (random.randint(6,13)):
            if STOP_IDLE == 0:
                move_right()
            
                if objects.POO == 1:
                    animate_poo(POO_ANIM_STEP)
    else:
        for x in range (random.randint(6,13)):
            if STOP_IDLE == 0:
                move_left()
            
                if objects.POO == 1:
                    animate_poo(POO_ANIM_STEP)
            
def move_right():
    global CH_X, CH_Y
    
    if (CH_X + config.STEP) < config.MAX_WIDTH:
        CH_X += config.STEP
        character.draw(CH_X, CH_Y)
        # Put white background after chracter move
        tft.rect(CH_X - config.STEP, CH_Y, config.STEP, character.SIZE[1], tft.WHITE, tft.WHITE)
    
    utime.sleep(config.ANIMATION_TIME)

def move_left():
    global CH_X, CH_Y

    if (CH_X - config.STEP) > config.MIN_WIDTH:
        CH_X -= config.STEP
        character.draw(CH_X,CH_Y)
        tft.rect(CH_X + character.SIZE[0], CH_Y, config.STEP, character.SIZE[1], tft.WHITE, tft.WHITE)

    utime.sleep(config.ANIMATION_TIME)
    
def perform_action_start():
    global STOP_IDLE
    
    # TODO check if our stat is not at it's max so we won't fire this animation but instead we will fire no no animation
    STOP_IDLE = 1
    reset_center()
    character.draw(ACTION_X, CH_Y)
    
def perform_action_end():
    global STOP_IDLE
    
    reset_center()
    character.draw(CH_X,CH_Y)
    STOP_IDLE = 0
    
def eating():

    perform_action_start()

    for x in range(0,4):
        # ADD SOUND
        objects.draw_food(x+1)
        utime.sleep(1)
    
    perform_action_end()
    
def eating_sweets():

    perform_action_start()

    for x in range(0,4):
        # ADD SOUND
        objects.draw_cake(x+1)
        utime.sleep(1)
    
    perform_action_end()
    
def drinking():
    
    perform_action_start()
    
    for x in range(0,4):
        # ADD SOUND
        objects.draw_drink(x+1)
        utime.sleep(1)
        
    perform_action_end()

def injection():
    
    perform_action_start()
    
    for x in range(0,6):
        #ADD SOUND
        objects.draw_injection(x+1)
        utime.sleep(0.6)
    
    perform_action_end()

def reading():
    
    perform_action_start()
    
    for x in range(0,5):
        #ADD SOUND
        objects.draw_book(x+1)
        utime.sleep(0.7)
    
    perform_action_end()

def sleeping():
    
    perform_action_start()
    
    while True:
        for x in range(0,2):
            #ADD SOUND
            objects.draw_sleep(x+1)
            utime.sleep(2)
    
    perform_action_end()
    
def shower():
    
    perform_action_start()
    
    for x in range(0,2):
        #ADD SOUND
        for y in range(0,3):
            objects.draw_shower(y+1)
            utime.sleep(0.5)
    
    perform_action_end()
    
def fun():
    ball_height = config.MAX_HEIGHT + 6
    
    perform_action_start()
    
    for x in range(0,12):
        # ADD SOUND
        for y in range(0,2):
            objects.draw_ball(y+1, ball_height, 2)
            ball_height += 2
            utime.sleep(0.07)
            

    perform_action_end()
    
def animate_poo(step):
  global POO_ANIM_STEP
  
  objects.draw_poo(POO_ANIM_STEP)
  
  if POO_ANIM_STEP < 3:
    POO_ANIM_STEP += 1
  else:
    POO_ANIM_STEP = 1
#


