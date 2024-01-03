import os
import time
from flask import Flask, render_template, jsonify, request
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar

from cv2resize import compressCV, uncompressCV
from filesize import getFileFolderSize
from opencv import compresscv
from tgz import targz_file, untargz_file
from zip import zip_file, unzip_file

from udpC import udpc
from ftpC import ftpc
from tcpC import tcpc

app = Flask(__name__)


def bar_base():

    timezip1 = time.time()
    zip_file('C:\date\ex', 'C:\date\exzip.zip')
    timezip2 = time.time()
    sizezip = (getFileFolderSize('C:\date\exzip.zip') / getFileFolderSize('C:\date\ex') * 100)
    unzip_file('C:\date\exzip.zip', 'C:\date\ee')
    timezip3 = time.time()

    timegz1 = time.time()
    targz_file('C:\date\ex', 'C:\date\extgz.tar.gz')
    timegz2 = time.time()
    sizegz = (getFileFolderSize('C:\date\extgz.tar.gz') / getFileFolderSize('C:\date\ex') * 100)
    untargz_file('C:\date\extgz.tar.gz', 'C:\date\ye')
    timegz3 = time.time()

    timeopencv1 = time.time()
    compresscv('C:\date\ex', 'C:\date\opencv')
    timeopencv2 = time.time()
    sizeopen = (getFileFolderSize('C:\date\opencv') / getFileFolderSize('C:\date\ex') * 100)

    timecv1 = time.time()
    compressCV('C:\date\ex', 'C:\date\CV')
    timecv2 = time.time()
    uncompressCV('C:\date\CV','C:\date\cv')
    timecv3 = time.time()
    sizecv = (getFileFolderSize('C:\date\CV') / getFileFolderSize('C:\date\ex') * 100)

    a1 = timezip2 - timezip1
    a2 = timegz2 - timegz1
    a3 = timeopencv2 - timeopencv1
    a4 = timecv2 - timecv1

    b1 = timezip3 - timezip2
    b2 = timegz3 - timegz2
    b4 = timecv3 - timecv2

    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["ZIP", "GZ", "CV2", "CV2优化"])
            .add_yaxis("压缩率", ['%.2f' % sizezip, '%.2f' % sizegz, '%.2f' % sizeopen, '%.2f' % sizecv])
            .add_yaxis("压缩时间", ['%.2f' % a1, '%.2f' % a2, '%.2f' % a3, '%.2f' % a4])
            .add_yaxis("解压缩时间", ['%.2f' % b1, '%.2f' % b2, '%.2f' % 0.00, '%.2f' % b4])
            .set_global_opts(title_opts=opts.TitleOpts(title="压缩率和压缩时间", subtitle="ZIP GZ CV2"))
    )

    return bar


def barr_base():
    a = tcpc()
    b = udpc()
    c = ftpc()

    barr = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["TCP", "UDP", "FTP"])
            .add_yaxis("传输时间", ['%.2f' % a, '%.2f' % b[0], '%.2f' % c[0]])
            .add_yaxis("丢包率", ['%.2f' % 0.00, '%.2f' % b[1], '%.2f' % 0.00])
            .set_global_opts(title_opts=opts.TitleOpts(title="网络传输", subtitle="TCP UDP FTP"))
    )
    '''
    barr.set_global_opts(visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        type_="color",
        range_text=("高", "低"),
        range_opacity=80,
        orient="horizontal",
        pos_right="20%",
        pos_top="bottom",
        split_number=10))
    '''
    return barr


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    d = barr_base()
    return jsonify({
        "chart1": c.dump_options_with_quotes(),
        "chart2": d.dump_options_with_quotes()
    })


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/api/start', methods=['POST'], strict_slashes=False)
def api_predict():
    CLASSIFY_REST_API_URL = 'http://xxx.xxx.xxx.xxx:5000/predict'
    headers = {'Content-Type': 'application/json'}
    fname = request.form['file_path']
    print(fname)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
