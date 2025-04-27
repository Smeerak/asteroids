import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    #init Pygame
    pygame.init()

    #create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #dynamically add a class variable
    Player.containers=(updateable, drawable)
    Asteroid.containers=(asteroids,updateable, drawable)
    AsteroidField.containers=(updateable)
    Shot.containers = (shots, drawable, updateable)


    #now that variable is added, create an instance. It will automagically be added to the two groups.
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #roid = Asteroid(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,20)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ticker = pygame.time.Clock()
    delta_time = 0

    #game looop
    while(True):
        delta_time = (ticker.tick(60))/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return()
        
        screen.fill(0)

        #itterage over the two groups - update and draw
        for u in updateable:
            u.update(delta_time)

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if(a.collision(player)):
                print("Game over!")
                sys.exit(1)
            for shot in shots:
                if(a.collision(shot)):
                    #a.kill()
                    a.split()
                    shot.kill()

        
            
        #player.update(delta_time)
        #player.draw(screen)

        pygame.display.flip()
        #delta_time = (ticker.tick(60))/1000

if __name__ == "__main__":
    main()