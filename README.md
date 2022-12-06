# Final-Project
@samroedl Final Project Memory Game

# DESCRIPTION OF GAME:

For the final project, i made the attempt at creating a memory game where there were two levels of varying difficulty where you had to initially press the button to start the game. Then follows is a prompt on the screen to prepare the player for the game and then they will be presented with the first level where they are given a series of four lights they have to memorize. They then will have to answer the prompt on the screen and if they are successful they will move on to the next level that moves much faster and adds an additiponl light. If they are successufl they will be prompted that tey have completed the game.

# How to set-up the pi for the game:

1. You will put the breadboard in front of you and ensure you have he following components in front of you:
      a. (4) Random LED Lights
      b. (4) 330 ohm Resistors
      c. (1) RasberryPi
      d. (10) Male to Female Wires
      e. (1) Breadboard
      f. (1) HDMI Cable
      g. (1) Mouse
      h. (1) Keyboard
      i. (1) Monitor
      j. (1) Button
     ![WIN_20221206_10_49_16_Pro](https://user-images.githubusercontent.com/115032842/205987854-99aee3f0-155a-4cdd-9258-9ab3a041d2c6.jpg)

 2. You will then proceed to connect all of the Leds in the same fashion with the longer end(anode) facing up and the shorter end(cathode) facing down as shown in the picture below.
 
 3. Then you will connect the male end of the wire to the port next to the anode to give the LED power from the Pi and then connect the female end of the wire to the Pi where there is an open GPIO port available. You will repeat these steps for the other three LEDs.
 
 4. We will then ensure that the LEDs are grounded so we will take the male end of the wire and count two ports down from the positive connection and insert there. You will then find a ground port open on the Pi and insert it there. You will repeat these steps for the other three LEDs.
 
 5. Next we want to make sure we monitor the amount of power being sent to the LEDs so we will place the resistors onto the breadboard. One end of the resistor will be in the port next to the positive wire and then the other end will be two ports down ensuring that it does not insert next to the next positive wire.

6. Next will be placing the button at the oppossite end of the breadboard. The orientation of the button down not matter neiter do the orientation of the wires. Place the button in a free two slots ensuring all of the connectors are securely fastened. Then connect a positive wire on one end of the button where it connects to the breadboard and to an open GPIO port on the Pi and a ground wire to the other connector on the button and then to a ground port on the Pi. No resistor is needed.

# Look at the picture below to ensure you set-up mathces mine.
![WIN_20221206_11_02_06_Pro](https://user-images.githubusercontent.com/115032842/205990588-f063fd5c-c6db-44d0-a59e-beb93c5bf704.jpg)
![WIN_20221206_11_02_36_Pro](https://user-images.githubusercontent.com/115032842/205990605-f4804c6b-c439-4f12-9434-2aef78a46f3b.jpg)
![WIN_20221206_11_02_51_Pro](https://user-images.githubusercontent.com/115032842/205990616-38fe88cf-f678-4ab1-818b-4414c75d5c24.jpg)

