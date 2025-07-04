import sys
import time
import pygame
from hero.tom import Tom


class StageDragon:
    def __init__(self, mainGame):
        font = pygame.font.SysFont(None, 48)
        text = font.render("Bienvenue dans le royaume des dragons", True, (255, 255, 255))
        text_rect = text.get_rect(center=(mainGame.screen_width // 2, mainGame.screen_height // 4))

        tom = Tom(x=500, y=300)
        start_time = time.time()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

            mainGame.screen.fill((30, 30, 30))
            mainGame.screen.blit(text, text_rect)

           
            mainGame.tom = tom
            mainGame.tom.draw(mainGame.screen)
            mainGame.tom.update()

            pygame.display.flip()


        