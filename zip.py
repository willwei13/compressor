import os
import zipfile
import time

from filesize import getFileFolderSize


def zip_file(src_dir, zip_name):
    """
        src_dir: 需要压缩的目录
        zip_name: 压缩文件名
    """

    z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()


def unzip_file(zip_src, dst_dir):
    """
        zip_src: 压缩文件名
        dst_dir: 解压后的存放路径
    """

    r = zipfile.is_zipfile(zip_src)
    fz = zipfile.ZipFile(zip_src, 'r')
    for file in fz.namelist():
        fz.extract(file, dst_dir)


if __name__ == '__main__':
    time1 = time.time()
    zip_file('C:\date\ex', 'C:\date\ex1.zip')
    time2 = time.time()
    print(str(time2 - time1) + 's')
    print(str(getFileFolderSize('C:\date\ex1.zip') / getFileFolderSize('C:\date\ex') * 100) + '%')

    time3 = time.time()
    unzip_file('C:\date\ex.zip', 'C:\date\ee')
    time4 = time.time()
    print(str(time4 - time3) + 's')

