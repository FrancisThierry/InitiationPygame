# hero/tom.py
import pygame
import os
import sys

TOM_SPRITE_SHEET_PATH = os.path.join(os.path.dirname(__file__), '..', 'sprite', 'tom-sprite.png')

class Tom:
    def __init__(self, x=0, y=0):
        self.name = "Tom"
        self.health = 100
        self.strength = 10
        self.x = x
        self.y = y
        self.display_size = 64  # Taille finale désirée (ex: 100x100 pixels)
        self.speed = 5

        self.size = self.display_size

        print(f"Tentative de chargement du sprite depuis : {TOM_SPRITE_SHEET_PATH}")

        try:
            self.sprite_sheet = pygame.image.load(TOM_SPRITE_SHEET_PATH).convert_alpha()
            print(f"Planche de sprites chargée. Dimensions réelles: {self.sprite_sheet.get_size()}") # Devrait afficher (1024, 1536)
        except pygame.error as e:
            print(f"Erreur de chargement de la planche de sprites: {e}")
            print(f"Vérifiez que le fichier '{TOM_SPRITE_SHEET_PATH}' existe et est accessible.")
            self.current_image = pygame.Surface((self.display_size, self.display_size), pygame.SRCALPHA)
            self.current_image.fill((255, 0, 0)) # Rouge si erreur critique
            sys.exit()

        self.sprite_width = 256
        self.sprite_height = 356

        # --- Charger et stocker les différentes images de Tom ---
        self.sprites = {
            "default": self.get_scaled_sprite(0, 0),  # Le premier sprite (colonne 0, ligne 0)
            "right": self.get_scaled_sprite(3, 0),    # Le quatrième sprite sur la première ligne (colonne 3, ligne 0)
            "left": self.get_scaled_sprite(0, 1)     # NOUVEAU : Le premier sprite sur la DEUXIÈME ligne (colonne 0, ligne 1)
        }
        self.current_image = self.sprites["default"] # Commence avec le sprite par défaut

    def get_scaled_sprite(self, col, row):
        x_offset = col * self.sprite_width
        y_offset = row * self.sprite_height
        
        # Sécurité : Vérifiez que le rectangle de découpe ne dépasse pas les limites de la planche
        if x_offset + self.sprite_width > self.sprite_sheet.get_width() or \
           y_offset + self.sprite_height > self.sprite_sheet.get_height():
            print(f"Avertissement: Tentative de découper un sprite hors limites à col={col}, row={row}")
            return pygame.Surface((self.display_size, self.display_size), pygame.SRCALPHA) # Retourne une surface vide si hors limites

        rect = pygame.Rect(x_offset, y_offset, self.sprite_width, self.sprite_height)
        sprite = self.sprite_sheet.subsurface(rect)
        return pygame.transform.scale(sprite, (self.display_size, self.display_size))

    def draw(self, screen):
        screen.blit(self.current_image, (self.x, self.y))

    def update(self):
        pass

    def move(self, dx, dy):
        # Change l'image en fonction de la direction
        if dx > 0:  # Mouvement vers la droite
            self.current_image = self.sprites["right"]
        elif dx < 0: # Mouvement vers la gauche
            self.current_image = self.sprites["left"] # NOUVEAU : Utilise le sprite "left"
        elif dy != 0: # Mouvement vertical (haut ou bas)
            self.current_image = self.sprites["default"]
        else: # Pas de mouvement
            self.current_image = self.sprites["default"]

        new_x = self.x + dx
        new_y = self.y + dy

        screen_width_limit = 800
        screen_height_limit = 600

        self.x = max(0, min(new_x, screen_width_limit - self.size))
        self.y = max(0, min(new_y, screen_height_limit - self.size))
    # Méthode pour obtenir le rectangle de collision de Tom
    # Utilisé pour la détection de collision avec d'autres objets
    def get_rect(self):
        import pygame
        return pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)

    # Add other methods as needed