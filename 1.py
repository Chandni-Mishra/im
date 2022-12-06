from collections import Counter #for iterating thorugh all values
from sklearn.cluster import KMeans # used for kmeans algo and sklearn is used for clustering here
from matplotlib import colors
import matplotlib.pyplot as plt #Matplotlib is a python library used to create 2D graphs and plots 
import numpy as np
import cv2 as cv 
def rgb_to_hex(rgb_color):
  hex_color = "#"
  for i in rgb_color:
    i = int(i)
    hex_color += ("{:02}".format(i))
  return hex_color
print(rgb_to_hex(((255,0,0))))
img_name = "img1.jpg"
raw_img = cv.imread(img_name)
raw_img = cv.cvtColor(raw_img,cv.COLOR_BGR2RGB)
#to convert an image to rgb format

