
import skimage
from skimage import data, io, color
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

rocket_image = data.rocket()
io.imshow(rocket_image)
plt.show()

#check shape of the image
rocket_image.shape

#print the image matrix
rocket_image

#Modify image to show edges in the image
from skimage.feature import canny
rocket_image_gray = color.rgb2gray(rocket_image)
rocket_image_with_edges = canny(rocket_image_gray)
io.imshow(rocket_image_with_edges)
plt.show()