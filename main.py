import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        for obj in updatable:
            obj.update(dt)

        for a in asteroids:
            if a.col_check(player):
                print("Game Over!")
                sys.exit()

            for s in shots:
                if a.col_check(s):
                    a.split()
                    s.kill()
            
        
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()