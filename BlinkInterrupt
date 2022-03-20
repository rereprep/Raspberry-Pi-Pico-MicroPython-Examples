#same as Blink.py but this time we are using interrupts instead of sleep function. Blink.py dosyası ile aynı ama bu sefer uyku fonksiyonu yerine interrupt, kesme kullanıyoruz.
#blink onboard LED for 1 second. Dahili LED'i saniyede bir defa aç-kapat.#        
from machine import Pin, Timer

led_onboard = machine.Pin(25, machine.Pin.OUT) #LED onboard. Dahili LED

def tick(timer):
  led_onboard.toggle()

Timer().init(freq=1, mode=Timer.PERIODIC, callback=tick) #Call the tick function periodically at 1 hz (once per second) intervals. Tick fonksiyonunu 1 hz (saniyede 1 defa) aralıkla çağır.
