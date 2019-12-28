import sys

### This is to allow us to exit to prompt quickly
from machine import Pin
goto_prompt = Pin(0, Pin.IN, Pin.PULL_UP)

# EXIT IF BUTTON PRESSED DURING START
if goto_prompt.value() == 0:
  print('getting into connection mode')
  sys.exit()

