#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


card11 = cv2.resize(cv2.imread("hanafuda_image/11.png"), dsize=(58,92))
card12 = cv2.resize(cv2.imread("hanafuda_image/12.png"), dsize=(58,92))
card13 = cv2.resize(cv2.imread("hanafuda_image/13.png"), dsize=(58,92))
card14 = cv2.resize(cv2.imread("hanafuda_image/14.png"), dsize=(58,92))

card21 = cv2.resize(cv2.imread("hanafuda_image/21.png"), dsize=(58,92))
card22 = cv2.resize(cv2.imread("hanafuda_image/22.png"), dsize=(58,92))
card23 = cv2.resize(cv2.imread("hanafuda_image/23.png"), dsize=(58,92))
card24 = cv2.resize(cv2.imread("hanafuda_image/24.png"), dsize=(58,92))

card31 = cv2.resize(cv2.imread("hanafuda_image/31.png"), dsize=(58,92))
card32 = cv2.resize(cv2.imread("hanafuda_image/32.png"), dsize=(58,92))
card33 = cv2.resize(cv2.imread("hanafuda_image/33.png"), dsize=(58,92))
card34 = cv2.resize(cv2.imread("hanafuda_image/34.png"), dsize=(58,92))

card41 = cv2.resize(cv2.imread("hanafuda_image/41.png"), dsize=(58,92))
card42 = cv2.resize(cv2.imread("hanafuda_image/42.png"), dsize=(58,92))
card43 = cv2.resize(cv2.imread("hanafuda_image/43.png"), dsize=(58,92))
card44 = cv2.resize(cv2.imread("hanafuda_image/44.png"), dsize=(58,92))

card51 = cv2.resize(cv2.imread("hanafuda_image/51.png"), dsize=(58,92))
card52 = cv2.resize(cv2.imread("hanafuda_image/52.png"), dsize=(58,92))
card53 = cv2.resize(cv2.imread("hanafuda_image/53.png"), dsize=(58,92))
card54 = cv2.resize(cv2.imread("hanafuda_image/54.png"), dsize=(58,92))

card61 = cv2.resize(cv2.imread("hanafuda_image/61.png"), dsize=(58,92))
card62 = cv2.resize(cv2.imread("hanafuda_image/62.png"), dsize=(58,92))
card63 = cv2.resize(cv2.imread("hanafuda_image/63.png"), dsize=(58,92))
card64 = cv2.resize(cv2.imread("hanafuda_image/64.png"), dsize=(58,92))

card71 = cv2.resize(cv2.imread("hanafuda_image/71.png"), dsize=(58,92))
card72 = cv2.resize(cv2.imread("hanafuda_image/72.png"), dsize=(58,92))
card73 = cv2.resize(cv2.imread("hanafuda_image/73.png"), dsize=(58,92))
card74 = cv2.resize(cv2.imread("hanafuda_image/74.png"), dsize=(58,92))

card81 = cv2.resize(cv2.imread("hanafuda_image/81.png"), dsize=(58,92))
card82 = cv2.resize(cv2.imread("hanafuda_image/82.png"), dsize=(58,92))
card83 = cv2.resize(cv2.imread("hanafuda_image/83.png"), dsize=(58,92))
card84 = cv2.resize(cv2.imread("hanafuda_image/84.png"), dsize=(58,92))

card91 = cv2.resize(cv2.imread("hanafuda_image/91.png"), dsize=(58,92))
card92 = cv2.resize(cv2.imread("hanafuda_image/92.png"), dsize=(58,92))
card93 = cv2.resize(cv2.imread("hanafuda_image/93.png"), dsize=(58,92))
card94 = cv2.resize(cv2.imread("hanafuda_image/94.png"), dsize=(58,92))

