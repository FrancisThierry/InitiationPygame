import sys
import time
import pygame
import os
import pytmx

from hero.tom import Tom
from hero.camera import Camera


class StageWithCamera:
    def __init__(self, mainGame):
        SCREEN_WIDTH, SCREEN_HEIGHT = 600, 500
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Stage with Camera")
        self.clock = pygame.time.Clock()
        self.tiles = []
        self.tile_size = 16

        self.tom = Tom(100, 100)
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.loadTilesMap()  # On charge la map AVANT la 1re mise à jour caméra
        self.camera.update(self.tom)
        self.camera.limit_to_map(self.map_width, self.map_height)

    def loadTilesMap(self):
        tmx_file = os.path.join(os.path.dirname(__file__), '..', 'assets', 'maps', 'yt-map.tmx')
        if not os.path.exists(tmx_file):
            print(f"Le fichier de carte {tmx_file} n'existe pas.")
            return

        tmx_data = pytmx.util_pygame.load_pygame(tmx_file)
        self.map_width = tmx_data.width * self.tile_size
        self.map_height = tmx_data.height * self.tile_size

        self.tiles = []

        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        tile = pygame.transform.scale(tile, (self.tile_size, self.tile_size))
                        sprite = pygame.sprite.Sprite()
                        sprite.image = tile
                        sprite.rect = tile.get_rect(topleft=(x * self.tile_size, y * self.tile_size))
                        self.tiles.append(sprite)

        if not self.tiles:
            print("Aucun tile trouvé dans la carte.")

    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, self.camera.apply(tile.rect))

    def start(self):
        pygame.init()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            dx = dy = 0
            if keys[pygame.K_LEFT]:
                dx = -self.tom.speed
            if keys[pygame.K_RIGHT]:
                dx = self.tom.speed
            if keys[pygame.K_UP]:
                dy = -self.tom.speed
            if keys[pygame.K_DOWN]:
                dy = self.tom.speed

            self.tom.move(dx, dy)
            self.camera.update(self.tom)
            self.camera.limit_to_map(self.map_width, self.map_height)

            self.screen.fill((0, 0, 0))  # Fond noir
            self.draw(self.screen)
            self.tom.drawWithCamera(self.screen, self.camera)

            pygame.display.flip()
            self.clock.tick(60)
