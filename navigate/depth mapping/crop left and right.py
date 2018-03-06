import cv2
import numpy as np

img = cv2.imread('/home/user/Downloads/1.jpg')
x, y, w, h =( 0 , 0 , np.size(img, 1) , np.size(img, 0))

print np.size(img, 1) , np.size(img, 0)

crop_img_1 = img[y:y+h, x:x+w/2]
crop_img_2 = img[y:y+h, x+w/2:x+w]

cv2.imwrite('left.jpg',crop_img_1)
cv2.imwrite('right.jpg',crop_img_2)
