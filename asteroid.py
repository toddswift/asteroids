import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        super().__init__(x, y, radius)
    
    # override the draw method of CircleShape
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # move the asteroid in a straight line
        self.position += self.velocity * dt