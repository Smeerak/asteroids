import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        #self.velocity = direction * PLAYER_SHOOT_SPEED

    def update(self, dt):
         self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), self.position,self.radius,2)
        #print("shot!")

