import os, glob
import numpy as np
from PIL import Image
from sklearn import cross_validation

root_dir = './tornado/static/images'
categories = ['普通の牛丼', '紅生姜牛丼', 'ネギ玉牛丼', 'チーズ牛丼']
nb_classes = len(categories)
image_size = 50

X = []
Y = []
for idx, cat in enumerate(categories):
    image_dir = root_dir + '/' + cat
    #import ipdb; ipdb.set_trace()
    files = glob.glob(image_dir + '/*.jpg')
    for i, f in enumerate(files):
        image = Image.open(f)
        image = image.convert('RGB')
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(idx)
        #import ipdb; ipdb.set_trace()
X = np.array(X)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = \
    cross_validation.train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test)
np.save('./tornado/static/images/gyudon.npy', xy)


