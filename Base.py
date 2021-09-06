#The base entity class, uppon which all other entities will be based
import pygame as pg
import numpy as np
from LevelManager import block_size

terminalVelocity = 10

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

def applyGravity(velocity):
    if velocity[1] < terminalVelocity:
        velocity[1] += 0.5

    return velocity

class Entity():
    def __init__(self, sprite, size, center, gravity=True, collision=True):
        self.velocity = [0, 0]
        self.sprite = sprite
        self.size = size
        self.center = center
        self.gravity = gravity
        self.collision = collision
        self.updateRect()
        self.isOnGround = False

    def __repr__(self):
        return 'Entity traveling at ' + str(self.velocity) + '  Center at ' + str(self.center)

    def updateRect(self):
        self.rect = pg.Rect(1, 1, self.size[0], self.size[1])
        self.rect.center = self.center[0], self.center[1]

    def coreUpdate(self, entities):
        self.updateGround(entities)
        #Gravity stuff here
        if self.gravity and not self.isOnGround:
            self.velocity = applyGravity(self.velocity)

        elif self.isOnGround and self.velocity[1] >= 0:
            self.velocity[1] = 0

        self.center[0] += self.velocity[0]

        if self.collision and self.collides(entities):
            #Allign to grid, you may need to differenciate between block and entity collisions,
            self.getBestFinalPos(self.center[0]-self.velocity[0], self.center[0], 0, entities)
            self.velocity[0] = 0
            self.updateRect()

        self.center[1] += self.velocity[1]

        if self.collision and self.collides(entities):
            #Allign to grid, you may need to differenciate between block and entity collisions,
            self.getBestFinalPos(self.center[1]-self.velocity[1], self.center[1], 1, entities)
            self.velocity[1] = 0
            self.updateRect()

    def getBestFinalPos(self, prevPos, nowPos, relevantChange, entities):
        sign = 1
        if prevPos > nowPos:
            sign = -1
        for pixel in range(int(prevPos), int(nowPos), sign):
            self.center[relevantChange] = pixel
            if self.collides(entities):
                self.center[relevantChange] -= sign
                return


    def draw(self, screen, offset=[0, 0]):
        #Blit a sprite here
        self.rect.centerx += offset[0]
        self.rect.centery += offset[1]
        pg.draw.rect(screen, (255, 0, 255), self.rect)
        self.rect.centerx -= offset[0]
        self.rect.centery -= offset[1]

    def collides(self, entities):
        self.updateRect()
        for e in entities:
            if self.rect.colliderect(e.rect) and e.rect != self.rect:
            #Temporary, should be what is below
            #if e.rect.colliderect(self.rect) and e.rect != self.rect:
                return True, e
        return False


    def updateGround(self, entities):
        #Checks if the entity is on the ground (or any entity), return true or false
        firstCollision = self.collides(entities)

        self.center[1] += 1
        self.updateRect()

        if self.collides(entities) and not firstCollision:
            self.isOnGround = True
        else:
            self.isOnGround = False

        self.center[1] -= 1
        self.updateRect()