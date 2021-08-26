#The base entity class, uppon which all other entities will be based
import pygame as pg
import numpy as np

def loadSprite(path, size=None, flip=[None, None]):
    image = pg.image.load(path + '.png')

    if size != None:
        streched = pg.transform.scale(image, size)

    flipped = pg.transform.flip(streched, flip[1], flip[0])

    return flipped

def blitRotImg(image, rect, surface, offset=[0, 0], angle=0):
    angle = angle*180/np.pi

    loc = rect.center
    loc[0] += offset[0]
    loc[1] += offset[1]
    rot_sprite = pg.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc

    surface.blit(rot_sprite, rect)

def calcGravity(velocity, isOnGround):
    pass

class Entity():
    def __init__(self, sprite, size, center, gravity=True, collision=True):
        self.velocity = [0, 0]
        self.sprite = sprite
        self.size = size
        self.center = center
        self.gravity = gravity
        self.collision = collision
        self.updateRect()

    def __repr__(self):
        return 'Entity traveling at ' + str(self.velocity) + '  Center at ' + str(self.center)

    def updateRect(self):
        self.rect = pg.Rect(1, 1, self.size[0], self.size[1])
        self.rect.center = self.center[0], self.center[1]

    def coreUpdate(self, entities):
        #Apply gravity + check collisions
        pass

    def draw(self, offset, screen):
        #Draw the entity (offset)
        pass

    def onGround(self, entities):
        #Checks if the entity is on the ground (or any entity), return true or false
        pass