card101 = cv2.resize(cv2.imread("hanafuda_image/101.png"), dsize=(58,92))
card102 = cv2.resize(cv2.imread("hanafuda_image/102.png"), dsize=(58,92))
card103 = cv2.resize(cv2.imread("hanafuda_image/103.png"), dsize=(58,92))
card104 = cv2.resize(cv2.imread("hanafuda_image/104.png"), dsize=(58,92))

card111 = cv2.resize(cv2.imread("hanafuda_image/111.png"), dsize=(58,92))
card112 = cv2.resize(cv2.imread("hanafuda_image/112.png"), dsize=(58,92))
card113 = cv2.resize(cv2.imread("hanafuda_image/113.png"), dsize=(58,92))
card114 = cv2.resize(cv2.imread("hanafuda_image/114.png"), dsize=(58,92))

card121 = cv2.resize(cv2.imread("hanafuda_image/121.png"), dsize=(58,92))
card122 = cv2.resize(cv2.imread("hanafuda_image/122.png"), dsize=(58,92))
card123 = cv2.resize(cv2.imread("hanafuda_image/123.png"), dsize=(58,92))
card124 = cv2.resize(cv2.imread("hanafuda_image/124.png"), dsize=(58,92))

CARDS_DICT = {11:card11, 12:card12, 13:card13, 14:card14, 21:card21, 22:card22, 23:card23, 24:card24, 31:card31, 32:card32, 33:card33, 34:card34, 41:card41, 42:card42, 43:card43, 44:card44,
              51:card51, 52:card52, 53:card53, 54:card54, 61:card61, 62:card62, 63:card63, 64:card64, 71:card71, 72:card72, 73:card73, 74:card74, 81:card81, 82:card82, 83:card83, 84:card84,
              91:card91, 92:card92, 93:card93, 94:card94, 101:card101, 102:card102, 103:card103, 104:card104, 111:card111, 112:card112, 113:card113, 114:card114, 121:card121, 122:card122, 123:card123, 124:card124}


#(blue, green, red)
FIELD_COLOR = (135, 153, 0)
CARD_COLOR = (76, 60, 167)
WHITE = (255, 255, 255)

COORDS_FIELD = [(10, 454, 68, 546), (88, 454, 146, 546), (166, 454, 224, 546), (244, 454, 302, 546), (322, 454, 380, 546), (400, 454, 458, 546), (478, 454, 536, 546), (556, 454, 614, 546), (634, 454, 692, 546), (712, 454, 770, 546), (790, 454, 848, 546), (868, 454, 926, 546), (946, 454, 1004, 546), (1024, 454, 1082, 546), (1102, 454, 1160, 546), (1180, 454, 1238, 546)]
COORDS_YAMAFUDA = [(1336, 454, 1394, 546), (1414, 454, 1472, 546)]
COORDS_MY_CARDS = [(483, 898, 541, 990), (561, 898, 619, 990), (639, 898, 697, 990), (717, 898, 775, 990), (795, 898, 853, 990), (873, 898, 931, 990), (951, 898, 1009, 990), (1029, 898, 1087, 990)]
COORDS_MY_GETCARDS = [[(60, 644, 118, 736), (138, 644, 196, 736), (216, 644, 274, 736), (99, 756, 157, 848), (177, 756, 235, 848)],
                      [(374, 644, 432, 736), (452, 644, 510, 736), (530, 644, 588, 736), (413, 756, 471, 848), (491, 756, 549, 848)],
                      [(688, 644, 746, 736), (766, 644, 824, 736), (844, 644, 902, 736), (727, 756, 785, 848), (805, 756, 863, 848)],
                      [(1002, 644, 1060, 736), (1080, 644, 1138, 736), (1158, 644, 1216, 736), (1236, 644, 1294, 736), (1314, 644, 1372, 736), (1002, 756, 1060, 848), (1080, 756, 1138, 848), (1158, 756, 1216, 848), (1236, 756, 1294, 848), (1314, 756, 1372, 848)]]
