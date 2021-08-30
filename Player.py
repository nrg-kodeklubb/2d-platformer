from Base import Entity
from pygame.locals import *

WALKINGSPEED = 2
airSpeed = 0.2
TerminalWalking = 8
JUMP = 12
friction = 0.25
airResitance = 0.01

class Player(Entity):
    def __init__(self, sprite, size, center, gravity=True, collision=True):
        super().__init__(sprite, size, center, gravity, collision)
        self.airJumps = 1
        self.completedAirJumps = 0
        self.framesSinceJump = 0

    def update(self, relevantEntities, keys):
        self.updateGround(relevantEntities)

        if self.isOnGround:
            speed = WALKINGSPEED
            resitance = friction
        else:
            speed = airSpeed
            resitance = airResitance

        #Inputs
        if K_a in keys:
            self.velocity[0] += -speed

        if K_d in keys:
            self.velocity[0] += speed


        if K_SPACE in keys:
            if self.isOnGround:
                self.velocity[1] = -JUMP
                self.framesSinceJump = 0
                self.completedAirJumps = 0

            elif self.framesSinceJump > 8 and self.completedAirJumps < self.airJumps:
                self.completedAirJumps += 1
                self.velocity[1] = -JUMP
                self.framesSinceJump = 0

        self.framesSinceJump += 1

        #Friction
        self.velocity[0] -= resitance*self.velocity[0]


        self.coreUpdate(relevantEntities)
