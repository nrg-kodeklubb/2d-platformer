from Base import Entity
from pygame.locals import *

WALKINGSPEED = 1
TerminalWalking = 8
JUMP = 12

class Player(Entity):
    def __init__(self, sprite, size, center, gravity=True, collision=True):
        super().__init__(sprite, size, center, gravity, collision)

    def update(self, relevantEntities, keys):
        self.updateGround(relevantEntities)

        #Inputs
        if K_a in keys:
            self.velocity[0] += -WALKINGSPEED

        if K_d in keys:
            self.velocity[0] += WALKINGSPEED


        if self.isOnGround: #Remove controll if in the air
            if K_SPACE in keys:
                self.velocity[1] = -JUMP

        if self.isOnGround: #Friction
            self.velocity[0] -= 0.25*self.velocity[0]


        self.coreUpdate(relevantEntities)
