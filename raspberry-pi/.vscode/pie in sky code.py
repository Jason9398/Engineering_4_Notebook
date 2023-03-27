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

#Acceloromiter set up
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
#Altimiter set up                                                                                              
# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Initialize the MPL3115A2.
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
# Alternatively you can specify a different I2C address for the device:
# sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

# You can configure the pressure at sealevel to get better altitude estimates.[]
# This value has to be looked up from your local weather forecast or meteorological
# reports.  It will change day by day and even hour by hour with weather
# changes.  Remember altitude estimation from barometric pressure is not exact!
# Set this to a value in pascals:
sensor.sealevel_pressure = 102250

# Main loop to read the sensor values and print them every second.
while True:
    pressure = sensor.pressure
    print("Pressure: {0:0.3f} pascals".format(pressure))
    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude))
    temperature = sensor.temperature
    print("Temperature: {0:0.3f} degrees Celsius".format(temperature))
    time.sleep(1.0)
   
while True:
    print(mpu.acceleration)
     
     
     
    



if button.value == True:
    for x in range(10,0,-1):
        print(x)
        led.value = True  
        time.sleep(1)
    led.value = False


      #print(butten.value)P
   