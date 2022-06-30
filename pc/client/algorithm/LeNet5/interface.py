from image_process.image_process import *
import numpy as np


def predict(image_np: np):
    object_image_process = ImageProcessForNumberRecognize()
    image_op_np, list_positions = object_image_process.image_locate(image_np)
    list_z_shape = object_image_process.image_z_list(list_positions, image_np.shape[0], image_np.shape[1])
    result = object_image_process.image_recognize(list_positions, list_z_shape, image_np)
    print("result:", result)
    return result


if __name__ == "__main__":
    image_np = cv2.imread("./image_process/sample.jpg")
    predict(image_np)
