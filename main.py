from pysimpleGUI import *
from gameManager import *
import sys
import pygame as pg
from pygame.locals import *

WINDOWWIDTH = 1500
WINDOWHEIGHT = 800

WS = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pg.display.set_caption('2D platformer')

#Here we need to load a level
GM = GameManager([], None, [], 0)

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
    GM.draw()
    pg.display.update()
    clock.tick(FPS)