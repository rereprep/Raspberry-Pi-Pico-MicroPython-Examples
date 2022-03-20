#Same as BlinkButton.py but this time interrupts are used to control onboard LED via button. Blinkbutton.py ile aynı ama bu sefer dahili LED'i buton ile kontrol etmek için kesme kullanıldı.
from machine import Pin, Timer
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT) #LED onboard. Dahili LED
button = machine.Pin(5, Pin.IN, Pin.PULL_DOWN) #Button is connected on Pin 5. Buton Pin 5'e bağlandı.

def handle_interrupt(Pin):           #define interrupt handling function. Kesme fonksiyonunu tanımla
  led_onboard.toggle()
  utime.sleep(1) #Sleep for 1 seconds, if it's too short, multiple button presses will be registered for one button press. 1 saniye uyu, eğer süre çok kısa olursa, butona basma çoklu algılanabilir.

button.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
