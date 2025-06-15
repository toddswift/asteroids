import pygame
import asteroidfield
import sys
from asteroid import Asteroid
from constants import *
from player import Player
from circleshape import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # create a clock object to control the frame rate
    
    updatable_group = pygame.sprite.Group() # create sprite groups
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    
    # Create a new group to contain all the shots
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group) # add the player to the groups
    Asteroid.containers = (updatable_group, drawable_group, asteroid_group) # add the asteroids to the groups
    Shot.containers = (updatable_group, drawable_group, shot_group) # add the shots to the groups

    # set the static containers field of the AsteroidField class to only the updatable group
    asteroidfield.AsteroidField.containers = (updatable_group)

    
    asteroid_field = asteroidfield.AsteroidField() # instantiate an AsteroidField object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # instantiate a Player object

    dt = 0 # delta time, the time since the last frame  
  
    while True: # this is the main loop which is infinite until the user does a control-c
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # if the user clicks the close button
                return # exit the program
        
        updatable_group.update(dt) # update all updatable sprites

        # Remove shots that are off-screen
        for shot in shot_group:
            if not shot.is_alive:
                shot.kill()

        # iterate over all asteroid sprites and check for collisions
        for asteroid in asteroid_group:

            # check if any asteroid collides with the Player object instance
            if asteroid.collides_with(player):
                # exit the game
                sys.exit("Game Over!")


        screen.fill(("black")) # fill the screen with black  

        for sprite in drawable_group: # draw all drawable sprites
            sprite.draw(screen)

        pygame.display.flip() # update the display
        
        # limit the frame rate to 60 FPS and get the time since the last frame
        dt = clock.tick(60) / 1000.0 
        
    

if __name__ == "__main__":
    main()
