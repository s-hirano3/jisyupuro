#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cv2
import numpy as np


# カード読みこみ
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


# カード番号と画像を対応付けるdict
CARDS_DICT = {11:card11, 12:card12, 13:card13, 14:card14, 21:card21, 22:card22, 23:card23, 24:card24, 31:card31, 32:card32, 33:card33, 34:card34, 41:card41, 42:card42, 43:card43, 44:card44,
              51:card51, 52:card52, 53:card53, 54:card54, 61:card61, 62:card62, 63:card63, 64:card64, 71:card71, 72:card72, 73:card73, 74:card74, 81:card81, 82:card82, 83:card83, 84:card84,
              91:card91, 92:card92, 93:card93, 94:card94, 101:card101, 102:card102, 103:card103, 104:card104, 111:card111, 112:card112, 113:card113, 114:card114, 121:card121, 122:card122, 123:card123, 124:card124}


# (blue, green, red)
FIELD_COLOR = (135, 153, 0)
CARD_COLOR = (76, 60, 167)
WHITE = (255, 255, 255)


# カード描画座標 (左上x, 左上y, 右下x, 右下y)
# cv2.rectangleするときは ((0,1),(2,3))
# roi指定するときは [1:3, 0:2]
COORDS_FIELD = [(10, 454, 68, 546), (88, 454, 146, 546), (166, 454, 224, 546), (244, 454, 302, 546), (322, 454, 380, 546), (400, 454, 458, 546), (478, 454, 536, 546), (556, 454, 614, 546), (634, 454, 692, 546), (712, 454, 770, 546), (790, 454, 848, 546), (868, 454, 926, 546), (946, 454, 1004, 546), (1024, 454, 1082, 546), (1102, 454, 1160, 546), (1180, 454, 1238, 546)]
COORDS_YAMAFUDA = [(1336, 454, 1394, 546), (1414, 454, 1472, 546)]
COORDS_MY_CARDS = [(483, 898, 541, 990), (561, 898, 619, 990), (639, 898, 697, 990), (717, 898, 775, 990), (795, 898, 853, 990), (873, 898, 931, 990), (951, 898, 1009, 990), (1029, 898, 1087, 990)]
COORDS_MY_GETCARDS = [[(30, 624, 88, 716), (98, 624, 156, 716), (166, 624, 224, 716), (64, 736, 122, 828), (132, 736, 190, 828)],
                      [(264, 624, 322, 716), (332, 624, 390, 716), (400, 624, 458, 716), (468, 624, 526, 716), (536, 624, 594, 716), (264, 736, 322, 828), (332, 736, 390, 828), (400, 736, 458, 828), (468, 736, 526, 828), (536, 736, 594, 828)],
                      [(634, 624, 692, 716), (702, 624, 760, 716), (770, 624, 828, 716), (838, 624, 896, 716), (906, 624, 964, 716), (634, 736, 692, 828), (702, 736, 760, 828), (770, 736, 828, 828), (838, 736, 896, 828), (906, 736, 964, 828)],
                      [(1004, 624, 1062, 716), (1072, 624, 1130, 716), (1140, 624, 1198, 716), (1208, 624, 1266, 716), (1276, 624, 1334, 716), (1344, 624, 1402, 716), (1412, 624, 1470, 716), (1004, 736, 1062, 828), (1072, 736, 1130, 828), (1140, 736, 1198, 828), (1208, 736, 1266, 828), (1276, 736, 1334, 828), (1344, 736, 1402, 828), (1412, 736, 1470, 828)]]
