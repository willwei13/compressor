import cv2
import cv2 as cv
import numpy as np
import math
import time

def linear(st,en):
    height = 250
    width = 250
    dst = np.zeros([width, height, 3], dtype='uint8')
    img = cv.imread(st)
    for c in range(3):
        for i in range(width):
            for j in range(height):
                x = (img.shape[0] / width) * i
                y = (img.shape[1] / height) * j
                x_top = math.ceil((img.shape[0] / width) * i)
                x_bottom = int((img.shape[0] / width) * i)
                y_top = math.ceil((img.shape[1] / height) * j)
                y_bottom = int((img.shape[1] / height) * j)
                dst[i, j, c] = img[x_top, y_top, c] * (x - x_bottom) * (y - y_bottom) + img[x_bottom, y_top, c] * (
                        x_top - x) * (y - y_bottom) + img[x_bottom, y_bottom, c] * (x_top - x) * (y_top - y) + img[
                                   x_top, y_bottom, c] * (x - x_bottom) * (y_top - y)
    cv2.imwrite(en, dst)



start = time.time()
linear('C:\date\www.png','C:\date\ww1.png')
end = time.time()
print(str(end - start))
'''
print(type(dst))
print(type(img))
cv.imshow("img", img)
cv.waitKey(0)
cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()
'''