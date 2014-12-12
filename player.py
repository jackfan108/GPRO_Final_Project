import pyglet
from character import *
from Map import *



class Player(Character):
    def __init__(self, x, y, path, BG, win, spdx = 0, spdy = 0):
        Character.__init__(self, x, y, path)
        self.map = BG
        self.mid = (win[0]/2-100, win[1]/2, 100)

    def move(self, dx, dy):
        if self.XaroundMid() and self.map.XinLim(-dx):
            self.map.move(-dx, 0)
        else:
            self.x += dx
            self.img.x += dx
        if self.YaroundMid() and self.map.YinLim(-dy):
            self.map.move(0, -dy)
        else:
            self.y += dy
            self.img.y += dy

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
