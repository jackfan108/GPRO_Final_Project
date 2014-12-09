import pyglet
from Map import *

window =pyglet.window.Window(fullscreen = True)
#window = pyglet.window.Window(800, 600, resizable=True)#fullscreen = True

def backgroundSetup():
    pass

def musicSetup():
    music = pyglet.media.Player()
    music.queue(pyglet.resource.media('audio/West_of_Henesys.mp3'))
    music.queue(pyglet.resource.media('audio/login_music.mp3'))
    music.play()
    music.eos_action = music.EOS_NEXT
    return music

def pygletSetup():
    pyglet.gl.glColor4f(0, 0, 255, 1)

def utilitySetup():
    pass

def main():
    pass

#this is called when pyglet decides something needs to be redrawn
@window.event
def on_draw():
    window.clear()
    bg.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == 65361:
        bg.spdx = 10
    elif symbol == 65362:
        bg.spdy = -10
    elif symbol == 65363:
        bg.spdx = -10
    elif symbol == 65364:
        bg.spdy = 10

# @window.event
# def on_text_motion(motion, *args):
#     if motion == 65361:
#         bg.spdx = 10
#     elif motion == 65362:
#         bg.spdy = -10
#     elif motion == 65363:
#         bg.spdx = -10
#     elif motion == 65364:
#         bg.spdy = 10

@window.event
def on_key_release(symbol, modifiers):
    if symbol == 65361:
        bg.spdx = 0
    elif symbol == 65362:
        bg.spdy = 0
    elif symbol == 65363:
        bg.spdx = 0
    elif symbol == 65364:
        bg.spdy = 0

def update(dt):
    bg.move(bg.spdx, bg.spdy)




if __name__ == '__main__':
    #music = musicSetup()
    bg = Map.pickleLoad('map1.p')

    pyglet.clock.schedule_interval(update, 1/60.)
    pyglet.app.run()