#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import copy
import numpy as np
from detect_yaku import *
from layer import *

CARDS = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44, 51, 52, 53, 54, 61, 62, 63, 64,
         71, 72, 73, 74, 81, 82, 83, 84, 91, 92, 93, 94, 101 ,102, 103, 104, 111, 112, 113, 114, 121, 122, 123, 124]
GOKOU = [11, 31, 81, 111, 121]
YONKOU = [11, 31, 81, 121]
AMESIKOU = [11, 31, 81, 121]  # 雨四光に111(雨柳)は必須なので，111だけ個別に処理する
SANKOU = [11, 31, 81, 121]
HANAMI = [31, 91]
TUKIMI = [81, 91]
INOSHIKATYO = [61, 71, 101]
AKATAN = [12, 22, 32]
AOTAN = [62, 92, 102]
TANE = [21, 41, 51, 61, 71, 82, 91, 101, 112]  # 9
TAN = [12, 22, 32, 42, 52, 62, 72, 92, 102, 113]  # 10
KASU = [13, 14, 23, 24, 33, 34, 43, 44, 53, 54, 63, 64, 73, 74, 83, 84, 91, 93, 94, 103, 104, 114, 122, 123, 124]  # 25

YAKU_DICT = {"GOKOU":GOKOU, "YONKOU":YONKOU, "AMESIKOU":[11,31,81,111,121], "SANKOU":SANKOU, "HANAMI":HANAMI, "TUKIMI":TUKIMI, 
             "INOSHIKATYO":INOSHIKATYO, "AKATAN":AKATAN, "AOTAN":AOTAN, "TANE":TANE, "TAN":TAN, "KASU":KASU}
YAKU_POINT = {"GOKOU":10.0, "YONKOU":8.0, "AMESIKOU":7.0, "SANKOU":5.0, "HANAMI":5.0, "TUKIMI":5.0, "INOSHIKATYO":5.0, "AKATAN":5.0, "AOTAN":5.0, "TANE":1.0, "TAN":1.0, "KASU":1.0}
YAKU_POINT_OOGATI = {"GOKOU":15.0, "YONKOU":12.0, "AMESIKOU":10.5, "SANKOU":7.5, "HANAMI":7.5, "TUKIMI":7.5, "INOSHIKATYO":7.5, "AKATAN":7.5, "AOTAN":7.5, "TANE":1.0, "TAN":1.0, "KASU":1.0}  # 大勝ちシチュ：大物のポイント1.5倍
YAKU_POINT_NIGEKIGI = {"GOKOU":10.0, "YONKOU":8.0, "AMESIKOU":7.0, "SANKOU":5.0, "HANAMI":5.0, "TUKIMI":5.0, "INOSHIKATYO":5.0, "AKATAN":5.0, "AOTAN":5.0, "TANE":10.0, "TAN":10.0, "KASU":10.0}  # 逃げ切りシチュ：タネ・タン・カスのポイント10倍
YAKU_TMP_NUM = {"GOKOU":0, "YONKOU":1, "AMESIKOU":2, "SANKOU":3, "HANAMI":4, "TUKIMI":5, "INOSHIKATYO":6, "AKATAN":7, "AOTAN":8, "TANE":9, "TAN":10, "KASU":11}

# [五光，四光，雨入り四光，三光，花見で一杯，月見で一杯，猪鹿蝶，赤短，青短，タネ，タン，カス]
YAKU_LIST = [GOKOU, YONKOU, AMESIKOU, SANKOU, HANAMI, TUKIMI, INOSHIKATYO, AKATAN, AOTAN, TANE, TAN, KASU]
YAKU_LIST_NUM = [5, 4, 4, 3, 2, 2, 3, 3, 3, 5, 5, 10]



