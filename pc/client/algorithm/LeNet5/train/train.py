from net_struct.LeNet5 import *
from dataset import MNIST_Dataset
import os
import tensorflow as tf
import logging
from distutils.util import strtobool
from configparser import ConfigParser
import shutil

def train():
    config_parser = ConfigParser()
    config_parser.read("../config/config.cfg")
    input_size = int(config_parser.get("INPUT_SIZE", "input_size"))
    learning_rate = float(config_parser.get("MODEL", "learning_rate"))
    epochs = int(config_parser.get("MODEL", "epochs"))
    batch_size = int(config_parser.get("MODEL", "batch_size"))
    use_gpu = strtobool(config_parser.get("GPU", "use_gpu"))
    weights_path = config_parser.get("FILE_PATH", "weights_path")
    if not os.path.exists(weights_path):
        os.mkdir(weights_path)
    else:
        shutil.rmtree(weights_path)
        os.mkdir(weights_path)
    log_path = config_parser.get("FILE_PATH", "log_path")
    if not os.path.exists(log_path):
        os.mkdir(os.path.dirname(log_path).split("/")[-1])
    else:
        shutil.rmtree(log_path)
        os.mkdir(os.path.dirname(log_path).split("/")[-1])
    log_file_path = os.path.join(log_path, "train.log")
    with open(log_file_path, "w") as f_lf:
        pass
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', filename=log_file_path, filemode='w+')
    log_tf = tf.keras.callbacks.TensorBoard(log_dir=log_path)
    callback_cp = tf.keras.callbacks.ModelCheckpoint(filepath=os.path.join(weights_path,
                                                                           "LeNet5.ckpt"),
                                                                            # "LeNet5-{epoch:02d}-{val_accuracy:.2f}.ckpt"),
                                                     save_best_only=True, save_weights_only=True, monitor="val_accuracy",
                                                     mode="max", save_freq="epoch", verbose=1)
    data_origin_train, data_origin_test = tf.keras.datasets.mnist.load_data()
    dataset_train = MNIST_Dataset(data_origin_train, True, batch_size)
    dataset_test = MNIST_Dataset(data_origin_test, False, batch_size)
    model_lenet5 = LeNet5(input_shape=[input_size, input_size, 1])
    model_lenet5.summary()
    model_lenet5.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                         loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])
    tf.debugging.set_log_device_placement(True)
    if use_gpu:
        list_gpus = tf.config.experimental.list_physical_devices(device_type="GPU")
        if list_gpus:
            for gpu in list_gpus:
                tf.config.experimental.set_memory_growth(device=gpu, enable=True)
                tf.print(gpu)
        else:
            os.environ["CUDA_VISIBLE_DEVICE"] = "-1"
            logging.info("没找到GPU,转用CPU")
    else:
        os.environ["CUDA_VISIBLE_DEVICE"] = "-1"
    history = model_lenet5.fit(dataset_train, epochs=epochs,
                               steps_per_epoch=dataset_train.number_samples // batch_size + 1,
                               validation_data=dataset_test,
                               validation_steps=dataset_test.number_samples // batch_size + 1,
                               callbacks=[callback_cp, log_tf])
    model_lenet5.save_weights(os.path.join(weights_path, "LeNet5.ckpt"), save_format="tf")
    # logging.info("模型已保存")


if __name__ == "__main__":
    train()
