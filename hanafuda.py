#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import datetime
import cv2
from enemy_move import *
from detect_yaku import *
from draw import *
from write_log import *


class Hanafuda():
    
    def __init__(self):
        self.cards = [11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,
                      71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124]

        self.my_cards = []
        self.my_getcard = []
        self.my_score = 0
        self.my_total_score = 0
        self.my_koikoi_flag = 0
        
        self.your_cards = []
        self.your_getcard = []
        self.your_score = 0
        self.your_total_score = 0
        self.your_koikoi_flag = 0
        
        self.field_cards = []

        self.yamafuda = []
        
        self.stage = draw_init()
        cv2.imshow("stage", self.stage)
        cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
        
    
        
    
    
    # 親決めを行う関数
    def oya_decision(self):
        print("\nOya decision")
        while True:
            for i in range(random.randint(1,10)):
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
        
        
        # logファイル設定
        dt_now = datetime.datetime.now()
        file_name = './log/' + dt_now.strftime('%Y%m%d-%H%M%S') + '_' + str(num_month) + '_' + str(displaymode) + '.txt'
        f = open(file_name, 'w')
        f.write(dt_now.strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
        f.write('oya mode(0:player is oya of odd month, 1:player is oya of even month)\n' + str(self.oya) + '\n\n')
        

         
        for month in range(1,num_month+1):
            self.my_score = 0
            self.your_score = 0
            self.field_cards = []
            self.my_cards = []
            self.my_getcard = []
            self.your_cards = []
            self.your_getcard = []
            self.my_koikoi_flag = 0
            self.your_koikoi_flag = 0
            self.yamafuda = []

            self.EnemyAlgorithm = EnemyMove()

            for i in range(random.randint(1,10)):
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

            self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)

            f.write('--------------------\n')
            f.write('initial condition\n')
            f = write_log_init(f, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
            f.write('--------------------\n\n')
            
            
            # 四手・くっつき判定用変数作成
            my_cards_month_dict = {}
            your_cards_month_dict = {}
            for i in range(8):
                my_card_month = self.my_cards[i] // 10
                if my_card_month not in my_cards_month_dict.keys():
                    my_cards_month_dict[my_card_month] = 1
                else:
                    my_cards_month_dict[my_card_month] += 1
                
                your_card_month = self.your_cards[i] // 10
                if your_card_month not in your_cards_month_dict.keys():
                    your_cards_month_dict[your_card_month] = 1
                else:
                    your_cards_month_dict[your_card_month] += 1
            my_site = 0
            your_site = 0
            my_kuttuki = []
            your_kuttuki = []
            for value in my_cards_month_dict.values():
                if value == 4:
                    my_site = 1
                if value == 2:
                    my_kuttuki.append(1)
                else:
                    my_kuttuki.append(0)
            for value in your_cards_month_dict.values():
                if value == 4:
                    your_site = 1
                if value == 2:
                    your_kuttuki.append(1)
                else:
                    your_kuttuki.append(0)
            my_kuttuki_flag = 1
            your_kuttuki_flag = 1
            for i in range(len(my_kuttuki)):
                if my_kuttuki[i] == 0:
                    my_kuttuki_flag = 0
                    break
            for i in range(len(your_kuttuki)):
                if your_kuttuki[i] == 0:
                    your_kuttuki_flag = 0
                    break
            #print(my_site, your_site, my_kuttuki_flag, your_kuttuki_flag)
            
            # 四手・くっつきダブル
            if (my_site == 1) & (your_kuttuki_flag == 1):
                print("\nYou are SITE and enemy is KUTTUKI")
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                continue
            elif (my_kuttuki_flag == 1) & (your_site == 1):
                print("\nYou are KUTTUKI and enemy is SITE")
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                continue
            
            # 四手判定
            if (my_site == 1) & (your_site == 1):
                print("\nYou and enemy are SITE")
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                continue
            elif (my_site == 1) & (your_site == 0):
                print("\nYou are SITE")
                self.my_score = 6
                self.my_total_score += self.my_score
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                continue
            elif (my_site == 0) & (your_site == 1):
                print("\nEnemy is SITE")
                self.your_score = 6
                self.your_total_score += self.your_score
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                continue
            
            # くっつき判定
            if (my_kuttuki_flag == 1) & (your_kuttuki_flag == 1):
                print("\nYou and enemy are KUTTUKI")
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                continue                
            elif (my_kuttuki_flag == 1) & (your_kuttuki_flag == 0):
                print("\nYou are KUTTUKI")
                self.my_score = 6
                self.my_total_score += self.my_score
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                continue                
            elif (my_kuttuki_flag == 0) & (your_kuttuki_flag == 1):
                print("\nEnemy is KUTTUKI")
                self.your_score = 6
                self.your_total_score += self.your_score
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                continue                
                
                
            


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
                    
                    flush_card_list = []
                    flush_card_list.append(select_key)

                                       
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
                        
                        flush_card_list.append(get_card_from_field)

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
                            
                            flush_card_list.append(get_cards_from_field[i])
                    
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
                        
                        flush_card_list.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 1")
                    
                    
                    print("Your get cards:  {}".format(self.my_getcard))

                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    
                    self.stage = draw_play_tefuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, displaymode)
                    self.stage = flush(self.stage, flush_card_list)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    f.write('--------------------\n')
                    f.write('your turn : select\n')
                    f = write_log(f, month, i,  self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    f.write('--------------------\n\n')
                    
                    
                    
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
                        
                    flush_card_list = []
                    flush_card_list.append(draw_card)

                                       
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
                        
                        flush_card_list.append(get_card_from_field)

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
                            
                            flush_card_list.append(get_cards_from_field[i])
                    
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
                        
                        flush_card_list.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 2")
                    
                    
                    print("Your get cards:  {}".format(self.my_getcard))

                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card, displaymode, timing=1)
                    self.stage = flush(self.stage, flush_card_list)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destoryAllWindows()
                    
                    
                    
                    
                    # 獲得したカードをdetect_yakuに渡す．こいこい判定のため，前ターンの得点も渡す（初めて役がそろったときにこいこいするかを聞く）
                    # 役が含まれるかの判定と，こいこいするかのinputはdetect_yakuで行う．
                    # 返り値はリスト[五光，四光，雨入り四光，三光，花見で一杯，月見で一杯，[猪鹿蝶，タネ枚数]，[赤短，タン枚数]，[青短，タン枚数]，[タネ，タネ枚数]，[タン，タン枚数]，[カス，カス枚数]]
                    # その役が成立していれば1，していなければ0が入る．
                    # こいこいステータス:    0:こいこい前    1:こいこい後    2:こいこいしない or こいこい後役が揃う
                    tmp_score = self.my_score
                    self.my_yaku, self.my_score = detect_yaku(self.my_getcard)
                    print("your score: {}".format(self.my_score))
                    print("koikoi status : you {}, enemy {}".format(self.my_koikoi_flag, self.your_koikoi_flag))
                    
                    if self.my_score > tmp_score:
                        if self.your_koikoi_flag == 0:
                            self.my_koikoi_flag = koikoi(self.my_koikoi_flag, 0)
                        elif self.your_koikoi_flag == 1:
                            self.my_koikoi_flag = 2
                            self.my_score = self.my_score * 2                    
                            
                    f.write('--------------------\n')
                    f.write('your turn : draw\n')
                    f = write_log(f, month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    f.write('--------------------\n\n')
                    
                    
                    # こいこいステータス == 2 なら次の月へ
                    if self.my_koikoi_flag == 2:
                        self.my_total_score += self.my_score
                        print("\n\nend of month {}.".format(month+1))
                        print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
                        print("---------------------------------------\n\n")
                        
                        f.write('--------------------\n')
                        f.write('result of month\n')
                        f = write_result_month(f, month, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                        f.write('--------------------\n\n\n\n')
                        
                        cv2.imshow("stage", self.stage)
                        cv2.waitKey(0)
                        #cv2.destroyAllWindows()
                        break
                    
                    
                    
                    
                    
                    # 敵のターン
                    print("\n---- Enemy's turn : select -----\n")
                    print("enemy's card: {}".format(self.your_cards))
                    print("field cards: {}".format(self.field_cards))
                    
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    select_card_enemy = self.EnemyAlgorithm.ChooseCard("You", 0, 0, 0)


                    # your_cards_month = []
                    # for your_card in self.your_cards:
                    #     your_cards_month.append(your_card // 10)
                    field_months = []
                    for field_month in self.field_cards:
                        field_months.append(field_month // 10)
                    
                    # # 場のカードと月が一致するカードを手札の先頭から選択
                    # # ない場合は手札の先頭を出す
                    # select_card_enemy = 0
                    # for i in range(len(self.your_cards)):
                    #     if your_cards_month[i] in field_months:
                    #         select_card_enemy = self.your_cards[i]
                    # if select_card_enemy == 0:
                    #     select_card_enemy = self.your_cards[0]
                        
                    select_month_enemy = select_card_enemy // 10
                    print("enemy select:  {}".format(select_card_enemy))
                    
                    flush_card_list = []
                    flush_card_list.append(select_card_enemy)
                    
                                      
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
                        
                        flush_card_list.append(get_card_from_field)
                    
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
                            
                            flush_card_list.append(get_cards_from_field[i])
                    
                    # 2枚の場合
                    elif field_months.count(select_month_enemy) == 2:
                        self.your_cards.remove(select_card_enemy)
                        
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month_enemy:
                                get_kouho_from_field.append(field_card)
                        
                        # select_from_kouho = get_kouho_from_field[0]
                        select_from_kouho = self.EnemyAlgorithm.ChooseCard("You", 1, select_card_enemy, get_kouho_from_field)
                        
                        self.field_cards.remove(select_from_kouho)
                        
                        self.your_getcard.append(select_card_enemy)
                        self.your_getcard.append(select_from_kouho)
                        
                        flush_card_list.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 3")
                    
                    print("Enemy's get cards:  {}".format(self.your_getcard))
                    
                    self.stage = draw_play_tefuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, displaymode)
                    self.stage = flush(self.stage, flush_card_list)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    f.write('--------------------\n')
                    f.write('enemy turn : select\n')
                    f = write_log(f, month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    f.write('--------------------\n\n')
                    
                    
                    
                    
                    # 山札から1枚引くするターン
                    print("\n---- Enemy's turn : draw -----\n")
                    print("Enemy's card: {}".format(self.your_cards))
                    print("field cards: {}".format(self.field_cards))
                    
                    # yamafudaの先頭を取り出し，削除
                    draw_card_enemy = self.yamafuda.pop(0)
                    print("enemy draw:  {}".format(draw_card_enemy))

                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card_enemy, displaymode, timing=0)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()

                    draw_month_enemy = draw_card_enemy // 10
                    field_months = []
                    for i in range(len(self.field_cards)):
                        field_months.append(self.field_cards[i] // 10)
                        
                    flush_card_list = []
                    flush_card_list.append(draw_card_enemy)

                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)

                                       
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
                        
                        flush_card_list.append(get_card_from_field)

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
                            
                            flush_card_list.append(get_cards_from_field[i])
                    
                    # 2枚の場合．場のどのカードを取るかを選択させる
                    elif field_months.count(draw_month_enemy) == 2:
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month_enemy:
                                get_kouho_from_field.append(field_card)

                        # select_from_kouho = get_kouho_from_field[0]
                        select_from_kouho = self.EnemyAlgorithm.ChooseCard("You", 1, draw_card_enemy, get_kouho_from_field)
                        self.field_cards.remove(select_from_kouho)

                        self.your_getcard.append(draw_card_enemy)
                        self.your_getcard.append(select_from_kouho)
                        
                        flush_card_list.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 2")
                    
                    
                    print("Enemy's get cards:  {}".format(self.your_getcard))
                    
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card_enemy, displaymode, timing=1)
                    self.stage = flush(self.stage, flush_card_list)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    tmp_score = self.your_score
                    self.your_yaku, self.your_score = detect_yaku(self.your_getcard)                    
                    print("Enemy's score: {}".format(self.your_score))
                    print("koikoi status : you {}, enemy {}".format(self.my_koikoi_flag, self.your_koikoi_flag))
                    
                    f.write('--------------------\n')
                    f.write('enemy turn : draw\n')
                    f = write_log(f, month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    f.write('--------------------\n\n')
                    
                    if self.your_score > tmp_score:
                        if self.my_koikoi_flag == 0:
                            self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                            koikoi_judge = self.EnemyAlgorithm.KoikoiJudge("You", month, i, 1)
                            if koikoi_judge:
                                self.your_koikoi_flag = 1
                            else:
                                self.your_koikoi_flag = 2
                            # self.your_koikoi_flag = koikoi(self.your_koikoi_flag, 1)
                        elif self.my_koikoi_flag == 1:
                            self.your_koikoi_flag = 2
                            self.your_score = self.your_score * 2
                                        
                    # こいこいステータス == 2 なら次の月へ
                    if self.your_koikoi_flag == 2:
                        self.your_total_score += self.your_score
                        print("\n\nend of month {}.".format(month+1))
                        print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
                        print("---------------------------------------\n\n")
                        
                        f.write('--------------------\n')
                        f.write('result of month\n')
                        f = write_result_month(f, month, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                        f.write('--------------------\n\n\n\n')
                        
                        cv2.imshow("stage", self.stage)
                        cv2.waitKey(0)
                        #cv2.destroyAllWindows()
                        break
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                elif ((self.oya == 0) & (month % 2 == 1)) | ((self.oya == 1) & (month % 2 == 0)):  # 敵が親
                    # 敵のターン
                    print("\n\n\n---- Enemy's turn : select -----\n")
                    print("enemy's card: {}".format(self.your_cards))
                    print("field cards: {}".format(self.field_cards))
                    
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    select_card_enemy = self.EnemyAlgorithm.ChooseCard("You", 0, 0, 0)

                    # your_cards_month = []
                    # for your_card in self.your_cards:
                    #     your_cards_month.append(your_card // 10)
                    field_months = []
                    for field_month in self.field_cards:
                        field_months.append(field_month // 10)
                    
                    # # 場のカードと月が一致するカードを手札の先頭から選択
                    # # ない場合は手札の先頭を出す
                    # select_card_enemy = 0
                    # for i in range(len(self.your_cards)):
                    #     if your_cards_month[i] in field_months:
                    #         select_card_enemy = self.your_cards[i]
                    # if select_card_enemy == 0:
                    #     select_card_enemy = self.your_cards[0]
                        
                    select_month_enemy = select_card_enemy // 10
                    print("enemy select:  {}".format(select_card_enemy))
                    
                    flush_card_list = []
                    flush_card_list.append(select_card_enemy)
                    
                                      
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
                        
                        flush_card_list.append(get_card_from_field)
                    
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
                            
                            flush_card_list.append(get_cards_from_field[i])
                    
                    # 2枚の場合
                    elif field_months.count(select_month_enemy) == 2:
                        self.your_cards.remove(select_card_enemy)
                        
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == select_month_enemy:
                                get_kouho_from_field.append(field_card)
                        
                        # select_from_kouho = get_kouho_from_field[0]
                        select_from_kouho = self.EnemyAlgorithm.ChooseCard("You", 1, select_card_enemy, get_kouho_from_field)
                        
                        self.field_cards.remove(select_from_kouho)
                        
                        self.your_getcard.append(select_card_enemy)
                        self.your_getcard.append(select_from_kouho)
                        
                        flush_card_list.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 5")
                    
                    print("Enemy's get cards:  {}".format(self.your_getcard))
                    
                    self.stage = draw_play_tefuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, displaymode)
                    self.stage = flush(self.stage, flush_card_list)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    f.write('--------------------\n')
                    f.write('enemy turn : select\n')
                    f = write_log(f, month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    f.write('--------------------\n\n')
                    
                    
                    
                    # 山札から1枚引くするターン
                    print("\n---- Enemy's turn : draw -----\n")
                    print("Enemy's card: {}".format(self.your_cards))
                    print("field cards: {}".format(self.field_cards))
                    

                    # yamafudaの先頭を取り出し，削除
                    draw_card_enemy = self.yamafuda.pop(0)
                    print("enemy draw:  {}".format(draw_card_enemy))

                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    
                    flush_card_list = []
                    flush_card_list.append(draw_card_enemy)
                    
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
                        
                        flush_card_list.append(get_card_from_field)

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
                            
                            flush_card_list.append(get_cards_from_field[i])
                    
                    # 2枚の場合．場のどのカードを取るかを選択させる
                    elif field_months.count(draw_month_enemy) == 2:
                        get_kouho_from_field = []
                        for field_card in self.field_cards:
                            if field_card // 10 == draw_month_enemy:
                                get_kouho_from_field.append(field_card)

                        # select_from_kouho = get_kouho_from_field[0]
                        select_from_kouho = self.EnemyAlgorithm.ChooseCard("You", 1, draw_card_enemy, get_kouho_from_field)
                        self.field_cards.remove(select_from_kouho)

                        self.your_getcard.append(draw_card_enemy)
                        self.your_getcard.append(select_from_kouho)
                        
                        flush_card_list.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 6")
                    
                    
                    print("Enemy's get cards:  {}".format(self.your_getcard))
                    
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card_enemy, displaymode, timing=1)
                    self.stage = flush(self.stage, flush_card_list)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    tmp_score = self.your_score
                    self.your_yaku, self.your_score = detect_yaku(self.your_getcard)
                    print("Enemy's score: {}".format(self.your_score))
                    print("koikoi status : you {}, enemy {}".format(self.my_koikoi_flag, self.your_koikoi_flag))
                    
                    f.write('--------------------\n')
                    f.write('enemy turn : select\n')
                    f = write_log(f, month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    f.write('--------------------\n\n')
                    
                    if self.your_score > tmp_score:
                        if self.my_koikoi_flag == 0:
                            self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                            koikoi_judge = self.EnemyAlgorithm.KoikoiJudge("You", month, i, 2)
                            if koikoi_judge:
                                self.your_koikoi_flag = 1
                            else:
                                self.your_koikoi_flag = 2
                            # self.your_koikoi_flag = koikoi(self.your_koikoi_flag, 1)
                        elif self.my_koikoi_flag == 1:
                            self.your_koikoi_flag = 2
                            self.your_score = self.your_score * 2
                                        
                    # こいこいステータス == 2 なら次の月へ
                    if self.your_koikoi_flag == 2:
                        self.your_total_score += self.your_score
                        print("\n\nend of month {}.".format(month+1))
                        print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
                        print("---------------------------------------\n\n")
                        
                        f.write('--------------------\n')
                        f.write('result of month\n')
                        f = write_result_month(f, month, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                        f.write('--------------------\n\n\n\n')
                        
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
                        
                    flush_card_list = []
                    flush_card_list.append(select_key)
                                       
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
                        
                        flush_card_list.append(get_card_from_field)

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
                            
                            flush_card_list.append(get_cards_from_field[i])
                    
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
                        
                        flush_card_list.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 7")
                    
                    
                    print("Your get cards:  {}".format(self.my_getcard))
                    
                    self.stage = draw_play_tefuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, displaymode)
                    self.stage = flush(self.stage, flush_card_list)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destroyAllWindows()
                    
                    f.write('--------------------\n')
                    f.write('your turn : select\n')
                    f = write_log(f, month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    f.write('--------------------\n\n')
                    
                    
                    
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
                        
                    flush_card_list = []
                    flush_card_list.append(draw_card)
                                       
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
                        
                        flush_card_list.append(get_card_from_field)

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
                            
                            flush_card_list.append(get_cards_from_field[i])
                    
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
                        
                        flush_card_list.append(select_from_kouho)
                    
                    # その他の場合
                    else:
                        print("ERROR 8")
                    
                    
                    print("Your get cards:  {}".format(self.my_getcard))
                    
                    # 描画
                    self.stage = draw_play_yamafuda(self.stage, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.field_cards, draw_card, displaymode, timing=1)
                    self.stage = flush(self.stage, flush_card_list)
                    cv2.imshow("stage", self.stage)
                    cv2.waitKey(0)
                    #cv2.destoryAllWindows()
                    
                    
                    
                    
                    # 獲得したカードをdetect_yakuに渡す．こいこい判定のため，前ターンの得点も渡す（初めて役がそろったときにこいこいするかを聞く）
                    # 役が含まれるかの判定と，こいこいするかのinputはdetect_yakuで行う．
                    # 返り値はリスト[[五光，四光，雨入り四光，三光，花見で一杯，月見で一杯，[猪鹿蝶，タネ枚数]，[赤短，タン枚数]，[青短，タン枚数]，[タネ，タネ枚数]，[タン，タン枚数]，[カス，カス枚数]], こいこい]
                    # その役が成立していれば1，していなければ0が入る．
                    # こいこいステータス:    0:こいこい前，1:こいこい後→月継続    2:こいこいしない or こいこい後役が揃う→月終了
                    tmp_score = self.my_score
                    self.my_yaku, self.my_score = detect_yaku(self.my_getcard)
                    print("your score: {}".format(self.my_score))
                    print("koikoi status : you {}, enemy {}".format(self.my_koikoi_flag, self.your_koikoi_flag))
                    
                    f.write('--------------------\n')
                    f.write('your turn : draw\n')
                    f = write_log(f, month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    f.write('--------------------\n\n')
                    
                    if self.my_score > tmp_score:
                        if self.your_koikoi_flag == 0:
                            self.my_koikoi_flag = koikoi(self.my_koikoi_flag, 0)
                        elif self.your_koikoi_flag == 1:
                            self.my_koikoi_flag = 2
                            self.my_score = self.my_score * 2
                    
                    # こいこいステータス == 2 なら次の月へ
                    if self.my_koikoi_flag == 2:
                        self.my_total_score += self.my_score
                        print("\n\nend of month {}.".format(month+1))
                        print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
                        print("---------------------------------------\n\n")
                        
                        f.write('--------------------\n')
                        f.write('result of month\n')
                        f = write_result_month(f, month, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                        f.write('--------------------\n\n\n\n')
                        
                        cv2.imshow("stage", self.stage)
                        cv2.waitKey(0)
                        #cv2.destroyAllWindows()
                        break



            
            # 「こいこいしない」という選択で月が終わらなかった場合
            else:
                if self.my_koikoi_flag == 1:
                    self.my_total_score += self.my_score
                elif self.your_koikoi_flag == 1:
                    self.your_total_score += self.your_score
                
                print("\n\nend of month {}".format(month+1))
                print("\nYour score is {}, enemy's score is {}".format(self.my_score, self.your_score))
                print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))  
                print("---------------------------------------\n\n")
                
                f.write('--------------------\n')
                f.write('result of month\n')
                f = write_result_month(f, month, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                f.write('--------------------\n\n\n\n')
                
                cv2.imshow("stage", self.stage)
                cv2.waitKey(0)
                #cv2.destroyAllWindows()
            continue
        
        
        
        print("\n\nend of game")
        print("Your total score is {}, enemy's total score is {}".format(self.my_total_score, self.your_total_score))
        f.write('\n\n--------------------\n')
        f.write('result of game\n')
        
        if self.my_total_score > self.your_total_score:
            print("You Win!!!")
            f.write('You Win\n')
        elif self.my_total_score < self.your_total_score:
            print("Enemy Win!!!")
            f.write('Enemy Win\n')
        else:
            print("Draw...")
            f.write('Draw')
            
        f = write_result_game(f, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
        f.write('--------------------\n\n')        
    
        f.close()


        
if __name__ == '__main__':
    month = int(input("Type play month:  "))
    displaymode = int(input("Type displaymode 0:not disp, 1:disp :  "))
    
    hanafuda = Hanafuda()
    hanafuda.oya_decision()
    hanafuda.play(month, displaymode)  # 何ヶ月でプレイするかを渡す．第2引数はdisplay_modeで，0なら相手の手札を見せない，1なら見せる
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# TODO
# DONE 別関数化したこいこい関数を使ったより正確なこいこい処理
# DONE 手四・くっつき処理を追加

# log出力機能を追加
# DONE 手札から出したカードを強調したい
