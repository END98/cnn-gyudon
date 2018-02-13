#/import gyudon_keras as gyudon

import os, random, shutil, sys
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_NAME = []


'''
image_size = 50
categories = [
    "普通の牛丼", "紅ショウガ牛丼", 
    "ネギ玉牛丼", "チーズ牛丼pytho"]
calories = [656, 658, 768, 836]

X = []
files = []
for fname in sys.argv[1:]:
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))
    in_data = np.asarray(img)
    X.append(in_data)
    files.append(fname)
X = np.array(X)

model = gyudon.build_model(X.shape[1:])
model.load_weights('./static/images/gyudon-model.hdf5')

html = ""
pre = model.predict(X)
for i, p in enumerate(pre):
    y = p.argmax()
    print("+ 入力:", files[i])
    print("| 牛丼名:", categories[y])
    print("| カロリー:", calories[y])
    html += """
        <h3>入力:{0}</h3>
        <div>
          <p><img src="{1}" width=300></p>
          <p>牛丼名:{2}</p>
          <p>カロリー:{3}kcal</p>
        </div>
    """.format(os.path.basename(files[i]),
        files[i],
        categories[y],
        calories[y])

html = "<html><body style='text-align:center;'>" + \
    "<style> p { margin:0; padding:0; } </style>" + \
    html + "</body></html>"
with open("gyudon-result.html", "w") as f:
    f.write(html)
'''

class IndexHandler(tornado.web.RequestHandler):
    '''
    def get(self, *args, **kwargs):
        if len(sys.argv) <= 1:
            print("show-app.py (ファイル名)")
            quit()
        image_name = self.sys.argv[1]
        self.render('result.html', \
            iamge_path=self.static_url(image_name))
    '''
    
    def post(self, *args, **kwargs):
        image = self.argument('image_path')
    
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