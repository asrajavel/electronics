import tm1637
from machine import Pin
from utime import sleep

mydisplay = tm1637.TM1637(clk=Pin(26), dio=Pin(27))
buzzer = Pin(15, Pin.OUT)

def countdown_timer():
    total_time = 600  # 10 minutes in seconds
    remaining_time = total_time

    while remaining_time >= 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        mydisplay.numbers(minutes, seconds)

        sleep(1)  # Delay for 1 second (1000 milliseconds)
        remaining_time -= 1

def beepBuzzer():
    buzzer.value(1)
    sleep(0.2)
    buzzer.value(0)
    sleep(0.2)
    
def beepBuzzerShort():
    buzzer.value(1)
    sleep(0.05)
    buzzer.value(0)
    sleep(0.2)

def beepBuzzerThrice():
    for i in range(3):
        beepBuzzer()
        
def beepBuzzerThriceEvery10Seconds():
    for i in range(60):
        beepBuzzerThrice()
        sleep(10)

# Run the countdown timer
beepBuzzerShort()
countdown_timer()
mydisplay.show('done')
beepBuzzerThriceEvery10Seconds()



