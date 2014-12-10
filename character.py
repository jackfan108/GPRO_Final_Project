import pyglet
import os
import Image
from sprite import *

class Character(object):
    def __init__(self, x, y, path, speedx = 0, speedy = 0):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.sprite = Sprite(path)
        print self.sprite
        self.img = self.sprite.sprite['walk1L'][0]
        self.img.x = self.x
        self.img.y = self.y
        self.frame = 0
        self.anime = self.sprite.sprite['walk1L']

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.img.x += dx
        self.img.y += dy

    def draw(self):
        self.img.draw()

    def nextframe(self):
        self.frame += 1
        self.img.x = self.x
        self.img.y = self.y
        self.img = self.anime[self.frame%len(self.anime)]