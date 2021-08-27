#The base entity class, uppon which all other entities will be based
import pygame as pg
import numpy as np

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

def applyGravity(velocity, isOnGround):
    if not isOnGround and terminalVelocity < 10: #Terminal velocity
        velocity[1] += 0.1 #Correct direction?

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

    def __repr__(self):
        return 'Entity traveling at ' + str(self.velocity) + '  Center at ' + str(self.center)

    def updateRect(self):
        self.rect = pg.Rect(1, 1, self.size[0], self.size[1])
        self.rect.center = self.center[0], self.center[1]

    def coreUpdate(self, entities):
        if self.gravity:
            self.velocity = applyGravity(self.velocity, self.gravity)

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.updateRect()
        #Here be collisions

    def draw(self, screen, offset=[0, 0]):
        #Blit a sprite here
        self.rect.centerx += offset[0]
        self.rect.centery += offset[1]
        pg.draw.rect(screen, (0, 255, 0), self.rect)
        self.rect.centerx -= offset[0]
        self.rect.centery -= offset[1]

    def collides(self, entities):
        for e in entities:
            if e.rect != self.rect and e.rect.colliderect(self.rect):
                return True


    def onGround(self, entities):
        #Checks if the entity is on the ground (or any entity), return true or false
        r = False
        self.pos[1] += 1
        self.updateRect()
        if self.collides(entities):
            r = True

        self.pos[1] -= 1
        self.updateRect()

        return r