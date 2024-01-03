import time
import cv2
import os
import numpy as np

from filesize import getFileFolderSize


def compresspng(path, cpath):
    img_cv2 = cv2.imdecode(np.fromfile(file=path, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite(cpath, img_cv2, [cv2.IMWRITE_PNG_COMPRESSION, 1])


def compresscv(path, cpath):
    if os.path.isdir(path):
        if os.path.exists(cpath):
            pass
        else:
            os.mkdir(cpath)
        for s in os.listdir(path):
            st = path + '\\' + s
            slist = st.split('\\')
            scpath = cpath + '\\' + slist[len(slist) - 1]
            compresscv(st, scpath)
    else:
        compresspng(path, cpath)



if __name__ == '__main__':
    path1 = 'C:\date\ex'
    path2 = 'C:\date\exoopen'

    time1 = time.time()
    compresscv(path1, path2)
    time2 = time.time()

    print(time2 - time1)
    size1 = getFileFolderSize(path1)
    size2 = getFileFolderSize(path2)
    print((size2 / size1) * 100)