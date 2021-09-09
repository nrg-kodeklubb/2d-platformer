#The game manager!

from pygame.locals import *
import pygame as pg
import copy

cameraCenter = [1250/2, 680/2]

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

        playerPos = copy.deepcopy(self.levels[self.currentLevel].entities[0].center)
        offSet = [-playerPos[0]+cameraCenter[0], -playerPos[1]+cameraCenter[1]]

        self.levels[self.currentLevel].draw(screen, offSet)

        self.layouts[self.currentLayout].draw()

    def update(self):
        #Runs all update methods
        self.levels[self.currentLevel].update(self.keys)

    def updateClick(self):
        #Runs updates for a click
        self.layouts[self.currentLayout].collide(pg.mouse.get_pos(), self)

