i = 0
COORDS_FIELD = [(10,454,68,546)]
while True:
    next_x0 = COORDS_FIELD[i][2] + 20
    if next_x0 + 58 > 1500:
        break
    next_coords = (next_x0, 454, next_x0+58, 546)
    COORDS_FIELD.append(next_coords)
    
    
    i += 1
    
COORDS_MY_CARD = [(483,898,541,990)]
for i in range(7):
    next_x0 = COORDS_MY_CARD[i][2] + 20
    next_coords = (next_x0, 898, next_x0+58, 990)
    COORDS_MY_CARD.append(next_coords)


COORDS_YOUR_CARD = []
for i in range(8):
    coords = COORDS_MY_CARD[i]
    coords1 = coords[1] - 888
    coords3 = coords[3] - 888
    coords = (coords[0], coords1, coords[2], coords3)
    COORDS_YOUR_CARD.append(coords)



coords_my_getcard =  [(60, 644, 118, 736), (138, 644, 196, 736), (216, 644, 274, 736), (99, 756, 157, 848), (177, 756, 235, 848)]
for i in range(5):
    coords = coords_my_getcard[i]
    new0 = coords[0] + 314
    new2 = coords[2] + 314
    new_coords = (new0, coords[1], new2, coords[3])
    coords_my_getcard.append(new_coords)
for i in range(5):
    coords = coords_my_getcard[i]
    new0 = coords[0] + 628
    new2 = coords[2] + 628
    new_coords = (new0, coords[1], new2, coords[3])
    coords_my_getcard.append(new_coords)

coords_my_getcard = []
init = (1004,644,1062,736)
coords_my_getcard.append(init)
for i in range(6):
    x0 = init[2] + 10 + 68*i
    newcoords = (x0,644,x0+58,736)
    coords_my_getcard.append(newcoords)
init2 = (1004,756,1062,848)
coords_my_getcard.append(init2)
for i in range(6):
    x0 = init2[2] + 10 + 68*i
    newcoords = (x0,756,x0+58,848)
    coords_my_getcard.append(newcoords)
    
    


COORDS_MY_GETCARDS = [(60, 644, 118, 736), (138, 644, 196, 736), (216, 644, 274, 736), (99, 756, 157, 848), (177, 756, 235, 848), (374, 644, 432, 736), (452, 644, 510, 736), (530, 644, 588, 736), (413, 756, 471, 848), (491, 756, 549, 848), (688, 644, 746, 736), (766, 644, 824, 736), (844, 644, 902, 736), (727, 756, 785, 848), (805, 756, 863, 848), (1002, 644, 1060, 736), (1080, 644, 1138, 736), (1158, 644, 1216, 736), (1236, 644, 1294, 736), (1314, 644, 1372, 736), (1002, 756, 1060, 848), (1080, 756, 1138, 848), (1158, 756, 1216, 848), (1236, 756, 1294, 848), (1314, 756, 1372, 848)]
coords_your_getcards = []
for i in range(len(COORDS_MY_GETCARDS)):
    coords = COORDS_MY_GETCARDS[i]
    newy0 = coords[1] - 492
    newy1 = coords[3] - 492
    new_coords = (coords[0], newy0, coords[2], newy1)
    coords_your_getcards.append(new_coords)
    
    
    

#print(COORDS_FIELD)
#print(COORDS_MY_CARD)
#print(COORDS_YOUR_CARD)
#print(coords_my_getcard)
#print(coords_your_getcards)



