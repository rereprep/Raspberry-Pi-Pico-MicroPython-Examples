#Uses Potentiometer to control LED brightness. Potansiyometre kullanarak LED'in parlaklığını ayarlayan uygulamadır
#https://github.com/cogullu/RPPicoDS/blob/main/17_POT_LED.py değiştirilerek uygulanmıştır. Used as base code.
from machine import ADC, PWM, Pin     
from time import sleep

pot = ADC(27)                  # 27 is the pin for potentiometer. 27 potansiyometre pini
led1 = PWM(Pin(16))             # Pin for LED for brightness control. Parlaklık değeri ayarlanacak LED Deney setindeki RGB LED'in mavi rengi.
led1.freq(1000)                # LED's frequency. LED' in 1 sn. deki çalışma frekansı.
threshold = 500               # Without a threshold, LED will never go off as the potentiometer doesn't output 0. Eşik değeri kullanılmazsa potansiyometre asla 0 çıktısı vermeyeceğinden LED asla sönmez.
while True: 
     potValue = pot.read_u16()   # Read the value from potentiometer. Potansiyometreden gelen değeri okuduk.  
     if potValue<threshold:
         potValue = 0
     print(potValue) # You can test the threshold value for your setup via the console output. Çıktı ile en iyi eşik değerinizi test edebilirsiniz.
     led1.duty_u16(potValue)                        
     sleep(0.1) #Higher values will increase the delay between the setting the potentiometer and the LED brightness reaction. Daha yüksek değerler potansiyometre ayarlanması ile LED parlaklığının değişmesi arasındaki gecikmeyi arttıracaktır.
