import sys
import pygame
import time

class StageKingDom:
    def __init__(self, mainGame):
        font = pygame.font.SysFont(None, 48)
        text = font.render("Bienvenue dans le royaume des ombres", True, (255, 255, 255))
        text_rect = text.get_rect(center=(mainGame.screen_width // 2, mainGame.screen_height // 2))

        countdown_font = pygame.font.SysFont(None, 36)
        countdown_pos = (mainGame.screen_width // 2, mainGame.screen_height // 2 + 60)

        start_time = time.time()
        waiting = True
        while waiting:
            elapsed = time.time() - start_time
            remaining = max(0, 5 - int(elapsed))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

            mainGame.screen.fill((30, 30, 30))
            mainGame.screen.blit(text, text_rect)

            countdown_text = countdown_font.render(f"Passage au stage avec tuiles dans {remaining}...", True, (200, 200, 0))
            countdown_rect = countdown_text.get_rect(center=countdown_pos)
            mainGame.screen.blit(countdown_text, countdown_rect)

            pygame.display.flip()
            pygame.time.delay(100)

            if elapsed >= 5:
                waiting = False

        # Afficher le stage avec tuiles
        if hasattr(mainGame, "show_stage_with_tiles"):
            mainGame.show_stage_with_tiles()