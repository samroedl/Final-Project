!/bin/python

##This series of code imports all of the tools and files to use the functions for the LED and the Pi.
from gpiozero import LED
from time import sleep
from gpiozero import LED, Button
from signal import pause

##Name of the LEDs and button
blue = LED(14)
red = LED(15)
clear = LED(23)
green = LED(25) 
button = Button(26)

##This is the name of the list needed to select from when randomly choosing for the game.
leds2 = [green, blue, green, clear, red]
leds3 = [green, r`ed, green, blue, red]

##This is the name of the function where the game prompts you with the questions and then gives the command to run the series of lights and then will ask the question of what lights were shown and thn will prompt you to go to the next game.
def run_game():
    print("Are You Ready")
    sleep(2)
    print(3)
    sleep(2)
    print(2)!/bin/python

from gpiozero import LED
from time import sleep

    sleep(2)
    print(1)
    
    for led in leds2:
         led.on()
         sleep(1)
         led.off()

    Question = input("Whats the Pattern Shown?")
    if Question == ("green blue green clear red"):
        print("Well Done")
    elif Question == ("green red blue green"):
        print("Try Again")

    print("Ready for the Next?")
    sleep(2)
    print(3)
    sleep(2)
    print(2)
    sleep(2)
    print(1)



    for led in leds3:
        led.on()
        sleep(0.5)
        led.off()

    Question = input("Whats the Pattern Shown?")
    if Question == ("green red green blue red"):
        print("Well Done")
    elif Question == ("green red blue green"):
        print("Try Again")




print("                                                                                                                                                                                                                                                >
print("Welcome to the Memory Game")
print("                                                                                                                                                                                                                                                >
sleep(2)
print("Press the Button the Start")
print("                                                                                                                                                                                                                                                >
button.wait_for_press(timeout=None)
run_game()
