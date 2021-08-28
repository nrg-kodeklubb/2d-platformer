#The level manager, containing class of levels, functions for loading levels
import pygame as pg
import copy

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
        #Hva søren er dette? Du starter med x. X aksen er ALLTID førstekoordinat!
        for y in range(self.height()):
            for x in range(self.width()):
                if self.tiles[y][x] == 1:
                    pg.draw.rect(screen, (0, 255, 0), (x*block_size, y*block_size, block_size, block_size))

        for e in self.entities:
            e.draw(screen)

    def getSuroundingTiles(self, centerPos, radius=2):
        centerPos[0] = int(centerPos[0]/block_size)
        centerPos[1] = int(centerPos[1]/block_size)
        r = []
        for x in range(-radius, radius):
            for y in range(-radius, radius):
                #Quite temporary code here, generating rects
                try:
                    if self.tiles[x+centerPos[1]][y+centerPos[0]] == 1:
                        rect = pg.Rect(1, 1, block_size, block_size)
                        rect.topleft = (y+centerPos[0])*block_size, (x+centerPos[1])*block_size
                        r += [rect] #A better append

                except IndexError:
                    pass #If the surrounding tiles are out of bounds

        return r

    def update(self, keys):
        ##Figure out relevant entities here
        for e in self.entities:
            e.update(self.getSuroundingTiles(copy.deepcopy(e.center)), keys)
