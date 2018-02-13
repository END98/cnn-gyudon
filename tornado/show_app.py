#/import gyudon_keras as gyudon

import os, random, shutil, sys
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_NAME = []

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('result.html')
    
    def post(self, *args, **kwargs):
        image = self.get_argument('image')
        picture = self.get_argument('picture')
        print(image)
        print(picture)

    
    #def ml(self, *args, **kwargs):

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