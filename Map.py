import pyglet
import pickle

class Map(object):
    
    def __init__(self, img, ratio = 1, ground = [], rope = []):
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

    def move(self, dx, dy):
        self.cord.x += dx
        self.cord.y += dy
        self.img.x += dx
        self.img.y += dy
        [ground.move(dx,dy) for ground in self.ground]

    def pickleDump(map, filename):
        raw = (map.imgName, map.ratio, map.ground, map.rope, map.cord)
        pickle.dump(raw, (open(filename, "wb")))

    @classmethod
    def pickleLoad(c, filename):
        f = pickle.load(open(filename, "rb"))
        mapp = Map(f[0], ratio = f[1], ground = f[2], rope = f[3])
        mapp.cord = f[4]
        mapp.img.set_position(mapp.cord.x, mapp.cord.y)
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

class Rope(object):

    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom