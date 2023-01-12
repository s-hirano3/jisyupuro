#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import time
import random
from layer import *

model = Model()
model.addlayer(Layer(125, 10))
model.addlayer(Layer_output(10, 5))

