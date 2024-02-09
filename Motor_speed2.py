import RPi.GPIO as GPIO
import time

sensor_pin = 17
GPIO.set_mode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN,
           pull_up_down=GPIO.PUD_UP)

rpm=0
previous_time=time.time()

def calculate_speed(channel):
global rpm, previous_time
rpm += 1
current_time=time.time()
elapsed_time=current_time-previous_time

if elapsed_time >= 1:
    motor_speedrpm/(elapsed_time/60)
    print(f"Motor Speed: {motor_speed} RPM")
    rpm=0
    previous_time = current_time
    GPIO.add_event-detect(sensor_pin,
                         GPIO.FALLING,
                          callback = calculate_speed,
                           bouncetime = 20)
    
    try:
        while True:

time.speed(1)

except KeyboardInterrupt:
GPIO.cleanup()