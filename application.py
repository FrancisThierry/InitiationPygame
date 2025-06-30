import pygame

from hero.tom import Tom


class Application:
    def __init__(self, name: str):
        self.name = name

    def run(self):
        print(f"Running application: {self.name}")
        pygame.init()
        screen = pygame.display.set_mode((800, 600))    
        pygame.display.set_caption(self.name)
        
        tom = Tom()
        tom.x = 100
        tom.y = 100  # Position de Tom
        tom.size = 50  # Taille de Tom
        

        clock = pygame.time.Clock()  # Ajout du clock
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                tom.x -= 5
            if keys[pygame.K_RIGHT]:
                tom.x += 5
            if keys[pygame.K_UP]:
                tom.y -= 5
            if keys[pygame.K_DOWN]:
                tom.y += 5
            
            screen.fill((0, 0, 0))
            tom.draw(screen)    
            pygame.display.flip()
            clock.tick(60)  # Limite à 60 FPS
        pygame.quit()
        print(f"Application {self.name} has exited.")

if __name__ == "__main__":
    app = Application("My Pygame Application")
    app.run()