from display_manager import tft, init_display
import buttons
import utime

stats = ("health", "drink", "food", "sweets", "fun", "book", "wash", "sleep", "reset")
stats_values = (10, 10, 10, 10, 10, 10, 10, 10)
current_stat = 0

def generate_images():
  tft.image(13, 20, "images/menu/health.jpg")
  tft.image(49, 20, "images/menu/drink.jpg")
  tft.image(85, 20, "images/menu/food.jpg")
  tft.image(121, 20, "images/menu/sweets.jpg")
  tft.image(13, 69, "images/menu/fun.jpg")
  tft.image(49, 69, "images/menu/book.jpg")
  tft.image(85, 69, "images/menu/wash.jpg")
  tft.image(121, 69, "images/menu/sleep.jpg")
  
def highlight_stat(element):
  global current_stat
  reset_highlight()
  
  if element == "health": tft.rect(8, 17, 36, 46, tft.RED)
  elif element == "drink": tft.rect(44, 17, 36, 46, tft.RED)
  elif element == "food": tft.rect(80, 17, 36, 46, tft.RED)
  elif element == "sweets": tft.rect(116, 17, 36, 46, tft.RED)
  elif element == "fun": tft.rect(8, 66, 36, 46, tft.RED)
  elif element == "book": tft.rect(44, 66, 36, 46, tft.RED)
  elif element == "wash": tft.rect(80, 66, 36, 46, tft.RED)
  elif element == "sleep": tft.rect(116, 66, 36, 46, tft.RED)
  elif element == "reset": 
    current_stat = 0
    tft.rect(8, 17, 36, 46, tft.RED)
    
def generate_stats_stripe(element, statistics):
  color = tft.RED if statistics <= 20 else tft.GREEN
  stripe_size = int(statistics / 2)

  if element == "health":
    tft.rect(10, 50, 32, 10, tft.BLACK)
    if stripe_size > 0: tft.rect(11, 51, stripe_size, 8, color, color) 
      
  if element == "drink":
    tft.rect(46, 50, 32, 10, tft.BLACK)
    if stripe_size > 0: tft.rect(47, 51, stripe_size, 8, color, color) 
      
  if element == "food":
    tft.rect(82, 50, 32, 10, tft.BLACK)
    if stripe_size > 0: tft.rect(83, 51, stripe_size, 8, color, color)
    
  if element == "sweets":
    tft.rect(118, 50, 32, 10, tft.BLACK)
    if stripe_size > 0: tft.rect(119, 51, stripe_size, 8, color, color)

  if element == "fun":
    tft.rect(10, 99, 32, 10, tft.BLACK)
    if stripe_size > 0: tft.rect(11, 100, stripe_size, 8, color, color)
    
  if element == "book":
    tft.rect(46, 99, 32, 10, tft.BLACK)
    if stripe_size > 0: tft.rect(47, 100, stripe_size, 8, color, color)
 
  if element == "wash":
    tft.rect(82, 99, 32, 10, tft.BLACK)
    if stripe_size > 0: tft.rect(83, 100, stripe_size, 8, color, color) 
 
  if element == "sleep":
    tft.rect(118, 99, 32, 10, tft.BLACK)
    if stripe_size > 0: tft.rect(119, 100, stripe_size, 8, color, color)

def reset_highlight():
  tft.rect(8, 17, 36, 46, tft.WHITE)
  tft.rect(44, 17, 36, 46, tft.WHITE)
  tft.rect(80, 17, 36, 46, tft.WHITE)
  tft.rect(116, 17, 36, 46, tft.WHITE)
  tft.rect(8, 66, 36, 46, tft.WHITE)
  tft.rect(44, 66, 36, 46, tft.WHITE)
  tft.rect(80, 66, 36, 46, tft.WHITE)
  tft.rect(116, 66, 36, 46, tft.WHITE)

def show_stats_screen():
  tft.clear(tft.WHITE)
  global current_stat
  generate_images()
  highlight_stat(stats[current_stat])
  generate_stats_stripe("health", 10)
  generate_stats_stripe("drink", 20)
  generate_stats_stripe("food", 30)
  generate_stats_stripe("sweets", 40)
  generate_stats_stripe("fun", 50)
  generate_stats_stripe("book", 60)
  generate_stats_stripe("wash", 20)
  generate_stats_stripe("sleep", 10)
  
  while not buttons.exit_pressed:
    if buttons.select_pressed:
      current_stat += 1
      highlight_stat(stats[current_stat])
    utime.sleep(0.02)
    ## WHILE CLICK 3rd button, CURRENT_SCREEN = main 



