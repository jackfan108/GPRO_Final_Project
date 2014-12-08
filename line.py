import pyglet
from mapcreator import *


if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, resizable=True)#fullscreen = True
    background = Map('image/map1.png')

    @window.event
    def on_draw():
        window.clear()
        background.img.draw()
        pyglet.gl.glColor4f(0, 0, 255, 1)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( 10, 1, 10, 400))
)

    pyglet.app.run()