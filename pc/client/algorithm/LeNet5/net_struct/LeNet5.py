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

