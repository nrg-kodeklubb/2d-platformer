#The game manager!

from pygame.locals import *
import pygame as pg

class GameManager():
    def __init__(self, layouts, player, levels, currentLevel, currentLayout=0):
        self.layouts = layouts
        self.currentLayout = currentLayout
        self.player = player
        self.levels = levels
        self.currentLevel = currentLevel
        self.keys = []

    def __repr__(self):
        return

    def keydown(self, key):
        if not key in self.keys:
            self.keys += [key]

    def keyup(self, key):
        if key in self.keys:
            self.keys.remove(key)

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

