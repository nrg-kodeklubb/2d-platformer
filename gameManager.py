#The game manager!

from pygame.locals import *
import pygame as pg

class GameManager():
    def __init__(self, layouts, player, levels, currentLevel=0, currentLayout=0):
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
        self.layouts[self.currentLayout].collide((x, y))

    def draw(self, screen):
        #Has to draw everything here
        self.levels[self.currentLevel].draw(screen)
        #self.player.draw()
        #self.layouts[self.currentLayout].draw()

    def update(self):
        #Runs all update methods
        self.levels[self.currentLevel].update(self.keys)

