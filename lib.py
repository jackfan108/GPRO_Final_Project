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