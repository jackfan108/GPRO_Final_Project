import Image
import ImageOps
import os
import matplotlib.image as mpimg


path = os.path.dirname(os.path.abspath(__file__)) + '/image/Mobs/Snail/'
spritelist = [f for f in os.listdir(path)]
for spritename in spritelist:
    if spritename[-4:] == '.png':
        name = spritename[:-4]
        print 'name = ', name
        img = Image.open("image/Mobs/Snail/" + spritename)
        pos = -1
        operation = True

        for i in range(len(name[:])):
            if name[i] == '_' and pos == -1:
                pos = i
            if name[i:i+4] == "flip":
                newname = name[:pos] + 'R' + name[pos:pos+2] + '.png'
                operation = False
                break
        if operation == True:
            #print 'hi', pos, name,  name[pos-1:pos+1]
            newname = name[:pos] + 'L' + name[pos:pos+2] + '.png'
        operation = True
        print 'newname = ', newname
        img.save("image/Mobs/SnailNew/" + newname)
