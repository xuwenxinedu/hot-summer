import numpy as np
import cv2
from predict.predict import get_predict_result


class ImageProcessForNumberRecognize:
    """
    图像预处理的类
    """

    def __init__(self):
        self.yellow_lower = np.array([26, 37, 46])
        self.yellow_upper = np.array([34, 255, 255])
        self.image_mask = np.zeros((28, 28, 1), np.uint8)
        self.image_mask[3: 25, 6: 23] = 255
        self.get_predict_result = get_predict_result

    @staticmethod
    def histogram_equalization(image_bgr_np: np.ndarray) -> np.ndarray:
        """
        直方图均衡化
        :param image_bgr_np:输入的BGR图像
        :return:均衡化后的BGR图像
        """
        # 将BGR图像转换到YCrCb空间中
        image_ycrcb_np = cv2.cvtColor(image_bgr_np, cv2.COLOR_BGR2YCR_CB)
        # 将YCrCb图像通道分离
        tuple_channels = cv2.split(image_ycrcb_np)
        # 对第1个通道即亮度通道进行全局直方图均衡化并保存
        cv2.equalizeHist(tuple_channels[0], tuple_channels[0])
        # 将处理后的通道和没有处理的两个通道合并
        cv2.merge(tuple_channels, image_ycrcb_np)
        # 将YCrCb图像转换到BGR空间中
        img_aft_hgtgrm_eqlzt_np = cv2.cvtColor(image_ycrcb_np, cv2.COLOR_YCR_CB2BGR)
        return img_aft_hgtgrm_eqlzt_np

    def image_locate(self, image_bgr_np: np.ndarray) -> (np.ndarray, list):
        """
        图像定位，为了拿出黄色块的区域
        :param image_bgr_np: 原始图像
        :return:
        """
        # BGR转换为HSV颜色空间
        image_hsv_np = cv2.cvtColor(image_bgr_np, cv2.COLOR_BGR2HSV)
        # 将黄色设置为白色，非黄色为黑色
        image_bnr_np = cv2.inRange(image_hsv_np, self.yellow_lower, self.yellow_upper)
        # 对二值化图进行中值滤波
        image_aft_ft_np = cv2.medianBlur(image_bnr_np, 7)
        # 开运算，先腐蚀，后膨胀
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        image_op_np = cv2.morphologyEx(image_aft_ft_np, cv2.MORPH_OPEN, kernel, iterations=1)
        # 寻找轮廓
        cts, hrch = cv2.findContours(image_op_np, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        list_positions = []
        # 逐一排查轮廓
        for i in range(len(cts)):
            contour = cts[i]
            area = cv2.contourArea(contour)
            # 面积小于10000的丢弃
            if area < 10000:
                continue
            # 找每个黄色块4个点的坐标
            rctg_min_area = cv2.minAreaRect(contour)
            box_points_np = cv2.boxPoints(rctg_min_area)
            box_points_np = np.int0(box_points_np)
            box_points_np = np.maximum(box_points_np, 0)
            list_x_coordinate = [box_points_np[0, 0], box_points_np[1, 0], box_points_np[2, 0], box_points_np[3, 0]]
            list_y_coordinate = [box_points_np[0, 1], box_points_np[1, 1], box_points_np[2, 1], box_points_np[3, 1]]
            list_index_x_cdnt = np.argsort(list_x_coordinate)
            list_index_y_cdnt = np.argsort(list_y_coordinate)
            x_cdnt_min = box_points_np[list_index_x_cdnt[0], 0]
            x_cdnt_max = box_points_np[list_index_x_cdnt[3], 0]
            y_cdnt_min = box_points_np[list_index_y_cdnt[0], 1]
            y_cdnt_max = box_points_np[list_index_y_cdnt[3], 1]
            list_location = [x_cdnt_min, x_cdnt_max, y_cdnt_min, y_cdnt_max]
            list_positions.append(list_location)
        return image_op_np, list_positions

    @staticmethod
    def image_z_list(list_positions: list, h: int = 480, w: int = 640) -> list:
        """
        # 按左上、右上、左下、右下的顺序排列黄色块
        :param list_positions:
        :param h:
        :param w:
        :return:
        """
        number_images = len(list_positions)
        list_z_shape = [[], [], [], []]
        for i in range(number_images):
            x_center_cdnt = (list_positions[i][0] + list_positions[i][1]) // 2
            y_center_cdnt = (list_positions[i][2] + list_positions[i][3]) // 2
            if (x_center_cdnt < w // 2) and (y_center_cdnt < h // 2):
                list_z_shape[0] = list_positions[i]
            elif (x_center_cdnt > w // 2) and (y_center_cdnt < h // 2):
                list_z_shape[1] = list_positions[i]
            elif (x_center_cdnt < w // 2) and (y_center_cdnt > h // 2):
                list_z_shape[2] = list_positions[i]
            elif (x_center_cdnt > w // 2) and (y_center_cdnt > h // 2):
                list_z_shape[3] = list_positions[i]
        return list_z_shape

    def edge_process(self, image_cut_np: np.ndarray) -> np.ndarray:
        """
        边缘处理
        :param image_cut_np:
        :return:
        """
        image_compress_np = cv2.resize(image_cut_np, (28, 28), interpolation=cv2.INTER_CUBIC)
        image_gray_np = cv2.cvtColor(image_compress_np, cv2.COLOR_BGR2GRAY)
        result, image_binary_np = cv2.threshold(image_gray_np, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        image_get_gray_np = cv2.bitwise_and(image_binary_np, self.image_mask)
        return image_get_gray_np

    def image_recognize(self, list_positions: list, list_z_shape: list, image_np: np.ndarray) -> dict:
        """
        识别
        :param list_positions:
        :param list_z_shape:
        :param image_np:
        :return:
        """
        result = {}
        number_cargos = len(list_positions)
        for i in range(number_cargos):
            if list_z_shape[i]:
                image_cut_np = image_np[list_z_shape[i][2]: list_z_shape[i][3], list_z_shape[i][0]: list_z_shape[i][1]]
                # cv2.imwrite("{}.png".format(i), image_cut_np)
                image_get_np = self.edge_process(image_cut_np)
                # cv2.imwrite("{}.png".format(i), image_get_np)
                # _, image_binary_np = cv2.threshold(image_get_np, 127, 1, cv2.THRESH_BINARY_INV)
                result[i] = self.get_predict_result(image_get_np)
        return result



