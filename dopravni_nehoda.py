from machine import Pin
import time
import math

Trig = Pin(0, Pin.OUT)
Echo = Pin(1, Pin.IN, Pin.PULL_DOWN)

t=20
v=331*math.sqrt(1+t/273.15)
Stop=5
Diff=200
while Diff>Stop:
    tTrig=time.ticks_us()
    if Echo.value()==0:
        Trig.on()
        time.sleep_us(20)
        print("vyslano")
    elif Echo.value()==1:
        Trig.off()
        tEcho=time.ticks_us()
        Diff=time.ticks_diff(tEcho,tTrig)
        print("ceska posta")
        print(Diff)