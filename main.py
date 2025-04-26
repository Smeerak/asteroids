import pygame
from player import Player
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    #init Pygame
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #dynamically add a class variable
    Player.containers=(updateable, drawable)

    #now that variable is added, create an instance. It will automagically be added to the two groups.
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ticker = pygame.time.Clock()
    delta_time = 0

    #game looop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return()
        
        screen.fill(0)

        #itterage over the two groups - update and draw
        for u in updateable:
            u.update(delta_time)
        for d in drawable:
            d.draw(screen)

        #player.update(delta_time)
        #player.draw(screen)
        
        pygame.display.flip()
        delta_time = (ticker.tick(60))/1000

if __name__ == "__main__":
    main()