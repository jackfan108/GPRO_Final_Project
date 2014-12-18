import pyglet
import os
import Image
from sprite import *

class Character(object):
    def __init__(self, x, y, path, BG, spdx = 0, spdy = 0):
        self.x = x
        self.y = y
        self.spdx = spdx
        self.spdy = spdy
        self.sprite = Sprite(path)
        self.img = self.sprite.sprite['standL'][0]
        self.img.x = self.x - self.img._texture.width/2
        self.img.y = self.y
        self.frame = 0
        self.framespd = 1.0/3
        self.anime = self.sprite.sprite['standL']
        self.map = BG
        self.ori = 'left'

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.img.x += dx
        self.img.y += dy

    def draw(self):
        self.img.draw()

    def nextframe(self):
        self.frame += self.framespd
        self.img = self.anime[int(self.frame)%len(self.anime)]
        self.img.x = self.x - self.img._texture.width/2
        self.img.y = self.y