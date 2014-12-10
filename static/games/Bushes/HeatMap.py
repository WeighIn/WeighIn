
__author__ = 'krishnamittal'

import numpy,cv2,cv
from PIL import Image
from pylab import *


def test1(Pixels,Points,radius1,radius2,size1,size2):
    for x, y in Points:
        if (y < size1 and x < size2):

            i = y - radius1

            while i <= (y + radius1):
                if (i >= 0) and (i<size1):

                    j = x - radius2
                    while j <= (x + radius2):
                        if (j >= 0) and (j < size2):
                            Pixels[i, j] += 1

                        j += 1

                i += 1



def average(Pixels,x,y,radius1,radius2,size1,size2):
    count = 0.0
    total = 0.0
    if (y < size1 and x < size2):
        total += Pixels[y, x]
        count += 1
        i = y - radius1

        while i <= y + radius1:
            if i >= 0 and i < size1:
                j = x - radius2
                while j <= x + radius2:
                    if j >= 0 and j < size2:
                        total += Pixels[i, j]
                        count += 1
                    j += 1
            i += 1
        if count > 0:
            return total/count


def main():
    """im = array(Image.open('engaged.jpg'))
    imshow(im)
    print "Please click 3 points"
    x = ginput(3)
    print "you clicked:",x
    show()"""

    size1 = int(input("Enter size1 of canvas: "))
    size2= int(input("Enter size2 of canvas:"))
    radius1 = int(raw_input("Enter height of rectangle around click:"))
    radius2=  int(raw_input("Enter width of rectangle around click:"))

    Pixels = numpy.ndarray((size1, size2),dtype='uint8')
    Pixels.fill(0)
    test1(Pixels, [(453,346),(446,310),(429,327),(436,262),(441,279),(451,236),(394,352),(379,303),(373,269),(353,339),(364,229),(387,245),(384,207),(383,194),(261,297),(235,303),(236,264),(242,240),(275,236),(266,255),(182,287),(176,249),(180,230),(153,230),(139,280),(121,250),(117,219),(99,258),(41,240),(50,203),(399,343),(384,306),(380,274),(378,243),(378,209),(379,195),(353,257),(349,330),(360,307),(460,339),(441,311),(432,317),(445,284),(450,250),(253,301),(252,271),(245,245),(275,240),(268,266),(188,287),(188,246),(187,228),(167,236),(147,271),(143,243),(106,231),(107,267),(47,243),(49,207),(47,183),(395,346),(390,318),(384,285),(350,330),(361,291),(379,252),(376,212),(380,188),(453,345),(434,327),(440,303),(447,280),(448,257),(450,238),(268,302),(267,265),(267,231),(244,247),(239,279),(237,316),(172,282),(171,257),(167,220),(185,222),(140,258),(141,244),(111,227),(101,259),(122,272),(43,239),(44,198),(53,228),(47,243),(99,263),(105,227),(121,238),(121,267),(156,257),(150,232),(180,226),(181,270),(175,290),(243,300),(243,268),(243,238),(265,239),(267,263),(268,291),(350,335),(363,309),(370,276),(396,348),(390,314),(453,330),(434,326),(441,271),(448,288),(447,247),(382,245),(377,221)], radius1,radius2, size1,size2)
    print "average=" + str(average(Pixels, 2, 2, radius1,radius2, size1,size2))
    for row in Pixels:
        print row

    maximum=numpy.amax(Pixels, axis=None, out=None)
    print maximum
    multiplier=256/maximum-1
    data = np.zeros( (size1,size2,3), dtype=np.uint8)
    for x in range(size1):
        for y in range(size2):
            value=Pixels[x,y]
            data[x,y]=[multiplier*value,multiplier*value,multiplier*value]

    img = Image.fromarray(data, 'RGB')
    img.save('new.png')


main()






