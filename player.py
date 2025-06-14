import pygame
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # override the draw method of CircleShape
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # draw the triangle

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # rotate right
            self.rotate(dt)

        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        
        if keys[pygame.K_s]:
            # move backward
            self.move(-dt)

    def move(self, dt):
        # move the player forward in the direction it is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt