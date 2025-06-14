import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # create a clock object to control the frame rate
    
    updatable_group = pygame.sprite.Group() # create sprite groups
    drawable_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group) # add the player to the groups
    
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # instantiate a Player object

    dt = 0 # delta time, the time since the last frame  
  
    while True: # this is the main loop which is infinite until the user does a control-c
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # if the user clicks the close button
                return # exit the program
        
        updatable_group.update(dt) # update all updatable sprites

        screen.fill(("black")) # fill the screen with black  

        for sprite in drawable_group: # draw all drawable sprites
            sprite.draw(screen)

        pygame.display.flip() # update the display
        
        # limit the frame rate to 60 FPS and get the time since the last frame
        dt = clock.tick(60) / 1000.0 
        
    

if __name__ == "__main__":
    main()
