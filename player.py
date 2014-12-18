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
        self.moving = False
        self.state = 'stand'

    def move(self, dx, dy):
        if dx == 0 and dy == 0 and self.onGround:
            if self.ori == 'left' and not self.moving:
                self.anime = self.sprite.sprite['standL']
            elif self.ori == 'right' and not self.moving:
                self.anime = self.sprite.sprite['standR']
        else:
            if self.XaroundMid() and self.map.XinLim(-dx):
                self.map.move(-dx, 0)
            else:
                self.x += dx
                self.img.x += dx
            temp = dy
            self.onGround, dy = self.groundCheck(dx, dy)
            if self.jumping:
                dy = temp
            if self.YaroundMid() and self.map.YinLim(-dy):
                self.map.move(0, -dy)
            else:
                self.y += dy
                self.img.y += dy
            if not self.jumping:
                if self.onGround:
                    self.spdy = 0
                    self.state = 'stand'
                else:
                    self.spdy -= GRAVITY
            else:
                    self.spdy -= GRAVITY

            # if self.onGround and not self.jumping:
            #     self.spdy = 0
            #     self.state = 'stand1'
            # else:
            #     self.spdy -= GRAVITY
            



            if self.jumping and self.spdy == 0:
                self.jumping = False

            if dx != 0:
                if self.onGround:
                    self.state = 'walk1'
                else:
                    self.state = 'jump'

    def groundCheck(self, dx = 0, dy = 0):
        a = min(self.y, self.y + dy)
        b = max(self.y, self.y + dy)
        for ypos in range(a, b + 1):
            for ground in self.map.ground:
                if ground.onGroundY(ypos):
                    if ground.onGroundX(self.x + dx):
                        if self.jumping:
                            return (True, dy)
                        else:
                            return (True, ypos - self.y)
        return (False, dy)

    def jump(self, dy):
        m = pyglet.media.Player()
        m.queue(pyglet.resource.media('audio/jump.mp3'))
        m.play()
        self.jumping = True
        if self.ori == 'left':
            self.anime = self.sprite.sprite['jumpL']
        else:
            self.anime = self.sprite.sprite['jumpR']
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

    def stateToAnime(self):
        if self.ori == 'left':
            self.anime = self.sprite.sprite[self.state + 'L']
        else:
            self.anime = self.sprite.sprite[self.state + 'R']

    def loadSprite(self, mode):
        return
