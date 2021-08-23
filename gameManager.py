#The game manager!

from pygame.locals import *
import pygame as pg

class GameManager():
    def __init__(self, layouts, player, enemies, platforms, projectiles, screenOffSet = [0, 0], currentLayout=0):
        self.layouts = layouts
        self.currentLayout = currentLayout
        self.player = player
        self.enemies = enemies
        self.platforms = platforms
        self.projectiles = projectiles
        self.screenoffSet = screenOffSet

    def __repr__(self):
        return

    def keydown(self, key):
        #Called when player has pressed a key: there will be a lot to do here...
        pass

    def keyup(self, key):
        # --||--
        pass

    def mouseButtonDown(self, button):
        x, y = pg.mouse.get_pos()
        #Called when player presses a button down
        pass

    def draw(self):
        #Has to draw everything here
        pass

    def update(self):
        #Runs all update methods
        pass