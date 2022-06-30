import matplotlib.pyplot as plt
import cv2
import numpy as np
import requests
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x)

def load_model():
    network = Net()
    network_state_dict = torch.load(r'D:\myuniversity\Daerlittle\training\hot-summer\pc\client\algorithm\model.pth')
    network.load_state_dict(network_state_dict)
    return network

def get_num(img):
    net = load_model()
    with torch.no_grad():
        output = net(torch.tensor(img).unsqueeze(0))
        return output[0].argmax()



def ans():
    return {0:8, 1:6, 2:4, 3:7}

if __name__ == "__main__":

    # response = requests.get("http://192.168.43.97:8087/video_feed_api")
    # image_array = np.frombuffer(response.content, dtype=np.uint8)
    # np_image = cv2.imdecode(image_array, 1)
    # np_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
    np_image = plt.imread('./pic.png')
    np_image = (np_image * 255).dtype(np.uint8)
    plt.imshow(np_image)
    plt.show()

    img1 = np_image[70: 190, 170: 270]
    img2 = np_image[70: 190, 440: 540]
    img3 = np_image[290: 400, 170: 270]
    img4 = np_image[290: 400, 450: 540]
    img1 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
    img1 = cv2.resize(img1, (28, 28))
    print(get_num(img1))

#     for i, img in enumerate([img1, img2, img3, img4]):
#         plt.imsave("%d.png" % i, img)
#     data = dict()
#     image_np_1 = cv2.imread(r".\0.png")
#     image_gray_1 = cv2.cvtColor(image_np_1, cv2.COLOR_BGR2GRAY)
#     image_28_1 = cv2.resize(image_gray_1, (28, 28))
#     data[0] = get_predict_result(image_28_1)
#     image_np_2 = cv2.imread(r".\1.png")
#     image_gray_2 = cv2.cvtColor(image_np_2, cv2.COLOR_BGR2GRAY)
#     image_28_2 = cv2.resize(image_gray_2, (28, 28))
#     data[1] = get_predict_result(image_28_2)
#     image_np_3 = cv2.imread(r".\2.png")
#     image_gray_3 = cv2.cvtColor(image_np_3, cv2.COLOR_BGR2GRAY)
#     image_28_3 = cv2.resize(image_gray_3, (28, 28))
#     data[2] = get_predict_result(image_28_3)
#     image_np_4 = cv2.imread(r".\3.png")
#     image_gray_4 = cv2.cvtColor(image_np_4, cv2.COLOR_BGR2GRAY)
#     image_28_4 = cv2.resize(image_gray_4, (28, 28))
#     data[3] = get_predict_result(image_28_4)

#     print(data)

#     # img1 = cv2.resize(img3, (28, 28))
#     # print(ans())