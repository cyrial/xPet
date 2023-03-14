<<<<<<< HEAD
import displaytft = display.TFT()def init_display():  global tft  tft.init(tft.ST7735R, speed=10000000, spihost=tft.HSPI, mosi=13, miso=12, clk=14, cs=15, dc=27, rst_pin=26, hastouch=False, bgr=False, width=128, height=160, rot=tft.LANDSCAPE, splash=False)  tft.clear(tft.WHITE)
=======
import displaytft = display.TFT()def init_display():  global tft  tft.init(tft.ST7735R, speed=10000000, spihost=tft.HSPI, mosi=13, miso=12, clk=14, cs=15, dc=27, rst_pin=26, hastouch=False, bgr=False, width=128, height=160, rot=tft.LANDSCAPE, splash=False)  tft.clear(tft.WHITE)  
>>>>>>> parent of 82c0ddc... fixing new lines
