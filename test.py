import pyglet

window = pyglet.window.Window(fullscreen = True)
#print 'window', window.__dict__
#image = pyglet.resource.image('image/map1.png')
#image = pyglet.sprite.Sprite(image)


music = pyglet.media.Player()
music.queue(pyglet.resource.media('audio/West_of_Henesys.mp3'))
music.queue(pyglet.resource.media('audio/login_music.mp3'))
music.play()
music.next()
music.eos_action = music.EOS_NEXT


class Player(object):
    def __init__(self, x, y, img, ratio = 1, speedx = 0, speedy = 0):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.img = pyglet.resource.image(img)
        self.img.height = int(self.img.height * ratio)
        self.img.width = int(self.img.width * ratio)
        self.img = pyglet.sprite.Sprite(self.img)
        self.img.x = self.x
        self.img.y = self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.img.x += dx
        self.img.y += dy
background = Player(0, 0, 'image/map1.png')
player = Player(200, 100, 'image/android.png', 0.5)   


@window.event
def on_draw():
    window.clear()
    background.img.draw()
    player.img.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == 65361:
        player.speedx = -3
        background.speedx = 10
    elif symbol == 65362:
        player.speedy = 3
        background.speedy = -10
    elif symbol == 65363:
        player.speedx = 3
        background.speedx = -10
    elif symbol == 65364:
        player.speedy = -3
        background.speedy = 10

@window.event
def on_text_motion(motion, *args):
    if motion == 65361:
        player.speedx = -3
        background.speedx = 10
    elif motion == 65362:
        player.speedy = 3
        background.speedy = -10
    elif motion == 65363:
        player.speedx = 3
        background.speedx = -10
    elif motion == 65364:
        player.speedy = -3
        background.speedy = 10

@window.event
def on_key_release(symbol, modifiers):
    if symbol == 65361:
        player.speedx = 0
        background.speedx = 0
    elif symbol == 65362:
        player.speedy = 0
        background.speedy = 0
    elif symbol == 65363:
        player.speedx = 0
        background.speedx = 0
    elif symbol == 65364:
        player.speedy = 0
        background.speedy = 0




def update(dt):
    player.move(player.speedx, player.speedy)
    background.move(background.speedx, background.speedy)
    #sprite.x += dt * 10

# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)

"""logs all the events to the console"""
#window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()
