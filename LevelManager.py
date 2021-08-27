#The level manager, containing class of levels, functions for loading levels
import pygame as pg

def loadLevel(path):
    file = open(path, 'r')
    lines = file.readlines()

    tiles = []
    entities = []

    for y in range(len(lines)):
        line = lines[y]

        line = line.replace('\n', '')

        # THIS LOOKS UNNECESSARY (there are easier ways to implement this), BUT IT HAS TO BE WRITTEN THIS WAY FOR LATER USE
        tile_row = [0] * len(line)
        for x in range(len(line)):
            tile_row[x] = int(line[x])

        tiles.append(tile_row)
    
    return Level(tiles, entities)

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
                    pg.draw.rect(screen, (0, 255, 0), (x*block_size, y*block_size, block_size, block_size))
