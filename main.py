import pygame
import sys
import consts as c
from coord_plane import coord_plane
from transformations import translation, scale, rotation

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

        triangle = pygame.draw.polygon(screen, c.RED, [(235, 469), (275, 519), (315, 469)])
        rectangle = pygame.draw.polygon(screen, c.GRAY, [(346, 340), (346, 260), (546, 260), (546, 340)])
        trapezium = pygame.draw.polygon(screen, c.RED, [(50, 50), (70, 70), (110, 70), (130, 50)])
        trect1 = pygame.draw.polygon(screen, c.BLUE, [(786, 135), (736, 50), (736, 135)])
        trect2 = pygame.draw.polygon(screen, c.BLUE, [(446, 578), (471, 578), (471, 578 - 42.5)])
        circle = pygame.draw.circle(screen, c.TURQUOISE, (57, 548), 30)

        pygame.display.flip()

        clock.tick(60)
