#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from cv2 import aruco
import os

dir_mark = "./AR"

num_mark = 48
size_mark = 500

dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)

for count in range(num_mark):
    id_mark = count
    img_mark = aruco.drawMarker(dict_aruco, id_mark, size_mark)

    if count < 10:
        img_name_mark = 'mark_id_0' + str(count) + '.jpg'
    else:
        img_name_mark = 'mark_id_' + str(count) + '.jpg'

    path_mark = os.path.join(dir_mark, img_name_mark)

    cv2.imwrite(path_mark, img_mark)