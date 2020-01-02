from sound_manager import play_sound
import animations

POO = 0

def generate_poo():
  global POO
  POO = 1
  animations.MAX_WIDTH -= 24
  play_sound("alert")
  
def clean_poo():
  global POO
  POO = 0
  animations.MAX_WIDTH += 24

