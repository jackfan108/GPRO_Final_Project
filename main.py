import pyglet as pg
from lib import *


def backgroundSetup():
    pass

def musicSetup():

def main():
    pass

#what happens when key is pressed
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

#what happens when key is held
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

#what happens when key is released
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



if __name__ == '__main__':
    main()