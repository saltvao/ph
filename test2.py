import numpy as np
from PIL import Image
import cv2

UC = ''.join([chr(ord(i)+975)for i in"ABCDEF2GHIJKLMNOPQRSTUVWXYZ[\\]^_`"]) + "I"
my_label = UC[int(8.000000000000000000e+00)]


a = np.matrix([1,4])
b = a.tolist()



from matplotlib.pyplot import imread


a = np.matrix([[0,1,0],[1,1,1],[0,1,0]]) 
b = [[0,0,0],
     [1,1,1],
     [0,0,0]]

x,y = np.where(a == 1)

print(x,y)
