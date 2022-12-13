import os

path = "/Users/hiranoseigo/DOwnloads/log"
filelist = os.listdir(path)
for i in range(len(filelist)):
    file = filelist[i]
    if file[:12] == "log_computer":
        print(file[12:])

