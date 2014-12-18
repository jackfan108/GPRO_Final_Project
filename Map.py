import pyglet
import pickle

class Map(object):
    
    def __init__(self, img, ratio = 1, ground = [], rope = [], xlim = 0, ylim = 0):
        self.imgName = img
        self.ratio = ratio
        self.img = pyglet.resource.image(img)
        self.img.height = int(self.img.height * ratio)
        self.img.width = int(self.img.width * ratio)
        self.img = pyglet.sprite.Sprite(self.img)
        self.spdx = 0
        self.spdy = 0
        self.cord = Cord(0,0)
        self.ground = ground
        self.rope = rope
        self.xlim = xlim
        self.ylim = ylim
        self.mobs = []

    def move(self, dx, dy):
        self.cord.x += dx
        self.cord.y += dy
        self.img.x += dx
        self.img.y += dy
        [ground.move(dx, dy) for ground in self.ground]
        [[mob.move(dx, dy) for mob in self.mobs[name]] for name in self.mobs]

    def XinLim(self, x=0):
        return self.xlim[1] <= self.cord.x + x <= self.xlim[0]

    def YinLim(self, y=0):
        return self.ylim[1] <= self.cord.y + y <= self.ylim[0]

    def pickleDump(self, filename):
        raw = (self.imgName, self.ratio, self.ground, self.rope, self.cord, self.xlim, self.ylim)
        pickle.dump(raw, (open(filename, "wb")))

    @classmethod
    def pickleLoad(c, filename):
        f = pickle.load(open(filename, "rb"))
        mapp = Map(f[0], ratio = f[1], ground = f[2], rope = f[3], xlim = f[5], ylim = f[6]) #''', limit = f[5]''')
        mapp.cord = f[4]
        mapp.img.set_position(mapp.cord.x, mapp.cord.y)
        mapp.move(-mapp.cord.x-950, -mapp.cord.y-200) # 2557, 1552 (-40) & (-1750)
        return mapp

    def draw(self):
        self.img.draw()
        for ground in self.ground:
            ground.draw()

class Cord(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "cordinate is (" + str(self.x) + ', ' + str(self.y) + ')'

    def add(a, b):
        return Cord(a.x + b.x, a.y + b.y)

    def subtract(a, b):
        return Cord(a.x - b.x, a.y - b.y)

class Ground(object):

    def __init__(self, refmap, left, right):
        self.left = Cord.add(refmap.cord, left)
        self.right = Cord.add(refmap.cord, right)   

    def move(self, dx, dy):
        self.left.x += dx
        self.right.x += dx
        self.left.y += dy
        self.right.y += dy

    def draw(self):
        x1 = self.right.x
        y1 = self.right.y
        x2 = self.left.x
        y2 = self.left.y
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y1, x2, y2)))

    def onGroundY(self, n):
        if n == self.left.y:
            return True
        return False

    def onGroundX(self, n):
        if self.left.x <= n <= self.right.x:
            return True
        return False

class Rope(object):

    def __init__(self, top, bot):
        self.top = top
        self.bot = bot

    def move(self, dx, dy):
        self.top.x += dx
        self.bot.x += dx
        self.top.y += dy
        self.bot.y += dy

    def draw(self):
        x1 = self.top.x
        y1 = self.top.y
        x2 = self.bot.x
        y2 = self.bot.y
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y1, x2, y2)))