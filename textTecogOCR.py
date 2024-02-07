import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import random

import zipfile
import string

# Load images and labels
X = np.loadtxt('cyrillic_data.csv', delimiter=",")
Y = np.loadtxt('cyrillic_label.csv', delimiter=",")
X_train = X
Y_train = Y[0:4487]
c = list(zip(X_train, Y_train))

random.shuffle(c)

X_train, Y_train = zip(*c)
m,n = X.shape


def init_params():
    W1 = np.random.randn(33,784)
    b1 = np.zeros((33,1))
    W2 = np.random.randn(33,33)
    b2 = np.zeros((33,1))
    W3 = np.random.randn(33,33)
    b3 = np.zeros((33,1))
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
    Z3 = W3.dot(A2) + b3
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

def backward_propagation(Z1, A1, Z2, A2, Z3, A3, W1, b1, W2, b2, W3, b3, label, X):
    X = X.reshape(784,1)
    #onehot encoding
    one_hot_Y = one_hot(label)
    #easyer represintation of loss function
    dZ3 = A3 - one_hot_Y
    dW3 = (dZ3.dot(A2.T))
    db3 = (dZ3)
    dZ2 = dReLU(A2)
    dW2 = (dZ2.dot(A1.T))
    db2 = (dZ2)
    dZ1 = dReLU(A1)
    dW1 = (dZ1.dot(X.T))
    db1 = (dZ1)
    return  dW1 ,db1 ,dW2 ,db2 ,dW3 ,db3 

def update_params(W1,b1,W2,b2,W3,b3,dW1,db1,dW2,db2,dW3,db3, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1
    W2 = W2 - alpha * dW2
    b2 = b2 - alpha * db2
    W3 = W3 - alpha * dW3
    b3 = b3 - alpha * db3
    return W1,b1,W2,b2,W3,b3

def get_predictions(A2):
    return np.argmax(A2,0)



def gradient_decent(iterations,epoches,X,Y):
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    W1,b1,W2,b2,W3,b3 = init_params()
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    nr_correct = 0
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    for e in range(0,epoches):
        for img in range(1,iterations):
            #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            X_img = X[img]
            UC = ''.join([chr(ord(i)+975)for i in"ABCDEF2GHIJKLMNOPQRSTUVWXYZ[\\]^_`"]) + "I"
            my_label = UC[int(Y[img])]
            #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            Z1, A1, Z2, A2, Z3, A3 = forward_propagation(W1,b1,W2,b2,W3,b3,X_img)
            dW1 ,db1 ,dW2 ,db2 ,dW3 ,db3  = backward_propagation(Z1, A1, Z2, A2, Z3, A3, W1, b1, W2, b2, W3, b3, my_label, X_img)
            W1,b1,W2,b2,W3,b3 = update_params(W1,b1,W2,b2,W3,b3,dW1,db1,dW2,db2,dW3,db3, -0.01)
            #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            pred = int(get_predictions(A3))
            tru = int(get_predictions(one_hot(my_label)))
            #print(pred,"                        ",tru)
            if pred == tru:
                nr_correct += 1
        acc = nr_correct/iterations
        nr_correct = 0
        print("Epoche acc:",acc)
    return W1,b1,W2,b2,W3,b3


WR1,bR1,WR2,bR2,WR3,bR3 = gradient_decent(4200,10,X_train,Y_train)




def res_ckeck(WR1,bR1,WR2,bR2,WR3,bR3,img_num,X,Y):
    UC = ''.join([chr(ord(i)+975)for i in"ABCDEF2GHIJKLMNOPQRSTUVWXYZ[\\]^_`"]) + "I"
    my_label = UC[int(Y[img_num])]
    _, _, _, _, _, A3 = forward_propagation(WR1,bR1,WR2,bR2,WR3,bR3,X[img_num])
    arg = int(get_predictions(A3))
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФКЦЧШЩЪЫЬЭЮЯ"
    print(arg)
    prediction = alphabet[arg]
    plt.imshow(X[img_num].reshape(28,28))
    plt.text(0,0,prediction)
    plt.show()
    pass


while True:
    a = int(input())
    res_ckeck(WR1,bR1,WR2,bR2,WR3,bR3,a,X,Y)







