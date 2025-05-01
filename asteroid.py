import pygame
import random
from circleshape import CircleShape
from constants import *


#comment
#comment 2
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.move(dt)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), self.position,self.radius,2)
        
    def move(self, dt):
        self.position += (self.velocity * dt)

    def split(self, ):
        
        if(self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
            return
        else:
            r_angle = random.uniform(20,50)
            #pygame.Vector2(0, 1).rotate(self.) * PLAYER_SHOOT_SPEED
            v1 = self.velocity.rotate(r_angle)
            v2 = self.velocity.rotate(r_angle * -1)
            roid1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            roid2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            roid1.velocity = v1 * 1.2
            roid2.velocity = v2 * -1.2
            self.kill()