COORDS_MY_GETCARDS = [[(30, 644, 88, 736), (98, 644, 156, 736), (166, 644, 224, 736), (64, 756, 122, 848), (132, 756, 190, 848)],
                      [(264, 644, 322, 736), (332, 644, 390, 736), (400, 644, 458, 736), (468, 644, 526, 736), (536, 644, 594, 736), (264, 756, 322, 848), (332, 756, 390, 848), (400, 756, 458, 848), (468, 756, 526, 848), (536, 756, 594, 848)],
                      [(634, 644, 692, 736), (702, 644, 760, 736), (770, 644, 828, 736), (838, 644, 896, 736), (906, 644, 964, 736), (634, 756, 692, 848), (702, 756, 760, 848), (770, 756, 828, 848), (838, 756, 896, 848), (906, 756, 964, 848)],
                      [(1004, 644, 1062, 736), (1072, 644, 1130, 736), (1140, 644, 1198, 736), (1208, 644, 1266, 736), (1276, 644, 1334, 736), (1344, 644, 1402, 736), (1412, 644, 1470, 736), (1004, 756, 1062, 848), (1072, 756, 1130, 848), (1140, 756, 1198, 848), (1208, 756, 1266, 848), (1276, 756, 1334, 848), (1344, 756, 1402, 848), (1412, 756, 1470, 848)]]
COORDS_MY_GETCARDS = [[(30, 152, 88, 244), (98, 152, 156, 244), (166, 152, 224, 244), (64, 264, 122, 356), (132, 264, 190, 356)],
                        [(264, 152, 322, 244), (332, 152, 390, 244), (400, 152, 458, 244), (468, 152, 526, 244), (536, 152, 594, 244), (264, 264, 322, 356), (332, 264, 390, 356), (400, 264, 458, 356), (468, 264, 526, 356), (536, 264, 594, 356)],
                        [(634, 152, 692, 244), (702, 152, 760, 244), (770, 152, 828, 244), (838, 152, 896, 244), (906, 152, 964, 244), (634, 264, 692, 356), (702, 264, 760, 356), (770, 264, 828, 356), (838, 264, 896, 356), (906, 264, 964, 356)],
                        [(1004, 152, 1062, 244), (1072, 152, 1130, 244), (1140, 152, 1198, 244), (1208, 152, 1266, 244), (1276, 152, 1334, 244), (1344, 152, 1402, 244), (1412, 152, 1470, 244), (1004, 264, 1062, 356), (1072, 264, 1130, 356), (1140, 264, 1198, 356), (1208, 264, 1266, 356), (1276, 264, 1334, 356), (1344, 264, 1402, 356), (1412, 264, 1470, 356)]]

COORDS_YOUR_GETCARDS = []
for i in range(len(COORDS_MY_GETCARDS)):
    for j in range(len(COORDS_MY_GETCARDS[i])):
        coords = COORDS_MY_GETCARDS[i][j]
        #newcoords = (coords[0],coords[1]-492, coords[2], coords[3]-492)
        newcoords = (coords[0],coords[1]+20,coords[2],coords[3]+20)
        COORDS_YOUR_GETCARDS.append(newcoords)
#print(COORDS_YOUR_GETCARDS)







COORDS_FIELD = [(10, 454, 68, 546), (88, 454, 146, 546), (166, 454, 224, 546), (244, 454, 302, 546), (322, 454, 380, 546), (400, 454, 458, 546), (478, 454, 536, 546), (556, 454, 614, 546), (634, 454, 692, 546), (712, 454, 770, 546), (790, 454, 848, 546), (868, 454, 926, 546), (946, 454, 1004, 546), (1024, 454, 1082, 546), (1102, 454, 1160, 546), (1180, 454, 1238, 546)]
COORDS_YAMAFUDA = [(1336, 454, 1394, 546), (1414, 454, 1472, 546)]
COORDS_MY_CARDS = [(483, 898, 541, 990), (561, 898, 619, 990), (639, 898, 697, 990), (717, 898, 775, 990), (795, 898, 853, 990), (873, 898, 931, 990), (951, 898, 1009, 990), (1029, 898, 1087, 990)]
COORDS_MY_GETCARDS = [[(30, 624, 88, 716), (98, 624, 156, 716), (166, 624, 224, 716), (64, 736, 122, 828), (132, 736, 190, 828)],
                      [(264, 624, 322, 716), (332, 624, 390, 716), (400, 624, 458, 716), (468, 624, 526, 716), (536, 624, 594, 716), (264, 736, 322, 828), (332, 736, 390, 828), (400, 736, 458, 828), (468, 736, 526, 828), (536, 736, 594, 828)],
                      [(634, 624, 692, 716), (702, 624, 760, 716), (770, 624, 828, 716), (838, 624, 896, 716), (906, 624, 964, 716), (634, 736, 692, 828), (702, 736, 760, 828), (770, 736, 828, 828), (838, 736, 896, 828), (906, 736, 964, 828)],
                      [(1004, 624, 1062, 716), (1072, 624, 1130, 716), (1140, 624, 1198, 716), (1208, 624, 1266, 716), (1276, 624, 1334, 716), (1344, 624, 1402, 716), (1412, 624, 1470, 716), (1004, 736, 1062, 828), (1072, 736, 1130, 828), (1140, 736, 1198, 828), (1208, 736, 1266, 828), (1276, 736, 1334, 828), (1344, 736, 1402, 828), (1412, 736, 1470, 828)]]
