import pyglet
from character import *



class Player(Character):
    def __init__(self, x, y, path, ratio = 1, spdx = 0, spdy = 0):
        Character.__init__(self, x, y, path)


    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.img.x += dx
        self.img.y += dy

    def draw(self):
        self.img.draw()

    def loadSprite(self, mode):
        return