class EnemyMove():
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
        # 要素はリスト[my, you]でそれぞれ↑のリストが入る = 3重リストとなる
        # 役成立までに必要な枚数 不可能な場合は-1
        self.need_cards = []  # 確定=獲得したカード(my/your_getcards)を基準に
        self.need_cards_possible = []  # 手札(my/your_cards)を基準に
        
        
        
        # 学習済みニューラルネットワークモデルの読み込み
        dims = [(240,500), (500,200), (200,100), (100,5)]
        f = open("./param/init.txt", "r")  # init用
        ff = f.readlines()
        g = open("./param/end_of_turn3.txt")  # end of turn3用
        gg = g.readlines()
        h = open("./param/end_of_turn6.txt", "r")  # end of turn6用
        hh = h.readlines()
        
        self.model_init = Model()
        self.model_init.addlayer(Layer(240, 500))
        self.model_init.addlayer(Layer(500, 200))
        self.model_init.addlayer(Layer(200, 100))
        self.model_init.addlayer(Layer_output(100, 5))
        
        self.model_endofturn3 = Model()
        self.model_endofturn3.addlayer(Layer(240, 500))
        self.model_endofturn3.addlayer(Layer(500, 200))
        self.model_endofturn3.addlayer(Layer(200, 100))
        self.model_endofturn3.addlayer(Layer(100, 5))
        
        self.model_endofturn6 = Model()
        self.model_endofturn6.addlayer(Layer(240, 500))
        self.model_endofturn6.addlayer(Layer(500, 200))
        self.model_endofturn6.addlayer(Layer(200, 100))
        self.model_endofturn6.addlayer(Layer(100, 5))
        
        for i in range(3):
            if i == 0:
                model = self.model_init
                lines = ff
                index = [-8, -7, -6, -5]
            elif i == 1:
                model = self.model_endofturn3
                lines = gg
                index = [-4, -3, -2, -1]
            elif i == 2:
                model = self.model_endofturn6
                lines = hh
                index = [-4, -3, -2, -1]
            
            for j in range(4):
                weight = lines[index[j]].split(" ")
                weight.pop(-1)
                for k in range(len(weight)):
                    weight[k] = float(weight[k])
                weight = np.reshape(np.array(weight), dims[j])
                model.layers[j].weight = weight
                


    
    
    def UpdateParam(self, field_cards, yamafuda, my_cards, my_getcards, your_cards, your_getcards, my_score, your_score, my_total_score, your_total_score, my_koikoi_flag, your_koikoi_flag):
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

        self.DetectNeedCards()


    
    
    def DetectNeedCardsMonteCarlo(self, my_cards, my_getcards, your_cards, your_getcards):
        need_card = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
        need_card_possible = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

        my_recent_getcards = copy.deepcopy(my_getcards)
        my_recent_getcards_possible = my_getcards + my_cards

        for yaku_num in range(len(YAKU_LIST)):
            counter = 0
            counter_possible = 0
            yaku_cards = YAKU_LIST[yaku_num]

            for card in yaku_cards:
                if card in my_recent_getcards:
                    counter += 1
                if card in my_recent_getcards_possible:
                    counter_possible += 1

            my_append_num = max(0, YAKU_LIST_NUM[yaku_num] - counter)
            my_append_num_possible = max(0, YAKU_LIST_NUM[yaku_num] - counter_possible)

            if yaku_num == 1:
                if my_append_num == 0:
                    if 111 not in my_recent_getcards:
                        my_append_num = 1
                if my_append_num_possible == 0:
                    if 111 not in my_recent_getcards_possible:
                        my_append_num_possible = 1

            need_card[0][yaku_num] = my_append_num
            need_card_possible[0][yaku_num] = my_append_num_possible

            if yaku_num in [0, 1, 4, 5, 6, 7, 8]:
                if counter >= 1:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 3:
                if counter >= 2:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 9:
                if counter >= 5:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 10:
                if counter >= 6:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 11:
                if counter >= 16:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 2:
                if 111 in my_recent_getcards:
                    need_card[1][yaku_num] = -1
                else:
                    if counter >= 2:
                        need_card[1][yaku_num] = -1
            

        # your_recent_getcards = your_getcards.copy()
        your_recent_getcards = copy.deepcopy(your_getcards)
        your_recent_getcards_possible = your_getcards + your_cards

        for yaku_num in range(len(YAKU_LIST)):
            counter = 0
            counter_possible = 0
            yaku_cards = YAKU_LIST[yaku_num]

            for card in yaku_cards:
                if card in your_recent_getcards:
                    counter += 1
                if card in your_recent_getcards_possible:
                    counter_possible += 1
            
            your_append_num = max(0, YAKU_LIST_NUM[yaku_num] - counter)
            your_append_num_possible = max(0, YAKU_LIST_NUM[yaku_num] - counter_possible)

            if yaku_num == 2:
                if your_append_num == 0:
                    if 111 not in your_recent_getcards:
                        your_append_num = 1
                if your_append_num_possible == 0:
                    if 111 not in your_recent_getcards_possible:
                        your_append_num_possible = 1
            
            if need_card[1][yaku_num] != -1:
                need_card[1][yaku_num] = your_append_num
                need_card_possible[1][yaku_num] = your_append_num_possible
            else:
                need_card_possible[1][yaku_num] = -1
            
            if yaku_num in [0, 1, 4, 5, 6, 7, 8]:
                if counter >= 1:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 3:
                if counter >= 2:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 9:
                if counter >= 5:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 10:
                if counter >= 6:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 11:
                if counter >= 16:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 2:
                if 111 in your_recent_getcards:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
                else:
                    if counter >= 2:
                        need_card[0][yaku_num] = -1
                        need_card_possible[0][yaku_num] = -1           

        return need_card, need_card_possible


    
    # モンテカルロ法の中でしか使わない
    def FieldMatchingProcess(self, my_need_card, my_need_card_possible, your_need_card, select_card, get_cards, field_cards):
        select_card_month = select_card // 10

        field_month = []
        for i in range(len(field_cards)):
            field_month.append(field_cards[i] // 10)

        
        if field_month.count(select_card_month) == 0:
            field_cards.append(select_card)
        
        elif field_month.count(select_card_month) == 1:
            tmp_index = field_month.index(select_card_month)
            get_card_from_field = field_cards[tmp_index]

            field_cards.remove(get_card_from_field)
            get_cards.append(select_card)
            get_cards.append(get_card_from_field)
        
        elif field_month.count(select_card_month) == 3:
            get_cards_from_field = []
            for field_card in field_cards:
                if field_card // 10 == select_card_month:
                    get_cards_from_field.append(field_card)
            
            for i in range(3):
                field_cards.remove(get_cards_from_field[i])
                get_cards.append(select_card)
                get_cards.append(get_cards_from_field[i])

        elif field_month.count(select_card_month) == 2:
            get_kouho_from_field = []
            for field_card in field_cards:
                if field_card // 10 == select_card_month:
                    get_kouho_from_field.append(field_card)
            
            kouho_cards = []
            for i in range(2):
                kouho_cards.append([select_card, get_kouho_from_field[i]])
            
            kouho_score = []
            kouho_score_possible = []
            kouho_score_teki = []
            for i in range(len(kouho_cards)):
                score = 0
                score_possible = 0
                score_teki = 0
                for j in range(2):
                    kouho = kouho_cards[i][j]
                    for key, value in YAKU_DICT.items():
                        yaku_num = YAKU_TMP_NUM[key]
                        if kouho in value:
                            if my_need_card[yaku_num] not in [-1, 0]:
                                score += YAKU_POINT[key] / my_need_card[yaku_num]
                            if my_need_card_possible[yaku_num] not in [-1, 0]:
                                score_possible += YAKU_POINT[key] / my_need_card_possible[yaku_num]
                            if j == 1:
                                if your_need_card[yaku_num] not in [-1, 0]:
                                    score_teki += YAKU_POINT[key] / your_need_card[yaku_num]
                kouho_score.append(score)
                kouho_score_possible.append(score_possible)
                kouho_score_teki.append(score_teki)
            new_score = []
            new_new_score = []
            for i in range(len(kouho_score)):
                new_score.append(kouho_score[i] + kouho_score_possible[i]/5)
                new_new_score.append(new_score[i] + kouho_score_teki[i])
            
            # select_from_kouho = kouho_cards[new_score.index(max(new_score))][1]
            select_from_kouho = kouho_cards[new_new_score.index(max(new_new_score))][1]
            
            field_cards.remove(select_from_kouho)
            get_cards.append(select_card)
            get_cards.append(select_from_kouho)

        return get_cards, field_cards


    
    
    
    def TefudaMonteCarlo(self, my_need_card, my_need_card_possible, your_need_card, tefuda_cards, get_cards, field_cards):
        tefuda_field_matching = []
        for i in range(len(tefuda_cards)):
            for j in range(len(field_cards)):
                if (tefuda_cards[i] // 10) == (field_cards[j] // 10):
                    tefuda_field_matching.append((tefuda_cards[i], field_cards[j]))
        
        tefuda_score = []
        tefuda_score_possible = []
        tefuda_score_teki = []
        if len(tefuda_field_matching) != 0:
            for i in range(len(tefuda_field_matching)):
                score = 0
                score_possible = 0
                score_teki = 0
                for j in range(2):
                    tefuda = tefuda_field_matching[i][j]
                    for key, value in YAKU_DICT.items():
                        yaku_num = YAKU_TMP_NUM[key]
                        if tefuda in value:
                            if my_need_card[yaku_num] not in [-1, 0]:
                                score += YAKU_POINT[key] / my_need_card[yaku_num]
                            if my_need_card_possible[yaku_num] not in [-1, 0]:
                                score_possible += YAKU_POINT[key] / my_need_card_possible[yaku_num]
                            if j == 1:
                                if your_need_card[yaku_num] not in [-1, 0]:
                                    score_teki += YAKU_POINT[key] / your_need_card[yaku_num]
                tefuda_score.append(score)
                tefuda_score_possible.append(score_possible)
                tefuda_score_teki.append(score_teki)
            new_score = []
            new_new_score = []
            for i in range(len(tefuda_score)):
                new_score.append(tefuda_score[i] + tefuda_score_possible[i]/5)
                new_new_score.append(new_score[i] + tefuda_score_teki[i])
            
            # select_card = tefuda_field_matching[new_score.index(max(new_score))][0]
            select_card = tefuda_field_matching[new_new_score.index(max(new_new_score))][0]
        
        else:
            tefuda_score = []
            for i in range(len(tefuda_cards)):
                score = 0
                tefuda = tefuda_cards[i]
                for key, value in YAKU_DICT.items():
                    yaku_num = YAKU_TMP_NUM[key]
                    if tefuda in value:
                        if your_need_card[yaku_num] not in [-1, 0]:
                            score += YAKU_POINT[key] / your_need_card[yaku_num]
                tefuda_score.append(score)
            
            select_card = tefuda_cards[tefuda_score.index(min(tefuda_score))]

        
        tefuda_cards.remove(select_card)
        get_cards, field_cards = self.FieldMatchingProcess(my_need_card, my_need_card_possible, your_need_card, select_card, get_cards, field_cards)

        return tefuda_cards, get_cards, field_cards



    
    
    def DrawMonteCarlo(self, nokori_cards, my_need_card, my_need_card_possible, your_need_card, get_cards, field_cards):
        draw_card = nokori_cards.pop(0)
        get_cards, field_cards = self.FieldMatchingProcess(my_need_card, my_need_card_possible, your_need_card,  draw_card, get_cards, field_cards)
        return nokori_cards, get_cards, field_cards




    def MonteCarlo(self, player, repeat_num, month, turn, repetition):
        my_cards_init = self.my_cards[-1]
        my_getcards_init = self.my_getcards[-1]
        your_cards_init = self.your_cards[-1]
        your_getcards_init = self.your_getcards[-1]
        my_score_init = self.my_score[-1]
        my_total_score_init = self.my_total_score[-1]
        your_score_init = self.your_score[-1]
        your_total_score_init = self.your_total_score[-1]
        field_cards_init = self.field_cards[-1]
        if player == "Me":
            siyouzumi_cards = my_cards_init + my_getcards_init + your_getcards_init + field_cards_init
        elif player == "You":
            siyouzumi_cards = my_getcards_init + your_cards_init + your_getcards_init + field_cards_init
        
        nokori_cards_init = []
        for card in CARDS:
            if card not in siyouzumi_cards:
                nokori_cards_init.append(card)
        
        if (month + repetition) % 2 == 0:
            player_list = ["Me", "You"] * (8-turn)
            if player == "Me":
                player_list = player_list[1:]
            elif player == "You":
                player_list = player_list[2:]
        elif (month + repetition) % 2 == 1:
            player_list = ["You", "Me"] * (8-turn)
            if player == "You":
                player_list = player_list[1:]
            elif player == "Me":
                player_list = player_list[2:]
        

        score_list = []
        for i in range(repeat_num):
            # print("start roop {}".format(i))
            my_score = 0
            your_score = 0

            my_cards = copy.deepcopy(my_cards_init)
            my_getcards = copy.deepcopy(my_getcards_init)
            your_cards = copy.deepcopy(your_cards_init)
            your_getcards = copy.deepcopy(your_getcards_init)
            field_cards = copy.deepcopy(field_cards_init)

            nokori_cards = copy.deepcopy(nokori_cards_init)

            for p in player_list:
                random.shuffle(nokori_cards)

                if p == "Me":
                    # Tefuda
                    need_card, need_card_possible = self.DetectNeedCardsMonteCarlo(my_cards, my_getcards, your_cards, your_getcards)
                    my_cards, my_getcards, field_cards = self.TefudaMonteCarlo(need_card[0], need_card_possible[0], need_card[1], my_cards, my_getcards, field_cards)

                    # Draw
                    need_card, need_card_possible = self.DetectNeedCardsMonteCarlo(my_cards, my_getcards, your_cards, your_getcards)
                    nokori_cards, my_getcards, field_cards = self.DrawMonteCarlo(nokori_cards, need_card[0], need_card_possible[0], need_card[1], my_getcards, field_cards)

                    my_yaku_list, my_score = detect_yaku(my_getcards)
                    # print("Me  {} {}".format(my_score_init, my_score))

                elif p == "You":
                    # Tefuda
                    need_card, need_card_possible = self.DetectNeedCardsMonteCarlo(my_cards, my_getcards, your_cards, your_getcards)
                    your_cards, your_getcards, field_cards = self.TefudaMonteCarlo(need_card[1], need_card_possible[1], need_card[0], your_cards, your_getcards, field_cards)

                    # Draw
                    need_card, need_card_possible = self.DetectNeedCardsMonteCarlo(my_cards, my_getcards, your_cards, your_getcards)
                    nokori_cards, your_getcards, field_cards = self.DrawMonteCarlo(nokori_cards, need_card[1], need_card_possible[1], need_card[0], your_getcards, field_cards)

                    your_yaku_list, your_score = detect_yaku(your_getcards)
                    # print("You {} {}".format(your_score_init, your_score))
                
                
                if player == "Me":  # 自分がこいこいしたとして，モンテカルロ法
                    if my_score > my_score_init:
                        score_list.append(my_score)
                        break
                    elif your_score > your_score_init:
                        score_list.append(your_score * (-2))
                        break
                elif player == "You":
                    if my_score > my_score_init:
                        score_list.append(my_score * (-2))
                        break
                    elif your_score > your_score_init:
                        score_list.append(your_score)
                        break

            else:
                if player == "Me":
                    score_list.append(my_score_init)
                elif player == "You":
                    score_list.append(your_score_init)

        return score_list


    
    
    def MonteCarlo_correct(self, player, repeat_num, month, turn, repetition):
        my_cards_init = self.my_cards[-1]
        my_getcards_init = self.my_getcards[-1]
        your_cards_init = self.your_cards[-1]
        your_getcards_init = self.your_getcards[-1]
        my_score_init = self.my_score[-1]
        my_total_score_init = self.my_total_score[-1]
        your_score_init = self.your_score[-1]
        your_total_score_init = self.your_total_score[-1]
        field_cards_init = self.field_cards[-1]
        if player == "Me":
            siyouzumi_cards = my_cards_init + my_getcards_init + your_getcards_init + field_cards_init
        elif player == "You":
            siyouzumi_cards = my_getcards_init + your_cards_init + your_getcards_init + field_cards_init
        
        nokori_cards_init = []
        for card in CARDS:
            if card not in siyouzumi_cards:
                nokori_cards_init.append(card)
        
        if (month + repetition) % 2 == 0:
            player_list = ["Me", "You"] * (8-turn)
            if player == "Me":
                player_list = player_list[1:]
            elif player == "You":
                player_list = player_list[2:]
        elif (month + repetition) % 2 == 1:
            player_list = ["You", "Me"] * (8-turn)
            if player == "You":
                player_list = player_list[1:]
            elif player == "Me":
                player_list = player_list[2:]
        

        score_list = []
        for i in range(repeat_num):
            # print("start roop {}".format(i))
            my_score = 0
            your_score = 0

            nokori_cards = copy.deepcopy(nokori_cards_init)

            # 相手プレイヤーの手札は分からないので，nokori_cardsからランダムに取り出す
            if player == "Me":
                my_cards = copy.deepcopy(my_cards_init)
                your_cards = []
                for j in range(len(your_cards_init)):
                    random.shuffle(nokori_cards)
                    your_cards.append(nokori_cards.pop(0))
            elif player == "You":
                my_cards = []
                for j in range(len(my_cards_init)):
                    random.shuffle(nokori_cards)
                    my_cards.append(nokori_cards.pop(0))
                your_cards = copy.deepcopy(your_cards_init)
            my_getcards = copy.deepcopy(my_getcards_init)
            your_getcards = copy.deepcopy(your_getcards_init)
            field_cards = copy.deepcopy(field_cards_init)
            

            for p in player_list:
                random.shuffle(nokori_cards)

                if p == "Me":
                    # Tefuda
                    need_card, need_card_possible = self.DetectNeedCardsMonteCarlo(my_cards, my_getcards, your_cards, your_getcards)
                    my_cards, my_getcards, field_cards = self.TefudaMonteCarlo(need_card[0], need_card_possible[0], need_card[1], my_cards, my_getcards, field_cards)

                    # Draw
                    need_card, need_card_possible = self.DetectNeedCardsMonteCarlo(my_cards, my_getcards, your_cards, your_getcards)
                    nokori_cards, my_getcards, field_cards = self.DrawMonteCarlo(nokori_cards, need_card[0], need_card_possible[0], need_card[1], my_getcards, field_cards)

                    my_yaku_list, my_score = detect_yaku(my_getcards)
                    # print("Me  {} {}".format(my_score_init, my_score))

                elif p == "You":
                    # Tefuda
                    need_card, need_card_possible = self.DetectNeedCardsMonteCarlo(my_cards, my_getcards, your_cards, your_getcards)
                    your_cards, your_getcards, field_cards = self.TefudaMonteCarlo(need_card[1], need_card_possible[1], need_card[0], your_cards, your_getcards, field_cards)

                    # Draw
                    need_card, need_card_possible = self.DetectNeedCardsMonteCarlo(my_cards, my_getcards, your_cards, your_getcards)
                    nokori_cards, your_getcards, field_cards = self.DrawMonteCarlo(nokori_cards, need_card[1], need_card_possible[1], need_card[0], your_getcards, field_cards)

                    your_yaku_list, your_score = detect_yaku(your_getcards)
                    # print("You {} {}".format(your_score_init, your_score))
                
                
                if player == "Me":  # 自分がこいこいしたとして，モンテカルロ法
                    if my_score > my_score_init:
                        score_list.append(my_score)
                        break
                    elif your_score > your_score_init:
                        score_list.append(your_score * (-2))
                        break
                elif player == "You":
                    if my_score > my_score_init:
                        score_list.append(my_score * (-2))
                        break
                    elif your_score > your_score_init:
                        score_list.append(your_score)
                        break

            else:
                if player == "Me":
                    score_list.append(my_score_init)
                elif player == "You":
                    score_list.append(your_score_init)

        return score_list




    def DetectNeedCards(self):
        need_card = [[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0]]  # my, your
        need_card_possible = [[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0]]  # my, your

        my_recent_getcards = self.my_getcards[-1]
        my_recent_getcards_possible = self.my_getcards[-1] + self.my_cards[-1]

        for yaku_num in range(len(YAKU_LIST)):
            counter = 0
            counter_possible = 0
            yaku_cards = YAKU_LIST[yaku_num]

            for card in yaku_cards:
                if card in my_recent_getcards:
                    counter += 1
                if card in my_recent_getcards_possible:
                    counter_possible += 1

            my_append_num = max(0, YAKU_LIST_NUM[yaku_num] - counter)
            my_append_num_possible = max(0, YAKU_LIST_NUM[yaku_num] - counter_possible)

            if yaku_num == 2:
                if my_append_num == 0:
                    if 111 not in my_recent_getcards:
                        my_append_num = 1
                if my_append_num_possible == 0:
                    if 111 not in my_recent_getcards_possible:
                        my_append_num_possible = 1

            need_card[0][yaku_num] = my_append_num
            need_card_possible[0][yaku_num] = my_append_num_possible

            # 相手が絶対に取れない役に-1をつける
            if yaku_num in [0, 1, 4, 5, 6, 7, 8]:  # 相手に1枚でも持たれたら終了
                if counter >= 1:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 3:
                if counter >= 2:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 9:
                if counter >= 5:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 10:
                if counter >= 6:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 11:
                if counter >= 16:
                    need_card[1][yaku_num] = -1
            elif yaku_num == 2:
                if 111 in my_recent_getcards:
                    need_card[1][yaku_num] = -1
                else:
                    if counter >= 2:
                        need_card[1][yaku_num] = -1
        

        your_recent_getcards = self.your_getcards[-1]
        your_recent_getcards_possible = self.your_getcards[-1] + self.your_cards[-1]

        for yaku_num in range(len(YAKU_LIST)):
            counter = 0
            counter_possible = 0
            yaku_cards = YAKU_LIST[yaku_num]

            for card in yaku_cards:
                if card in your_recent_getcards:
                    counter += 1
                if card in your_recent_getcards_possible:
                    counter_possible += 1
                    
            your_append_num = max(0, YAKU_LIST_NUM[yaku_num] - counter)
            your_append_num_possible = max(0, YAKU_LIST_NUM[yaku_num] - counter_possible)

            if yaku_num == 2:
                if your_append_num == 0:
                    if 111 not in your_recent_getcards:
                        your_append_num = 1
                if your_append_num_possible == 0:
                    if 111 not in your_recent_getcards_possible:
                        your_append_num_possible = 1

            if need_card[1][yaku_num] != -1:
                need_card[1][yaku_num] = your_append_num
                need_card_possible[1][yaku_num] = your_append_num_possible
            else:
                need_card_possible[1][yaku_num] = -1

            # 相手が絶対に取れない役に-1をつける
            if yaku_num in [0, 1, 4, 5, 6, 7, 8]:  # 相手に1枚でも持たれたら終了
                if counter >= 1:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 3:
                if counter >= 2:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 9:
                if counter >= 5:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 10:
                if counter >= 6:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 11:
                if counter >= 16:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1
            elif yaku_num == 2:
                if 111 in your_recent_getcards:
                    need_card[0][yaku_num] = -1
                    need_card_possible[0][yaku_num] = -1           
                else:
                    if counter >= 2:
                        need_card[0][yaku_num] = -1
                        need_card_possible[0][yaku_num] = -1
        

        self.need_cards.append(need_card)
        self.need_cards_possible.append(need_card_possible)




    
    # case 0: 手札から出すカードを決める
    # case 1: 手札から出した後or山札から引いた後で，月が同じ札が2枚あったとき，その2枚のうちどちらを取るかを決める
    def ChooseCard(self, player, case, draw_card, select_from_field_kouho):
        if player == "Me":
            my_need_card = self.need_cards[-1][0]
            my_need_card_possible = self.need_cards_possible[-1][0]
            your_need_card = self.need_cards[-1][1]
            kouho_cards = self.my_cards[-1]
            # my_point = self.my_score[-1]
            # my_total_point = self.my_total_score[-1]
            # your_point = self.your_score[-1]
            # your_total_point = self.your_total_score[-1]
        elif player == "You":
            my_need_card = self.need_cards[-1][1]
            my_need_card_possible = self.need_cards_possible[-1][1]
            your_need_card = self.need_cards[-1][0]
            kouho_cards = self.your_cards[-1]
            # my_point = self.your_score[-1]
            # my_total_point = self.your_total_score[-1]
            # your_point = self.my_score[-1]
            # your_total_score = self.my_score[-1]
        
        
        if case == 0:
            field_cards = self.field_cards[-1]
            
            kouho_field_mathcing = []
            for i in range(len(kouho_cards)):
                for j in range(len(field_cards)):
                    if (kouho_cards[i] // 10) == (field_cards[j] // 10):
                        kouho_field_mathcing.append((kouho_cards[i], field_cards[j]))
            # print(kouho_field_mathcing)

            kouho_score = []
            kouho_score_possible = []
            kouho_score_teki = []
            if len(kouho_field_mathcing) != 0:
                for i in range(len(kouho_field_mathcing)):
                    score = 0
                    score_possible = 0
                    score_teki = 0
                    for j in range(2):
                        kouho = kouho_field_mathcing[i][j]
                        for key, value in YAKU_DICT.items():
                            tmp_num = YAKU_TMP_NUM[key]
                            if kouho in value:
                                if my_need_card[tmp_num] not in [-1, 0]:
                                    score += YAKU_POINT[key] / my_need_card[tmp_num]
                                if my_need_card_possible[tmp_num] not in [-1, 0]:
                                    score_possible += YAKU_POINT[key] / my_need_card_possible[tmp_num]
                                if j == 1:
                                    if your_need_card[tmp_num] not in [-1, 0]:
                                        score_teki = YAKU_POINT[key] / float(your_need_card[tmp_num])
                    kouho_score.append(score)
                    kouho_score_possible.append(score_possible)
                    kouho_score_teki.append(score_teki)
                new_score = []
                new_new_score = []
                for i in range(len(kouho_score)):
                    new_score.append(kouho_score[i] + kouho_score_possible[i]/5)
                    new_new_score.append(new_score[i] + kouho_score_teki[i])

                # select_card = kouho_field_mathcing[new_score.index(max(new_score))][0]
                select_card = kouho_field_mathcing[new_new_score.index(max(new_new_score))][0]

            else:
                kouho_score = []
                for i in range(len(kouho_cards)):
                    score = 0
                    kouho = kouho_cards[i]
                    for key, value in YAKU_DICT.items():
                        tmp_num = YAKU_TMP_NUM[key]
                        if kouho in value:
                            if your_need_card[tmp_num] not in [-1, 0]:
                                score += YAKU_POINT[key] / your_need_card[tmp_num]
                    kouho_score.append(score)

                select_card = kouho_cards[kouho_score.index(min(kouho_score))]

        
        elif case == 1:
            kouho_cards = []
            for i in range(2):
                kouho_cards.append([draw_card, select_from_field_kouho[i]])
            
            kouho_score = []
            kouho_score_possible = []
            kouho_score_teki = []
            for i in range(len(kouho_cards)):
                score = 0
                score_possible = 0
                score_teki = 0
                for j in range(2):
                    kouho = kouho_cards[i][j]
                    for key, value in YAKU_DICT.items():
                        tmp_num = YAKU_TMP_NUM[key]
                        if kouho in value:
                            if my_need_card[tmp_num] not in [-1, 0]:
                                score += YAKU_POINT[key] / my_need_card[tmp_num]
                            if my_need_card_possible[tmp_num] not in [-1, 0]:
                                score_possible += YAKU_POINT[key] / my_need_card_possible[tmp_num]
                            if j == 1:
                                if your_need_card[tmp_num] not in [-1, 0]:
                                    score_teki += YAKU_POINT[key] / your_need_card[tmp_num]
                kouho_score.append(score)
                kouho_score_possible.append(score_possible)
                kouho_score_teki.append(score_teki)
            new_score = []
            new_new_score = []
            for i in range(len(kouho_score)):
                new_score.append(kouho_score[i] + kouho_score_possible[i]/5)
                new_new_score.append(new_score[i] + kouho_score_teki[i])
            
            # select_card = kouho_cards[new_score.index(max(new_score))][1]
            select_card = kouho_cards[new_new_score.index(max(new_new_score))][1]      

        
        return select_card
        

    
    
    # こいこいするかを判断する．返り値はするならTrue, しないならFalse
    def KoikoiJudge(self, player, month, turn, repetition):
        if player == "Me":
            my_need_card = self.need_cards[-1][0]
            my_need_card_possible = self.need_cards_possible[-1][0]
            your_need_card = self.need_cards[-1][1]
            my_point = self.my_score[-1]
            my_total_point = self.my_total_score[-1]
            your_point = self.your_score[-1]
            your_total_point = self.your_total_score[-1]
        elif player == "You":
            my_need_card = self.need_cards[-1][1]
            my_need_card_possible = self.need_cards_possible[-1][1]
            your_need_card = self.need_cards[-1][0]
            my_point = self.your_score[-1]
            my_total_point = self.your_total_score[-1]
            your_point = self.my_score[-1]
            your_total_point = self.my_total_score[-1]

        
        # モンテカルロ法：繰り返し回数300回
        # 相手の手札情報も使ってしまっている間違ったモンテカルロ法
        # score_list = self.MonteCarlo(player, 300, month, turn, repetition)
        # print(score_list)
        # print("\nMonteCarlo predict: {}, variance: {}, current score: {} (cheat)".format(np.mean(score_list), np.var(score_list), my_point))

        # 正しいモンテカルロ法
        score_list_correct = self.MonteCarlo_correct(player, 100, month, turn, repetition)
        kitaiti_seikai = np.mean(score_list_correct)
        # print(score_list_correct)
        print("MonteCarlo predict: {}, variance: {}, current score: {}\n".format(kitaiti_seikai, np.var(score_list_correct), my_point))
        
        if kitaiti_seikai > my_point:
            judge = True
        else:
            judge = False

        
        if month == 12:
            if my_total_point > your_total_point:
                judge = False
            elif my_total_point < your_total_point:
                judge = True
            else:
                if my_point > your_point:
                    judge = False
                elif my_point < your_point:
                    judge = True
                else:
                    judge = False
            
        return judge
    
    
    
    def neural_network_judge(self, case, tefuda, getcards, enemy_getcards, field_cards):
        if case == 0:
            model = self.model_init
        elif case == 1:
            model = self.model_endofturn3
        elif case == 2:
            model = self.model_endofturn6
        
        input_data = make_learning_list(tefuda, getcards, enemy_getcards, field_cards)
        output_data = model.predict(input_data)
        predict_case = 4 - np.argmax(np.array(output_data))
        
        return predict_case
        





if __name__ == '__main__':
    enemy = EnemyMove()
    # UpdateParam(field, yamafuda, my_cards, my_getcards, your_, your_, my_score, your_, my_total_, your_total_, my_koikoi_, your_)
    enemy.UpdateParam(0, 0, [11], [31], [121], [81], 0, 0, 0, 0, 0, 0)    
    enemy.UpdateParam(0, 0, [11,12], [31,32], [51,52], [81,82], 0, 0, 0, 0, 0, 0)
    enemy.UpdateParam([94,52,82,92,112],[123,44,34,33,24,81,71,83,42,41,32,124,111,22,14,31,84,101,54,91,13,23,63],[121,51,113,114,11,53],[72,74,103,102],[21,93,73,64,43,104,12],[61,62],0,0,4,4,0,0)
    # enemy.UpdateParam([92,83,114,64,32,11],[111,22,14,31,84,101,54,91,13,23,63],[53],[72,74,103,102,121,123,51,52,33,34,113,112,81,82,41,42,124,122],[104,12],[61,62,93,94,43,44,21,24,73,71],1,0,4,4,1,0)
    # enemy.UpdateParam([43,114,83,22,113,33,44,104],[62,111,12,94,122,92,101,42,82,64,123,84,34,11,91,51,71,103,31,61,73,54,81,63],[121,13,14,112,24,21,102,72],[],[93,53,23,41,32,124,52,74],[],0,0,5,4,0,0)
    enemy.UpdateParam([23,54,84,31,74,22,81,124],[],[52,112,33,94,73,21,111,121],[],[102,61,11,41,122,103,42,101],[],0,0,7,33,0,0)

    print(enemy.need_cards[-1])
    print(enemy.need_cards_possible[-1])




# TODO
# ChooseCard　の得点期待値で，
#   7点以上で得点2倍を反映させる
#   赤タン・青タン・猪鹿蝶等の追加ポイントを反映させる
#   相手との総得点差・月で重みを変える