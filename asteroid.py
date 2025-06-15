import pygame
import random
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

    
    def split(self):
        self.kill() # immediately remove the asteroid from the screen - this asteroid is always destroyed, and maybe we'll spawn new ones

        # If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS, just return (this was a small asteroid and we're done)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        # Otherwise, split the asteroid into two smaller asteroids
        new_radius = self.radius / 2

        # Use random.uniform to generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        # Use the rotate method on the asteroid's velocity vector to create 2 new vectors, that are rotated by random_angle and -random_angle respectively (they should split in opposite directions)
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        # Compute the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create two new Asteroid objects at the current asteroid position with the new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        # Set the first's velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2
        asteroid1.velocity = new_vector1 * 1.2
        # Do the same for the second asteroid, but with the second new vector
        asteroid2.velocity = new_vector2 * 1.2
        # Return the two new asteroids
        return [asteroid1, asteroid2]
