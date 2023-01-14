#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

eta = 0.05

CARD_LIST = [11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,
             71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124]


def relu(array):
    relu_mask = np.maximum(0, array)
    relu_mask = np.where(relu_mask>0, 1, relu_mask)
    relu_array = array * relu_mask
    return relu_mask, relu_array

def softmax(array):
    softmax_array = np.exp(array) / np.sum(np.exp(array))
    return softmax_array

def label_to_fugou(label):
    if label == 0:
        answer = [0, 0, 0, 0, 1]
    elif label == 1:
        answer = [0, 0, 0, 1, 0]
    elif label == 2:
        answer = [0, 0, 1, 0, 0]
    elif label == 3:
        answer = [0, 1, 0, 0, 0]
    elif label == 4:
        answer = [1, 0, 0, 0, 0]
    return answer


def make_learning_list(tefuda, my_getcards, your_getcards, field_cards):
    learning_list = []
    
    for card in CARD_LIST:
        l = [0, 0, 0, 0, 0]
        if card in tefuda:
            l[0] = 1
        elif card in my_getcards:
            l[1] = 1
        elif card in your_getcards:
            l[2] = 1
        elif card in field_cards:
            l[3] = 1
        else:
            l[4] = 0
        
        learning_list += l
    
    return learning_list




class Model():
    def __init__(self):
        self.layers = []
        self.output = []

    def addlayer(self, layer):
        self.layers.append(layer)
    
    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        self.output.append(x)
        return x

    def backpropagation(self, d):
        for layer in reversed(self.layers):
            d = layer.backward(d)
    


class Layer():
    def __init__(self, input, output):
        self.input = input
        self.output = output

        self.weight = np.random.normal(scale=np.sqrt(1.0/input), size=(input,output)).astype(np.float32)
        
        self.x_in = np.zeros(self.input)
        self.x_out = np.zeros(self.output)

        self.relu_mask = np.zeros(self.output)
        self.u = np.zeros(self.output)
        self.delta = np.zeros(self.output)
    
    
    def forward(self, x):
        self.x_in = np.ravel(np.array(x))

        self.u = np.dot(self.x_in, self.weight)
        self.relu_mask, self.x_out = relu(self.u)

        return self.x_out

    
    def backward(self, sigma):
        sigma = np.array(sigma)
        self.delta = sigma * self.relu_mask

        sigma = np.dot(self.weight, self.delta)

        self.weight = self.weight - eta * np.dot(np.reshape(self.x_in, (self.input,1)), np.reshape(self.delta, (1,self.output)))

        return sigma



class Layer_output(Layer):
    def __init__(self, input, output):
        super().__init__(input, output)
        self.d = np.zeros(self.output)
        self.grad = np.zeros(self.output)

    
    def forward(self, x):
        self.x_in = np.array(x)

        self.u = np.dot(self.x_in, self.weight)
        self.x_out = softmax(self.u)

        return self.x_out

    
    def backward(self, d):
        self.d = np.array(d)
        self.grad = self.x_out * (1 - self.x_out)
        self.delta = (self.x_out - self.d) * self.grad
        
        sigma = np.dot(self.weight, self.delta)

        self.weight = self.weight - eta * np.dot(np.reshape(self.x_in, (self.input,1)), np.reshape(self.delta, (1,self.output)))
        
        return sigma