from display_manager import tft

CHARACTER = 4

if CHARACTER == 1:
    WIDTH = 39
    HEIGHT = 47
elif CHARACTER == 2:
    WIDTH = 39
    HEIGHT = 47
elif CHARACTER == 3:
    WIDTH = 39
    HEIGHT = 47
elif CHARACTER == 4:
    WIDTH = 48
    HEIGHT = 45
    
    
def draw(CH_X, CH_Y):
    tft.image(CH_X, CH_Y, "images/character/" + str(CHARACTER) + "-1.jpg")