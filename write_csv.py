import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import csv


data_wrong = pd.read_csv("dataSet\letters.csv")
data_wrong = data_wrong.drop(data_wrong.columns[[3]], axis=1)
data = np.array(data_wrong)

m,n = data.shape

np.savetxt("DataSet.csv", data, delimiter=",")