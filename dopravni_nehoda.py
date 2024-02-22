from machine import Pin, time_pulse_us
import time
#import math

Trig = Pin(0, Pin.OUT)
Echo = Pin(1, Pin.IN, Pin.PULL_DOWN)

#t=20000
#v=331*math.sqrt(1+t/273.15)
Stop = 69
Jarda_jede = True
while True:
    Trig.value(0)
    time.sleep_us(5)
    Trig.value(1)
    time.sleep_us(10)
    Trig.value(0)
    Bouracka = time_pulse_us(Echo, 1, 30000)
    if Bouracka < Stop:
        Jarda_jede = False
    else:
        Jarda_jede = True