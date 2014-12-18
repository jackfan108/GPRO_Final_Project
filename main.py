import pyglet
from random import choice
from Map import *
from player import *
from mobs import *

#window = pyglet.window.Window(800, 600, resizable=True)#fullscreen = True
window = pyglet.window.Window(fullscreen = True)
    
#print window.width, window.height

spd = 15

def backgroundSetup():
    pic = pyglet.resource.image('image/bg.png')
    pic.height = int(pic.height * 1.4)
    pic.width = int(pic.width * 1.5)
    pic = pyglet.sprite.Sprite(pic)
    return pic

def musicSetup():
    music = pyglet.media.Player()
    music.queue(pyglet.resource.media('audio/login_music.mp3'))
    music.queue(pyglet.resource.media('audio/West_of_Henesys.mp3'))
    music.play()
    music.eos_action = music.EOS_NEXT
    return music

def pygletSetup():
    pyglet.gl.glColor4f(0, 0, 255, 1)

def utilitySetup():
    pass

def mobsSetup():
    mob_list = []
    for i in range(20):
        mob_list.append(Mobs('/image/Mobs/SnailNew', bg, spdx = 1))
    bg.mobs = {'Snail' : mob_list}
    return bg.mobs

def mobUpdate():
    [[mob.move(mob.spdx, mob.spdy) for mob in bg.mobs[name]] for name in bg.mobs]
    [[mob.behavior() for mob in bg.mobs[name]] for name in bg.mobs]
    [[mob.stateToAnime() for mob in bg.mobs[name]] for name in bg.mobs]
    [[mob.nextframe() for mob in bg.mobs[name]] for name in bg.mobs]
    [[mob.debug() for mob in bg.mobs[name]] for name in bg.mobs]



def mobDraw():
    for mobs in bg.mobs:
        for mob in bg.mobs[mobs]:
            mob.draw()

def main():
    pass

#this is called when pyglet decides something needs to be redrawn
@window.event
def on_draw():
    window.clear()
    pic.draw()
    bg.draw()
    mobDraw()    
    player.draw()

    x1 = player.mid[0] - player.mid[2]
    x2 = player.mid[0] + player.mid[2]
    y1 = player.mid[1] - player.mid[2]
    y2 = player.mid[1] + player.mid[2]
    

    #206, 140
    pyglet.gl.glColor4f(255, 255, 255, 1)
    w = player.img.x
    z = player.img.y
    # pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y1, x1, y2)))
    # pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x2, y1, x2, y2)))
    # pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y2, x2, y2)))
    # pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( x1, y1, x2, y1)))
    # pyglet.gl.glColor4f(0, 0, 255, 1)
    # pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( w, z, w + 51, z)))
    # pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( w+51, z, w+51, z+71)))
    # pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( w, z+71, w+51, z+71)))
    # pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( w, z, w, z+71)))


@window.event
def on_key_press(symbol, modifiers):
    if symbol == 65361:
        player.spdx -= spd
        player.ori = 'left'
    elif symbol == 65362:
        player.jump(spd*2)
        player.spdy = spd*2
        player.state = 'jump'
    elif symbol == 65363:
        player.spdx += spd
        player.ori = 'right'
    elif symbol == 65364:
        player.spdy -= spd*2
        player.jumping = True
    elif symbol == 97:
        player.state = choice(['stabO1', 'stabO2', 'stabOF', 'stabT1', 'stabT2', 'stabTF'])
    elif symbol == 115:
        player.state = choice(['shoot1', 'shoot2', 'shootF'])
    elif symbol == 100:
        player.state = choice(['swingO1', 'swingO2', 'swingO3', 'swingOF', 'swingP1', 'swingP2', 'swingPF'])

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
    elif symbol == 65363:
        player.spdx -= spd
    elif symbol == 65364:
        pass
    elif symbol == 97:
        player.state = 'stand'
    elif symbol == 115:
        player.state = 'stand'
    elif symbol == 100:
        player.state = 'stand'
def update(dt):
    #print player.x, player.img.x
    bg.move(bg.spdx, bg.spdy)
    player.move(player.spdx, player.spdy)
    player.stateToAnime()
    player.nextframe()
    mobUpdate()





if __name__ == '__main__':
    music = musicSetup()
    bg = Map.pickleLoad('map1.p')
    #window.push_handlers(pyglet.window.event.WindowEventLogger())
    pic = backgroundSetup()
    bg.mobs = mobsSetup()
    bg.lim = (-40, -950)
    player = Player(600, 350, '/image/BrendanNew2', bg, (window.width, window.height))
    bg.ylim = (-150, -2000)
    bg.pickleDump('map1.p')

    pyglet.clock.schedule_interval(update, 1/30.)
    pyglet.app.run()