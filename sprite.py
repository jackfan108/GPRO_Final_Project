import os
import pyglet

#window = pyglet.window.Window(800, 600, resizable=True)#fullscreen = True

class Sprite(object):
    def __init__(self, path):
        self.sprite = {}
        path = os.path.dirname(os.path.abspath(__file__)) + path
        spritelist = [f for f in os.listdir(path)]
        for name in spritelist:
            for i in range(len(name)):
                if name[i] == '_':
                    img = pyglet.resource.image('image/Jack/' + name)
                    img = pyglet.sprite.Sprite(img)
                    if name[:i] in self.sprite.keys():
                        self.sprite[name[:i]].append(img)
                    else:
                        self.sprite[name[:i]] = [img]



if __name__ == '__main__':
    a = Sprite('/image/Jack')
    print a.sprite
