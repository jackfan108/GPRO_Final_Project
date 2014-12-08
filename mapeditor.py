import pyglet
from mapcreator import *
import pickle

window = pyglet.window.Window(800, 600, resizable=True)#fullscreen = True




if __name__ == '__main__':
    backgroundraw = pickle.load(open("test.p", "rb"))
    background = Map.reloadFromPickle(backgroundraw)
    print 'hihi', background.cord
    pyglet.gl.glColor4f(0, 0, 255, 1)

    print background

    @window.event
    def on_draw():
        window.clear()
        background.img.set_position(background.cord.x, background.cord.y)
        background.img.draw()
        for ground in background.ground:
            x1 = ground.right.x
            y1 = ground.right.y
            x2 = ground.left.x
            y2 = ground.left.y
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y1, x2, y2)))


    pyglet.app.run()