from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin, disable_irq, enable_irq
import sys
import utime
import math

import images
import bitmaps

def split(word): 
  return [char for char in word] 
  
# SCREEN INIT
spi = SPI(1, baudrate=32000000, polarity=0, bits=8, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
#spi = SPI(2, baudrate=rate, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(22))
tft=TFT(spi,16,17,18)
tft.initb2()
tft.rgb(True)
tft.fill(TFT.WHITE)
tft.rotation(3)
screen_width = 120
screen_height = 160

button_select_pressed = False
button_enter_pressed = False
button_select = Pin(27, Pin.IN, Pin.PULL_UP)

# CHECK IF BUTTON IS PRESSED DURING START SO WE CAN GO TO CONNECT MODE FOR UPYCRAFT
if button_select.value() == 0:
  tft.text((20, screen_width/2), "Connection mode", TFT.RED, sysfont, 1, nowrap=True)
  sys.exit()
  
def button_select_callback(pin):
  global button_select_pressed
  button_select_pressed = True
  
button_select = Pin(27, Pin.IN, Pin.PULL_UP)
button_select.irq(trigger=Pin.IRQ_FALLING, handler=button_select_callback)

def paint(ascii, top_space, left_space):
  paint = ascii.splitlines()
  lines = len(paint)
  
  for line in range(0, lines):
    line_len = len(split(paint[line]))
      
    for char in range(0, line_len):
      if paint[line][char] == "#":
        tft.pixel((top_space+char, left_space+line), TFT.BLACK)
      if paint[line][char] == "@":
        tft.pixel((top_space+char, left_space+line), TFT.RED)
      if paint[line][char] == "$":
        tft.pixel((top_space+char, left_space+line), TFT.WHITE)
      if paint[line][char] == "G":
        tft.pixel((top_space+char, left_space+line), TFT.GREEN)
      if paint[line][char] == "Y":
        tft.pixel((top_space+char, left_space+line), TFT.YELLOW)
      
  #tft.fill(TFT.BLACK)
 
while True:
  if button_select_pressed:
    utime.sleep_ms(250)    
    button_select_pressed = False
    
  
  #paint(images.health, 12, 12)
  #paint(images.food, 10, 46)
  bitmaps.add_sprite("images/health.bmp", 12, 12, tft)
  bitmaps.add_sprite("images/food.bmp", 10, 46, tft)

  tft.fillrect((50,12), (90,20), TFT.RED)
  tft.fillrect((50,45), (90,20), TFT.RED)
  
  utime.sleep_ms(1500)
  print('after sleep')

