import pyglet
from Map import *
from player import *

window = pyglet.window.Window(1200, 800, resizable=True)#fullscreen = True
#window =pyglet.window.Window(fullscreen = True)

print window.width, window.height

spd = 15

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
    player.draw()
    x1 = player.mid[0] - player.mid[2]
    x2 = player.mid[0] + player.mid[2]
    y1 = player.mid[1] - player.mid[2]
    y2 = player.mid[1] + player.mid[2]
    pyglet.gl.glColor4f(0, 0, 255, 1)
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y1, x1, y2)))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x2, y1, x2, y2)))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y2, x2, y2)))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y1, x2, y1)))


@window.event
def on_key_press(symbol, modifiers):
    if symbol == 65361:
        player.spdx -= spd
        player.anime = player.sprite.sprite['walk1L']
    elif symbol == 65362:
        player.spdy += spd
    elif symbol == 65363:
        player.spdx += spd
        player.anime = player.sprite.sprite['walk1R']
    elif symbol == 65364:
        player.spdy -= spd

# @window.event
# def on_text_motion(motion, *args):
#     if motion == 65361:
#         player.nextframe()
#     elif motion == 65362:
#         player.nextframe()
#     elif motion == 65363:
#         player.nextframe()
#     elif motion == 65364:
#         player.nextframe()

@window.event
def on_key_release(symbol, modifiers):
    if symbol == 65361:
        player.spdx += spd
    elif symbol == 65362:
        player.spdy -= spd
    elif symbol == 65363:
        player.spdx -= spd
    elif symbol == 65364:
        player.spdy += spd

def update(dt):
    bg.move(bg.spdx, bg.spdy)
    player.move(player.spdx, player.spdy)
    #print player.x, player.y
    player.nextframe()
    #print bg.lim, bg.cord



if __name__ == '__main__':
    #music = musicSetup()
    bg = Map.pickleLoad('map1.p')
    bg.lim = (-40, -950)
    player = Player(700, 250, '/image/Jack', bg, (window.width, window.height))
    bg.ylim = (-150, -2000)
    bg.pickleDump('map1.p')
    print bg.xlim, bg.ylim

    pyglet.clock.schedule_interval(update, 1/30.)
    pyglet.app.run()