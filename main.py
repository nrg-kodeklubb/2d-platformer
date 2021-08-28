from pysimpleGUI import *
from gameManager import *
from LevelManager import *
from Player import Player
import sys
import pygame as pg
from pygame.locals import *

WINDOWWIDTH = 1250
WINDOWHEIGHT = 680

WS = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pg.display.set_caption('2D platformer')

#Here we need to load a level
level1 = loadLevel('levels/level1.txt')
Player = Player(None, [32, 64], [200, 400], gravity=True, collision=True)
level1.entities += [Player]
GM = GameManager([], None, [level1], 0)

FPS = 30

clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pg.quit()
            sys.exit()

        if event.type == KEYDOWN:
            GM.keydown(event.key)

        if event.type == KEYUP:
            GM.keyup(event.key)

    GM.update()

    WS.fill(WHITE)
    GM.draw(WS)
    pg.display.update()
    clock.tick(FPS)