COORDS_YOUR_CARDS = [(483, 10, 541, 102), (561, 10, 619, 102), (639, 10, 697, 102), (717, 10, 775, 102), (795, 10, 853, 102), (873, 10, 931, 102), (951, 10, 1009, 102), (1029, 10, 1087, 102)]
COORDS_YOUR_GETCARDS = [[(30, 172, 88, 264), (98, 172, 156, 264), (166, 172, 224, 264), (64, 284, 122, 376), (132, 284, 190, 376)],
                        [(264, 172, 322, 264), (332, 172, 390, 264), (400, 172, 458, 264), (468, 172, 526, 264), (536, 172, 594, 264), (264, 284, 322, 376), (332, 284, 390, 376), (400, 284, 458, 376), (468, 284, 526, 376), (536, 284, 594, 376)],
                        [(634, 172, 692, 264), (702, 172, 760, 264), (770, 172, 828, 264), (838, 172, 896, 264), (906, 172, 964, 264), (634, 284, 692, 376), (702, 284, 760, 376), (770, 284, 828, 376), (838, 284, 896, 376), (906, 284, 964, 376)],
                        [(1004, 172, 1062, 264), (1072, 172, 1130, 264), (1140, 172, 1198, 264), (1208, 172, 1266, 264), (1276, 172, 1334, 264), (1344, 172, 1402, 264), (1412, 172, 1470, 264), (1004, 284, 1062, 376), (1072, 284, 1130, 376), (1140, 284, 1198, 376), (1208, 284, 1266, 376), (1276, 284, 1334, 376), (1344, 284, 1402, 376), (1412, 284, 1470, 376)]]


# カード番号表示座標 (左上x, 左上y, 右下x, 右下y)
COORDS_YAMAFUDA_MOJI = [(1336, 413, 1394, 453), (1414, 413, 1472, 453)]
COORDS_FIELD_MOJI = [(10, 413, 68, 453), (88, 413, 146, 453), (166, 413, 224, 453), (244, 413, 302, 453), (322, 413, 380, 453), (400, 413, 458, 453), (478, 413, 536, 453), (556, 413, 614, 453), (634, 413, 692, 453), (712, 413, 770, 453), (790, 413, 848, 453), (868, 413, 926, 453), (946, 413, 1004, 453), (1024, 413, 1082, 453), (1102, 413, 1160, 453), (1180, 413, 1238, 453)]
COORDS_MY_CARDS_MOJI = [(483, 857, 541, 897), (561, 857, 619, 897), (639, 857, 697, 897), (717, 857, 775, 897), (795, 857, 853, 897), (873, 857, 931, 897), (951, 857, 1009, 897), (1029, 857, 1087, 897)]
COORDS_YOUR_CARDS_MOJI = [(483, 103, 541, 143), (561, 103, 619, 143), (639, 103, 697, 143), (717, 103, 775, 143), (795, 103, 853, 143), (873, 103, 931, 143), (951, 103, 1009, 143), (1029, 103, 1087, 143)]
COORDS_MOJI_ALL = COORDS_YAMAFUDA_MOJI + COORDS_FIELD_MOJI + COORDS_MY_CARDS_MOJI + COORDS_YOUR_CARDS_MOJI

# 役リスト
HIKARI = [11, 31, 81, 111, 121]
TANE = [21, 41, 51, 61, 71, 82, 91, 101, 112]
TAN = [12, 22, 32, 42, 52, 62, 72, 92, 102, 113]
KASU = [13, 14, 23, 24, 33, 34, 43, 44, 53, 54, 63, 64, 73, 74, 83, 84, 91, 93, 94, 103, 104, 114, 122, 123, 124]



# ゲーム開始時・月始まりで呼ばれる描画関数
# ステージを作り直し，全てのカード枠を表示
def draw_init():
    stage = np.full((1000, 1500, 3), FIELD_COLOR, dtype=np.uint8)  # ステージ背景設定
    stage = cv2.rectangle(stage, (200,500), (258,593),color=FIELD_COLOR, thickness=5)  # ステージ作成(ダミー)
    
    dst_stage = stage.copy()
    
    # 文字表示領域をリセット
    for i in range(len(COORDS_MOJI_ALL)):
        coords = COORDS_MOJI_ALL[i]
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
    
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



