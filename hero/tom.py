import pygame

class Tom:
    def __init__(self, x=0, y=0):
        self.name = "Tom"
        self.health = 100
        self.strength = 10
        self.x = x
        self.y = y
        self.size = 20  # taille du carré

    def attack(self, target):
        damage = self.strength
        target.health -= damage
        return f"{self.name} attacks {target.name} for {damage} damage!"
    
    def heal(self, amount):
        self.health += amount
        return f"{self.name} heals for {amount} health!"

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.size, self.size))