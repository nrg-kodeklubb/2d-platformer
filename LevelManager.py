#The level manager, containing class of levels, functions for loading levels
import pygame as pg

def loadLevel(path):
    pass

block_size = 16
class Level():
    def __init__(self, tiles, enemies):
        self.tiles = tiles
        self.enemies = enemies

        self.width = len(self.tiles)
        self.height = len(self.tiles[0])

    def draw(self, screen):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[0])):
                if self.tiles[y][x] == 1:
                    pg.draw.rect(screen, (255, 255, 255), (x*block_size, y*block_size, block_size, block_size))