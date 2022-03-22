# Example using PIO to blink an RGB LED trio and raise an IRQ. PIO ile RGB LED üçlüsü yapmak ve kesme uyarısı için örnek kod.
# Led will be on for 1 second and off for 1 second. Multiple output pins were chosen to handle RGB LED trio with one StateMachine.
# LED 1 saniye açık kalacak ve 1 saniye kapalı kalacak. Üçlü RGB LED'i tek StateMachine ile kullanmak için çoklu çıktı pini seçildi.

import time
from machine import Pin
import rp2


@rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW, rp2.PIO.OUT_LOW, rp2.PIO.OUT_LOW)) #We defined three output pins, base pin plus the two next pins. Üç çıktı pini tanımlandı, taban pini ve takip eden iki pin.
def blink():
    # 2000 Cycles Döngü (1 + 1 + 10 + 1 + (32 * (30 + 1)) + 1 + 1 + (32 * (30 + 1)) + 1)
    irq(rel(0))
    set(pins, 7) #Pin 16 = 1 (Blue, Mavi), Pin 17 = 2 (Green, Yesil), Pin 18 = 4 (Red, Kırmızı), add them to choose the RGB color you want. 7 is white. İstediğin renk için topla, 7 beyaz.
    set(y, 1)                   [9]
    label("delay_highy")
    set(x, 31)
    label("delay_high")
    nop()                       [29]
    jmp(x_dec, "delay_high")
    jmp(y_dec, "delay_highy")

    # 2000 Cycles Döngü (1 + 11 + 1 + (32 * (30 + 1)) + 1 + 1 + (32 * (30 + 1)) + 1) 
    set(pins, 0)
    set(y, 1)                   [10]
    label("delay_lowy")
    set(x, 31)
    label("delay_low")
    nop()                       [29]
    jmp(x_dec, "delay_low")
    jmp(y_dec, "delay_lowy")


# Create the StateMachine with the blink program with 2000 frequency. 2000 freakans ve blink programı ile StateMachine yarat.
sm = rp2.StateMachine(0, blink, freq=2000, set_base=Pin(16)) #Base is pin 16, but we got pin 16, 17 and 18 covered in the decorater function. Taban pin 16 ama tanım fonksiyonu ile pin 16, 17 ve 18'i kontrol edebiliriz.

# Set the IRQ handler to print the millisecond timestamp to see the exact cycle count. Kesme fonksiyonu ile kesin döngü sayısını görebiliriz.
sm.irq(lambda p: print(time.ticks_ms()))


# Start the StateMachine. StateMachine'i başlat.
sm.active(1)
