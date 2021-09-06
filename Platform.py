import pygame as pg
from pysimpleGUI import GREEN

class Platform():
    def __init__(self, center, size, collision=True, show=True, color=GREEN):
        self.center = center
        self.size = size
        self.hasCollision = collision
        self.show = show
        self.color = color
        self.updateRect()

    def updateRect(self):
        self.rect = pg.Rect(1, 1, self.size[0], self.size[1])
        self.rect.center = self.center[0], self.center[1]

    def draw(self, surface, offset=[0, 0]):
        #print('hey', self.center, self.size, self.rect, self.show)
        #Might want to have sprites here later
        if self.show:
            self.rect.center = self.center[0]+offset[0], self.center[1]+offset[1]
            pg.draw.rect(surface, self.color, self.rect)
            self.rect.center = self.center[0], self.center[1]

    def update(self):
        #Dummy, incase you later want to inherit platforms that need to update
        pass