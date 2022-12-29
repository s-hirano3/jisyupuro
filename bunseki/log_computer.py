#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os




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


dir_path2 = dir_path + "/log_computer" + str(log_num)
filelist2 = os.listdir(dir_path2)
NUMBER = len(filelist2)

# NUMBER = 4000

print("directory number : {}, file number : {}\n\n".format(log_num, NUMBER))

my_scores = np.zeros(NUMBER)
your_scores = np.zeros(NUMBER)
x = np.zeros(NUMBER)

my_win_scores = []
my_lose_scores = []
my_total_tokusitu = []
my_win_tokusitu = []

your_win_scores = []
your_lose_scores = []
your_total_tokusitu = []
your_win_tokusitu = []

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
        my_win_scores.append(my_score)
        my_total_tokusitu.append(my_score - your_score)
        my_win_tokusitu.append(my_score - your_score)
        your_lose_scores.append(your_score)
        your_total_tokusitu.append(your_score - my_score)
        
    elif my_score < your_score:
        your_win += 1
        your_win_scores.append(your_score)
        your_total_tokusitu.append(your_score - my_score)
        your_win_tokusitu.append(your_score - my_score)
        my_lose_scores.append(my_score)
        my_total_tokusitu.append(my_score - your_score)
        
    else:
        hikiwake += 1
        my_total_tokusitu.append(0)
        your_total_tokusitu.append(0)

    if i % 100 == 0:
        print(i)

# my_scores.sort()
# your_scores.sort()



print("\n勝利数  me: {}, you: {}, hikiwake: {}".format(my_win, your_win, hikiwake))
print("勝率  me: {}%, you: {}%, hikiwake: {}%\n".format(my_win/NUMBER*100, your_win/NUMBER*100, hikiwake/NUMBER*100))

print("my得点情報  average: {}, max: {}, min: {}".format(np.mean(my_scores), np.max(my_scores), np.min(my_scores)))
print("your得点情報  average: {}, max: {}, min: {}\n".format(np.mean(your_scores), np.max(your_scores), np.min(your_scores)))

print("勝ったときの平均score  me: {}, you: {}".format(np.mean(my_win_scores), np.mean(your_win_scores)))
print("負けたときの平均score  me: {}, you: {}".format(np.mean(my_lose_scores), np.mean(your_lose_scores)))
print("全体の平均得失点差  me: {}, you: {}".format(np.mean(my_total_tokusitu), np.mean(your_total_tokusitu)))
print("勝ったときの平均得失点差  me: {}, you: {}".format(np.mean(my_win_tokusitu), np.mean(your_win_tokusitu)))

# plt.plot(x, my_scores)
# plt.plot(x, your_scores)
# plt.show()

plt.subplot(221)
labels = ["Algorithm", "Random"]
plt.hist([my_scores, your_scores], stacked=False, bins=20, label=labels, range=(0,np.max(my_scores+your_scores)))
plt.legend()
plt.title("tokuten histogram")
# plt.show()

plt.subplot(222)
labels = ["Algorithm", "Random"]
plt.hist([my_total_tokusitu, your_total_tokusitu], stacked=False, bins=20, label=labels)
plt.legend()
plt.title("tokusitutennsa")
# plt.show()

plt.subplot(223)
labels = ["Algorithm", "Random"]
plt.hist([my_win_scores, your_win_scores], stacked=False, bins=20, label=labels, range=(0,np.max(my_scores+your_scores)))
plt.legend()
plt.title("win tokuten")
# plt.show()

plt.subplot(224)
labels = ["Algorithm", "Random"]
plt.hist([my_lose_scores, your_lose_scores], stacked=False, bins=20, label=labels, range=(0,np.max(my_scores+your_scores)))
plt.legend()
plt.title("lose tokuten")
# labels = ["Algorithm-win", "Random-win", "Algorithm-lose", "Random-lose"]
# plt.hist([my_win_scores, your_win_scores, my_lose_scores, your_lose_scores], bins=20, label=labels, range=(0,np.max(my_scores+your_scores)))
# plt.legend()
# plt.title("tokuten when win or lose")

plt.show()