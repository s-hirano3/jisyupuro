#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import random
from time import sleep
from falling_process import fall_check

RED    = (0, 0, 250)
YELLOW = (0, 255, 255)
GREEN  = (0, 255, 0)
BLUE   = (255, 0, 0)
PURPLE = (255, 0, 255)
COLOR_DICT = {1: RED, 2: YELLOW, 3:GREEN, 4:BLUE, 5: PURPLE}  # randrangeで発生させた0-5とCOLORを対応させる

BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)



class ball6:
    def __init__(self):
        self.stage = np.full((800, 500, 3), (255, 255, 255), dtype=np.uint8)  # ステージ全体
        cv2.rectangle(self.stage, (90, 421), (410, 750), color=BLACK)  # パズルエリアの長方形を描画
      
        self.ball = [[RED,YELLOW,0,0,0,0,0,0,0,0],[BLUE,0,0,0,0,0,0,0,0],  # ボールの配置を格納した変数．各値にはボールのカラー，空の場合は0
                     [RED,YELLOW,0,0,0,0,0,0,0,0],[BLUE,0,0,0,0,0,0,0,0],  # パズルエリア下から上に0~11行
                     [RED,YELLOW,0,0,0,0,0,0,0,0],[BLUE,0,0,0,0,0,0,0,0],  # 偶数行は左から右に10個
                     [RED,YELLOW,0,0,0,0,0,0,0,0],[BLUE,0,0,0,0,0,0,0,0],  # 奇数行は左から右に9個
                     [RED,YELLOW,0,0,0,0,0,0,0,0],[BLUE,0,0,0,0,0,0,0,0],
                     [RED,YELLOW,0,0,0,0,0,0,0,0],[BLUE,0,0,PURPLE,0,0,0,0,BLUE]]

        self.next_next_ball = [0, 0, 0]  # 画面左上に表示される，次のツモを作成
        for i in range(3):
            COLOR_NUM = random.randrange(1, 6)
            self.next_next_ball[i] = COLOR_DICT[COLOR_NUM]
        cv2.circle(self.stage, (74, 173), 16, self.next_next_ball[0], thickness=-1)
        cv2.circle(self.stage, (58, 200), 16, self.next_next_ball[1], thickness=-1)
        cv2.circle(self.stage, (90, 200), 16, self.next_next_ball[2], thickness=-1)
        cv2.rectangle(self.stage, (38, 150), (110, 220), BLACK)
        cv2.imshow("test", self.stage)
        cv2.waitKey(2000)


        
    def draw_ball(self):
        for tate in range(12):
            if tate % 2 == 0:
                for yoko in range(10):
                    if self.ball[tate][yoko] != 0:
                        cv2.circle(self.stage, (106+yoko*32, 734-tate*27), 16, self.ball[tate][yoko], thickness=-1)
            if tate % 2 == 1:
                for yoko in range(9):
                    if self.ball[tate][yoko] != 0:
                        cv2.circle(self.stage, (122+yoko*32, 734-tate*27), 16, self.ball[tate][yoko], thickness=-1)
        cv2.imshow("test", self.stage)

        

    def new_ball(self):  # 新しいツモ生成を行う関数．すでにあるnext_next_ballをnext_ballに代入し，next_next_ballを更新
        self.next_ball = self.next_next_ball
        cv2.circle(self.stage, (250, 378), 16, self.next_ball[0], thickness=-1)
        cv2.circle(self.stage, (234, 405), 16, self.next_ball[1], thickness=-1)
        cv2.circle(self.stage, (266, 405), 16, self.next_ball[2], thickness=-1)

        # 落下処理のため，操作ツモの色と座標を合わせた変数を導入
        self.now_ball = [[self.next_ball[0], self.next_ball[1], self.next_ball[2]], [(250, 378), (234, 405), (266, 405)]]
        print(self.now_ball)
        
        for i in range(3):
            COLOR_NUM = random.randrange(1, 6)
            self.next_next_ball[i] = COLOR_DICT[COLOR_NUM]
        cv2.circle(self.stage, (74, 173), 16, self.next_next_ball[0], thickness=-1)
        cv2.circle(self.stage, (58, 200), 16, self.next_next_ball[1], thickness=-1)
        cv2.circle(self.stage, (90, 200), 16, self.next_next_ball[2], thickness=-1)
        cv2.imshow("test", self.stage)
        
        cv2.waitKey(2000)


    def fall_checking(self):
        fall_flag = fall_check(self.ball, self.now_ball)
        print(fall_flag)
        return fall_flag


        
        
        
    def falling(self, move):
        print(move)

        
        for i in range(3):
            cv2.circle(self.stage, self.now_ball[1][i], 16, WHITE, thickness=-1)
            cv2.rectangle(self.stage, (90, 421), (410, 750), color=BLACK)  # パズルエリアの長方形を描画
            

        if move == 'rotate-left':
            color1 = self.now_ball[1][0]
            color2 = self.now_ball[1][1]
            color3 = self.now_ball[1][2]
            self.now_ball[1] = [color]
            
        elif move == 'rotate-right':
            aiueo = 0
        
        elif move == 'left':    
            for i in range(3):
                new_center_x = self.now_ball[1][i][0] - 16
                self.now_ball[1][i] = (new_center_x, self.now_ball[1][i][1])
                cv2.circle(self.stage, self.now_ball[1][i], 16, self.now_ball[0][i], thickness=-1)

        elif move == 'right':
            for i in range(3):
                new_center_x = self.now_ball[1][i][0] + 16
                self.now_ball[1][i] = (new_center_x, self.now_ball[1][i][1])
                cv2.circle(self.stage, self.now_ball[1][i], 16, self.now_ball[0][i], thickness=-1)
        
        elif move == 'down':
            if self.now_ball[1][0][1] == 378:
                dy = 32
            else:
                dy = 27
            for i in range(3):
                new_center_y = self.now_ball[1][i][1] + dy
                self.now_ball[1][i] = (self.now_ball[1][i][0], new_center_y)
                cv2.circle(self.stage, self.now_ball[1][i], 16, self.now_ball[0][i], thickness=-1)
        
        cv2.imshow("test", self.stage)
        


    


        
if __name__=='__main__':
    six_ball = ball6()
    six_ball.draw_ball()
    six_ball.new_ball()
    
    while True:
        
        key = cv2.waitKey(100)

        fall_flag = six_ball.fall_checking()
        
        if key == ord('a'):
            move_direction = 'rotate-left'
            six_ball.falling(move_direction)
        elif key == ord('s'):
            move_direction = 'rotate-right'
            six_ball.falling(move_direction)
        elif key == ord('j'):
            move_direction = 'left'
            six_ball.falling(move_direction)
        elif key == ord('l'):
            move_direction = 'right'
            six_ball.falling(move_direction)
        elif key == ord('i'):
            move_direction = 'up'
            six_ball.falling(move_direction)
        elif key == ord('k'):
            move_direction = 'down'
            six_ball.falling(move_direction)
        elif key == ord('q'):
            print('break')
            break

        # ボールの再描画
        six_ball.draw_ball()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
