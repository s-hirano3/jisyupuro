import matplotlib.pyplot as plt
import numpy as np
me = []
you = []
sa = []

filenum = 1000

for i in range(1,filenum+1):
    file_name = './log_computer/log-computer-' + str(i) + '.txt'
    f = open(file_name, 'r')
    datalist = f.readlines()
    mojiretu = datalist[-3].split(' ')
    my_score = int(mojiretu[1][:-1])
    your_score = int(mojiretu[3][:-1])

    tokusitu = my_score - your_score
    
    me.append(my_score)
    you.append(your_score)
    sa.append(tokusitu)
    
    print(i, mojiretu)
    
    f.close

x = range(1,filenum+1)
plt.plot(x, me, '.', label='me')
plt.plot(x, you, '.', label='you')
plt.legend()
plt.show()

me = sorted(me)
plt.plot(x, me)
plt.show()

you = sorted(you)
plt.plot(x, you)
plt.show()



print("total me: {}, you: {}".format(np.sum(me), np.sum(you)))
print("mean  me: {}, you: {}".format(np.mean(me), np.mean(you)))
print("max  me: {}, you: {}".format(np.max(me), np.max(you)))
print("min  me: {}, you: {}".format(np.min(me), np.min(you)))
print("tokusitu(+me -you) mean {}, max {}, min {}".format(np.mean(sa), np.max(sa), np.min(sa)))