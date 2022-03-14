#blink onboard LED for 1 second#        

from machine import Pin
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
  led_onboard.toggle()
  utime.sleep(1)
