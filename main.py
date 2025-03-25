import pygame
import sys
import consts as c
from coord_plane import coord_plane

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("Cena 2D")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        coord_plane(screen)

        #triangle = pygame.draw.polygon(screen, c.RED, [(), (), ()])
        #rectangle = pygame.draw.polygon(screen, c.GRAY, [(), (), (), ()])
        #trapezium = pygame.draw.polygon(screen, c.RED, [(), (), (), ()])
        #trect1 = pygame.draw.polygon(screen, c.BLUE, [(), (), ()])
        #trect2 = pygame.draw.polygon(screen, c.BLUE, [(), (), ()])
        circle = pygame.draw.circle(screen, c.TURQUOISE, (57, 548), 30)

        pygame.display.flip()

        clock.tick(60)
