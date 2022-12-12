#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import datetime
import gc
from detect_yaku import *
from write_log import *
from enemy_move import *


class Hanafuda():

    def __init__(self):
        self.ResetParam()

        self.my_total_score = 0
        self.your_total_score = 0
        self.score_record = []        


    def ResetParam(self):
        self.cards = [11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,
                      71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124]
        
        self.my_cards = []
        self.my_getcard = []
        self.my_score = 0
        self.my_koikoi_flag = 0

        self.your_cards = []
        self.your_getcard = []
        self.your_score = 0
        self.your_koikoi_flag = 0

        self.field_cards = []
        self.yamafuda = []

        self.end_flag = False
        self.winner = "HIKIWAKE"

        self.EnemyAlgorithm = EnemyMove()


    
    def EndMonthProcess(self):
        self.f.write('------------------\n')

        self.f.write('end of month {}\n'.format(self.month))
        self.f.write('winner : {}\n'.format(self.winner))
        self.f.write('my_score: {}, your_score: {}\n'.format(self.my_score, self.your_score))
        
        if self.winner == "Me":
            self.my_total_score += self.my_score
        elif self.winner == "You":
            self.your_total_score += self.your_score
        self.f.write('my_total_score: {}, your_total_score: {}\n'.format(self.my_total_score, self.your_total_score))

        self.f.write('------------------\n\n')

        self.score_record.append((self.my_total_score, self.your_total_score))

    

    def EndGameProcess(self):
        if self.my_total_score > self.your_total_score:
            winner = "Me"
        elif self.my_total_score < self.your_total_score:
            winner = "You"
        elif self.my_total_score == self.your_total_score:
            winner = "HIKIWAKE"

        self.f.write('\n\n------------------\n')

        self.f.write('end of game\n')
        self.f.write('winner : {}\n'.format(winner))
        self.f.write('my_total_score: {}, your_total_score: {}\n'.format(self.my_total_score, self.your_total_score))
        
        self.f.write('------------------\n\n')

        for i in range(len(self.score_record)):
            self.f.write('{} {} {}\n'.format(i, self.score_record[i][0], self.score_record[i][1]))






    def ShiteKuttukiJudge(self):
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

        my_site_flag = False
        your_site_flag = False
        my_kuttuki = []
        your_kuttuki = []
        for value in my_cards_month_dict.values():
            if value == 4:
                my_site_flag = True
            if value == 2:
                my_kuttuki.append(1)
            else:
                my_kuttuki.append(0)
        for value in your_cards_month_dict.values():
            if value == 4:
                your_site_flag = True
            if value == 2:
                your_kuttuki.append(1)
            else:
                your_kuttuki.append(0)
        
        my_kuttuki_flag = True
        your_kuttuki_flag = True
        for i in range(len(my_kuttuki)):
            if my_kuttuki[i] == 0:
                my_kuttuki_flag = False
                break
        for i in range(len(your_kuttuki)):
            if your_kuttuki[i] == 0:
                your_kuttuki_flag = False
                break
        
        # 四手・くっつきが同時に起こった場合
        if my_site_flag & your_kuttuki_flag:
            self.f.write('------------------\n')
            self.f.write('You are SHITE and enemy is KUTTUKI\n')
            self.f.write('------------------\n')
            self.end_flag = True
        elif my_kuttuki_flag & your_site_flag:
            self.f.write('------------------\n')
            self.f.write('You are KUTTUKI and enemy is SHITE\n')
            self.f.write('------------------\n')
            self.end_flag = True
        
        # 四手のみ
        if my_site_flag & your_site_flag:
            self.f.write('------------------\n')
            self.f.write('You are SHITE and enemy is SHITE\n')
            self.f.write('------------------\n')
            self.end_flag = True
        elif my_site_flag & ~your_site_flag:
            self.f.write('------------------\n')
            self.f.write('You are SHITE\n')
            self.f.write('------------------\n')
            self.my_score = 6
            self.winner = "Me"
            self.end_flag = True
        elif ~my_site_flag & your_site_flag:
            self.f.write('------------------\n')
            self.f.write('Enemy is SHITE\n')
            self.f.write('------------------\n')
            self.your_score = 6
            self.winner = "You"
            self.end_flag = True

        # くっつきのみ
        if my_kuttuki_flag & your_kuttuki_flag:
            self.f.write('------------------\n')
            self.f.write('You are KUTTUKI and enemy is KUTTUKI\n')
            self.f.write('------------------\n')
            self.end_flag = True
        elif my_kuttuki_flag & ~your_kuttuki_flag:
            self.f.write('------------------\n')
            self.f.write('You are KUTTUKI\n')
            self.f.write('------------------\n')
            self.my_score = 6
            self.winner = "Me"
            self.end_flag = True
        elif ~my_kuttuki_flag & your_kuttuki_flag:
            self.f.write('------------------\n')
            self.f.write('Enemy is KUTTUKI\n')
            self.f.write('------------------\n')
            self.your_score = 6
            self.winner = "You"
            self.end_flag = True





    def FieldMatchingProcess(self, card, player):
        card_month = card // 10

        field_month = []
        for i in range(len(self.field_cards)):
            field_month.append(self.field_cards[i] // 10)
        

        # 選んだカードと同じ月のカードが場に何枚あるかで場合分け
        # 0枚
        if field_month.count(card_month) == 0:
            self.field_cards.append(card)
        
        # 1枚
        elif field_month.count(card_month) == 1:
            tmp_index = field_month.index(card_month)
            get_card_from_field = self.field_cards[tmp_index]
            
            self.field_cards.remove(get_card_from_field)
            if player == "Me":
                self.my_getcard.append(card)
                self.my_getcard.append(get_card_from_field)
            elif player == "You":
                self.your_getcard.append(card)
                self.your_getcard.append(get_card_from_field)
        
        # 3枚
        elif field_month.count(card_month) == 3:
            get_cards_from_field = []
            for field_card in self.field_cards:
                if field_card // 10 == card_month:
                    get_cards_from_field.append(field_card)
            
            for i in range(3):
                self.field_cards.remove(get_cards_from_field[i])
                if player == "Me":
                    self.my_getcard.append(card)
                    self.my_getcard.append(get_cards_from_field[i])
                elif player == "You":
                    self.your_getcard.append(card)
                    self.your_getcard.append(get_cards_from_field[i])
        
        # 2枚
        elif field_month.count(card_month) == 2:
            get_kouho_from_field = []
            for field_card in self.field_cards:
                if field_card // 10 == card_month:
                    get_kouho_from_field.append(field_card)
            
            select_from_kouho = get_kouho_from_field[0]
            self.field_cards.remove(select_from_kouho)
            if player == "Me":
                self.my_getcard.append(card)
                self.my_getcard.append(select_from_kouho)
            elif player == "You":
                self.your_getcard.append(card)
                self.your_getcard.append(select_from_kouho)





    def Tefuda(self, player):
        if player == "Me":
            my_cards_month = []
            for my_card in self.my_cards:
                my_cards_month.append(my_card // 10)
            field_cards_month = []
            for field_card in self.field_cards:
                field_cards_month.append(field_card // 10)
            
            select_card = 0
            for i in range(len(self.my_cards)):
                if my_cards_month[i] in field_cards_month:
                    select_card = self.my_cards[i]
                    break
                select_card = self.my_cards[0]
            
            self.my_cards.remove(select_card)

        elif player == "You":
            your_cards_month = []
            for your_card in self.your_cards:
                your_cards_month.append(your_card // 10)
            field_cards_month = []
            for field_card in self.field_cards:
                field_cards_month.append(field_card // 10)
            
            select_card = 0
            for i in range(len(self.your_cards)):
                if your_cards_month[i] in field_cards_month:
                    select_card = self.your_cards[i]
                    break
                select_card = self.your_cards[0]
            
            self.your_cards.remove(select_card)
        
        self.FieldMatchingProcess(select_card, player)
    
        

    def Draw(self, player):
        draw_card = self.yamafuda.pop(0)
        self.FieldMatchingProcess(draw_card, player)

    
    def Score(self, player):
        if player == "Me":
            tmp_score = self.my_score
            self.my_yaku, self.my_score = detect_yaku(self.my_getcard)
            if self.my_score > tmp_score:
                if self.my_koikoi_flag == 1:
                    self.my_koikoi_flag = 2
                    self.winner = "Me"
                    self.end_flag = True
                elif self.my_koikoi_flag == 0:
                    if self.your_koikoi_flag == 1:
                        self.my_koikoi_flag = 2
                        self.my_score *= 2
                        self.winner = "Me"
                        self.end_flag = True
                    elif self.your_koikoi_flag == 0:
                        self.my_koikoi_flag = 1
                        self.f.write('------------------\n')
                        self.f.write('DO KOIKOI\n')
                        self.f.write('my_koikoi_flag: {}, your_koikoi_flag: {}, my_score: {}, your_score: {}\n'.format(self.my_koikoi_flag, self.your_koikoi_flag, self.my_score, self.your_score))
                        self.f.write('------------------\n')
        
        elif player == "You":
            tmp_score = self.your_score
            self.your_yaku, self.your_score = detect_yaku(self.your_getcard)
            if self.your_score > tmp_score:
                if self.your_koikoi_flag == 1:
                    self.your_koikoi_flag = 2
                    self.winner = "You"
                    self.end_flag = True
                elif self.your_koikoi_flag == 0:
                    if self.my_koikoi_flag == 1:
                        self.your_koikoi_flag = 2
                        self.your_score *= 2
                        self.winner = "You"
                        self.end_flag = True
                    elif self.my_koikoi_flag == 0:
                        self.your_koikoi_flag = 1
                        self.f.write('------------------\n')
                        self.f.write('DO KOIKOI\n')
                        self.f.write('my_koikoi_flag: {}, your_koikoi_flag: {}, my_score: {}, your_score: {}\n'.format(self.my_koikoi_flag, self.your_koikoi_flag, self.my_score, self.your_score))
                        self.f.write('------------------\n')




    def Play(self, repetition):

        dt_now = datetime.datetime.now()
        file_name = './log_computer/log-computer-' + str(repetition) + '.txt'
        self.f = open(file_name, 'w')
        self.f.write(dt_now.strftime('%Y-%m-%d %H:%M:%S.%f') + '\n\n')
        self.f.write("")  ############ TODO log

        
        for self.month in range(1, 13):
            self.ResetParam()

            for i in range(random.randint(1,10)):
                random.shuffle(self.cards)

            if (repetition * self.month) % 2 == 1:
                for i in range(4):
                    self.my_cards.append(self.cards[0+i*6])
                    self.my_cards.append(self.cards[1+i*6])
                    self.field_cards.append(self.cards[2+i*6])
                    self.field_cards.append(self.cards[3+i*6])
                    self.your_cards.append(self.cards[4+i*6])
                    self.your_cards.append(self.cards[5+i*6])
            elif (repetition * self.month) % 2 == 0:
                for i in range(4):
                    self.your_cards.append(self.cards[0+i*6])
                    self.your_cards.append(self.cards[1+i*6])
                    self.field_cards.append(self.cards[2+i*6])
                    self.field_cards.append(self.cards[3+i*6])
                    self.my_cards.append(self.cards[4+i*6])
                    self.my_cards.append(self.cards[5+i*6])
            self.yamafuda = self.cards[24:]

            self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)

            self.f.write('------------------\n')
            self.f.write('initial condition\n')
            self.f = write_log_init(self.f, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
            self.f.write('------------------\n')

            # 四手・くっつき判定
            self.ShiteKuttukiJudge()
            if self.end_flag:
                self.EndMonthProcess()
                continue
            

            # 最大で8回手札を出したら終了
            for i in range(8):
                if (repetition * self.month) % 2 == 1:
                    self.Tefuda("Me")
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.f.write('my turn : Tefuda\n')
                    self.f = write_log(self.f, self.month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')

                    self.Draw("Me")
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.f.write('my turn : Draw\n')
                    self.f = write_log(self.f, self.month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.Score("Me")
                    if self.end_flag:
                        self.EndMonthProcess()
                        break

                    self.Tefuda("You")
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.f.write('your turn : Tefuda\n')
                    self.f = write_log(self.f, self.month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')

                    self.Draw("You")
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.f.write('your turn : Draw\n')
                    self.f = write_log(self.f, self.month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.Score("You")
                    if self.end_flag:
                        self.EndMonthProcess()
                        break

                elif (repetition * self.month) % 2 == 0:
                    self.Tefuda("You")
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.f.write('your turn : Tefuda\n')
                    self.f = write_log(self.f, self.month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')

                    self.Draw("You")
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.f.write('your turn : Draw\n')
                    self.f = write_log(self.f, self.month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.Score("You")
                    if self.end_flag:
                        self.EndMonthProcess()
                        break

                    self.Tefuda("Me")
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.f.write('my turn : Tefuda\n')
                    self.f = write_log(self.f, self.month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')

                    self.Draw("Me")
                    self.EnemyAlgorithm.UpdateParam(self.field_cards, self.yamafuda, self.my_cards, self.my_getcard, self.your_cards, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.f.write('my turn : Draw\n')
                    self.f = write_log(self.f, self.month, i, self.field_cards, self.yamafuda, self.my_cards, self.your_cards, self.my_getcard, self.your_getcard, self.my_score, self.your_score, self.my_total_score, self.your_total_score, self.my_koikoi_flag, self.your_koikoi_flag)
                    self.f.write('------------------\n')
                    self.Score("Me")
                    if self.end_flag:
                        self.EndMonthProcess()
                        break

            # どちらも役ができない or こいこいしたが役ができない 場合
            else:
                if self.my_koikoi_flag == 1:
                    self.winner = "Me"
                elif self.your_koikoi_flag == 1:
                    self.winner = "You"
                self.EndMonthProcess()

        # end of game        
        self.EndGameProcess()
            




if __name__ == '__main__':
    start = 1
    repeat = int(input("Type num of games to play : "))

    for i in range(start,start+repeat):
        print("{} : {}".format(i, datetime.datetime.now().strftime('%Y%m%d-%H%M%S.%f')))
        hanafuda = Hanafuda()
        hanafuda.Play(i)

        # del hanafuda
        # gc.collect()