import sys
import pygame

from hero.tom import Tom
from wall.brick_wall import BrickWall


class StageOne:
    def __init__(self, mainGame):
        print(f"Running application: {mainGame.name}")
        pygame.init()

        mainGame.screen = pygame.display.set_mode((mainGame.screen_width, mainGame.screen_height))
        pygame.display.set_caption(mainGame.name)
        
        mainGame.brick_wall = BrickWall(x=10, y=10, width=100, height=100)
        mainGame.tom = Tom(x=500, y=300)
        mainGame.clock = pygame.time.Clock()

        running = True
        while running:
            dx, dy = 0, 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                dx = -mainGame.tom.speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx = mainGame.tom.speed
            if keys[pygame.K_UP] or keys[pygame.K_z]:
                dy = -mainGame.tom.speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                dy = mainGame.tom.speed

            # Gestion collision
            future_rect = mainGame.tom.get_rect().move(dx, dy)
            if not mainGame.check_collision(future_rect, mainGame.brick_wall.get_rect()):
                mainGame.tom.move(dx, dy)
            else:
                # Affiche l'écran spécial et quitte la boucle principale
                mainGame.show_shadow_realm()
                running = False
                continue

            mainGame.tom.update()

            mainGame.screen.fill((0, 0, 0))
            mainGame.tom.draw(mainGame.screen)
            mainGame.brick_wall.draw(mainGame.screen)
            pygame.display.flip()

            mainGame.clock.tick(mainGame.FPS)

        pygame.quit()
        sys.exit()
        print(f"Application {mainGame.name} has exited.")