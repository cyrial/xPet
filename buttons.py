from machine import Pin
import utime

counter = 0
select_pressed = False
enter_pressed = False

def button_select(pin):
  global select_pressed
  global counter
  
  
  if not select_pressed:
    select_handler.irqvalue(trigger=0)
    select_pressed = True
    utime.sleep_ms(250)
    select_pressed = False
    print("select clicked" + str(counter))
    counter += 1

def button_enter(pin):
  print("enter clicked")
  
select_handler = Pin(32, Pin.IN, Pin.PULL_UP, trigger=Pin.IRQ_RISING, handler=button_select)
#enter_handler = Pin(32, Pin.IN, Pin.PULL_UP, trigger=Pin.IRQ_FALLING, handler=button_enter)

# EXIT IF BUTTON PRESSED DURING START
if select_handler.value() == 0:
  tft.clear(tft.BLACK)
  tft.text(10, 10, "Connection mode...", tft.RED)
  sys.exit()



