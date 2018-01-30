# https://qiita.com/Hironsan/items/f4100e2884efd2ad215d#_reference-94b6d787ea68ee42e35c
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import url


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        

class Application(tornado.web.Application):
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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