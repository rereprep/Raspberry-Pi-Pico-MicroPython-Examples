#blink onboard LED for 1 second via button#
from machine import Pin
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
button = machine.Pin(14, Pin.IN, Pin.PULL_DOWN)
while True:
  if button.value():
    led_onboard.toggle()
    utime.sleep(1)
