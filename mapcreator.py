import pyglet
import pickle
#from lib import *

"""This script allows the user to manually draw lines for ground of a map 
    and saves the drawn line with the map as a pickle file. Enter file name
    and start drawing. Hold mouse left to start a line and release at the
    end point of the line. """

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

    def reduceForPickle(map):
        return (map.imgName, map.ratio, map.ground, map.rope, map.cord)

    @classmethod
    def reloadFromPickle(c, data):
        mapp = Map(data[0], ratio = data[1], ground = data[2], rope = data[3])
        mapp.cord = data[4]
        print mapp.cord
        return mapp

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

class Rope(object):

    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

if __name__ == '__main__':
    #window = pyglet.window.Window(fullscreen = True)
    window = pyglet.window.Window(800, 600, resizable=True)#fullscreen = True
    printcount = 0
    pyglet.gl.glColor4f(0, 0, 255, 1)
    
    @window.event
    def on_draw():
        window.clear()
        background.img.draw()
        for ground in background.ground:
            x1 = ground.right.x
            y1 = ground.right.y
            x2 = ground.left.x
            y2 = ground.left.y
            if x1 > 0 and y1 > 0:
                pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y1, x2, y2)))



    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == 65361:
            background.spdx = 10
        elif symbol == 65362:
            background.spdy = -10
        elif symbol == 65363:
            background.spdx = -10
        elif symbol == 65364:
            background.spdy = 10

    @window.event
    def on_text_motion(motion, *args):
        if motion == 65361:
            background.spdx = 10
        elif motion == 65362:
            background.spdy = -10
        elif motion == 65363:
            background.spdx = -10
        elif motion == 65364:
            background.spdy = 10

    @window.event
    def on_key_release(symbol, modifiers):
        if symbol == 65361:
            background.spdx = 0
        elif symbol == 65362:
            background.spdy = 0
        elif symbol == 65363:
            background.spdx = 0
        elif symbol == 65364:
            background.spdy = 0
        if symbol == 100:
            print background.ground
            backgrounddump = Map.reduceForPickle(background)
            pickle.dump(backgrounddump, open( "test.p", "wb" ) )

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == 1:
            #print 'key pressed :DD'
            background.ground.append(Ground(background, Cord.subtract(Cord(x, y), background.cord), Cord(0,0)))
            pass

    @window.event
    def on_mouse_release(x, y, button, modifiers):
        if button == 1:
            #print 'key released :DD'
            #print background.ground
            background.ground[-1].right = Cord(x, background.ground[-1].left.y)
            
            #print Cord.subtract(Cord(x, y), background.cord)
            #pass

    def update(dt):
        global printcount
        background.move(background.spdx, background.spdy)
        if printcount%60 == 0:
            for ground in background.ground:
                print ground.left, ground.right
            print ':DD'
            printcount = 0
        printcount += 1
        #sprite.x += dt * 10





    # mapp = Map('img')
    # ground1 = Ground(Cord(3, 7), Cord(10, 7))
    # mapp.ground.append(ground1)
    # print mapp.ground[0].left, mapp.ground[0].right
    # mapp.move(2,3)
    # print 'move (2,3)'
    # print mapp.ground[0].left, mapp.ground[0].right
    # ground2 = Ground(Cord(10,2), Cord(20, 2))
    # mapp.ground.append(ground2)
    # print mapp.ground[1].left, mapp.ground[1].right
    # mapp.move(4,5)
    # print 'move (4,5)'
    # print mapp.ground[0].left, mapp.ground[0].right, mapp.ground[1].left, mapp.ground[1].right
    background = Map('image/map1.png')
    #testground = Ground(background, Cord(20, 30), Cord(50, 30))
    printcount = 0

    #background = Player(0, 0, 'image/map1.png')
    pyglet.clock.schedule_interval(update, 1/60.)
    """logs all the events to the console"""
    #window.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.app.run()