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

YAKU_DICT = {"GOKOU":GOKOU, "YONKOU":YONKOU, "AMESIKOU":[11,31,81,111,121], "SANKOU":SANKOU, "HANAMI":HANAMI, "TUKIMI":TUKIMI, 
             "INOSHIKATYO":INOSHIKATYO, "AKATAN":AKATAN, "AOTAN":AOTAN, "TANE":TANE, "TAN":TAN, "KASU":KASU}
YAKU_POINT = {"GOKOU":10, "YONKOU":8, "AMESIKOU":7, "SANKOU":5, "HANAMI":5, "TUKIMI":5, "INOSHIKATYO":5, "AKATAN":5, "AOTAN":5, "TANE":1, "TAN":1, "KASU":1}

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
            if len(kouho_field_mathcing) != 0:
                for i in range(len(kouho_field_mathcing)):
                    score = 0
                    score_possible = 0
                    for j in range(2):
                        tmp_num = 0
                        kouho = kouho_field_mathcing[i][j]
                        for key, value in YAKU_DICT.items():
                            if kouho in value:
                                if my_need_card[tmp_num] not in [-1, 0]:
                                    if my_need_card[tmp_num] != 1:
                                        score += YAKU_POINT[key] / my_need_card[tmp_num]
                                    elif my_need_card[tmp_num] == 1:
                                        score += YAKU_POINT[key]
                                if my_need_card_possible[tmp_num] not in [-1, 0]:
                                    if my_need_card_possible[tmp_num] != 1:
                                        score_possible += YAKU_POINT[key] / my_need_card_possible[tmp_num]
                                    elif my_need_card_possible[tmp_num] == 1:
                                        score_possible += YAKU_POINT[key]
                            tmp_num += 1
                    kouho_score.append(score)
                    kouho_score_possible.append(score_possible)
                new_score = []
                for i in range(len(kouho_score)):
                    new_score.append(kouho_score[i]+kouho_score_possible[i]/5)
                select_index = new_score.index(max(new_score))
                select_card = kouho_field_mathcing[select_index][0]

                # print(kouho_score)
                # print(kouho_score_possible)
                # print(new_score)

            else:
                aiueo
                select_card = kouho_cards[0]


            

            
        


                        
        
        
        
        
        
        
        return select_card
        







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