import time
import board 
import digitalio 
led = digitalio.DigitalInOut(board.GP13) 
led.direction = digitalio.Direction.OUTPUT
ledgreen = digitalio.DigitalInOut(board.GP18) 
ledgreen.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16)  
button.direction = digitalio.Direction.INPUT
button.pull=digitalio.Pull.DOWN


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