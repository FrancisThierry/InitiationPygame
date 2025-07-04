# application.py

import pygame
import sys
from hero.tom import Tom
from stages.stage_kingdom import StageKingDom
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

    def check_collision(self, rect1, rect2):
        return rect1.colliderect(rect2)

    def show_shadow_realm(self):
        self.stageKingDom()

    def stageKingDom(self):
        stageKingdom = StageKingDom(self)

    def run(self):
        self.stageOne()

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