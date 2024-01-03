import os

import cv2
import numpy as np
import time


def function(st, en):
    img = cv2.imread(st)
    height, width, channels = img.shape
    emptyImage = np.zeros((108, 192, channels), np.uint8)
    sh = 108 / height
    sw = 192 / width
    for i in range(108):
        for j in range(192):
            x = int(i / sh)
            y = int(j / sw)
            emptyImage[i, j] = img[x, y]
    cv2.imwrite(en, emptyImage)


def compressN(path, cpath):
    if os.path.isdir(path):
        if os.path.exists(cpath):
            pass
        else:
            os.mkdir(cpath)
        for s in os.listdir(path):
            st = path + '\\' + s
            slist = st.split('\\')
            scpath = cpath + '\\' + slist[len(slist) - 1]
            compressN(st, scpath)
    else:
        function(path, cpath)





if __name__ == '__main__':
    start = time.time()
    compressN('C:\date\ex', 'C:\date\kkk')
    end = time.time()
    print(str(end - start))
    '''
    start = time.time()
    img = cv2.imread('C:\date\www.png')
    zoom = function(img)
    cv2.imwrite('C:\date\ll.png',zoom)
    end = time.time()

    print(str(end - start))
    cv2.imshow("nearest neighbor", zoom)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    '''
