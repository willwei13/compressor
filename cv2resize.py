import time
import cv2
import os
import numpy as np

from filesize import getFileFolderSize


def compressPNG(path, cpath):
    img = cv2.imdecode(np.fromfile(file=path, dtype=np.uint8), cv2.IMREAD_COLOR)
    dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imwrite(cpath, dst)


def compressCV(path, cpath):
    if os.path.isdir(path):
        if os.path.exists(cpath):
            pass
        else:
            os.mkdir(cpath)
        for s in os.listdir(path):
            st = path + '\\' + s
            slist = st.split('\\')
            scpath = cpath + '\\' + slist[len(slist) - 1]
            compressCV(st, scpath)
    else:
        compressPNG(path, cpath)


def uncompressPNG(path, cpath):
    img = cv2.imdecode(np.fromfile(file=path, dtype=np.uint8), cv2.IMREAD_COLOR)
    dst = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(cpath, dst)

def uncompressCV(path, cpath):
    if os.path.isdir(path):
        if os.path.exists(cpath):
            pass
        else:
            os.mkdir(cpath)
        for s in os.listdir(path):
            st = path + '\\' + s
            slist = st.split('\\')
            scpath = cpath + '\\' + slist[len(slist) - 1]
            uncompressCV(st, scpath)
    else:
        uncompressPNG(path, cpath)

if __name__ == '__main__':
    start = time.time()
    compressCV('C:\date\ex', 'C:\date\excv')
    mid = time.time()
    uncompressCV('C:\date\excv','C:\date\excvjieya')
    end = time.time()
    s1 = getFileFolderSize('C:\date\ex')
    s2 = getFileFolderSize('C:\date\excv')
    t1 = time.time()

    print(str(mid - start))
    print(str(end - mid))
    print(str(s2 / s1))
    print(t1 - end)