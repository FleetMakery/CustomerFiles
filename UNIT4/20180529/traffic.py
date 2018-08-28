from time import sleep
import pibrella

def button_input(pin):
    pibrella.light.on()
    pibrella.buzzer.buzz(1000)
    sleep(0.1)
    pibrella.buzzer.off()
    pibrella.light.off()
    
pibrella.light.red.on()
sleep(1)
pibrella.light.red.off()
pibrella.light.amber.on()
sleep(1)
pibrella.light.amber.off()
pibrella.light.green.on()
sleep(1)
pibrella.light.green.off()
sleep(1.5)
pibrella.light.on()
pibrella.buzzer.buzz(1000)
sleep(1)
pibrella.buzzer.off()
pibrella.light.off()

pibrella.button.pressed(button_input)

pibrella.pause()
