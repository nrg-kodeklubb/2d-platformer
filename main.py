from pysimpleGUI import *
import sys
import pygame as pg
from pygame.locals import *

WINDOWWIDTH = 1500
WINDOWHEIGHT = 800

WS = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pg.display.set_caption('2D platformer')

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    WS.fill(WHITE)
    pg.display.update()