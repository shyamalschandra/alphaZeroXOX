#!/usr/bin/env python

# Author: Shyamal S. Chandra
# Date: October 31, 2018

# Function: To log the joystick commands on the Xbox One Controller and display them and put
# them eventually into the protobuf or logfile for later use.

# STATE: NON_WORKING CODE!!!! IN ALPHA MODE!!!!

# Source adapted from: https://inputs.readthedocs.io/en/latest/user/quickstart.html

# Source adapted from: https://raw.githubusercontent.com/zeth/inputs/master/examples/gamepad_example.py

# TODO: Please check out the following for vibration:
# https://raw.githubusercontent.com/zeth/inputs/master/examples/vibrate_example.py

# TODO: Please check out the following for other options:
# https://www.pygame.org/docs/ref/joystick.html
# https://nerdparadise.com/programming/pygamejoystick
# Source adapted from: https://github.com/ryanvade/robotproject/blob/master/xboneControllerTest.py

from __future__ import get_gamepad
from __future__ import TextPrint

from inputs import devices
from inputs import get_gamepad
from time import sleep

import pygame

#for device in devices:
#	print(device)

def main():

	pygame.init()

	# Set the width and height of the screen [width,height]
	size = [500, 700]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("My Game")

	# Loop until the user clicks the close button.
	done = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	pygame.joystick.init()

	textPrint = TextPrint()

	while done == False:
	    # EVENT PROCESSING STEP
	    for event in pygame.event.get():  # User did something
	        if event.type == pygame.QUIT:  # If user clicked close
	            done = True  # Flag that we are done so we exit this loop

	        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
	        if event.type == pygame.JOYBUTTONDOWN:
	            print("Joystick button pressed.")
	        if event.type == pygame.JOYBUTTONUP:
	            print("Joystick button released.")
	        if event.type == pygame.JOYAXISMOTION:
	            print("Axis ID: " + str(event.axis))

	    # DRAWING STEP
	    # First, clear the screen to white. Don't put other drawing commands
	    # above this, or they will be erased with this command.
	    screen.fill(WHITE)
	    textPrint.reset()

	    # Get count of joysticks
	    joystick_count = pygame.joystick.get_count()

	    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
	    textPrint.indent()

	    # For each joystick:
	    for i in range(joystick_count):
	        joystick = pygame.joystick.Joystick(i)
	        joystick.init()

	        textPrint.print(screen, "Joystick {}".format(i))
	        textPrint.indent()

	        # Get the name from the OS for the controller/joystick
	        name = joystick.get_name()
	        textPrint.print(screen, "Joystick name: {}".format(name))

	        # Usually axis run in pairs, up/down for one, and left/right for
	        # the other.
	        axes = joystick.get_numaxes()
	        textPrint.print(screen, "Number of axes: {}".format(axes))
	        textPrint.indent()

	        for i in range(axes):
	            axis = (joystick.get_axis(i) + 1.0) / 2.0
	            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
	        textPrint.unindent()

	        buttons = joystick.get_numbuttons()
	        textPrint.print(screen, "Number of buttons: {}".format(buttons))
	        textPrint.indent()

	        for i in range(buttons):
	            button = joystick.get_button(i)
	            textPrint.print(screen, "Button {:>2} value: {}".format(i, button))
	        textPrint.unindent()

	        # Hat switch. All or nothing for direction, not like joysticks.
	        # Value comes back in an array.
	        hats = joystick.get_numhats()
	        textPrint.print(screen, "Number of hats: {}".format(hats))
	        textPrint.indent()

	        for i in range(hats):
	            hat = joystick.get_hat(i)
	            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)))
	        textPrint.unindent()

	        textPrint.unindent()


	    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

	    # Go ahead and update the screen with what we've drawn.
	    pygame.display.flip()

	    # Limit to 20 frames per second
	clock.tick(20)	

	pygame.quit()

	#while 1:
	#	events = get_gamepad()
	#	for event in events:
	#		print(event.ev_type, event.code, event.state)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just output the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
self.x -= 10


if __name__ == "__main__":
	main()