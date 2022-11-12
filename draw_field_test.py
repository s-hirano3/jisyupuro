#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from detect_yaku import detect_yaku

#(blue, green, red)
FIELD_COLOR = (135, 153, 0)
CARD_COLOR = (76, 60, 167)
WHITE = (255, 255, 255)

COORDS_FIELD = [(10, 454, 68, 546), (88, 454, 146, 546), (166, 454, 224, 546), (244, 454, 302, 546), (322, 454, 380, 546), (400, 454, 458, 546), (478, 454, 536, 546), (556, 454, 614, 546), (634, 454, 692, 546), (712, 454, 770, 546), (790, 454, 848, 546), (868, 454, 926, 546), (946, 454, 1004, 546), (1024, 454, 1082, 546), (1102, 454, 1160, 546), (1180, 454, 1238, 546)]
COORDS_YAMAFUDA = [(1336, 454, 1394, 546), (1414, 454, 1472, 546)]
COORDS_MY_CARDS = [(483, 898, 541, 990), (561, 898, 619, 990), (639, 898, 697, 990), (717, 898, 775, 990), (795, 898, 853, 990), (873, 898, 931, 990), (951, 898, 1009, 990), (1029, 898, 1087, 990)]
COORDS_MY_GETCARDS = [(60, 644, 118, 736), (138, 644, 196, 736), (216, 644, 274, 736), (99, 756, 157, 848), (177, 756, 235, 848), (374, 644, 432, 736), (452, 644, 510, 736), (530, 644, 588, 736), (413, 756, 471, 848), (491, 756, 549, 848), (688, 644, 746, 736), (766, 644, 824, 736), (844, 644, 902, 736), (727, 756, 785, 848), (805, 756, 863, 848), (1002, 644, 1060, 736), (1080, 644, 1138, 736), (1158, 644, 1216, 736), (1236, 644, 1294, 736), (1314, 644, 1372, 736), (1002, 756, 1060, 848), (1080, 756, 1138, 848), (1158, 756, 1216, 848), (1236, 756, 1294, 848), (1314, 756, 1372, 848)]
COORDS_YOUR_CARDS = [(483, 10, 541, 102), (561, 10, 619, 102), (639, 10, 697, 102), (717, 10, 775, 102), (795, 10, 853, 102), (873, 10, 931, 102), (951, 10, 1009, 102), (1029, 10, 1087, 102)]
COORDS_YOUR_GETCARDS = [(60, 152, 118, 244), (138, 152, 196, 244), (216, 152, 274, 244), (99, 264, 157, 356), (177, 264, 235, 356), (374, 152, 432, 244), (452, 152, 510, 244), (530, 152, 588, 244), (413, 264, 471, 356), (491, 264, 549, 356), (688, 152, 746, 244), (766, 152, 824, 244), (844, 152, 902, 244), (727, 264, 785, 356), (805, 264, 863, 356), (1002, 152, 1060, 244), (1080, 152, 1138, 244), (1158, 152, 1216, 244), (1236, 152, 1294, 244), (1314, 152, 1372, 244), (1002, 264, 1060, 356), (1080, 264, 1138, 356), (1158, 264, 1216, 356), (1236, 264, 1294, 356), (1314, 264, 1372, 356)]


card_11 = cv2.resize(cv2.imread("hanafuda_image/11.png"), dsize=(58,92))
card_12 = cv2.resize(cv2.imread("hanafuda_image/12.png"), dsize=(58,92))
card_13 = cv2.resize(cv2.imread("hanafuda_image/13.png"), dsize=(58,92))
card_14 = cv2.resize(cv2.imread("hanafuda_image/14.png"), dsize=(58,92))
card_dict = {11:card_11, 12:card_12, 13:card_13, 14:card_14}

def draw_field(my_cards, my_getcards, your_cards, your_getcards, field_cards, month, end_month, desplay_mode):
    stage = np.full((1000, 1500, 3), FIELD_COLOR, dtype=np.uint8)  # ステージ背景設定
    stage = cv2.rectangle(stage, (200,500), (258,593),color=FIELD_COLOR, thickness=5)  # ステージ作成(ダミー)
    
    
    
    dst_stage = stage.copy()
    
    for i in range(len(COORDS_FIELD)):
        roi = COORDS_FIELD[i]
        dst_stage[roi[1]:roi[3], roi[0]:roi[2]] = card_dict[11]
    cv2.imshow("stage", dst_stage)
    cv2.waitKey(2000)
    for i in range(len(COORDS_YAMAFUDA)):
        roi = COORDS_YAMAFUDA[i]
        dst_stage[roi[1]:roi[3], roi[0]:roi[2]] = card_dict[12]
    for i in range(len(COORDS_MY_CARDS)):
        roi = COORDS_MY_CARDS[i]
        dst_stage[roi[1]:roi[3], roi[0]:roi[2]] = card_dict[13]
    for i in range(len(COORDS_YOUR_CARDS)):
        roi = COORDS_YOUR_CARDS[i]
        dst_stage[roi[1]:roi[3], roi[0]:roi[2]] = card_dict[14]
    for i in range(len(COORDS_MY_GETCARDS)):
        roi = COORDS_MY_GETCARDS[i]
        dst_stage[roi[1]:roi[3], roi[0]:roi[2]] = card_dict[12]
    for i in range(len(COORDS_YOUR_GETCARDS)):
        roi = COORDS_YOUR_GETCARDS[i]
        dst_stage[roi[1]:roi[3], roi[0]:roi[2]] = card_dict[11]
    
    
    cv2.imshow("stage", dst_stage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return dst_stage


if __name__ == '__main__':
    stage = draw_field(0,0,0,0,0,0,0,0)
    #print(stage)
    #cv2.imshow("stage", stage)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()