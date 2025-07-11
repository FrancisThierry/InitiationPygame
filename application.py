# application.py

import os
import pygame
import sys
from hero.tom import Tom
from sound.sound_player import SoundPlayer
from stages.stage_kingdom import StageKingDom
from stages.stage_with_camera import StageWithCamera
from stages.stage_with_tiles import StageWithTiles
from wall.brick_wall import BrickWall
from stages.stage_one import StageOne
from stages.stage_dragon import StageDragon

class Application:
    def __init__(self, name: str):
        self.name = name
        self.screen_width = 800
        self.screen_height = 608
        self.screen = None
        self.clock = None
        self.tom = None
        self.brick_wall = None
        self.FPS = 60
        self.music_sound =  os.path.join(os.path.dirname(__file__), 'assets', 'music', 'Friends.ogg')


    def check_collision(self, rect1, rect2):
        return rect1.colliderect(rect2)

    def show_stage_kingdom(self):
        self.stageKingDom()

    def stageKingDom(self):
        stageKingdom = StageKingDom(self)

    def run(self):
        self.stageOne()
        # self.stageWithCamera()
        
    def stageWithCamera(self):
        # Placeholder for showing a stage with camera functionality
        sound = SoundPlayer(self.music_sound)
        sound.play()        
        print("Showing stage with camera functionality")
        stageWithCamera = StageWithCamera(self)
        stageWithCamera.start()

    def stageOne(self):
        print(f"Running application: {self.name}")        
        stageOne = StageOne(self)
        
    def show_stage_dragon(self):
        stageDragon = StageDragon(self)
        
    def show_stage_with_tiles(self):
        # Placeholder for showing a stage with tiles                   
        
        try:
            stageWithTiles = StageWithTiles(self)
        except Exception as e:
            print(f"An error occurred in show_stage_with_tiles: {e}")

        
        
if __name__ == "__main__":
    app = Application("My Pygame Application")
    app.run()