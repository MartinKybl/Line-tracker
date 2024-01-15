from time import ticks_ms, sleep_ms
from machine import Pin 

tsleep = 100

inp = Pin(5, Pin.IN,Pin.PULL_DOWN)
while 1:
    if inp.value() == 1:
        print("bilej")
        sleep_ms(tsleep)
        
    if inp.value() == 0:
        print("cernej")
        sleep_ms(tsleep)