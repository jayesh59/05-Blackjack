import cv2
import numpy as np
import matplotlib.pyplot as plt

shape = (133, 75, 3)
img = np.ones(shape, dtype = np.uint16) * 255
img_copy = img.copy()


#Initiation:
Spade_1 = cv2.imread('Spade.jpg')
Diamond_2 = cv2.imread('Diamond.jpg')
Club_3 = cv2.imread('Club.jpg')
Heart_4 = cv2.imread('Heart.jpg')
i  = 0
shapes = [Spade_1, Diamond_2, Club_3, Heart_4]

for s in shapes: _, s = cv2.threshold(s, 127, 255, cv2.THRESH_BINARY); shapes[i] = s ; i += 1
i = 0
for s in shapes: s = cv2.resize(s, (0,0), s, 0.2, 0.2); shapes[i] = s ; i += 1

a = 113

y = int((img.shape[0] - shapes[int((a/100))].shape[0])/2)
x = int((img.shape[1] - shapes[int((a/100))].shape[1])/2)
img_copy[y:y+shapes[int((a/100))].shape[0], x:x+shapes[int((a/100))].shape[1]] = shapes[int((a/100))]

x = a%100
a = a/100

if x<10 & x != 0:
    if a%2 == 0:
        cv2.putText(img_copy, str(x+1), (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)

    else:
        cv2.putText(img_copy, str(x+1), (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

else:
    if a%2 == 0:
        if x == 0:
            x='A'

        elif x == 10:
            x='J'

        elif x == 11:
            x='Q'

        elif x == 12:
            x='K'


        cv2.putText(img_copy, str(x), (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)

    else:
        if x == 0:
            x='A'

        elif x == 10:
            x='J'

        elif x == 11:
            x='Q'

        elif x == 12:
            x='K'
            
        cv2.putText(img_copy, str(x), (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)


plt.imshow(img_copy)
plt.show()

