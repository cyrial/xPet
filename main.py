import display
import buttons
import gc
import time
tft = display.TFT()

def init_display():
  global tft
  tft.init(tft.ST7735R, speed=10000000, spihost=tft.HSPI, mosi=13, miso=12, clk=14, cs=15, dc=27, rst_pin=26, hastouch=False, bgr=False, width=129, height=161, rot=tft.LANDSCAPE)
  tft.clear(tft.WHITE)
  
init_display()

while True:
  tft.image(13, 20, "images/health.jpg")
  tft.rect(11, 50, 30, 10, tft.BLACK, tft.GREEN)
  tft.image(49, 20, "images/drink.jpg")
  tft.rect(47, 50, 30, 10, tft.BLACK, tft.GREEN)
  tft.image(85, 20, "images/food.jpg")
  tft.rect(83, 50, 30, 10, tft.BLACK, tft.GREEN)
  tft.image(121, 20, "images/sweets.jpg")
  tft.rect(119, 50, 30, 10, tft.BLACK, tft.GREEN)
  
  tft.image(13, 69, "images/fun.jpg")
  tft.rect(11, 99, 30, 10, tft.BLACK, tft.GREEN)
  tft.image(49, 69, "images/book.jpg")
  tft.rect(47, 99, 30, 10, tft.BLACK, tft.GREEN)
  tft.image(85, 69, "images/wash.jpg")
  tft.rect(83, 99, 30, 10, tft.BLACK, tft.GREEN)
  tft.image(121, 69, "images/sleep.jpg")
  tft.rect(119, 99, 30, 10, tft.BLACK, tft.GREEN)
  
  #
  #tft.fillrect((50,45), (90,20), TFT.RED)




