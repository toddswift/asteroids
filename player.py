import pygame
from circleshape import CircleShape
from constants import *
from circleshape import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0.0

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
        # Decrement shot cooldown
        if self.shot_cooldown > 0:
            self.shot_cooldown = max(0, self.shot_cooldown - dt)

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

        if keys[pygame.K_SPACE]:
            # shoot as long as the cooldown is not active
            if self.shot_cooldown <= 0:
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
                # shoot a shot
                shot = self.shoot()
                if shot:
                    return shot

    def move(self, dt):
        # move the player forward in the direction it is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        # create a new shot at the player's position with the player's rotation
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        return shot