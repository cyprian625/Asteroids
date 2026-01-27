from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    VERSION = pygame.version.ver
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        pygame.Surface.fill(screen, color = "black")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()