COORDS_YOUR_CARDS = [(483, 10, 541, 102), (561, 10, 619, 102), (639, 10, 697, 102), (717, 10, 775, 102), (795, 10, 853, 102), (873, 10, 931, 102), (951, 10, 1009, 102), (1029, 10, 1087, 102)]
COORDS_YOUR_GETCARDS = [[(60, 152, 118, 244), (138, 152, 196, 244), (216, 152, 274, 244), (99, 264, 157, 356), (177, 264, 235, 356)],
                        [(374, 152, 432, 244), (452, 152, 510, 244), (530, 152, 588, 244), (413, 264, 471, 356), (491, 264, 549, 356)],
                        [(688, 152, 746, 244), (766, 152, 824, 244), (844, 152, 902, 244), (727, 264, 785, 356), (805, 264, 863, 356)],
                        [(1002, 152, 1060, 244), (1080, 152, 1138, 244), (1158, 152, 1216, 244), (1236, 152, 1294, 244), (1314, 152, 1372, 244), (1002, 264, 1060, 356), (1080, 264, 1138, 356), (1158, 264, 1216, 356), (1236, 264, 1294, 356), (1314, 264, 1372, 356)]]





def draw_init():
    stage = np.full((1000, 1500, 3), FIELD_COLOR, dtype=np.uint8)  # ステージ背景設定
    stage = cv2.rectangle(stage, (200,500), (258,593),color=FIELD_COLOR, thickness=5)  # ステージ作成(ダミー)
    
    dst_stage = stage.copy()
    
    for coords in COORDS_FIELD:
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
    
    for coords in COORDS_YAMAFUDA:
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=CARD_COLOR, thickness=-1)
    
    for coords in COORDS_MY_CARDS:
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
    
    for i in range(4):    
        for coords in COORDS_MY_GETCARDS[i]:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
        
    for coords in COORDS_YOUR_CARDS:
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
        
    for i in range(4):
        for coords in COORDS_YOUR_GETCARDS[i]:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
    
    #cv2.imshow("stage", dst_stage)
    #cv2.waitKey(0)
    #cv2.destoryAllWindows()
    
    return dst_stage



def draw_oya_decision(stage, my_card, your_card):
    print('aiueo')
    dst_stage = stage.copy()
    
    my_coords = COORDS_YAMAFUDA[0]
    dst_stage[my_coords[1]:my_coords[3], my_coords[0]:my_coords[2]] = CARDS_DICT[my_card]
    
    your_cooords = COORDS_YAMAFUDA[1]
    dst_stage[your_cooords[1]:your_cooords[3], your_cooords[0]:your_cooords[2]] = CARDS_DICT[your_card]
    
    #v2.imshow("stage", dst_stage)
    #cv2.waitKey(0)
    
    return dst_stage



def draw_play_init(stage, my_cards, your_cards, field_cards, displaymode):
    dst_stage = stage.copy()
    
    for i in range(len(field_cards)):
        coords = COORDS_FIELD[i]
        field_card = field_cards[i]
        dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[field_card]
    
    for i in range(len(my_cards)):
        coords = COORDS_MY_CARDS[i]
        my_card = my_cards[i]
        dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_card]
    
    # displaymode=0なら相手の手札を表示しない
    if displaymode == 0:
        for i in range(len(your_cards)):
            coords = COORDS_YOUR_CARDS[i]
            dst_stage = cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=CARD_COLOR, thickness=-1)
    else:
        for i in range(len(your_cards)):
            coords = COORDS_YOUR_CARDS[i]
            your_card = your_cards[i]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_card]
      
    return dst_stage



def draw_play(stage, my_cards, my_getcards, your_cards, your_getcards, field_cards, displaymode):
    dst_stage = stage.copy()
    
    return dst_stage
    
    

if __name__ == '__main__':
    stage = draw_init()
    stage = draw_oya_decision(stage, 112, 101)
    cv2.imshow("stage", stage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()