#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import time

for i in range(10000):
    file_name = "/Users/hiranoseigo/Downloads/log/log-computer15/" + str(i) + ".txt"
    f = open(file_name, "r")
    lines = f.readlines()
    
    