import pygame
import consts as c

def coord_plane(screen):
    screen.fill(c.WHITE)

    for y in range(0, c.HEIGHT, c.SCALE):
        pygame.draw.line(screen, c.GRAY, (0, y), (c.WIDTH, y), 1)

    for x in range(0, c.WIDTH, c.SCALE):
        pygame.draw.line(screen, c.GRAY, (x, 0), (x, c.HEIGHT), 1)

    pygame.draw.line(screen, c.BLACK, (0, c.ORIGIN_Y), (c.WIDTH, c.ORIGIN_Y), 2)

    pygame.draw.line(screen, c.BLACK, (c.ORIGIN_X, 0), (c.ORIGIN_X, c.HEIGHT), 2)

    for x in range(0, c.WIDTH, c.SCALE):
        pygame.draw.line(screen, c.BLACK, (x, c.ORIGIN_Y - 5), (x, c.ORIGIN_Y + 5), 2)
        if x != c.ORIGIN_X:
            value = (x - c.ORIGIN_X) // c.SCALE
            font = pygame.font.SysFont(None, 20)
            text = font.render(str(value), True, c.BLACK)
            screen.blit(text, (x - 10, c.ORIGIN_Y + 10))

    for y in range(0, c.HEIGHT, c.SCALE):
        pygame.draw.line(screen, c.BLACK, (c.ORIGIN_X - 5, y), (c.ORIGIN_X + 5, y), 2)
        if y != c.ORIGIN_Y:
            value = (c.ORIGIN_Y - y) // c.SCALE
            font = pygame.font.SysFont(None, 20)
            text = font.render(str(value), True, c.BLACK)
            screen.blit(text, (c.ORIGIN_X + 10, y - 10))
