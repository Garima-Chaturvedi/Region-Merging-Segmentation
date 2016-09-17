from PIL import Image
import numpy
import scipy
import math
from scipy.misc import toimage


#Reading image dimensions
i = Image.open('Peppers.jpg')
width, height = i.size

#Reading image
im = numpy.array(Image.open('Peppers.jpg'))

#Recursively merging regions based on criteria of similarity in values of image pixels intensity
for x in range (1, height-1):
    for y in range(1, width-1):
        if (im[x,y]> im[x,y-1]-10 and im[x,y]< im[x,y-1]+20 ):
            im[x,y]=im[x,y-1]
        elif (im[x,y]> im[x-1,y]-30 and im[x,y]< im[x-1,y]+30):
            im[x,y]=im[x-1,y]
            

toimage(im).show()

toimage(im).save('RegMergeRecur.jpeg')

