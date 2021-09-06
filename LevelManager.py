#The level manager, containing class of levels, functions for loading levels
import pygame as pg
import copy
from Platform import Platform

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
        for y in range(self.height()):
            for x in range(self.width()):
                if self.tiles[y][x] == 1:
                    self.tiles[y][x] = Platform((x*block_size, y*block_size), (block_size, block_size))
                else:
                    self.tiles[y][x] = 0 #If it is not full, is is empty

        self.entities = entities #Spiller er alltid entity 0

    def width(self):
        return len(self.tiles[0])
    
    def height(self):
        return len(self.tiles)

    def draw(self, screen, offset=[0, 0]):
        #Hva søren er dette? Du starter med x. X aksen er ALLTID førstekoordinat!
        for y in range(self.height()):
            for x in range(self.width()):
                if self.tiles[y][x] != 0:
                    self.tiles[y][x].draw(screen, offset)

        for e in self.entities:
            e.draw(screen, offset)

    def getSuroundingTiles(self, centerPos, radius=3):
        centerPos[0] = int(centerPos[0]/block_size)
        centerPos[1] = int(centerPos[1]/block_size)
        r = []
        for x in range(-radius, radius+1):
            for y in range(-radius, radius+1):
                #Quite temporary code here, generating rects
                try:
                    if self.tiles[x+centerPos[1]][y+centerPos[0]] != 0: #Not empty
                        r += [self.tiles[x+centerPos[1]][y+centerPos[0]]] #A better append

                except IndexError:
                    pass #If the surrounding tiles are out of bounds

        return r

    def update(self, keys):
        ##Figure out relevant entities here
        for e in self.entities:
            e.update(self.getSuroundingTiles(copy.deepcopy(e.center)), keys)

        for y in range(self.height()):
            for x in range(self.width()):
                if self.tiles[y][x] != 0:
                    self.tiles[y][x].update()