# 親決めの際に呼ばれる描画関数
# 山札座標に自分が引いたカードと相手が引いたカードを表示する
def draw_oya_decision(stage, my_card, your_card):
    dst_stage = stage.copy()
    
    # 文字表示領域をリセット
    for i in range(len(COORDS_MOJI_ALL)):
        coords = COORDS_MOJI_ALL[i]
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
    
    my_coords = COORDS_YAMAFUDA[0]
    my_coords_moji = COORDS_YAMAFUDA_MOJI[0]
    dst_stage[my_coords[1]:my_coords[3], my_coords[0]:my_coords[2]] = CARDS_DICT[my_card]
    cv2.putText(dst_stage, str(my_card), (my_coords_moji[0],my_coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
    
    your_coords = COORDS_YAMAFUDA[1]
    your_coords_moji = COORDS_YAMAFUDA_MOJI[1]
    dst_stage[your_coords[1]:your_coords[3], your_coords[0]:your_coords[2]] = CARDS_DICT[your_card]
    cv2.putText(dst_stage, str(your_card), (your_coords_moji[0],your_coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
    
    #v2.imshow("stage", dst_stage)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    return dst_stage



# 月始まりに，自分の手札と場のカード(+相手の手札)を表示する描画関数
def draw_play_init(stage, my_cards, your_cards, field_cards, displaymode):
    stage = draw_init()
    dst_stage = stage.copy()

    # 文字表示領域をリセット
    for i in range(len(COORDS_MOJI_ALL)):
        coords = COORDS_MOJI_ALL[i]
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)

    for i in range(len(COORDS_YAMAFUDA)):
        coords = COORDS_YAMAFUDA[i]
        if i == 0:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
        elif i == 1:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=CARD_COLOR, thickness=-1)
    
    field_cards.sort()
    for i in range(len(field_cards)):
        coords = COORDS_FIELD[i]
        coords_moji = COORDS_FIELD_MOJI[i]
        field_card = field_cards[i]
        dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[field_card]
        cv2.putText(dst_stage, str(field_card), (coords_moji[0],coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
    
    my_cards.sort()
    for i in range(len(my_cards)):
        coords = COORDS_MY_CARDS[i]
        coords_moji = COORDS_MY_CARDS_MOJI[i]
        my_card = my_cards[i]
        dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_card]
        cv2.putText(dst_stage, str(my_card), (coords_moji[0],coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
    
    # displaymode=0なら相手の手札を表示しない
    your_cards.sort()
    if displaymode == 0:
        for i in range(len(your_cards)):
            coords = COORDS_YOUR_CARDS[i]
            dst_stage = cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=CARD_COLOR, thickness=-1)
    else:
        for i in range(len(your_cards)):
            coords = COORDS_YOUR_CARDS[i]
            coords_moji = COORDS_YOUR_CARDS_MOJI[i]
            your_card = your_cards[i]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_card]
            cv2.putText(dst_stage, str(your_card), (coords_moji[0],coords_moji[1]+24), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
            
            
    #cv2.imshow("stage", dst_stage)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
      
    return dst_stage



# 「手札から1枚出す」ターンの終わりのタイミングで，手札・場・獲得カードを更新して表示する描画関数 
def draw_play_tefuda(stage, my_cards, my_getcards, your_cards, your_getcards, field_cards, displaymode):
    dst_stage = stage.copy()
    
    # 文字表示領域をリセット
    for i in range(len(COORDS_MOJI_ALL)):
        coords = COORDS_MOJI_ALL[i]
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)

    for i in range(len(COORDS_YAMAFUDA)):
        coords = COORDS_YAMAFUDA[i]
        if i == 0:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
        elif i == 1:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=CARD_COLOR, thickness=-1)
            
    field_cards.sort()
    num_field_card = len(field_cards)
    for i in range(len(COORDS_FIELD)):
        coords = COORDS_FIELD[i]
        coords_moji = COORDS_FIELD_MOJI[i]
        if i < num_field_card:
            field_card = field_cards[i]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[field_card]
            cv2.putText(dst_stage, str(field_card), (coords_moji[0],coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
        else:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
    
    my_cards.sort()
    num_my_card = len(my_cards)
    for i in range(len(COORDS_MY_CARDS)):
        coords = COORDS_MY_CARDS[i]
        coords_moji = COORDS_MY_CARDS_MOJI[i]
        if i < num_my_card:
            my_card = my_cards[i]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_card]
            cv2.putText(dst_stage, str(my_card), (coords_moji[0],coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
        else:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)        
    
    # displaymode=0なら相手の手札を表示しない
    your_cards.sort()
    num_your_cards = len(your_cards)
    if displaymode == 0:
        for i in range(len(COORDS_YOUR_CARDS)):
            coords = COORDS_YOUR_CARDS[i]
            if i < num_your_cards:
                dst_stage = cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=CARD_COLOR, thickness=-1)
            else:
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)        
    else:
        for i in range(len(COORDS_YOUR_CARDS)):
            coords = COORDS_YOUR_CARDS[i]
            coords_moji = COORDS_YOUR_CARDS_MOJI[i]
            if i < num_your_cards:
                your_card = your_cards[i]
                dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_card]
                cv2.putText(dst_stage, str(your_card), (coords_moji[0],coords_moji[1]+24), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
            else:
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)        
    
    count_my_getcard_hikari = 0
    count_my_getcard_tane = 0
    count_my_getcard_tan = 0
    count_my_getcard_kasu = 0
    for i in range(len(my_getcards)):
        my_getcard = my_getcards[i]
        if my_getcard in HIKARI:
            coords = COORDS_MY_GETCARDS[0][count_my_getcard_hikari]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_getcard]
            count_my_getcard_hikari += 1
        if my_getcard in TANE:
            coords = COORDS_MY_GETCARDS[1][count_my_getcard_tane]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_getcard]
            count_my_getcard_tane += 1
        if my_getcard in TAN:
            coords = COORDS_MY_GETCARDS[2][count_my_getcard_tan]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_getcard]
            count_my_getcard_tan += 1
        if my_getcard in KASU:
            coords = COORDS_MY_GETCARDS[3][count_my_getcard_kasu]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_getcard]
            count_my_getcard_kasu += 1
    
    count_your_getcard_hikari = 0
    count_your_getcard_tane = 0
    count_your_getcard_tan = 0
    count_your_getcard_kasu = 0
    for i in range(len(your_getcards)):
        your_getcard = your_getcards[i]
        if your_getcard in HIKARI:
            coords = COORDS_YOUR_GETCARDS[0][count_your_getcard_hikari]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_getcard]
            count_your_getcard_hikari += 1
        if your_getcard in TANE:
            coords = COORDS_YOUR_GETCARDS[1][count_your_getcard_tane]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_getcard]
            count_your_getcard_tane += 1
        if your_getcard in TAN:
            coords = COORDS_YOUR_GETCARDS[2][count_your_getcard_tan]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_getcard]
            count_your_getcard_tan += 1
        if your_getcard in KASU:
            coords = COORDS_YOUR_GETCARDS[3][count_your_getcard_kasu]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_getcard]
            count_your_getcard_kasu += 1
    
    #cv2.imshow("stage", dst_stage)
    #cv2.waitKey(0)
    #cv2.destoryAllWindows()
        
    return dst_stage
    
    

