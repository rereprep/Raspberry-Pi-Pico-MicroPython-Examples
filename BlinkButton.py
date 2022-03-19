#blink onboard LED for 1 second via button. Cihazdaki dahili LED'i buton ile 1 saniye boyunca aç-kapat.#
from machine import Pin
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT) #onboard LED is on Pin 25. Dahili LED Pin 25'tedir.
button = machine.Pin(5, Pin.IN, Pin.PULL_DOWN) #Button is connected on Pin 5. Buton Pin 5'e bağlandı.
while True:
  if button.value(): #If the button is pressed. Eğer butona basıldıysa
    led_onboard.toggle() #Toggle the onboard LED. Dahili LED'i aç-kapa yap.
    utime.sleep(1) #Sleep for 1 seconds, if it's too short, multiple button presses will be registered for one button press. 1 saniye uyu, eğer süre çok kısa olursa, butona basma çoklu algılanabilir.
