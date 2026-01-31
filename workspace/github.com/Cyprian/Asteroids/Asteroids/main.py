from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from player import Player
clock = pygame.time.Clock()
dt = 0
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    VERSION = pygame.version.ver
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()


