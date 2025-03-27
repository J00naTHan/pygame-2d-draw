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
        "rect": [(246, 440), (246, 360), (446, 360), (446, 440)],
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
                        # corpo
                        current_coords["rect"] = rotation(original_coords["rect"], 120, original_coords["rect"][3])
                        current_coords["rect"] = translation(current_coords["rect"], 0, -100)

                        # ponta
                        current_coords["tri"] = scale(original_coords["tri"], 1, 1.5)
                        current_coords["tri"] = rotation(current_coords["tri"], 328, current_coords["tri"][1])
                        current_coords["tri"] = translation(current_coords["tri"], 343, -570)

                        # propulsor
                        current_coords["trap"] = rotation(original_coords["trap"], 31, (90, 60))
                        current_coords["trap"] = translation(current_coords["trap"], 386, 308)

                        # barbatana 1
                        current_coords["tr1"] = rotation(original_coords["tr1"], 31, original_coords["tr1"][1])
                        current_coords["tr1"] = translation(current_coords["tr1"], -195, 280)

                        # barbatana 2
                        current_coords["tr2"] = rotation(original_coords["tr2"], 31, original_coords["tr2"][1])
                        current_coords["tr2"] = scale(current_coords["tr2"], 2, 2)
                        current_coords["tr2"] = translation(current_coords["tr2"], -512, -788)

                        # cabine
                        current_coords["cir"] = translation(original_coords["cir"], 503, -320)

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
