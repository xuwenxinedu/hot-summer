from statistics import mode
import torch
import torch.nn.functional as F
import torchvision
from torch import nn
import requests
import numpy as np
import cv2
import matplotlib.pyplot as plt

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

def get_num(pic):
    model = Net()
    network_state_dict = torch.load('./algorithm/model.pth', map_location=torch.device('cpu'))
    model.load_state_dict(network_state_dict)
    transform = torchvision.transforms.Compose([
                    torchvision.transforms.ToTensor(),
                    torchvision.transforms.Normalize(
                    (0.1307,), (0.3081,))])
    img = transform(pic).unsqueeze(0)
    model.eval()
    with torch.no_grad():
        print(model(img).argmax())

if __name__ == "__main__":

    # response = requests.get("http://192.168.43.97:8087/video_feed_api")
    # image_array = np.frombuffer(response.content, dtype=np.uint8)
    # np_image = cv2.imdecode(image_array, 1)
    # np_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)

    np_image = plt.imread('pic.png')
    img1 = np_image[70: 190, 170: 270]
    img2 = np_image[70: 190, 440: 540]
    img3 = np_image[290: 400, 170: 270]
    img4 = np_image[290: 400, 450: 540]

    img1 = np.array(cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY) * 255, dtype=np.uint8)
    img2 = np.array(cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY) * 255, dtype=np.uint8)
    img3 = np.array(cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY) * 255, dtype=np.uint8)
    img4 = np.array(cv2.cvtColor(img4, cv2.COLOR_RGB2GRAY) * 255, dtype=np.uint8)

    # img1[(255 - img1) > 100] = 255
    # img1[img1 != 255] = 0
    # img2[(255 - img2) > 100] = 255
    # img2[img2 != 255] = 0
    # img3[(255 - img3) >  255
    # img3[img3 != 255] = 0
    # img4[(255 - img4) > 100] = 255
    # img4[img4 != 255] = 0

    plt.subplot(2, 2, 1), plt.imshow(img1, cmap='gray')
    plt.subplot(2, 2, 2), plt.imshow(img2, cmap='gray')
    plt.subplot(2, 2, 3), plt.imshow(img3, cmap='gray')
    plt.subplot(2, 2, 4), plt.imshow(img4, cmap='gray')
    plt.show()

    img1 = cv2.resize(img3, (28, 28))
    get_num(img1)