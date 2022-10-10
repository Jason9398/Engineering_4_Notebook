import time 
import board
import digitalio 
import adafruit_mpu6050 
import busio
sda_pin =board.GP16
scl_pin =board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led = digitalio.DigitalInOut(board.GP13) 
led.direction = digitalio.Direction.OUTPUT
while True:
    print(mpu.acceleration)
    time.sleep(1)
    if mpu.acceleration[0] > 9:
        #do stuff 
        led.value = True 
        time.sleep(1) 
        led.value = False
    if mpu.acceleration[0] < -9:
        #do stuff 
        led.value = True 
        time.sleep(.5) 
        led.value = False
    if mpu.acceleration[1] > 9:
        #do stuff 
        led.value = True 
        time.sleep(.5) 
        led.value = False
    if mpu.acceleration[1] < -9:
        #do stuff 
        led.value = True 
        time.sleep(.5) 
        led.value = False
