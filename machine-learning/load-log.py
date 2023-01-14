#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import time
from layer import *

# model_initial = Model()
# model_initial.addlayer(Layer(240, 200))
# model_initial.addlayer(Layer_output(200, 5))

# model_startturn4 = Model()
# model_startturn4.addlayer(Layer(240, 200))
# model_startturn4.addlayer(Layer_output(200, 5))

model_initial = Model()
model_initial.addlayer(Layer(240, 500))
model_initial.addlayer(Layer(500, 200))
model_initial.addlayer(Layer(200, 100))
model_initial.addlayer(Layer_output(100, 5))

model_startturn4 = Model()
model_startturn4.addlayer(Layer(240, 500))
model_startturn4.addlayer(Layer(500, 200))
model_startturn4.addlayer(Layer(200, 100))
model_startturn4.addlayer(Layer_output(100, 5))


xi = []
x4 = []
yi = []
y4 = []


CARD_LIST = [11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,
             71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124]


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

all_num_init = 0
seikai_num_init = 0
near_num_init = 0
near_seikai_num_init = 0
all_num_4 = 0
seikai_num_4 = 0
near_num_4 = 0
near_seikai_num_4 = 0


for i in range(1, 10001):
    file_name = "/Users/hiranoseigo/Downloads/log/log_computer16/log-computer-" + str(i) + ".txt"
    f = open(file_name, "r")
    lines = f.readlines()
    # if i == 1000:
    #     break
    
    j = 0
    turn = 0
    initial_condition = []
    end_of_turn_4 = []
    month_list = []
    my_total_scores = []
    your_total_scores = []
    tokusitutensa = []
    kakutoku_ten = []
    seikai_label = []
    while True:
        try:
            l = lines[j]
            flag = 0
            
            if l[:17] == "initial condition":
                field_cards = []
                tefuda = []  # コンピュータにとってのtefudaなので，your_cards
                my_getcards = []  # こちらもコンピュータにとってのmy_getcardsになっているので，logの変数名はyour_getcard
                your_getcards = []
                for k in range(25):
                    if k == 2:
                        field_cards = list(map(int, lines[j][1:-2].split()))
                    elif k == 8:
                        tefuda = list(map(int, lines[j][1:-2].split()))
                    elif k == 10:
                        your_getcards = list(map(int, lines[j][1:-2].split()))
                    elif k == 12:
                        my_getcards = list(map(int, lines[j][1:-2].split()))
                        
                    j += 1
                    
                learning_list = make_learning_list(tefuda, my_getcards, your_getcards, field_cards)
                    
                initial_condition.append(learning_list)
            
            if (l[:9] == "your turn") | (l[:7] == "my turn"):
                field_cards = []
                tefuda = []
                my_getcards = []
                your_getcards = []
                for k in range(29):
                    if k == 2:
                        month = int(lines[j][:-1])
                    if k == 4:
                        last_turn = turn
                        turn = int(lines[j][:-1])
                        if not (last_turn == 6) & (turn == 7):
                            break
                    if k == 6:
                        field_cards = list(map(int, lines[j][1:-2].split()))
                    elif k == 12:
                        tefuda = list(map(int, lines[j][1:-2].split()))
                    elif k == 14:
                        your_getcards = list(map(int, lines[j][1:-2].split()))
                    elif k == 16:
                        my_getcards = list(map(int, lines[j][1:-2].split()))
                    
                    j += 1
                
                else:
                    learning_list = make_learning_list(tefuda, my_getcards, your_getcards, field_cards)
                    month_list.append(month)
                    end_of_turn_4.append(learning_list)
                    continue
                
                
                

            j += 1
        except:
            break
        
    
    for m in range(-12, 0, 1):
        scores = list(map(int, lines[m][:-1].split()))
        my_total_scores.append(scores[1])
        your_total_scores.append(scores[2])
        tokusitutensa.append(scores[2] - scores[1])
        # print(scores)
    
        
    kakutoku_ten.append(your_total_scores[0])
    for n in range(11):
        kakutoku_ten.append(tokusitutensa[n+1] - tokusitutensa[n])
        
    for o in range(12):
        tokusitu = kakutoku_ten[o]
        if tokusitu == 0:
            label = 0
        elif 0 < tokusitu <= 2:
            label = 1
        elif tokusitu > 2:
            label = 2
        elif -2 <= tokusitu < 0:
            label = 3
        elif tokusitu < -2:
            label = 4
        seikai_label.append(label)

    # print(kakutoku_ten)
    # print(seikai_label)
    # print(len(end_of_turn_4))
    # print(len(initial_condition))
    # print(month_list)
    # print("---------------------")
    
    
    
    for m in range(12):
        input_data = initial_condition[m]
        output_data = model_initial.predict(input_data)
        
        train_label = seikai_label[m]
        model_initial.backpropagation(label_to_fugou(train_label))
        
        yosoku = 4 - np.argmax(np.array(output_data))
        # print(yosoku, train_label)
        all_num_init += 1
        near_num_init += 1
        if yosoku == train_label:
            seikai_num_init += 1
            near_seikai_num_init += 1
    
    # print("-------------------")
    
    for n in range(len(month_list)):
        input_data = end_of_turn_4[n]
        output_data = model_startturn4.predict(input_data)
        
        train_label = seikai_label[month_list[n] - 1]
        model_startturn4.backpropagation(label_to_fugou(train_label))
        
        yosoku = 4 - np.argmax(np.array(output_data))
        # print(yosoku, train_label)
        all_num_4 += 1
        near_num_4 += 1
        if yosoku == train_label:
            seikai_num_4 += 1
            near_seikai_num_4 += 1
            
            
    
    
    if i % 100 == 0:
        print(i)
        print("all: {}, {},  near: {}, {}".format(all_num_init, seikai_num_init/all_num_init*100, near_num_init, near_seikai_num_init/near_num_init*100))
        print("all: {}, {},  near: {}, {}".format(all_num_4, seikai_num_4/all_num_4*100, near_num_4, near_seikai_num_4/near_num_4*100))
        xi.append(all_num_init)
        yi.append(near_seikai_num_init / near_num_init * 100)
        x4.append(all_num_4)
        y4.append(near_seikai_num_4 / near_num_4 * 100)
        near_num_4, near_num_init, near_seikai_num_4, near_seikai_num_init = 0, 0, 0, 0
        
        
g = open("./weight-param.txt", "w")
for n in range(len(model_initial.layers)):
    weight = np.ravel(model_initial.layers[n].weight)
    for v in weight:
        g.write("{} ".format(v))
    g.write("\n")
for n in range(len(model_startturn4.layers)):
    weight = np.ravel(model_startturn4.layers[n].weight)
    for v in weight:
        g.write("{} ".format(v))
    g.write("\n")
    
    
import matplotlib.pyplot as plt
plt.plot(xi, yi)
plt.show()
plt.plot(x4, y4)
plt.show()
