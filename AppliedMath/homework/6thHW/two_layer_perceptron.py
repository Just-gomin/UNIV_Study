import os
import pickle
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import matplotlib.pyplot as plt
import numpy as np

from common.functions import *

from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

class TwoLayerPerceptron:
    def __init__(self, input_size=2, hidden_size=15, output_size=1, train_size=5, batch_size=3, iter_nums=500, learning_rate=0.5):
        """
        Keyword arguments:
        input_size -- 입력변수의 갯수
        hidden_size -- 은닉층 크기
        output_size -- 결과값 갯수
        train_size -- 훈련 입력값의 갯수
        batch_size -- 훈련 배치 갯수
        iter_nums -- 반복 횟수
        learning_rate -- 학습률
        """
        self.network = TwoLayerNet(input_size, hidden_size, output_size)

        self.train_size = train_size
        self.batch_size = batch_size
        self.iter_nums = iter_nums
        self.learning_rate = learning_rate

        self.accuracy_list = []

    # 가중치 학습
    # x는 2차원 배열, t는 1차원 label 배열; 훈련 메소드
    def train(self, x, t):
        for i in range(self.iter_nums):
            grad = self.network.numerical_gradient(x,t)
            for key in ('W1', 'b1', 'W2', 'b2'):
                self.network.params[key] = self.learning_rate * grad[key]
            
            if i % 10 == 0:
                acc = self.accuracy(x, t)
                self.accuracy_list.append(acc)

    # 추정 값 계산
    def predict(self, x):
        params = self.network.params
        W1, b1 = params['W1'], params['b1']
        W2, b2 = params['W2'], params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    # 정확도
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y==t) / float(x.shape[0])
        return accuracy
        

    # 정확도 그래프 그리기
    def draw(self):
        x = np.arange(len(self.accuracy_list))
        plt.plot(x, self.accuracy_list, label="train acc")
        plt.xlabel("Iteration Count")
        plt.ylabel("Accuracy")
        plt.ylim(0, 1.0)
        plt.legend(loc="lower right")
        plt.show()


if __name__ == '__main__':
    q1_x = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 2]])
    q1_y = np.array([[1], [0], [1], [0], [0]])

    perceptron1 = TwoLayerPerceptron(input_size=q1_x.shape[1], hidden_size=5, output_size=1, train_size= q1_x.shape[0])
    perceptron1.train(q1_x, q1_y)
    perceptron1.draw()