# 「山札から1枚引く」ターンで，引いた直後とターン終了時に2回呼ばれ，ドローカード・手札・場・獲得カードを更新して表示する描画関数
# timing: 0ならドローした直後，1ならターン終了時
def draw_play_yamafuda(stage, my_cards, my_getcards, your_cards, your_getcards, field_cards, draw_card, displaymode, timing):
    dst_stage = stage.copy()
    
    # 文字表示領域をリセット
    for i in range(len(COORDS_MOJI_ALL)):
        coords = COORDS_MOJI_ALL[i]
        cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
    
    # 山札から引いたカードの表示/非表示
    for i in range(len(COORDS_YAMAFUDA)):
        coords = COORDS_YAMAFUDA[i]
        coords_moji = COORDS_YAMAFUDA_MOJI[i]
        if i == 0:
            if timing == 0:
                dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[draw_card]
                cv2.putText(dst_stage, str(draw_card), (coords_moji[0],coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
            else:
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
        elif i == 1:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=CARD_COLOR, thickness=-1)
    
    field_cards.sort()
    num_field_card = len(field_cards)
    for i in range(len(COORDS_FIELD)):
        coords = COORDS_FIELD[i]
        coords_moji = COORDS_FIELD_MOJI[i]
        if i < num_field_card:
            field_card = field_cards[i]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[field_card]
            cv2.putText(dst_stage, str(field_card), (coords_moji[0],coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
        else:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
    
    my_cards.sort()
    num_my_card = len(my_cards)
    for i in range(len(COORDS_MY_CARDS)):
        coords = COORDS_MY_CARDS[i]
        coords_moji = COORDS_MY_CARDS_MOJI[i]
        if i < num_my_card:
            my_card = my_cards[i]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_card]
            cv2.putText(dst_stage, str(my_card), (coords_moji[0],coords_moji[3]-4), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
        else:
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
            cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)        
    
    # displaymode=0なら相手の手札を表示しない
    your_cards.sort()
    num_your_cards = len(your_cards)
    if displaymode == 0:
        for i in range(len(COORDS_YOUR_CARDS)):
            coords = COORDS_YOUR_CARDS[i]
            if i < num_your_cards:
                dst_stage = cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=CARD_COLOR, thickness=-1)
            else:
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)
    else:
        for i in range(len(COORDS_YOUR_CARDS)):
            coords = COORDS_YOUR_CARDS[i]
            coords_moji = COORDS_YOUR_CARDS_MOJI[i]
            if i < num_your_cards:
                your_card = your_cards[i]
                dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_card]
                cv2.putText(dst_stage, str(your_card), (coords_moji[0],coords_moji[1]+24), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=WHITE, thickness=2, lineType=cv2.LINE_4)
            else:
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=FIELD_COLOR, thickness=-1)
                cv2.rectangle(dst_stage, (coords[0],coords[1]), (coords[2],coords[3]), color=WHITE, thickness=2)        
                
    count_my_getcard_hikari = 0
    count_my_getcard_tane = 0
    count_my_getcard_tan = 0
    count_my_getcard_kasu = 0
    for i in range(len(my_getcards)):
        my_getcard = my_getcards[i]
        if my_getcard in HIKARI:
            coords = COORDS_MY_GETCARDS[0][count_my_getcard_hikari]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_getcard]
            count_my_getcard_hikari += 1
        if my_getcard in TANE:
            coords = COORDS_MY_GETCARDS[1][count_my_getcard_tane]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_getcard]
            count_my_getcard_tane += 1
        if my_getcard in TAN:
            coords = COORDS_MY_GETCARDS[2][count_my_getcard_tan]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_getcard]
            count_my_getcard_tan += 1
        if my_getcard in KASU:
            coords = COORDS_MY_GETCARDS[3][count_my_getcard_kasu]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[my_getcard]
            count_my_getcard_kasu += 1
    
    count_your_getcard_hikari = 0
    count_your_getcard_tane = 0
    count_your_getcard_tan = 0
    count_your_getcard_kasu = 0
    for i in range(len(your_getcards)):
        your_getcard = your_getcards[i]
        if your_getcard in HIKARI:
            coords = COORDS_YOUR_GETCARDS[0][count_your_getcard_hikari]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_getcard]
            count_your_getcard_hikari += 1
        if your_getcard in TANE:
            coords = COORDS_YOUR_GETCARDS[1][count_your_getcard_tane]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_getcard]
            count_your_getcard_tane += 1
        if your_getcard in TAN:
            coords = COORDS_YOUR_GETCARDS[2][count_your_getcard_tan]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_getcard]
            count_your_getcard_tan += 1
        if your_getcard in KASU:
            coords = COORDS_YOUR_GETCARDS[3][count_your_getcard_kasu]
            dst_stage[coords[1]:coords[3], coords[0]:coords[2]] = CARDS_DICT[your_getcard]
            count_your_getcard_kasu += 1    
    
    #cv2.imshow("stage", dst_stage)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    return dst_stage
    

if __name__ == '__main__':
    stage = draw_init()
    stage = draw_oya_decision(stage, 112, 101)
    cv2.imshow("stage", stage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


# TODO
# DONE 手札・場のカードを獲得したときに，そのカードの表示を消す 　　現状放置なので無限カード増殖してる
# DONE 獲得カードの枠を増やす：tane5→10, tan5→10, kasu10→16???
# DONE カードの番号を表示する：自分の手札・相手の手札・場のカード
# DONE ちょっと小さいけど macで試してみて表示エリアの大きさの確認
# DONE 山札から引いたカードを表示する

# tane 10→8 kasu 14→16
