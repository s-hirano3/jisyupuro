#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

cards = [11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,
         71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124]
card_image_dict = {}
card_image_dict_reverse = {}
for i in range(len(cards)):
    file_name = "hanafuda_image/" + str(cards[i]) + ".png"
    # card = cv2.resize(cv2.imread(file_name), dsize=(292,468))
    card = cv2.resize(cv2.imread(file_name), dsize=(58,92))
    card = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
    card_image_dict[cards[i]] = card
    card_reverse = cv2.rotate(card, rotateCode=cv2.ROTATE_180)
    card_image_dict_reverse[cards[i]] = card_reverse



def transform_cutting(img, points):
    points = sorted(points, key=lambda x:x[1])
    top = sorted(points[:2], key=lambda x:x[0])
    bottom = sorted(points[2:], key=lambda x:x[0], reverse=True)
    points = np.array(top + bottom, dtype='float32')
    
    width = max(np.sqrt(((points[0][0]-points[2][0])**2)*2), np.sqrt(((points[1][0]-points[3][0])**2)*2))
    height = max(np.sqrt(((points[0][1]-points[2][1])**2)*2), np.sqrt(((points[1][1]-points[3][1])**2)*2))

    dst = np.array([
        np.array([0, 0]),
        np.array([width-1, 0]),
        np.array([width-1, height-1]),
        np.array([0, height-1]),
        ], np.float32)
        
    trans = cv2.getPerspectiveTransform(points, dst)
    return cv2.warpPerspective(img, trans, (int(width), int(height)))




# capture = cv2.VideoCapture(0)  # Ubuntuで動かす場合
capture = cv2.VideoCapture(1)  # MacでiPhoneをつないで，iPhoneを外付けカメラとして使う場合

cv2.namedWindow("Capture")

while True:
    ret, frame_original = capture.read()
    frame = frame_original.copy()
    
    # frame_canny = cv2.Canny(frame, 300, 700)
    frame_canny = cv2.Canny(frame, 50, 200)
    contours, hierarchy = cv2.findContours(frame_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        areas = []
        area_roi = []
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            
            if area > 6000:
                epsilon = 0.1 * cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, epsilon, True)
                approx = np.squeeze(approx)
                if approx.shape[0] == 4:
                    areas.append(approx)
                                
        for i in range(len(areas)):
            coords = areas[i]
            card  = transform_cutting(frame, coords)
            card_resize = cv2.resize(card, dsize=(58,92))
            card_resize = cv2.cvtColor(card_resize, cv2.COLOR_BGR2GRAY)
            
            min_xor = 255
            min_key = 0
            for key, card_sample in card_image_dict_reverse.items():
                bitwise_xor = cv2.bitwise_xor(card_resize, card_sample)
                if np.mean(bitwise_xor) < min_xor:
                    min_xor = np.mean(bitwise_xor)
                    min_key = key
            for key, card_sample in card_image_dict.items():
                bitwise_xor = cv2.bitwise_xor(card_resize, card_sample)
                if np.mean(bitwise_xor) < min_xor:
                    min_xor = np.mean(bitwise_xor)
                    min_key = key
            center = np.mean(coords, axis=0).astype(np.uint16)
            cv2.putText(frame, str(min_key), (center[0],center[1]), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=3.0, color=(0,255,255), thickness=20, lineType=cv2.LINE_4)
        
        cv2.drawContours(frame, areas, -1, (0,0,255), 3)

    
    cv2.imshow("Canny", frame_canny)
    cv2.moveWindow("Canny", 700, 10)
    
    cv2.imshow("Capture", frame)
    
    c = cv2.waitKey(2)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()


# TODO
# スレッドを分けて処理を高速化したい
# DONE 上下反転もチェックするように
# 左右からも