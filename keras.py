import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils

root_dir = './tornado/static/images'
categories = ['普通の牛丼', '紅生姜牛丼', 'ネギ玉牛丼', 'チーズ牛丼']
nb_classes = len(categories)

def main():
    X_train, X_test, Y_train, Y_test = \
    np.load('./tornado/static/images/gyudon.npy')
    X_train = X_train.astype('float') / 256
    X_test = X_test.astype('float') / 256
    Y_train = np_utils.to_categorical(Y_train, nb_classes)
    Y_test = np_utils.to_categorical(Y_test, nb_classes)

def build_model(in_shape):

def model_train(X, Y):

def model_eval(model, X, Y):

if __name__ == '__main__': main()