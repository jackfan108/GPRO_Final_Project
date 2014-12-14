import xml.etree.ElementTree as ET
import pyglet

window = pyglet.window.Window(400, 400, resizable=True)#fullscreen = True
pyglet.gl.glColor4f(255, 255, 255, 1)
count = 0

"""This script shows the sprite images from BannedStory 4, using data.xml to
   load meta data. Sprites images have red boarders and the intersection of 
   white lines are the cordinates provided by the xml file.
"""

@window.event
def on_draw():
    window.clear()
    img.draw()
    pyglet.gl.glColor4f(255, 255, 255, 1)
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( -x, 1, -x, 400)))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( 1, -y, 400, -y)))
    pyglet.gl.glColor4f(255, 0, 0, 1)
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( w, 1, w, h)))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', ( 1, h, w, h)))

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == 1:
        global count
        #print 'key pressed :DD'
        count += 1


tree = ET.parse('data.xml')
root = tree.getroot()
#print root._children
#print root._children[0].attrib['image']


def update(dt):
    global img, x, y, w, h
    ele = root._children[count]
    #print ele.attrib['image']
    img = pyglet.resource.image(ele.attrib['image'])
    # print 'width = ', img.width, 'height = ', img.height
    w = img.width
    h = img.height
    img = pyglet.sprite.Sprite(img)
    x = int(ele.attrib['x'])
    y = int(ele.attrib['y'])


ele = root._children[0]
img = pyglet.resource.image(ele.attrib['image'])
w = img.width
h = img.height
img = pyglet.sprite.Sprite(img)
x = int(ele.attrib['x'])
y = int(ele.attrib['y'])

pyglet.clock.schedule_interval(update, 1/60.)
pyglet.app.run()
