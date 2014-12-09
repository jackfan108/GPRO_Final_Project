import pyglet
from Map import *
import pickle

window = pyglet.window.Window(fullscreen = True)
#window = pyglet.window.Window(800, 600, resizable=True)#fullscreen = True

@window.event
def on_draw():
    window.clear()
    background.img.draw()
    for ground in background.ground:
        x1 = ground.right.x
        y1 = ground.right.y
        x2 = ground.left.x
        y2 = ground.left.y
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

# @window.event
# def on_text_motion(motion, *args):
#     if motion == 65361:
#         background.spdx = 10
#     elif motion == 65362:
#         background.spdy = -10
#     elif motion == 65363:
#         background.spdx = -10
#     elif motion == 65364:
#         background.spdy = 10

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

def update(dt):
    global printcount
    background.move(background.spdx, background.spdy)
    # if printcount%60 == 0:
    #     for ground in background.ground:
    #         print ground.left, ground.right
    #     print ':DD'
    #     printcount = 0
    printcount += 1


if __name__ == '__main__':
    background = Map.pickleLoad('map1.p')
    printcount = 0
    pyglet.gl.glColor4f(0, 0, 255, 1)

    # for g in background.ground:
    #     print g.left.x, g.right.x

    #raw = Map.reduceForPickle(background)
    #pickle.dump( raw , open("map1.p", "wb"))

    
    
    pyglet.clock.schedule_interval(update, 1/60.)
    pyglet.app.run()
