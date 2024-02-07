import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt



data = open("cyrillic_data_1.csv","a+")
label = open("cyrillic_label_1.csv","a+")
X = np.loadtxt('cyrillic_data.csv', delimiter=",")
Y = np.loadtxt('cyrillic_label.csv', delimiter=",")

class Morph:

    def kernelApply(kernel, img):
        res = sig.convolve2d(img,kernel)
        return res
    

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

    gaussKernel = [[1,2,1],
                  [2,4,2],
                  [1,2,1]]
    pass



img1 = Morph.kernelApply(Morph.sobelKernelS,X[1].reshape(28,28))

 

plt.imshow(img1)



plt.show()

data.close()
label.close()



