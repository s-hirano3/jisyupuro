#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os

NUMBER = 2000

my_scores = np.zeros(NUMBER)
your_scores = np.zeros(NUMBER)
x = np.zeros(NUMBER)

my_win = 0
your_win = 0
hikiwake = 0

dir_path = "/Users/hiranoseigo/Downloads/log"
log_num_list = []
filelist = os.listdir(dir_path)
for file in filelist:
    if file[:12] == "log_computer":
        log_num_list.append(int(file[12:]))    
log_num = max(log_num_list)

# log_num = 8


for i in range(NUMBER):
    file_name = dir_path + "/log_computer" + str(log_num) + "/log-computer-" + str(i+1) + ".txt"
    f = open(file_name, "r")
    lines = f.readlines()
    
    scores = lines[-1][:-1].split(" ")
    my_score = int(scores[1])
    your_score = int(scores[2])

    my_scores[i] = my_score
    your_scores[i] = your_score
    x[i] = i

    if my_score > your_score:
        my_win += 1
    elif my_score < your_score:
        your_win += 1
    else:
        hikiwake += 1

    if i % 100 == 0:
        print(i)

# my_scores.sort()
# your_scores.sort()

plt.hist([my_scores, your_scores], stacked=False, bins=20, label=["Rule", "Random"])
plt.show()


print("my win: {}, your win: {}, hikiwake: {}".format(my_win, your_win, hikiwake))
print("my win: {}%, your win: {}%, hikiwake: {}%".format(my_win/NUMBER*100, your_win/NUMBER*100, hikiwake/NUMBER*100))

print("me   average: {}, max: {}, min: {}".format(np.mean(my_scores), np.max(my_scores), np.min(my_scores)))
print("you  average: {}, max: {}, min: {}".format(np.mean(your_scores), np.max(your_scores), np.min(your_scores)))

# plt.plot(x, my_scores)
# plt.plot(x, your_scores)
# plt.show()