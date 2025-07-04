class Camera:
    def __init__(self, width, height, screen_width, screen_height):
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset_x = 0
        self.offset_y = 0

    def update(self, target_rect):
        # Centre la caméra sur Tom
        self.offset_x = target_rect.centerx - self.screen_width // 2
        self.offset_y = target_rect.centery - self.screen_height // 2

        # Optionnel : limite la caméra aux bords du niveau
        self.offset_x = max(0, min(self.offset_x, self.width - self.screen_width))
        self.offset_y = max(0, min(self.offset_y, self.height - self.screen_height))

    def apply(self, rect):
        # Retourne un rect décalé par la caméra
        return rect.move(-self.offset_x, -self.offset_y)
