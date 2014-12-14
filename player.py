import pyglet
from character import *
from Map import *

GRAVITY = 2

class Player(Character):
    def __init__(self, x, y, path, BG, win, spdx = 0, spdy = 0):
        Character.__init__(self, x, y, path, BG)
        self.mid = (win[0]/2-100, win[1]/2, 100)
        self.onGround = False
        self.jumping = False

    def move(self, dx, dy):
        print 'spdy', self.spdy, 'onGround', self.onGround, 'jumping', self.jumping
        if self.XaroundMid() and self.map.XinLim(-dx):
            self.map.move(-dx, 0)
        else:
            self.x += dx
            self.img.x += dx
        self.onGround, dy = self.groundCheck(dx, dy)
        #print self.map.ylim
        #print self.map.YinLim(-dy), 'hi'
        if self.YaroundMid() and self.map.YinLim(-dy):
            self.map.move(0, -dy)
        else:
            self.y += dy
            self.img.y += dy
        if self.onGround and not self.jumping:
            self.spdy = 0
        else:
            self.spdy -= GRAVITY
        if self.jumping and self.spdy == 0:
            self.jumping = False

    def groundCheck(self, dx = 0, dy = 0):
        a = min(self.y, self.y + dy)
        b = max(self.y, self.y + dy)
        for ypos in range(a + 1, b + 1):
            for ground in self.map.ground:
                if ground.onGroundY(ypos):
                    if ground.onGroundX(self.x + dx):
                        return (True, ypos - self.y)
        return (False, dy)

    def jump(self, dy):
        if not self.onGround:
            self.jumping = True
            if self.YaroundMid() and self.map.YinLim(-dy):
                self.map.move(0, -dy)
            else:
                self.y += dy
                self.img.y += dy
        else:
            pass


    def XaroundMid(self):
        midx = self.mid[0] - self.mid[2] <= self.x < self.mid[0] + self.mid[2]
        return midx
    
    def YaroundMid(self):
        midy = self.mid[1] - self.mid[2] <= self.y < self.mid[1] + self.mid[2]
        return midy

    def draw(self):
        self.img.draw()

    def loadSprite(self, mode):
        return
