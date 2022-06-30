import numpy as np

class MNIST_Dataset:
    def __init__(self, datas_origin: tuple, need_shuffle: bool, batch_size: int):
        self._datas = datas_origin[0]
        self._labels = datas_origin[1]
        self.number_samples = self._datas.shape[0]
        self._need_shuffle = need_shuffle
        self._indicator_start = 0
        self._batch_size = batch_size
        if self._need_shuffle:
            self._shuffle_datas()

    def __iter__(self):
        return self

    def _shuffle_datas(self):
        permutation_np = np.random.permutation(self.number_samples)
        self._datas = self._datas[permutation_np]
        self._labels = self._labels[permutation_np]

    def next_batch(self):
        indicator_end = self.number_samples if self.number_samples < self._indicator_start + self._batch_size else\
            (self._indicator_start + self._batch_size)
        datas_batch = self._datas[self._indicator_start : indicator_end] / 255.0
        labels_batch = self._labels[self._indicator_start : indicator_end]
        self._indicator_start = indicator_end
        if self._indicator_start == self.number_samples:
            if self._need_shuffle:
                self._shuffle_datas()
            self._indicator_start = 0
        return datas_batch, labels_batch

    def __next__(self):
        return self.next_batch()
