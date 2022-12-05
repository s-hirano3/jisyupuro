#!/usr/bin/env python
# -*- coding: utf-8 -*-


CARDS = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44, 51, 52, 53, 54, 61, 62, 63, 64,
         71, 72, 73, 74, 81, 82, 83, 84, 91, 92, 93, 94, 101 ,102, 103, 104, 111, 112, 113, 114, 121, 122, 123, 124]
HIKARI = [11, 31, 81, 111, 121]
TANE = [21, 41, 51, 61, 71, 82, 91, 101, 112]
TAN = [12, 22, 32, 42, 52, 62, 72, 92, 102, 113]
KASU = [13, 14, 23, 24, 33, 34, 43, 44, 53, 54, 63, 64, 73, 74, 83, 84, 91, 93, 94, 103, 104, 114, 122, 123, 124]
HANAMI = [31, 91]
TUKIMI = [81, 91]
INOSHIKATYO = [61, 71, 101]
AKATAN = [12, 22, 32]
AOTAN = [62, 92, 102]

YAKU_CARDS = [HIKARI, HIKARI, HIKARI, HIKARI, HANAMI, TUKIMI, INOSHIKATYO, AKATAN, AOTAN, TANE, TAN, KASU]


class enemy_move():
    def __init__(self):        
        self.my_cards = []
        self.my_getcards = []
        self.my_score = []
        self.my_total_score = []
        self.my_koikoi_flag = []

        self.your_cards = []
        self.your_getcards = []
        self.your_score = []
        self.your_total_score = []
        self.your_koikoi_flag = []

        self.field_cards = []
        self.yamafuda = []

        # [五光，四光，雨入り四光，三光，花見で一杯，月見で一杯，猪鹿蝶，赤短，青短，タネ，タン，カス]
        self.need_cards = []  # 役成立までに必要な枚数 確定/獲得したカード(getcards)を基準に
        self.need_cards_possible = []  # 役成立までに必要な枚数 手札を基準に

        


    
    def UpdateParam(self, field_cards, yamafuda, my_cards, my_getcards, your_cards, your_getcards, my_score, my_total_score, your_score, your_total_score, my_koikoi_flag, your_koikoi_flag):
        self.my_cards.append(my_cards)
        self.my_getcards.append(my_getcards)
        self.my_score.append(my_score)
        self.my_total_score.append(my_total_score)
        self.my_koikoi_flag.append(my_koikoi_flag)

        self.your_cards.append(your_cards)
        self.your_getcards.append(your_getcards)
        self.your_score.append(your_score)
        self.your_total_score.append(your_total_score)
        self.your_koikoi_flag.append(your_koikoi_flag)

        self.field_cards.append(field_cards)
        self.yamafuda.append(yamafuda)


    
    def detect_need_cards(self):
        for i in range(len(YAKU_CARDS)):
            

    