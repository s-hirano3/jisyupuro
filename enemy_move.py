#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
                if 111 in my_recent_getcards:
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
    def ChooseCard(self, player, case):
        if player == "Me":
            my_need_card = self.need_cards[-1][0]
            my_need_card_possible = self.need_cards_possible[-1][0]
            your_need_card = self.need_cards[-1][1]
        elif player == "You":
            my_need_card = self.need_cards[-1][1]
            my_need_card_possible = self.need_cards_possible[-1][1]
            your_need_card = self.need_cards[-1][0]
            my_card = self.your_cards[-1]
        
        if case == 0:
            if player == "Me":
                kouho_cards = self.my_cards[-1]
            elif player == "You":
                kouho_cards = self.your_cards[-1]
            field_cards = self.field_cards[-1]


            
        elif case == 1:
            aiueo
        







if __name__ == '__main__':
    enemy = EnemyMove()
    # UpdateParam(field, yamafuda, my_cards, my_getcards, your_, your_, my_score, your_, my_total_, your_total_, my_koikoi_, your_)
    enemy.UpdateParam (0, 0, [11], [31], [121], [81], 0, 0, 0, 0, 0, 0)    
    enemy.UpdateParam (0, 0, [11,12], [31,32], [51,52], [81,82], 0, 0, 0, 0, 0, 0)
    

    print(enemy.need_cards)
    print(enemy.need_cards_possible)