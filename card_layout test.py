import cv2
import numpy as np
import matplotlib.pyplot as plt

#Initiation:
Spade = cv2.imread('Spade.jpg')
Diamond = cv2.imread('Diamond.jpg')
Club = cv2.imread('Club.jpg')
Heart = cv2.imread('Heart.jpg')

shapes = [Spade, Diamond, Club, Heart]
for s in shapes: _, s = cv2.threshold(s, 127, 255, cv2.THRESH_BINARY)

resized_shapes = []
for s in shapes:
    s_copy = s.copy()
    s_copy = cv2.resize(s_copy, (0,0), s_copy, 0.2, 0.2)
    resized_shapes.append(s_copy)


#Base For Cards:
shape = (133, 75, 3)
img = np.ones(shape, dtype = np.uint16) * 255
img_copy = img.copy
c = 0
cards = []


for s in resized_shapes:
    
    img = np.ones(shape, dtype = np.uint16) * 255
    img_copy = img.copy()
    
    y = int((img.shape[0] - s.shape[0])/2)
    x = int((img.shape[1] - s.shape[1])/2)
    w,h = (img.shape[0]-3, img.shape[1]-24)

    img_copy = cv2.putText(img_copy, '10', (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    
    img_copy[y:y+s.shape[0], x:x+s.shape[1]] = s
    cards.append(img_copy)
    

for i in cards:
    plt.imshow(i)
    plt.show()


'''
plt.imshow(cards[0])
plt.show()
'''
