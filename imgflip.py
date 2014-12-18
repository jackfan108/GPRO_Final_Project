import Image
import ImageOps
import os
import matplotlib.image as mpimg


path = os.path.dirname(os.path.abspath(__file__)) + '/image/Arrows/redArrow'
spritelist = [f for f in os.listdir(path)]
for spritename in spritelist:
    if spritename[-4:] != '.png':
        continue
    name = spritename[:-4]
    print name
    img = Image.open("image/Arrows/redArrow/" + spritename)
    img = ImageOps.mirror(img)
    img.save("image/Arrows/redArrowNew/" + name + '_flip.png')
