from time import sleep
from random import randint
import pibrella

def red_press(pin):
    if redLight == True:
        print("You Won")
        pibrella.buzzer.buzz(1000)
        sleep(1)
        pibrella.buzzer.off()
    else:
        pass

while True:
    colour = randint(1,3)
    redLight = False
    if colour == 1:
        redLight = True
        pibrella.light.red.on()
        pibrella.button.pressed(red_press)
        sleep(0.3)
        pibrella.button.pressed(red_press)
        pibrella.light.off()
        
        
    elif colour == 2:
        pibrella.light.amber.on()
        sleep(0.3)
        pibrella.light.off()

    elif colour == 3:
        pibrella.light.green.on()
        sleep(0.3)
        pibrella.light.off()
        
pibrella.button.pressed(red_press)

pibrella.pause()
