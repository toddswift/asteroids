# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player



def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock() # create a clock object to control the frame rate
    dt = 0 # delta time, the time since the last frame  

    # instantiate a Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True: # this is the main loop which is infinite until the user does a control-c
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # if the user clicks the close button
                return # exit the program
        screen.fill(("black")) # fill the screen with black  

        # rotate the player
        player.update(dt)

        player.draw(screen) #draw the player

        pygame.display.flip() # update the display
        
        dt = clock.tick(60) / 1000.0 # convert milliseconds to seconds
        
    
if __name__ == "__main__":
    main()
