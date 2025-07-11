import pygame
'''Read a ogg sound file and play it using pygame.mixer.'''
class SoundPlayer:
    def __init__(self, sound_file):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sound_file)

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()

    def set_volume(self, volume):
        self.sound.set_volume(volume)  # volume should be between 0.0 and 1.0