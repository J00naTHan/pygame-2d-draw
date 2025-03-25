import pygame
import sys
import consts as c
from coord_plane import coord_plane

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("Cena 2D Desordenada")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        coord_plane(screen)
        pygame.display.flip()
        clock.tick(60)
