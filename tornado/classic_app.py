# https://qiita.com/Hironsan/items/f4100e2884efd2ad215d#_reference-94b6d787ea68ee42e35c
import os
import random
import shutil
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = BASE_DIR + '/static/images/'
CLASS_DIR = ['普通の牛丼', '紅生姜牛丼', 'ねぎ玉牛丼', 'チーズ牛丼', 'キムチ牛丼', 'その他']
IMAGE_NAME = []
NUMBER = 0

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print('get')
        if os.path.exists(IMAGE_DIR + '普通の牛丼') != True:
            for dir in CLASS_DIR:
                os.mkdir('./static/images/' + dir)

        image_name = self.select_image(NUMBER)
        IMAGE_NAME.extend([image_name])
        self.render('index.html', image_path=self.static_url('images/牛丼/' + image_name))
    
    def post(self, *args, **kwargs):
        print('post')
        variety = self.get_argument('variety')
        print(variety, IMAGE_NAME)

        if variety == '普通の牛丼':
            shutil.move(IMAGE_DIR + '牛丼/' + IMAGE_NAME[0],\
            IMAGE_DIR + '普通の牛丼/' + IMAGE_NAME[0])

        elif variety == '紅生姜牛丼':
            shutil.move(IMAGE_DIR + '牛丼/' + IMAGE_NAME[0],\
            IMAGE_DIR + '紅生姜牛丼/' + IMAGE_NAME[0])

        elif variety == 'ねぎ玉牛丼':
            shutil.move(IMAGE_DIR + '牛丼/' + IMAGE_NAME[0],\
            IMAGE_DIR + 'ねぎ玉牛丼/' + IMAGE_NAME[0])

        elif variety == 'チーズ牛丼':
            shutil.move(IMAGE_DIR + '牛丼/' + IMAGE_NAME[0],\
            IMAGE_DIR + 'チーズ牛丼/' + IMAGE_NAME[0])

        elif variety == 'キムチ牛丼':
            shutil.move(IMAGE_DIR + '牛丼/' + IMAGE_NAME[0],\
            IMAGE_DIR + 'キムチ牛丼/' + IMAGE_NAME[0])

        elif variety == 'その他':
            shutil.move(IMAGE_DIR + '牛丼/' + IMAGE_NAME[0],\
            IMAGE_DIR + 'その他/' + IMAGE_NAME[0])

        # IMAGE_NAME変数 0023_thum.jpg にそれを突っ込む
        # 牛丼 ディレクトリから IMAGE_NAME変数 0023_thum.jpgを削除

        image_name = self.select_image(NUMBER)
        IMAGE_NAME.extend([image_name])
        IMAGE_NAME.pop(0)
        self.render('index.html', image_path=self.static_url('images/牛丼/' + image_name))
    
    def select_image(self, *args, **kwargs):
        global NUMBER
        NUMBER += 1
        files = os.listdir(IMAGE_DIR + '牛丼')
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