#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import cv2
#from enemy_move import enemy_move
from detect_yaku import detect_yaku
from draw import *


class flower:
    
    def __init__(self):
        self.cards = [11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,
                      71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124]

        self.my_cards = []
        self.my_getcard = []
        self.my_score = 0
        self.my_total_score = 0
        
        self.your_cards = []
        self.your_getcard = []
        self.your_score = 0
        self.your_total_score = 0
        
        self.field_cards = []

        self.yamafuda = []
        
        self.stage = draw_init()
        cv2.imshow("stage", self.stage)
        cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
        

        
    
    
    # 親決めを行う関数
    def oya_decision(self):
        while True:
            random.shuffle(self.cards)
            
            while True:
                key = int(input("Type number from 1 to 48: "))
                if 1 <= key <= 48:
                    my_key = key - 1
                    break
            my_card = self.cards[my_key]
            
            while True:        
                your_key = random.randint(0, 47)
                your_card = self.cards[your_key]
                if your_card != my_card:
                    break
            
            my_month = my_card // 10
            your_month = your_card // 10
            
            self.stage = draw_oya_decision(self.stage, my_card, your_card)
            cv2.imshow("stage", self.stage)
            cv2.waitKey(0)
            #cv2.destroyAllWindows()
            
            if my_month == your_month:
                print("Oya decision: your month is {}, enemy's month is {}".format(my_month, your_month))
                print("Draw. Please retype number.")
            else:
                print("Oya decision: your month is {}, enemy's month is {}".format(my_month, your_month))
                break
        
        
        # 1月目の親がプレイヤーなら0，敵なら1
        if my_month < your_month:
            self.oya = 0  
        elif my_month > your_month:
            self.oya = 1
    
    
    
    
    
    # ゲームの進行を行う関数．何ヶ月でプレイするかを引数として渡す．
    def play(self, num_month, displaymode):
        for month in range(num_month):
            self.my_score = 0
            self.your_score = 0
            self.field_cards = []
            self.my_cards = []
            self.my_getcard = []
            self.your_cards = []
            self.your_getcard = []
            self.yamafuda = []
            random.shuffle(self.cards)

            if ((self.oya == 0) & (month % 2 == 0)) | ((self.oya == 1) & (month % 2 == 1)):  # プレイヤーが親
                print("MONTH {}:  You are oya.".format(month+1))
                for i in range(4):
                    self.my_cards.append(self.cards[0+i*6])
                    self.my_cards.append(self.cards[1+i*6])
                    self.field_cards.append(self.cards[2+i*6])
                    self.field_cards.append(self.cards[3+i*6])
                    self.your_cards.append(self.cards[4+i*6])
                    self.your_cards.append(self.cards[5+i*6])
            elif ((self.oya == 0) & (month % 2 == 1)) | ((self.oya == 1) & (month % 2 == 0)):  # 敵が親
                print("MONTH {}:  You are not oya.".format(month+1))
                for i in range(4):
                    self.your_cards.append(self.cards[0+i*6])
                    self.your_cards.append(self.cards[1+i*6])
                    self.field_cards.append(self.cards[2+i*6])
                    self.field_cards.append(self.cards[3+i*6])
                    self.my_cards.append(self.cards[4+i*6])
                    self.my_cards.append(self.cards[5+i*6])
                    
            self.stage = draw_play_init(self.stage, self.my_cards, self.your_cards, self.field_cards, displaymode)
            cv2.imshow("stage", self.stage)
            cv2.waitKey(0)
            
            self.yamafuda = self.cards[24:]


            # お互いに8枚出したらゲーム終了，次の月に
            for i in range(8):
                if ((self.oya == 0) & (month % 2 == 0)) | ((self.oya == 1) & (month % 2 == 1)):  # プレイヤーが親

                    # 手札から1枚選択するターン
                    print("\n\n\n----- Your turn : select -----\n")
                    print("your_cards: {}".format(self.my_cards))
                    print("field_cards: {}".format(self.field_cards))
                                        
                    while True:
                        select_key = int(input("select card    :"))
                        if select_key in self.my_cards:
                            break
                        else:
                            print("{} is not your cards.".format(select_key))

                    
                    select_month = select_key // 10
                    field_months = []
                    for i in range(len(self.field_cards)):
                        field_months.append(self.field_cards[i] // 10)

                                       
                    # 選んだカードと同じ月のカードが場に何枚あるかで処理を変える
                    # 0枚の場合．選んだカードを場に置く
                    if field_months.count(select_month) == 0:
                        self.my_cards.remove(select_key)
                        self.field_cards.append(select_key)

                    # 1枚の場合．選んだカードと対応する場のカードをmy_getcardに追加
                    elif field_months.count(select_month) == 1:
                        self.my_cards.remove(select_key)
                        
                        tmp_index = field_months.index(select_month)
                        get_card_from_field = self.field_cards[tmp_index]
                        self.field_cards.remove(get_card_from_field)

                        self.my_getcard.append(select_key)
                        self.my_getcard.append(get_card_from_field)

                    # 3枚の場合．全取り
                    elif field_months.count(select_month) == 3:
                        self.my_cards.remove(select_key)

                        get_cards_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month:
                                get_cards_from_field.append(field_card)
                        
                        self.my_getcard.append(select_key)
                        for i in range(3):
                            self.field_cards.remove(get_cards_from_field[i])
                            self.my_getcard.append(get_cards_from_field[i])
                    
                    # 2枚の場合．場のどのカードを取るかを選択させる
                    elif field_months.count(select_month) == 2:
                        self.my_cards.remove(select_key)

                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month:
                                get_kouho_from_field.append(field_card)

                        while True:
                            select_from_kouho = int(input("type 1 card from {}    :".format(get_kouho_from_field)))
                            if select_from_kouho in get_kouho_from_field:
                                break
                            else:
                                print("you cannot select {}".format(select_from_kouho))
                        self.field_cards.remove(select_from_kouho)

                        self.my_getcard.append(select_key)
                        self.my_getcard.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 1")
                    
                    
                    print("Your get cards:  {}".format(self.my_getcard))
                    
                    self.stage = draw_play_tefuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, displaymode)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    
                    
                    # 山札から1枚引くするターン
                    print("\n----- Your turn : draw -----\n")
                    print("Your cards: {}".format(self.my_cards))
                    print("field cards: {}".format(self.field_cards))
                    
                    # yamafudaの先頭を取り出し，削除
                    draw_card = self.yamafuda.pop(0)
                    print("you draw:  {}".format(draw_card))
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card, displaymode, timing=0)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    draw_month = draw_card // 10
                    field_months = []
                    for i in range(len(self.field_cards)):
                        field_months.append(self.field_cards[i] // 10)

                                       
                    # 山札から引いたカードと同じ月のカードが場に何枚あるかで処理を変える
                    # 0枚の場合．引いたカードを場に置いて終了
                    if field_months.count(draw_month) == 0:
                        self.field_cards.append(draw_card)

                    # 1枚の場合．山札から引いたカードと対応する場のカードをmy_getcardに追加
                    elif field_months.count(draw_month) == 1:
                        tmp_index = field_months.index(draw_month)
                        get_card_from_field = self.field_cards[tmp_index]
                        self.field_cards.remove(get_card_from_field)

                        self.my_getcard.append(draw_card)
                        self.my_getcard.append(get_card_from_field)

                    # 3枚の場合．全取り
                    elif field_months.count(draw_month) == 3:
                        get_cards_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month:
                                get_cards_from_field.append(field_card)
                        
                        self.my_getcard.append(draw_card)
                        for i in range(3):
                            self.field_cards.remove(get_cards_from_field[i])
                            self.my_getcard.append(get_cards_from_field[i])
                    
                    # 2枚の場合．場のどのカードを取るかを選択させる
                    elif field_months.count(draw_month) == 2:
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month:
                                get_kouho_from_field.append(field_card)

                        while True:
                            select_from_kouho = int(input("type 1 card from {}    :".format(get_kouho_from_field)))
                            if select_from_kouho in get_kouho_from_field:
                                break
                            else:
                                print("you cannot select {}".format(select_from_kouho))
                        self.field_cards.remove(select_from_kouho)

                        self.my_getcard.append(draw_card)
                        self.my_getcard.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 2")
                    
                    
                    print("Your get cards:  {}".format(self.my_getcard))
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card, displaymode, timing=1)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destoryAllWindows()
                    
                    
                    
                    
                    # 獲得したカードをdetect_yakuに渡す．こいこい判定のため，前ターンの得点も渡す（初めて役がそろったときにこいこいするかを聞く）
                    # 役が含まれるかの判定と，こいこいするかのinputはdetect_yakuで行う．
                    # 返り値はリスト[[五光，四光，雨入り四光，三光，花見で一杯，月見で一杯，[猪鹿蝶，タネ枚数]，[赤短，タン枚数]，[青短，タン枚数]，[タネ，タネ枚数]，[タン，タン枚数]，[カス，カス枚数]], こいこい]
                    # その役が成立していれば1，していなければ0が入る．
                    # こいこいステータス:    0:こいこい前    1:こいこい後    2:こいこいしない or こいこい後役が揃う
                    self.my_yaku, self.my_score = detect_yaku(self.my_getcard, self.my_score, 0)
                    
                    print("your score: {}".format(self.my_score))
                    
                    
                    # こいこいステータス == 2 なら次の月へ
                    if self.my_yaku[1] == 2:
                        self.my_total_score += self.my_score
                        print("\n\nend of month {}.".format(month+1))
                        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
                        print("---------------------------------------\n\n")
                        
                        cv2.imshow("stage", self.stage)
                        cv2.waitKey(0)
                        #cv2.destroyAllWindows()
                        break
                    
                    
                    
                    
                    
                    # 敵のターン
                    print("\n---- Enemy's turn : select -----\n")
                    print("enemy's card: {}".format(self.your_cards))
                    print("field cards: {}".format(self.field_cards))
                    your_cards_month = []
                    for your_card in self.your_cards:
                        your_cards_month.append(your_card // 10)
                    field_months = []
                    for field_month in self.field_cards:
                        field_months.append(field_month // 10)
                    
                    # 場のカードと月が一致するカードを手札の先頭から選択
                    # ない場合は手札の先頭を出す
                    select_card_enemy = 0
                    for i in range(len(self.your_cards)):
                        if your_cards_month[i] in field_months:
                            select_card_enemy = self.your_cards[i]
                    if select_card_enemy == 0:
                        select_card_enemy = self.your_cards[0]
                        
                    select_month_enemy = select_card_enemy // 10
                    print("enemy select:  {}".format(select_card_enemy))
                    
                                      
                    # 選んだカードと同じ月のカードの枚数で処理を変える
                    # 0枚の場合
                    if field_months.count(select_month_enemy) == 0:
                        self.your_cards.remove(select_card_enemy)
                        self.field_cards.append(select_card_enemy)
                    
                    # 1枚の場合
                    elif field_months.count(select_month_enemy) == 1:
                        self.your_cards.remove(select_card_enemy)
                        
                        tmp_index = field_months.index(select_month_enemy)
                        get_card_from_field = self.field_cards[tmp_index]
                        self.field_cards.remove(get_card_from_field)
                        
                        self.your_getcard.append(select_card_enemy)
                        self.your_getcard.append(get_card_from_field)
                    
                    # 3枚の場合
                    elif field_months.count(select_month_enemy) == 3:
                        self.your_cards.remove(select_card_enemy)
                        
                        get_cards_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month_enemy:
                                get_cards_from_field.append(field_card)
                        
                        self.your_getcard.append(select_card_enemy)
                        for i in range(3):
                            self.field_cards.remove(get_cards_from_field[i])
                            self.your_getcard.append(get_cards_from_field[i])
                    
                    # 2枚の場合
                    elif field_months.count(select_month_enemy) == 2:
                        self.your_cards.remove(select_card_enemy)
                        
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month_enemy:
                                get_kouho_from_field.append(field_card)
                        
                        select_from_kouho = get_kouho_from_field[0]
                        
                        self.field_cards.remove(select_from_kouho)
                        
                        self.your_getcard.append(select_card_enemy)
                        self.your_getcard.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 3")
                    
                    print("Enemy's get cards:  {}".format(self.your_getcard))
                    
                    self.stage = draw_play_tefuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, displaymode)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    
                    
                    
                    # 山札から1枚引くするターン
                    print("\n---- Enemy's turn : draw -----\n")
                    print("Enemy's card: {}".format(self.your_cards))
                    print("field cards: {}".format(self.field_cards))
                    
                    # yamafudaの先頭を取り出し，削除
                    draw_card_enemy = self.yamafuda.pop(0)
                    print("enemy draw:  {}".format(draw_card_enemy))
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card_enemy, displaymode, timing=0)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()

                    draw_month_enemy = draw_card_enemy // 10
                    field_months = []
                    for i in range(len(self.field_cards)):
                        field_months.append(self.field_cards[i] // 10)

                                       
                    # 山札から引いたカードと同じ月のカードが場に何枚あるかで処理を変える
                    # 0枚の場合．引いたカードを場に置いて終了
                    if field_months.count(draw_month_enemy) == 0:
                        self.field_cards.append(draw_card_enemy)

                    # 1枚の場合．山札から引いたカードと対応する場のカードをmy_getcardに追加
                    elif field_months.count(draw_month_enemy) == 1:
                        tmp_index = field_months.index(draw_month_enemy)
                        get_card_from_field = self.field_cards[tmp_index]
                        self.field_cards.remove(get_card_from_field)

                        self.your_getcard.append(draw_card_enemy)
                        self.your_getcard.append(get_card_from_field)

                    # 3枚の場合．全取り
                    elif field_months.count(draw_month_enemy) == 3:
                        get_cards_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month_enemy:
                                get_cards_from_field.append(field_card)
                        
                        self.your_getcard.append(draw_card_enemy)
                        for i in range(3):
                            self.field_cards.remove(get_cards_from_field[i])
                            self.your_getcard.append(get_cards_from_field[i])
                    
                    # 2枚の場合．場のどのカードを取るかを選択させる
                    elif field_months.count(draw_month_enemy) == 2:
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month_enemy:
                                get_kouho_from_field.append(field_card)

                        select_from_kouho = get_kouho_from_field[0]
                        self.field_cards.remove(select_from_kouho)

                        self.your_getcard.append(draw_card_enemy)
                        self.your_getcard.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 2")
                    
                    
                    print("Enemy's get cards:  {}".format(self.your_getcard))
                    
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card_enemy, displaymode, timing=1)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    
                    self.your_yaku, self.your_score = detect_yaku(self.your_getcard, self.your_score, 1)
                    
                    print("Enemy's score: {}".format(self.your_score))
                    
                    # こいこいステータス == 2 なら次の月へ
                    if self.your_yaku[1] == 2:
                        self.your_total_score += self.your_score
                        print("\n\nend of month {}.".format(month+1))
                        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
                        print("---------------------------------------\n\n")
                        
                        cv2.imshow("stage", self.stage)
                        cv2.waitKey(0)
                        #cv2.destroyAllWindows()
                        break
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                elif ((self.oya == 0) & (month % 2 == 1)) | ((self.oya == 1) & (month % 2 == 0)):  # 敵が親
                    # 敵のターン
                    print("\n---- Enemy's turn : select -----\n")
                    print("enemy's card: {}".format(self.your_cards))
                    print("field cards: {}".format(self.field_cards))
                    your_cards_month = []
                    for your_card in self.your_cards:
                        your_cards_month.append(your_card // 10)
                    field_months = []
                    for field_month in self.field_cards:
                        field_months.append(field_month // 10)
                    
                    # 場のカードと月が一致するカードを手札の先頭から選択
                    # ない場合は手札の先頭を出す
                    select_card_enemy = 0
                    for i in range(len(self.your_cards)):
                        if your_cards_month[i] in field_months:
                            select_card_enemy = self.your_cards[i]
                    if select_card_enemy == 0:
                        select_card_enemy = self.your_cards[0]
                        
                    select_month_enemy = select_card_enemy // 10
                    print("enemy select:  {}".format(select_card_enemy))
                    
                                      
                    # 選んだカードと同じ月のカードの枚数で処理を変える
                    # 0枚の場合
                    if field_months.count(select_month_enemy) == 0:
                        self.your_cards.remove(select_card_enemy)
                        self.field_cards.append(select_card_enemy)
                    
                    # 1枚の場合
                    elif field_months.count(select_month_enemy) == 1:
                        self.your_cards.remove(select_card_enemy)
                        
                        tmp_index = field_months.index(select_month_enemy)
                        get_card_from_field = self.field_cards[tmp_index]
                        self.field_cards.remove(get_card_from_field)
                        
                        self.your_getcard.append(select_card_enemy)
                        self.your_getcard.append(get_card_from_field)
                    
                    # 3枚の場合
                    elif field_months.count(select_month_enemy) == 3:
                        self.your_cards.remove(select_card_enemy)
                        
                        get_cards_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month_enemy:
                                get_cards_from_field.append(field_card)
                        
                        self.your_getcard.append(select_card_enemy)
                        for i in range(3):
                            self.field_cards.remove(get_cards_from_field[i])
                            self.your_getcard.append(get_cards_from_field[i])
                    
                    # 2枚の場合
                    elif field_months.count(select_month_enemy) == 2:
                        self.your_cards.remove(select_card_enemy)
                        
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month_enemy:
                                get_kouho_from_field.append(field_card)
                        
                        select_from_kouho = get_kouho_from_field[0]
                        
                        self.field_cards.remove(select_from_kouho)
                        
                        self.your_getcard.append(select_card_enemy)
                        self.your_getcard.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 5")
                    
                    print("Enemy's get cards:  {}".format(self.your_getcard))
                    
                    self.stage = draw_play_tefuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, displaymode)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    
                    
                    
                    # 山札から1枚引くするターン
                    print("\n---- Enemy's turn : draw -----\n")
                    print("Enemy's card: {}".format(self.your_cards))
                    print("field cards: {}".format(self.field_cards))
                    
                    # yamafudaの先頭を取り出し，削除
                    draw_card_enemy = self.yamafuda.pop(0)
                    print("enemy draw:  {}".format(draw_card_enemy))
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card_enemy, displaymode, timing=0)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()

                    draw_month_enemy = draw_card_enemy // 10
                    field_months = []
                    for i in range(len(self.field_cards)):
                        field_months.append(self.field_cards[i] // 10)

                                       
                    # 山札から引いたカードと同じ月のカードが場に何枚あるかで処理を変える
                    # 0枚の場合．引いたカードを場に置いて終了
                    if field_months.count(draw_month_enemy) == 0:
                        self.field_cards.append(draw_card_enemy)

                    # 1枚の場合．山札から引いたカードと対応する場のカードをmy_getcardに追加
                    elif field_months.count(draw_month_enemy) == 1:
                        tmp_index = field_months.index(draw_month_enemy)
                        get_card_from_field = self.field_cards[tmp_index]
                        self.field_cards.remove(get_card_from_field)

                        self.your_getcard.append(draw_card_enemy)
                        self.your_getcard.append(get_card_from_field)

                    # 3枚の場合．全取り
                    elif field_months.count(draw_month_enemy) == 3:
                        get_cards_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month_enemy:
                                get_cards_from_field.append(field_card)
                        
                        self.your_getcard.append(draw_card_enemy)
                        for i in range(3):
                            self.field_cards.remove(get_cards_from_field[i])
                            self.your_getcard.append(get_cards_from_field[i])
                    
                    # 2枚の場合．場のどのカードを取るかを選択させる
                    elif field_months.count(draw_month_enemy) == 2:
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month_enemy:
                                get_kouho_from_field.append(field_card)

                        select_from_kouho = get_kouho_from_field[0]
                        self.field_cards.remove(select_from_kouho)

                        self.your_getcard.append(draw_card_enemy)
                        self.your_getcard.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 6")
                    
                    
                    print("Enemy's get cards:  {}".format(self.your_getcard))
                    
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card_enemy, displaymode, timing=1)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    
                    self.your_yaku, self.your_score = detect_yaku(self.your_getcard, self.your_score, 1)
                    
                    print("Enemy's score: {}".format(self.your_score))
                    
                    # こいこいステータス == 2 なら次の月へ
                    if self.your_yaku[1] == 2:
                        self.your_total_score += self.your_score
                        print("\n\nend of month {}.".format(month+1))
                        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
                        print("---------------------------------------\n\n")
                        
                        cv2.imshow("stage", self.stage)
                        cv2.waitKey(0)
                        #cv2.destroyAllWindows()
                        break







                    # 手札から1枚選択するターン
                    print("\n\n\n----- Your turn : select -----\n")
                    print("your_cards: {}".format(self.my_cards))
                    print("field_cards: {}".format(self.field_cards))
                                        
                    while True:
                        select_key = int(input("select card    :"))
                        if select_key in self.my_cards:
                            break
                        else:
                            print("{} is not your cards.".format(select_key))

                    
                    select_month = select_key // 10
                    field_months = []
                    for i in range(len(self.field_cards)):
                        field_months.append(self.field_cards[i] // 10)

                                       
                    # 選んだカードと同じ月のカードが場に何枚あるかで処理を変える
                    # 0枚の場合．選んだカードを場に置く
                    if field_months.count(select_month) == 0:
                        self.my_cards.remove(select_key)
                        self.field_cards.append(select_key)

                    # 1枚の場合．選んだカードと対応する場のカードをmy_getcardに追加
                    elif field_months.count(select_month) == 1:
                        self.my_cards.remove(select_key)
                        
                        tmp_index = field_months.index(select_month)
                        get_card_from_field = self.field_cards[tmp_index]
                        self.field_cards.remove(get_card_from_field)

                        self.my_getcard.append(select_key)
                        self.my_getcard.append(get_card_from_field)

                    # 3枚の場合．全取り
                    elif field_months.count(select_month) == 3:
                        self.my_cards.remove(select_key)

                        get_cards_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month:
                                get_cards_from_field.append(field_card)
                        
                        self.my_getcard.append(select_key)
                        for i in range(3):
                            self.field_cards.remove(get_cards_from_field[i])
                            self.my_getcard.append(get_cards_from_field[i])
                    
                    # 2枚の場合．場のどのカードを取るかを選択させる
                    elif field_months.count(select_month) == 2:
                        self.my_cards.remove(select_key)

                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month:
                                get_kouho_from_field.append(field_card)

                        while True:
                            select_from_kouho = int(input("type 1 card from {}    :".format(get_kouho_from_field)))
                            if select_from_kouho in get_kouho_from_field:
                                break
                            else:
                                print("you cannot select {}".format(select_from_kouho))
                        self.field_cards.remove(select_from_kouho)

                        self.my_getcard.append(select_key)
                        self.my_getcard.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 7")
                    
                    
                    print("Your get cards:  {}".format(self.my_getcard))
                    
                    self.stage = draw_play_tefuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, displaymode)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    
                    
                    # 山札から1枚引くするターン
                    print("\n----- Your turn : draw -----\n")
                    print("Your cards: {}".format(self.my_cards))
                    print("field cards: {}".format(self.field_cards))
                    
                    # yamafudaの先頭を取り出し，削除
                    draw_card = self.yamafuda.pop(0)
                    print("you draw:  {}".format(draw_card))
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card, displaymode, timing=0)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    draw_month = draw_card // 10
                    field_months = []
                    for i in range(len(self.field_cards)):
                        field_months.append(self.field_cards[i] // 10)

                                       
                    # 山札から引いたカードと同じ月のカードが場に何枚あるかで処理を変える
                    # 0枚の場合．引いたカードを場に置いて終了
                    if field_months.count(draw_month) == 0:
                        self.field_cards.append(draw_card)

                    # 1枚の場合．山札から引いたカードと対応する場のカードをmy_getcardに追加
                    elif field_months.count(draw_month) == 1:
                        tmp_index = field_months.index(draw_month)
                        get_card_from_field = self.field_cards[tmp_index]
                        self.field_cards.remove(get_card_from_field)

                        self.my_getcard.append(draw_card)
                        self.my_getcard.append(get_card_from_field)

                    # 3枚の場合．全取り
                    elif field_months.count(draw_month) == 3:
                        get_cards_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month:
                                get_cards_from_field.append(field_card)
                        
                        self.my_getcard.append(draw_card)
                        for i in range(3):
                            self.field_cards.remove(get_cards_from_field[i])
                            self.my_getcard.append(get_cards_from_field[i])
                    
                    # 2枚の場合．場のどのカードを取るかを選択させる
                    elif field_months.count(draw_month) == 2:
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month:
                                get_kouho_from_field.append(field_card)

                        while True:
                            select_from_kouho = int(input("type 1 card from {}    :".format(get_kouho_from_field)))
                            if select_from_kouho in get_kouho_from_field:
                                break
                            else:
                                print("you cannot select {}".format(select_from_kouho))
                        self.field_cards.remove(select_from_kouho)

                        self.my_getcard.append(draw_card)
                        self.my_getcard.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 8")
                    
                    
                    print("Your get cards:  {}".format(self.my_getcard))
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card, displaymode, timing=1)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destoryAllWindows()
                    
                    
                    
                    
                    # 獲得したカードをdetect_yakuに渡す．こいこい判定のため，前ターンの得点も渡す（初めて役がそろったときにこいこいするかを聞く）
                    # 役が含まれるかの判定と，こいこいするかのinputはdetect_yakuで行う．
                    # 返り値はリスト[[五光，四光，雨入り四光，三光，花見で一杯，月見で一杯，[猪鹿蝶，タネ枚数]，[赤短，タン枚数]，[青短，タン枚数]，[タネ，タネ枚数]，[タン，タン枚数]，[カス，カス枚数]], こいこい]
                    # その役が成立していれば1，していなければ0が入る．
                    # こいこいステータス:    0:こいこい前，1:こいこい後→月継続    2:こいこいしない or こいこい後役が揃う→月終了
                    self.my_yaku, self.my_score = detect_yaku(self.my_getcard, self.my_score, 0)
                    
                    print("your score: {}".format(self.my_score))
                    
                    # こいこいステータス == 2 なら次の月へ
                    if self.my_yaku[1] == 2:
                        self.my_total_score += self.my_score
                        print("\n\nend of month {}.".format(month+1))
                        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
                        print("---------------------------------------\n\n")
                        
                        cv2.imshow("stage", self.stage)
                        cv2.waitKey(0)
                        #cv2.destroyAllWindows()
                        break



            
            
            else:
                print("\n\nend of month {}".format(month+1))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                
                cv2.imshow("stage", self.stage)
                cv2.waitKey(0)
                #cv2.destroyAllWindows()
            continue
        
        
        print("\n\nend of game")
        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
        if self.my_total_score > self.your_total_score:
            print("You win!!!")
        elif self.my_total_score < self.your_total_score:
            print("Enemy win!!!")
        else:
            print("Draw...")


        
if __name__ == '__main__':
    hanafuda = flower()
    hanafuda.oya_decision()
    hanafuda.play(2, 0)  # 何ヶ月でプレイするかを渡す．第2引数はdisplay_modeで，0なら相手の手札を見せない，1なら見せる
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()