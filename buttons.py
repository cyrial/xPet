from machine import Pin, disable_irq, enable_irq, Timer
from sound_manager import play_sound
import utime
import gc
import sys

SELECT_PIN = 21
ENTER_PIN = 18
EXIT_PIN = 19

timer = Timer(0)
counter = 0
select_pressed = 0
enter_pressed = 0
exit_pressed = 0

def disable_timer_select(timer):
  global select_pressed
  select_pressed = 0
  timer.deinit()
  
def disable_timer_enter(timer):
  global enter_pressed
  enter_pressed = 0
  timer.deinit()

def disable_timer_exit(timer):
  global exit_pressed
  exit_pressed = 0
  timer.deinit()
  
def button_select(pin):
  start_time = utime.time()
  global select_pressed

  if not select_pressed:
    timer.init(period=150, mode=Timer.PERIODIC, callback=disable_timer_select)
    play_sound('select')
    select_pressed = 1
   
def button_enter(pin):
  start_time = utime.time()
  global enter_pressed

  if not enter_pressed:
    timer.init(period=150, mode=Timer.PERIODIC, callback=disable_timer_enter)
    play_sound('enter')
    enter_pressed = 1
    
def button_exit(pin):
  start_time = utime.time()
  global exit_pressed

  if not exit_pressed:
    timer.init(period=150, mode=Timer.PERIODIC, callback=disable_timer_exit)
    play_sound('enter')
    exit_pressed = 1
    
select_handler = Pin(SELECT_PIN, Pin.IN, Pin.PULL_UP, trigger=Pin.IRQ_RISING, handler=button_select)
enter_handler = Pin(ENTER_PIN, Pin.IN, Pin.PULL_UP, trigger=Pin.IRQ_FALLING, handler=button_enter)
exit_handler = Pin(EXIT_PIN, Pin.IN, Pin.PULL_UP, trigger=Pin.IRQ_FALLING, handler=button_exit)







