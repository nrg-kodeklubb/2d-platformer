#The base entity class, uppon which all other entities will be based
import pygame as pg

def setAngle(sprite, angle):
    pass

def loadSprite(path, size, flip, angle):
    pass

def calcGravity(velocity, isOnGround):
    pass

class Entity():
    def __init__(self, sprite, size, center, surface, gravity=True, collision=True):
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
        #Draw the entity (remember angle + offset)
        pass

    def onGround(self, entities):
        #Checks if the entity is on the ground (or any entity), return true or false
        pass
