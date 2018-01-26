# https://qiita.com/Hironsan/items/f4100e2884efd2ad215d#_reference-94b6d787ea68ee42e35c
import os
import tornado.ioloop
import tornado.web
from tornado.web import url


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')


class PythonHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('python.html')


class PHPHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('php.html')


class RubyHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('ruby.html')


BASE_DIR = os.path.dirname(__file__)

application = tornado.web.Application([
    url(r'/', IndexHandler, name='index'),
    url(r'/python/', PythonHandler, name='python'),
    url(r'/php/', PHPHandler, name='php'),
    url(r'/ruby/', RubyHandler, name='ruby'),
    ],
    template_path=os.path.join(BASE_DIR, 'templates'),
    static_path=os.path.join(BASE_DIR, 'static'),
)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()