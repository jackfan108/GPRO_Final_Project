import pyglet
from character import *
from Map import *
from random import choice, randint

GRAVITY = 2

class Mobs(Character):

    def __init__(self, path, BG, spdx = 0, spdy = 0):
        grd = choice(BG.ground)
        self.grd = grd
        x = randint(grd.left.x, grd.right.x)
        Character.__init__(self, x, grd.left.y, path, BG, spdx = spdx, spdy = spdy)
        self.moving = True
        self.state = 'move'

    def move(self, dx, dy):
        if self.onGround(dx):
            self.x += dx
            self.y += dy
            self.img.x += dx
            self.img.y += dy
        else:
            self.spdx = -self.spdx
            if self.ori == 'left':
                self.ori = 'right'
            else:
                self.ori = 'left'

    def behavior(self):
        if randint(1,30)%30 == 0:
            self.spdx = -self.spdx
            if self.ori == 'left':
                self.ori = 'right'
            else:
                self.ori = 'left'

    def onGround(self, dx = 0):
        if self.grd.left.x <= self.x + dx <= self.grd.right.x:
            return True
        return False

    def stateToAnime(self):
        if self.ori == 'left':
            self.anime = self.sprite.sprite[self.state + 'L']
        else:
            self.anime = self.sprite.sprite[self.state + 'R']

    def loadSprite(self, mode):
        return

    def debug(self):
        #print self.x, self.img.x
        pass