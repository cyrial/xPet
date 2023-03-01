from display_manager import tft
import config

CHARACTER = 4

if CHARACTER == 1:
    SIZE = [39,47]
elif CHARACTER == 2:
    SIZE = [39,47]
elif CHARACTER == 3:
    SIZE = [39,47]
elif CHARACTER == 4:
    SIZE = [48,45]
    
#X = 0
#Y = config.GROUND - HEIGHT

def draw(CH_X, CH_Y):
    tft.image(CH_X, CH_Y, "images/character/" + str(CHARACTER) + "-1.jpg")