from display_manager import tft
import utime
from sound_manager import play_sound

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
  


