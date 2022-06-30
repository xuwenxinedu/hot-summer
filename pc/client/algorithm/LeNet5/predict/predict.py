import numpy as np
from configparser import ConfigParser

import os
import cv2
TEST = True

from keras.models import Model
from keras.layers import *


def LeNet5(input_shape: list):
    inputs = Input(shape=input_shape)
    conv_1 = Conv2D(6, 5, activation="relu", padding="same")(inputs)
    pool_1 = MaxPooling2D((2, 2))(conv_1)
    conv_2 = Conv2D(16, 5, activation="relu", padding="same")(pool_1)
    pool_2 = MaxPooling2D((2, 2))(conv_2)
    fc_0 = Flatten()(pool_2)
    fc_1 = Dense(120, activation="relu")(fc_0)
    # drop_out = Dropout(0.5)(fc_1)
    fc_2 = Dense(84, activation="relu")(fc_1)
    fc_3 = Dense(10, activation="softmax")(fc_2)
    model = Model(inputs, fc_3)
    return model




config_parser = ConfigParser()
config_parser.read("{}/../config/config.cfg".format(os.path.split(os.path.realpath(__file__))[0]))
input_size = int(config_parser.get("INPUT_SIZE", "input_size"))
model_lenet5 = LeNet5(input_shape=[input_size, input_size, 1])
model_lenet5.load_weights("{}/../weights/LeNet5.ckpt".format(os.path.split(os.path.realpath(__file__))[0]))


def predict(img_binary_np: np.ndarray) -> int:
    index_max = np.argmax(model_lenet5.predict(img_binary_np))
    # print("index_max:", index_max)
    # print("index_max type:", type(index_max))
    # print("LeNet5被调用!")
    return int(index_max)


def get_predict_result(image_get_np: np.ndarray) -> int:
    if TEST:
        # 测试用
        _, img_binary_np = cv2.threshold(image_get_np, 127, 1, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    else:
        # 带整体预处理
        _, img_binary_np = cv2.threshold(image_get_np, 127, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return predict(np.array([img_binary_np]))


# if TEST:
#     image_np = cv2.imread("./0.png")
#     image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
#     image_28 = cv2.resize(image_gray, (28, 28))
#     print("识别结果：", get_predict_result(image_28))
