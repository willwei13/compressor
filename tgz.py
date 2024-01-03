import os
import tarfile
import time

from filesize import getFileFolderSize


def targz_file(src_dir, tgz_name):
    """
    src_dir: 需要打包的目录
    tgz_name: 压缩文件名
    """

    try:
        with tarfile.open(tgz_name, "w:gz") as tar:
            tar.add(src_dir, arcname=os.path.basename(src_dir))

        return True
    except Exception as e:
        print(e)
        return False


def untargz_file(tgz_name, dst_dir):
    """
    tga_name: 压缩文件名
    dst_dir: 解压后的存放路径
    """

    try:
        t = tarfile.open(tgz_name)
        t.extractall(path=dst_dir)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':

    time1 = time.time()
    targz_file('C:\date\ex', 'C:\date\ex2.tar.gz')
    time2 = time.time()
    print(str(time2 - time1) + 's')
    print(str(getFileFolderSize('C:\date\ex2.tar.gz') / getFileFolderSize('C:\date\ex') * 100) + '%')

    time3 = time.time()
    untargz_file('C:\date\ex2.tar.gz', 'C:\date\ye')
    time4 = time.time()
    print(str(time4 - time3) + 's')



