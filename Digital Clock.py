from machine import Pin
import tm1637
from utime import sleep

display = tm1637.TM1637(clk=Pin(17), dio=Pin(16))

hour = 20

minute = 38

print('Hello')

while True:
    display.numbers(hour, minute)
    sleep(60)
    minute = minute +1
    display.numbers(hour, minute)
    if minute >= 60:
        minute = 00
        hour = hour+1
    if hour >= 24:
        hour = 00   
