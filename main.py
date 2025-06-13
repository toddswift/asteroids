# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True: # this is the main loop which is infinite until the user does a control-c
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # if the user clicks the close button
                return # exit the program
        screen.fill(("black")) # fill the screen with black
        pygame.display.flip() # update the display
    

    
if __name__ == "__main__":
    main()
