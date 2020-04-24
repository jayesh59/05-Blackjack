import cv2
import numpy as np
import matplotlib.pyplot as plt

#Initiation:
Spade = cv2.imread('Spade.jpg')
_, Spade_copy = cv2.threshold(Spade, 127, 255, cv2.THRESH_BINARY)
print(Spade_copy.shape)

while True:

    cv2.imshow('Spade', Spade)
    cv2.imshow('Thresh', Spade_copy)    

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
