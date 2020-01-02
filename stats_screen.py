from display_manager import tft, init_display
import utime
from database import read_db_value

stats = ("health", "drink", "food", "sweets", "fun", "book", "wash", "sleep", "reset")
CURRENT_STAT = -1

def generate_images():
  tft.image(0, 0, "images/actions.jpg")

  
def highlight_stat(element):
  global CURRENT_STAT
  reset_highlight(0)
  
  if element == "health": tft.rect(0, 22, 36, 2, tft.RED, tft.RED)
  elif element == "drink": tft.rect(40, 22, 36, 2, tft.RED)
  elif element == "food": tft.rect(80, 22, 36, 2, tft.RED)
  elif element == "sweets": tft.rect(120, 22, 36, 2, tft.RED)
  elif element == "fun": tft.rect(0, 126, 36, 2, tft.RED)
  elif element == "book": tft.rect(40, 126, 36, 2, tft.RED)
  elif element == "wash": tft.rect(80, 126, 36, 2, tft.RED)
  elif element == "sleep": tft.rect(120, 126, 36, 2, tft.RED)
  elif element == "reset": 
    CURRENT_STAT = 0
    tft.rect(0, 22, 36, 2, tft.RED)
    
def generate_stats_stripe(element, statistics):
  color = tft.RED if statistics <= 3 else tft.GREEN
  stripe_size = statistics * 2
  stripe_width = 10
  stripe_height = 18
  
  if element == "health":
    tft.rect(25, 3, stripe_width, stripe_height, tft.BLACK)
    if stripe_size > 0: tft.rect(26, 4+(stripe_height-2-stripe_size), 8, stripe_size, color, color) 
      
  if element == "drink":
    tft.rect(66, 3, stripe_width, stripe_height, tft.BLACK)
    if stripe_size > 0: tft.rect(67, 4+(stripe_height-2-stripe_size), 8, stripe_size, color, color) 
      
  if element == "food":
    tft.rect(106, 3, stripe_width, stripe_height, tft.BLACK)
    if stripe_size > 0: tft.rect(107, 4+(stripe_height-2-stripe_size), 8, stripe_size, color, color)
    
  if element == "sweets":
    tft.rect(146, 3, stripe_width, stripe_height, tft.BLACK)
    if stripe_size > 0: tft.rect(147, 4+(stripe_height-2-stripe_size), 8, stripe_size, color, color)

  if element == "fun":
    tft.rect(25, 107, stripe_width, stripe_height, tft.BLACK)
    if stripe_size > 0: tft.rect(26, 108+(stripe_height-2-stripe_size), 8, stripe_size, color, color)
    
  if element == "book":
    tft.rect(66, 107, stripe_width, stripe_height, tft.BLACK)
    if stripe_size > 0: tft.rect(67, 108+(stripe_height-2-stripe_size), 8, stripe_size, color, color)
 
  if element == "wash":
    tft.rect(106, 107, stripe_width, stripe_height, tft.BLACK)
    if stripe_size > 0: tft.rect(107, 108+(stripe_height-2-stripe_size), 8, stripe_size, color, color) 
 
  if element == "sleep":
    tft.rect(146, 107, stripe_width, stripe_height, tft.BLACK)
    if stripe_size > 0: tft.rect(147, 108+(stripe_height-2-stripe_size), 8, stripe_size, color, color)

def reset_highlight(remove_highlight):
  global CURRENT_STAT
  tft.rect(0, 22, 36, 2, tft.WHITE)
  tft.rect(40, 22, 36, 2, tft.WHITE)
  tft.rect(80, 22, 36, 2, tft.WHITE)
  tft.rect(120, 22, 36, 2, tft.WHITE)
  tft.rect(0, 126, 36, 2, tft.WHITE)
  tft.rect(40, 126, 36, 2, tft.WHITE)
  tft.rect(80, 126, 36, 2, tft.WHITE)
  tft.rect(120, 126, 36, 2, tft.WHITE)
  if remove_highlight:
    CURRENT_STAT = -1
  
def show_stripe(stripe):
  if stripe == "all":
    generate_stats_stripe("health", int(read_db_value("health")))
    generate_stats_stripe("drink", int(read_db_value("drink")))
    generate_stats_stripe("food", int(read_db_value("food")))
    generate_stats_stripe("sweets", int(read_db_value("sweets")))
    generate_stats_stripe("fun", int(read_db_value("fun")))
    generate_stats_stripe("book", int(read_db_value("book")))
    generate_stats_stripe("wash", int(read_db_value("wash")))
    generate_stats_stripe("sleep", int(read_db_value("sleep")))
  else:
    generate_stats_stripe(stripe, int(read_db_value(stripe)))
  
def select_from_menu():
  global CURRENT_STAT  
    
  CURRENT_STAT += 1
  highlight_stat(stats[CURRENT_STAT])



