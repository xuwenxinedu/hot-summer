import matplotlib.pyplot as plt
import cv2
import numpy as np
import requests
from algorithm.LeNet5.predict.predict import get_predict_result


    
def ans():
    response = requests.get("http://192.168.43.97:8087/video_feed_api")
    image_array = np.frombuffer(response.content, dtype=np.uint8)
    np_image = cv2.imdecode(image_array, 1)
    np_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)

    img1 = np_image[70: 190, 170: 270]
    img2 = np_image[70: 190, 440: 540]
    img3 = np_image[280: 400, 170: 270]
    img4 = np_image[290: 400, 430: 520]

    data = dict()
    for i, img in enumerate([img1, img2, img3, img4]):
        plt.imsave(".\img\%d.png" % i, img)
    
    image_np_1 = cv2.imread(r".\img\0.png")
    image_gray_1 = cv2.cvtColor(image_np_1, cv2.COLOR_BGR2GRAY)
    image_28_1 = cv2.resize(image_gray_1, (28, 28))
    data[0] = get_predict_result(image_28_1)
    
    image_np_1 = cv2.imread(r".\img\1.png")
    image_gray_1 = cv2.cvtColor(image_np_1, cv2.COLOR_BGR2GRAY)
    image_28_1 = cv2.resize(image_gray_1, (28, 28))
    data[1] = get_predict_result(image_28_1)
    
    image_np_1 = cv2.imread(r".\img\2.png")
    image_gray_1 = cv2.cvtColor(image_np_1, cv2.COLOR_BGR2GRAY)
    image_28_1 = cv2.resize(image_gray_1, (28, 28))
    data[2] = get_predict_result(image_28_1)
    
    image_np_1 = cv2.imread(r".\img\3.png")
    image_gray_1 = cv2.cvtColor(image_np_1, cv2.COLOR_BGR2GRAY)
    image_28_1 = cv2.resize(image_gray_1, (28, 28))
    data[3] = get_predict_result(image_28_1)
    
    return data