COORDS_YOUR_CARDS = [(483, 10, 541, 102), (561, 10, 619, 102), (639, 10, 697, 102), (717, 10, 775, 102), (795, 10, 853, 102), (873, 10, 931, 102), (951, 10, 1009, 102), (1029, 10, 1087, 102)]
COORDS_YOUR_GETCARDS = [[(30, 172, 88, 264), (98, 172, 156, 264), (166, 172, 224, 264), (64, 284, 122, 376), (132, 284, 190, 376)],
                        [(264, 172, 322, 264), (332, 172, 390, 264), (400, 172, 458, 264), (468, 172, 526, 264), (536, 172, 594, 264), (264, 284, 322, 376), (332, 284, 390, 376), (400, 284, 458, 376), (468, 284, 526, 376), (536, 284, 594, 376)],
                        [(634, 172, 692, 264), (702, 172, 760, 264), (770, 172, 828, 264), (838, 172, 896, 264), (906, 172, 964, 264), (634, 284, 692, 376), (702, 284, 760, 376), (770, 284, 828, 376), (838, 284, 896, 376), (906, 284, 964, 376)],
                        [(1004, 172, 1062, 264), (1072, 172, 1130, 264), (1140, 172, 1198, 264), (1208, 172, 1266, 264), (1276, 172, 1334, 264), (1344, 172, 1402, 264), (1412, 172, 1470, 264), (1004, 284, 1062, 376), (1072, 284, 1130, 376), (1140, 284, 1198, 376), (1208, 284, 1266, 376), (1276, 284, 1334, 376), (1344, 284, 1402, 376), (1412, 284, 1470, 376)]]

COORDS_YAMAFUDA_MOJI = []
for i in range(len(COORDS_YAMAFUDA)):
    coords = COORDS_YAMAFUDA[i]
    newcoords = (coords[0], coords[1]-41, coords[2], coords[1]-1)
    COORDS_YAMAFUDA_MOJI.append(newcoords)
#print(COORDS_YAMAFUDA_MOJI)

COORDS_FIELD_MOJI = []
for i in range(len(COORDS_FIELD)):
    coords = COORDS_FIELD[i]
    newcoords = (coords[0], coords[1]-41, coords[2], coords[1]-1)
    COORDS_FIELD_MOJI.append(newcoords)
#print(COORDS_FIELD_MOJI)

COORDS_MY_CARDS_MOJI = []
for i in range(len(COORDS_MY_CARDS)):
    coords = COORDS_MY_CARDS[i]
    newcoords = (coords[0], coords[1]-41, coords[2], coords[1]-1)
    COORDS_MY_CARDS_MOJI.append(newcoords)
#print(COORDS_MY_CARDS_MOJI)

COORDS_YOUR_CARDS_MOJI = []
for i in range(len(COORDS_YOUR_CARDS)):
    coords = COORDS_YOUR_CARDS[i]
    newcoords = (coords[0], coords[3]+1, coords[2], coords[3]+41)
    COORDS_YOUR_CARDS_MOJI.append(newcoords)
print(COORDS_YOUR_CARDS_MOJI)
        
