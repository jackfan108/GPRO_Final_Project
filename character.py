import pyglet
import os
import Image
from sprite import *

class Character(object):
    def __init__(self, x, y, path, spdx = 0, spdy = 0):
        self.x = x
        self.y = y
        self.spdx = spdx
        self.spdy = spdy
        self.sprite = Sprite(path)
        print self.sprite
        self.img = self.sprite.sprite['walk1L'][0]
        self.img.x = self.x
        self.img.y = self.y
        self.frame = 0
        self.framespd = 1.0/3
        self.anime = self.sprite.sprite['walk1L']

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.img.x += dx
        self.img.y += dy

    def draw(self):
        self.img.draw()

    def nextframe(self):
        if self.spdx != 0 or self.spdy != 0:
            self.frame += self.framespd
            self.img = self.anime[int(self.frame)%len(self.anime)]
            self.img.x = self.x
            self.img.y = self.y