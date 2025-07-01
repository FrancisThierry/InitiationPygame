# application.py

import pygame
import sys
from hero.tom import Tom
from wall.brick_wall import BrickWall

class Application:
    def __init__(self, name: str):
        self.name = name
        self.screen_width = 800
        self.screen_height = 600
        self.screen = None
        self.clock = None
        self.tom = None
        self.brick_wall = None
        self.FPS = 60

    def check_collision(self, rect1, rect2):
        return rect1.colliderect(rect2)

    def show_shadow_realm(self):
        self.stageKingDom()

    def stageKingDom(self):
        font = pygame.font.SysFont(None, 48)
        text = font.render("Bienvenue dans le royaume des ombres", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.fill((30, 30, 30))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        # Attend que l'utilisateur ferme la fenêtre ou appuie sur une touche
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    def run(self):
        self.stageOne()

    def stageOne(self):
        print(f"Running application: {self.name}")
        pygame.init()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.name)
        
        self.brick_wall = BrickWall(x=10, y=10, width=100, height=100)
        self.tom = Tom(x=500, y=300)
        self.clock = pygame.time.Clock()

        running = True
        while running:
            dx, dy = 0, 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                dx = -self.tom.speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx = self.tom.speed
            if keys[pygame.K_UP] or keys[pygame.K_z]:
                dy = -self.tom.speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                dy = self.tom.speed

            # Gestion collision
            future_rect = self.tom.get_rect().move(dx, dy)
            if not self.check_collision(future_rect, self.brick_wall.get_rect()):
                self.tom.move(dx, dy)
            else:
                # Affiche l'écran spécial et quitte la boucle principale
                self.show_shadow_realm()
                running = False
                continue

            self.tom.update()

            self.screen.fill((0, 0, 0))
            self.tom.draw(self.screen)
            self.brick_wall.draw(self.screen)
            pygame.display.flip()

            self.clock.tick(self.FPS)

        pygame.quit()
        sys.exit()
        print(f"Application {self.name} has exited.")

if __name__ == "__main__":
    app = Application("My Pygame Application")
    app.run()