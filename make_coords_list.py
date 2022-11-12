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


init = (1002,644,1060,736)
coords_my_getcard.append(init)
for i in range(4):
    x0 = init[2] + 20 + 78*i
    newcoords = (x0,644,x0+58,736)
    coords_my_getcard.append(newcoords)
init2 = (1002,756,1060,848)
coords_my_getcard.append(init2)
for i in range(4):
    x0 = init2[2] + 20 + 78*i
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
print(coords_your_getcards)