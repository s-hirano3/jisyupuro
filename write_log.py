#/usr/bin/env python
# -*- coding: utf-8 -*-

def write_init(file, num):
    file.write('oya mode(0:player is oya of odd month, 1:player is oya of even month) = ' + str(num) + '\n\n')
    return file