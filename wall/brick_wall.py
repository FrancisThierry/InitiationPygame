import pygame


class BrickWall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill((139, 69, 19))  # Couleur marron pour le mur en brique

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Dessine le mur sur la surface donnée