from scipy import signal as sig
import numpy as np

import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = "test_image/sup_img.jpg"

image = cv.imread(img)
print('opend')

gray_img = cv.cvtColor(image,cv.COLOR_BGR2GRAY)


robertsKernelF = [[0,-1],
                 [1,0]]

robertsKernelS = [[-1,0],
                 [0,1]]

sobelKernelF = [[-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]]

sobelKernelS = [[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]]

hzKernel = [[1,0,1],
            [0,1,0],
            [1,0,1]]

dilat_Kernel = [[0,0,0],
                [1,1,1],
                [0,0,0]]

erose_Kernel = [[1,1,1],
                [1,1,1],
                [1,1,1]]

erose_Kernel = np.array(erose_Kernel)
dilat_Kernel = np.array(dilat_Kernel)

laplacian_kernel = [[0,1,0],
                    [1,-4,1],
                    [0,1,0]]

inverse = [[-1]]

robertsKernelFT = np.transpose(robertsKernelF)
robertsKernelST = np.transpose(robertsKernelS)
sobelKernelFT = np.transpose(sobelKernelF)
sobelKernelST = np.transpose(sobelKernelS)

def dilat(img,kernel):
    y,x = img.shape
    m,n = kernel.shape
    add_img = np.zeros((y+2,x+2))
    for i in range(y):
        for j in range(x):
            add_img[i+1,j+1] = img[i,j]
    ay,ax = add_img.shape
    ay = ay - m + 1
    ax = ax - m + 1
    new_img = np.zeros((ay,ax))
    for i in range(ay):
        for j in range(ax):
            new_img[i,j] = np.max(add_img[i:i+m, j:j+n]*kernel)
    return new_img

def erose(img,kernel):
    y,x = img.shape
    m,n = kernel.shape
    add_img = np.zeros((y+2,x+2))
    for i in range(y):
        for j in range(x):
            add_img[i+1,j+1] = img[i,j]
    ay,ax = add_img.shape
    ay = ay - m + 1
    ax = ax - m + 1
    new_img = np.zeros((ay,ax))
    for i in range(ay):
        for j in range(ax):
            temp = []
            y,x = np.where(kernel == 1)
            part = add_img[i:i+m, j:j+n]*kernel
            for pos in range(0,len(y)):
                temp.append(part[y[pos]][x[pos]])
            new_img[i,j] = np.min(temp)
    return new_img

def kernelApply(kernel, img):
    res = sig.convolve2d(img,kernel)
    return res

def matrix_sum(mat1,mat2):
    temporary_arr = []
    for temp in mat1:
        temporary_arr.append(temp)
    for i in range(len(mat1)):
        for g in range(len(mat2)):
            temporary_arr[i][g] += mat2[i][g]
    return temporary_arr

def matrix_diff(mat1,mat2):
    temporary_arr = []
    for temp in mat1:
        temporary_arr.append(temp)
    for i in range(len(mat1)):
        for g in range(len(mat2)):
            temporary_arr[i][g] -= mat2[i][g]
    return temporary_arr

def depth(type, img, kernel,times):
    if type == "erose":
        res = erose(img, kernel)
        for i in range(times):
            res = erose(res, kernel)
    elif type == "dilat":
        res = dilat(img, kernel)
        for i in range(times):
            res = dilat(res, kernel)
    return res

cornerimg_F = kernelApply(sobelKernelF, gray_img)
cornerimg_S = kernelApply(sobelKernelST, gray_img)

lap = kernelApply(laplacian_kernel,gray_img)

hz = kernelApply(inverse,gray_img)

sum = matrix_sum(cornerimg_F,cornerimg_S)

ers = depth('erose',gray_img,dilat_Kernel,10)

dil = dilat(gray_img,dilat_Kernel)




fig2 = plt.figure(3)
img1,img2 = fig2.add_subplot(121),fig2.add_subplot(122)
img1.imshow(gray_img,cmap = 'gray')
img2.imshow(ers,cmap = 'gray')

plt.show()