import sys
import time
import pygame
import pytmx
import os
class StageWithTiles:
    def __init__(self, mainGame):
        self.mainGame = mainGame
        self.tiles = []
        self.tile_size = 16
        font = pygame.font.SysFont(None, 48)

        start_time = time.time()
        waiting = True
        while waiting:
            
            
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

            mainGame.screen.fill((30, 30, 30))

           
            
            self.loadTilesMap()
            self.draw(mainGame.screen)
            mainGame.tom.draw(mainGame.screen)
            mainGame.tom.update()

            pygame.display.flip()


        
    def loadTilesMap(self):
        # map de tiles dans assets/maps/yt-map.tmx
        tmx_file =  os.path.join(os.path.dirname(__file__), '..', 'assets', 'maps', 'yt-map.tmx')
        if not os.path.exists(tmx_file):
            print(f"Le fichier de carte {tmx_file} n'existe pas.")
            return None
        # les images sont ans assets/images/1.png
        tmx_image = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', '1.png')
        if not os.path.exists(tmx_image):
            print(f"L'image de carte {tmx_image} n'existe pas.")
            return None
        self.tiles = []
        tmx_data = pytmx.util_pygame.load_pygame(tmx_file)
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        tile = pygame.transform.scale(tile, (self.tile_size, self.tile_size))
                        self.tiles.append(pygame.sprite.Sprite())
                        self.tiles[-1].image = tile
                        self.tiles[-1].rect = tile.get_rect(topleft=(x * self.tile_size, y * self.tile_size))
                        self.tiles[-1].x = x * self.tile_size
                        self.tiles[-1].y = y * self.tile_size
                        self.tiles[-1].width = self.tile_size
                        self.tiles[-1].height = self.tile_size
                        self.tiles[-1].rect = pygame.Rect(self.tiles[-1].x, self.tiles[-1].y, self.tile_size, self.tile_size)
        if not self.tiles:
            print("Aucun tile trouvé dans la carte.")
            return None
    def draw(self, screen):
        for tile in self.tiles:                   
            screen.blit(tile.image, (tile.x, tile.y))    

        

    