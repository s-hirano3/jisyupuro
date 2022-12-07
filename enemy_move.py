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
TANE = [21, 41, 51, 61, 71, 82, 91, 101, 112]
TAN = [12, 22, 32, 42, 52, 62, 72, 92, 102, 113]
KASU = [13, 14, 23, 24, 33, 34, 43, 44, 53, 54, 63, 64, 73, 74, 83, 84, 91, 93, 94, 103, 104, 114, 122, 123, 124]

# [五光，四光，雨入り四光，三光，花見で一杯，月見で一杯，猪鹿蝶，赤短，青短，タネ，タン，カス]
YAKU_CARDS = [GOKOU, YONKOU, AMESIKOU, SANKOU, HANAMI, TUKIMI, INOSHIKATYO, AKATAN, AOTAN, TANE, TAN, KASU]
YAKU_CARDS_NUM = [5, 4, 4, 3, 2, 2, 3, 3, 3, 5, 5, 10]



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


    
    def DetectNeedCards(self):
        need_card = [[], []]  # my, your
        need_card_possible = [[], []]  # my, your

        for player in range(2):
            if player == 0:
                getcards = self.my_getcards[-1]
                getcards_possible = self.my_getcards[-1] + self.my_cards[-1]
            elif player == 1:
                getcards = self.your_getcards[-1]
                getcards_possible = self.your_getcards[-1] + self.your_cards[-1]

            for yaku_num in range(len(YAKU_CARDS)):
                counter = 0
                counter_possible = 0
                YAKU = YAKU_CARDS[yaku_num]

                for card in YAKU:
                    if card in getcards:
                        counter += 1
                    if card in getcards_possible:
                        counter_possible += 1

                append_num = max(0, YAKU_CARDS_NUM[yaku_num] - counter)
                append_num_possible = max(0, YAKU_CARDS_NUM[yaku_num] - counter_possible)

                # 雨四光のときは，111をイレギュラー処理
                if yaku_num == 2:
                    if append_num == 0:
                        if 111 not in getcards:
                            append_num = 1
                    if append_num_possible == 0:
                        if 111 not in getcards_possible:
                            append_num_possible = 1
                
                # print('player: {}, yaku_num: {}, append_num: {}, append_num_possible: {}'.format(player, yaku_num, append_num, append_num_possible))
                need_card[player].append(append_num)
                need_card_possible[player].append(append_num_possible)

            
        for i in range(len(YAKU_CARDS)):
            me = need_card[0][i]
            you = need_card[1][i]

            # 五光
            if i == 0:
                if me != 5:
                    need_card[1][i] = -1
                if you != 5:
                    need_card[0][i] = -1
            # 四光
            elif i == 1:
                if me != 4:
                    need_card[1][i] = -1
                if you != 4:
                    need_card[0][i] = -1



                
                    

        self.need_cards.append(need_card)
        self.need_cards_possible.append(need_card_possible)








if __name__ == '__main__':
    enemy = EnemyMove()
    # UpdateParam(field, yamafuda, my_cards, my_getcards, your_, your_, my_score, my_total_, your_, your_, my_koikoi_, your_)
    enemy.UpdateParam (0, 0, [11], [31], [51], [81], 0, 0, 0, 0, 0, 0)
    enemy.UpdateParam (0, 0, [11,12], [31,32], [51,52], [81,82], 0, 0, 0, 0, 0, 0)
    enemy.DetectNeedCards()

    print(enemy.need_cards)
    print(enemy.need_cards_possible)