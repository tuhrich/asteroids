import sys
import pygame

from asteroid import Asteroid
from player import Player
from logger import log_state, log_event
from asteroidfield import AsteroidField
from shot import Shot

from constants import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT,
)

# or import everything: from module_name import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroidfield = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
               if asteroid.collides_with(shot):
                   log_event("asteroid_shot")
                   asteroid.split()                   
        
        for draw in drawable:
            draw.draw(screen) 

        pygame.display.flip()            
        dt = clock.tick(60) / 1000          
    
  
if __name__ == "__main__":
    main()
