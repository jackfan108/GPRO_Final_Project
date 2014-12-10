import Image
import ImageOps
import os
import matplotlib.image as mpimg


path = os.path.dirname(os.path.abspath(__file__)) + '/image/Jack/'
spritelist = [f for f in os.listdir(path)]
for spritename in spritelist:
    name = spritename[:-4]
    print name
    img = Image.open("image/JackSprite/" + spritename)
    img = ImageOps.mirror(img)
    img.save("image/JackSprite/" + name + '_flip.png')
