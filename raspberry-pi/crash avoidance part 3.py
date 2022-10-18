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
sda_pin =board.GP16
scl_pin =board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)


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
        # create the display group
    splash = displayio.Group()

    # add title block to display group
    title = "ANGULAR VELOCITY"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)    

    title = f"{mpu.acceleration[0]}"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=15)
    splash.append(text_area)    

    title =f"{mpu.acceleration[1]}"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=25)
    splash.append(text_area)    

    title =f"{mpu.acceleration[2]}"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=35)
    splash.append(text_area)    

    # you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
    # Don't forget to round the angular velocity values to three decimal places

    # send display group to screen
    display.show(splash)