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

    original_coords = {
        "tri": [(235, 469), (275, 519), (315, 469)],
        "rect": [(346, 340), (346, 260), (546, 260), (546, 340)],
        "trap": [(50, 50), (70, 70), (110, 70), (130, 50)],
        "tr1": [(786, 135), (736, 50), (736, 135)],
        "tr2": [(446, 578), (471, 578), (471, 578 - 42.5)],
        "cir": [(57, 548)]
    }

    current_coords = original_coords.copy()    
    transform_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # Adicionei esta verificação que estava faltando
                if event.key == pygame.K_SPACE:
                    transform_active = not transform_active
        
                    if not transform_active:
                        current_coords = original_coords.copy()
                    else:
                        current_coords["rect"] = scale(original_coords["rect"], 0.5, 2.5)
                        current_coords["rect"] = translation(current_coords["rect"], 100, -150)
                        current_coords["tri"] = scale(original_coords["tri"], 1.8, 1.8)
                        current_coords["tri"] = translation(current_coords["tri"], 100, -280)
                        current_coords["trap"] = rotation(original_coords["trap"], 180, (90, 60))
                        current_coords["trap"] = scale(current_coords["trap"], 2.5, 1)
                        current_coords["trap"] = translation(current_coords["trap"], 100, -50)
                        current_coords["tr1"] = scale(original_coords["tr1"], 0.8, 3)
                        current_coords["tr1"] = translation(current_coords["tr1"], 70, 100)
                        current_coords["tr2"] = scale(original_coords["tr2"], 0.8, 3)
                        current_coords["tr2"] = translation(current_coords["tr2"], 130, 100)
                        current_coords["cir"] = translation(original_coords["cir"], 200, -200)

        screen.fill(c.BLACK)

        coord_plane(screen)

        pygame.draw.polygon(screen, c.RED, current_coords["tri"])
        pygame.draw.polygon(screen, c.GRAY, current_coords["rect"])
        pygame.draw.polygon(screen, c.RED, current_coords["trap"])
        pygame.draw.polygon(screen, c.BLUE, current_coords["tr1"])
        pygame.draw.polygon(screen, c.BLUE, current_coords["tr2"])
        pygame.draw.circle(screen, c.TURQUOISE, current_coords["cir"][0], 30)

        pygame.display.flip()
        clock.tick(60)
