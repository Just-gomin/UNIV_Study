import os
import pickle
import sys

import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from dataset.mnist import load_mnist

# Common Functions
def sigmoid(x):
    return 1/(1+np.exp(-x))


def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axix=0)
        return y.T

    x = x - np.max(x)
    return np.exp(x)/np.sum(np.exp(x))


# Load MNIST Data
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(
        normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

# Error Functions
def mean_square_error(y,t):
    return 0.5 * np.sum((y - t) ** 2)

def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))

# Main part
x, t = get_data()
network = init_network()
picked_data = [0,2,4,6,8]
mse_list = []
cee_list = []

for i in picked_data:
    y = predict(network, x[i])
    temp = np.zeros(10)
    temp[t[i]]= 1
    mse_list.append(mean_square_error(y,temp))
    cee_list.append(cross_entropy_error(y,temp))

print("{0:<6} {1:<10}".format("index", "MSE"))
for i,mse in zip(picked_data, mse_list):
    print("{0:<6} {1:<10}".format(i,mse))

print("Average MSE : ", sum(mse_list)/len(mse_list))

print("\n");

print("{0:<6} {1:<10}".format("index", "CEE"))
for i,cee in zip(picked_data, cee_list):
    print("{0:<6} {1:<10}".format(i,cee))

print("Average CEE : ", sum(cee_list)/len(cee_list))