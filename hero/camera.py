# camera.py
class Camera:
    def __init__(self, screen_width, screen_height):
        self.offset_x = 0
        self.offset_y = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, target):
        # Centrer la caméra sur le centre du personnage
        self.offset_x = target.x + target.display_size // 2 - self.screen_width // 2
        self.offset_y = target.y + target.display_size // 2 - self.screen_height // 2

    def apply(self, obj_rect):
        # Décale la position d’un objet selon l’offset de la caméra
        return obj_rect.move(-self.offset_x, -self.offset_y)
    def apply_rect(self, target_rect):
        return target_rect.move(-self.offset_x, -self.offset_y)

    def limit_to_map(self, map_width, map_height):
        self.offset_x = max(0, min(self.offset_x, map_width - self.screen_width))
        self.offset_y = max(0, min(self.offset_y, map_height - self.screen_height))
