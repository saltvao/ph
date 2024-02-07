import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread


import zipfile
import string

# Load images and labels
X = np.loadtxt('cyrillic_data.csv', delimiter=",")
Y = np.loadtxt('cyrillic_label.csv', delimiter=",")

m,n = X.shape


def init_params():
    W1 = np.random.randn(33,784)
    b1 = np.random.randn(33,1)
    W2 = np.random.randn(33,33)
    b2 = np.random.randn(33,1)
    W3 = np.random.randn(33,33)
    b3 = np.random.randn(33,1)
    return W1,b1,W2,b2,W3,b3

def ReLU(Z):
    return np.maximum(0,Z)

def dReLU(A):
    return A > 0

def SoftMaxFunc(Z):
    A = np.exp(Z) / np.sum(np.exp(Z))
    return A

def forward_propagation(W1,b1,W2,b2,W3,b3,X):
    X = np.array(X).reshape(784,1)
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = ReLU(Z2)
    Z3 = W3.dot(A2)
    A3 = SoftMaxFunc(Z3)
    return Z1, A1, Z2, A2, Z3, A3

def one_hot(label):
    counter = 0
    Y_one_hot = np.zeros((1,33))
    for i in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
        if i == label:
            Y_one_hot[0][counter] = 1
        counter += 1
        pass
    Y_one_hot = Y_one_hot.T
    return Y_one_hot

def error_calc(A3,Hot):
    e = 1/len(A3) * (np.sum((A3 - Hot)**2,axis=0))
    return e 

def backward_propagation(Z1, A1, Z2, A2, Z3, A3, W1, b1, W2, b2, W3, b3, label, X, alpha):
    X = X.reshape(784,1)
    #onehot encoding
    one_hot_Y = one_hot(label)
    #easyer represintation of loss function
    dZ3 = A3.T - one_hot_Y
    dW3 = alpha * (dZ3.dot(A2))
    db3 = alpha * (dZ3)
    dZ2 = dReLU(A2)
    dW2 = alpha * (dZ2.dot(A1.T))
    db2 = alpha * (dZ2)
    dZ1 = dReLU(A1)
    dW1 = alpha * (dZ1.dot(X.T))
    db1 = alpha * (dZ1)
    return db1, dW1 ,db2 ,dW2 ,db3 ,dW3

def update_params(W1,b1,W2,b2,W3,b3,dW1,db1,dW2,db2,dW3,db3):
    W1 = W1 - dW1
    b1 = b1 - db1
    W2 = W2 - dW2
    b2 = b2 - db2
    W3 = W3 - dW3
    b3 = b3 - db3
    return W1,b1,W2,b2,b3,W3

def get_predictions(A2):
    return np.argmax(A2)



def gradient_decent(iterations,epoches,X,Y):
    W1,b1,W2,b2,W3,b3 = init_params()
    b4 = np.random.randn(33,1)
    nr_correct = 0
    for i in range(0,epoches):
        for img in range(1,iterations):
            current_img = X[img]
            Z1, A1, Z2, A2, Z3, A3 = forward_propagation(W1,b1,W2,b2,W3,b4,current_img)
            print(A2)
            print(A3)
            UC = ''.join([chr(ord(i)+975)for i in"ABCDEF2GHIJKLMNOPQRSTUVWXYZ[\\]^_`"]) + "I"
            my = UC[int(Y[i])]
            if np.argmax(A3,0)==np.argmax(one_hot(my),0):
                nr_correct += 1

            print(np.argmax(A3,0))
            print(my)
            print(one_hot(my))
            db1, dW1 ,db2 ,dW2 ,db3 ,dW3 = backward_propagation(Z1, A1, Z2, A2, Z3, A3, W1, b1, W2, b2, W3, b3,my, current_img, 0.01)
            W1,b1,W2,b2,W3,b3 = update_params(W1,b1,W2,b2,W3,b3,dW1,db1,dW2,db2,dW3,db3)
            print(img)
        Acc = round((nr_correct/iterations)*100,2)
        print(f"Acc {Acc}")
        nr_correct = 0
    return W1,b1,W2,b2,W3,b3


WR1,bR1,WR2,bR2,WR3,bR3 = gradient_decent(400,1,X,Y)


def res_ckeck(WR1,bR1,WR2,bR2,WR3,bR3,img_num,X,Y):
    UC = ''.join([chr(ord(i)+975)for i in"ABCDEF2GHIJKLMNOPQRSTUVWXYZ[\\]^_`"]) + "I"
    my_label = UC[int(Y[img_num])]
    Z1, A1, Z2, A2, Z3, A3 = forward_propagation(WR1,bR1,WR2,bR2,WR3,bR3,X[img_num])
    arg = get_predictions(A3)
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФКЦЧШЩЪЫЬЭЮЯ"
    print(A3)
    print(A3.shape)
    print(arg)
    prediction = alphabet[arg]
    plt.imshow(X[img_num].reshape(28,28))
    plt.text(0,0,prediction)
    plt.show()
    pass


num = int(input())

res_ckeck(WR1,bR1,WR2,bR2,WR3,bR3,num,X,Y)





