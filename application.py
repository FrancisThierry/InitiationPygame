# application.py

import pygame
import sys
from hero.tom import Tom # Importez Tom depuis le module hero.tom

class Application:
    def __init__(self, name: str):
        self.name = name
        self.screen_width = 800
        self.screen_height = 600
        self.screen = None
        self.clock = None
        self.tom = None
        self.FPS = 60

    def run(self):
        print(f"Running application: {self.name}")
        pygame.init()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.name)

        # Initialisation de Tom. Sa taille est maintenant gérée DANS la classe Tom
        # et est fixée à 50 par défaut pour le redimensionnement du sprite.
        # Vous ne définissez plus tom.size ici directement.
        self.tom = Tom(x=100, y=100) # Utilisez les positions initiales que vous avez définies

        self.clock = pygame.time.Clock()

        running = True
        while running:
            # Réinitialise le déplacement pour la frame actuelle
            dx, dy = 0, 0

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Gestion des touches pressées pour le mouvement continu
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                dx = -self.tom.speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx = self.tom.speed
            if keys[pygame.K_UP] or keys[pygame.K_z]:
                dy = -self.tom.speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                dy = self.tom.speed

            # La méthode move de Tom gère le déplacement et la limitation aux bords.
            self.tom.move(dx, dy)
            # La méthode update de Tom ne fait rien maintenant, mais l'appel est inoffensif.
            self.tom.update()

            # Dessin
            self.screen.fill((0, 0, 0)) # Fond noir
            self.tom.draw(self.screen) # Dessine Tom
            pygame.display.flip()       # Met à jour l'écran

            # Contrôle du Framerate
            self.clock.tick(self.FPS)

        pygame.quit()
        sys.exit() # sys.exit() est préférable après pygame.quit()
        print(f"Application {self.name} has exited.")

if __name__ == "__main__":
    app = Application("My Pygame Application")
    app.run()