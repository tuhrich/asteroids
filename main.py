import pygame
from logger import log_state
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

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            screen.fill("black")
            pygame.display.flip()

if __name__ == "__main__":
    main()
