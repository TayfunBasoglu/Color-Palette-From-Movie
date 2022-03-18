# For google colab

import cv2 as cv
from skimage import io
from google.colab.patches import cv2_imshow
import numpy as np
from sklearn.cluster import KMeans

#Read Image
image = io.imread("https://www.themoviedb.org/t/p/original/bKCKP0j7Ua9qceKH0TEXRDQ3EVs.jpg")[:,:,::-1]

#KNN Model
n_clusters = 10
model = KMeans(n_clusters=n_clusters,random_state=1).fit(image.reshape(-1,3))

#Each Color-box Size
height = 100
width = 100

#Create Color Boxes
color_palette = []
for i in model.cluster_centers_: 
  img = np.full((height, width, 3), i, np.uint8)   #create color box and fill with center
  img = cv.copyMakeBorder(img,5,5,2,2,cv.BORDER_CONSTANT,value=[0,0,0])   #add black border
  color_palette.append(img)

#Create Color Palette
palette = color_palette[0]
for i in color_palette[1:]:
  palette = np.concatenate((palette,i),axis=1)
palette = cv.copyMakeBorder(palette,0,0,3,3,cv.BORDER_CONSTANT,value=[0,0,0])

#Show
cv2_imshow(image)
cv2_imshow(palette)
