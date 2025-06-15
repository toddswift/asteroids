import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # add a new method that detects collisions with other CircleShape objects
    def collides_with(self, other):
        if not isinstance(other, CircleShape):
            return False
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius) # added <= to include touching circles
    
# Class to represent a bullet (which is represented by a small circle) inheriting from CircleShape so that we can use the same collision detection code
class Shot(CircleShape):
    def __init__(self, x, y, radius):   
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(x, y)    # boots recommended to add this line to use a copy but I don't understand it yet, code works without it
        self.is_alive = True  # Flag to track if the bullet is still active

    # override the draw method of CircleShape to draw the small circles "bullets" on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    # override the update method of CircleShape to move the shot in a straight line
    def update(self, dt):
        # move the circle/shot "bullet" in a straight line
        self.position += self.velocity * dt

        # Check if the bullet is off-screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.is_alive = False  # Mark for removal