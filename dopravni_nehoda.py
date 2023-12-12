from machine import Pin
import time

Trig = Pin(0, Pin.OUT)
Echo = Pin(1, Pin.IN, Pin.PULL_DOWN)

Diff=0
while True:
    tTrig=time.ticks_ms()
    if Echo.value()==0:
        Trig.on()
        time.sleep_ms(1000)
        print("vyslano")
    elif Echo.value()==1:
        Trig.off()
        tEcho=time.ticks_ms()
        Diff=time.ticks_diff(tEcho,tTrig)
        print("ceska posta")
        print(Diff)