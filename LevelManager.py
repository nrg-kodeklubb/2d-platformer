#The level manager, containing class of levels, functions for loading levels
import pygame as pg

def loadLevel(path):
    pass

block_size = 16
class Level():
    def __init__(self, tiles, entities):
        self.tiles = tiles
        self.entities = entities

    def width(self):
        return len(self.tiles[0])
    
    def height(self):
        return len(self.tiles)

    def draw(self, screen):
        for y in range(self.height()):
            for x in range(self.width()):
                if self.tiles[y][x] == 1:
                    pg.draw.rect(screen, (255, 255, 255), (x*block_size, y*block_size, block_size, block_size))