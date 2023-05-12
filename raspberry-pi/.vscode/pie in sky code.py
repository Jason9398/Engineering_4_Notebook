import time 
import board
import digitalio 
import adafruit_mpu6050 
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
from adafruit_motor import servo
import pwmio
import  adafruit_mpl3115a2
import displayio
displayio.release_displays()
#set up i2c
sda_pin =board.GP16
scl_pin =board.GP17
i2c = busio.I2C(scl_pin, sda_pin)

#Acceloromiter set up
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
led = digitalio.DigitalInOut(board.GP13) 
led.direction = digitalio.Direction.OUTPUT
ledgreen = digitalio.DigitalInOut(board.GP18) 
ledgreen.direction = digitalio.Direction.OUTPUT

#Altimiter set up                                                                                              
# Create sensor object, communicating over the board's default I2C bus
 # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Initialize the MPL3115A2.
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
# Alternatively you can specify a different I2C address for the device:
# sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

# You can configure the pressure at sealevel to get better altitude estimates.[]
# This value has to be looked up from your local weather forecast or meteorological
# reports.  It will change day by day and even hour by hour with weather
# changes.  Remember altitude estimation from barometric pressure is not exact!
# Set this to a value in pascals:
sensor.sealevel_pressure = 102250
pwm_servo = pwmio.PWMOut(board.GP5, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0 
# Main loop to read the sensor values and print them every second.
altitude = 0
while True:
    lastalt = altitude
    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude)) 
    print(mpu.acceleration)
    if altitude+1 < lastalt:
        servo1.angle =90 