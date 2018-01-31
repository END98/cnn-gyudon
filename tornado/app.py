# https://qiita.com/Hironsan/items/f4100e2884efd2ad215d#_reference-94b6d787ea68ee42e35c
import os
import random
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLASS_DIR = ['普通の牛丼', '紅生姜牛丼', 'ねぎ玉牛丼', 'チーズ牛丼', 'キムチ牛丼', 'その他']
IMAGE_NAME = []
NUMBER = 0

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print('get')
        if os.path.exists(BASE_DIR + '/static/images/normal') != True:
            for dir in CLASS_DIR:
                os.mkdir('./static/images/' + dir)

        image_name = self.select_image(NUMBER)
        IMAGE_NAME.extend([image_name])
        self.render('index.html', image_path=self.static_url('images/gyudon/' + image_name))
    
    def post(self, *args, **kwargs):
        print('post')
        variety = self.get_argument('variety')
        print(variety, IMAGE_NAME)
        # print(IMAGE_NAME)
        # チーズ牛丼、0023_thum.jpg
        # if variety変数 チーズ牛丼 から ディレクトリ を選択
        # IMAGE_NAME変数 0023_thum.jpg にそれを突っ込む
        # gyudon ディレクトリから IMAGE_NAME変数 0023_thum.jpgを削除
        # IMAGE_NAMEリストから、変数を削除する
        image_name = self.select_image(NUMBER)
        IMAGE_NAME.extend([image_name])
        IMAGE_NAME.pop(0)
        self.render('index.html', image_path=self.static_url('images/gyudon/' + image_name))
    
    def select_image(self, *args, **kwargs):
        global NUMBER
        NUMBER += 1
        files = os.listdir(BASE_DIR + '/static/images/gyudon/')
        image_name = files[NUMBER]
        return image_name


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,
        [
            url(r'/', IndexHandler, name='index'),
        ],
        template_path=os.path.join(BASE_DIR, 'templates'),
        static_path=os.path.join(BASE_DIR, 'static'),
        )

if __name__ == '__main__':
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()