import time 
import board
import digitalio 
import adafruit_mpu6050 
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
displayio.release_displays()
#set up i2c
sda_pin =board.GP16
scl_pin =board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
#setting up display
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
led = digitalio.DigitalInOut(board.GP13) 
led.direction = digitalio.Direction.OUTPUT
ledgreen = digitalio.DigitalInOut(board.GP18) 
ledgreen.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16)  
button.direction = digitalio.Direction.INPUT
button.pull=digitalio.Pull.DOWN
mpu = adafruit_mpu6050.MPU6050(i2c)
led = digitalio.DigitalInOut(board.GP13) 
led.direction = digitalio.Direction.OUTPUT
while True:
    print(mpu.acceleration)




if button.value == True:
    for x in range(10,0,-1):
        print(x)
        led.value = True  
        time.sleep(1)
    led.value = False

    print("lift off")
    ledgreen.value = True  
    time.sleep(1)
    ledgreen.value = False

      #print(butten.value)P