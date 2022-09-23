import time
import board 
import digitalio 
led = digitalio.DigitalInOut(board.GP13) 
led.direction = digitalio.Direction.OUTPUT
ledgreen = digitalio.DigitalInOut(board.GP18) 
ledgreen.direction = digitalio.Direction.OUTPUT 
for x in range(10,0,-1):
  print(x)
led.value = True  
time.sleep(1)
led.value = False

print("lift off")
ledgreen.value = True  
time.sleep(1)
ledgreen.value = False
butten,direction = digitalio.Direction.OUTPUT 
butten.pull = digitalio.Pull.DOWN
#print(butten.value)