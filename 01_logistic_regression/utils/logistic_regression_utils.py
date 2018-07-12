import numpy as np
import h5py
from numpy.core.multiarray import ndarray


def load_dataset() -> object:
    train_dataset = h5py.File('../resources/datasets/train_catvnoncat.h5', "r")
    train_set_x_orig: ndarray = np.array(train_dataset["train_set_x"][:])  # your train set features
    train_set_y_orig: ndarray = np.array(train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('../resources/datasets/test_catvnoncat.h5', "r")
    test_set_x_orig: ndarray = np.array(test_dataset["test_set_x"][:])  # your test set features
    test_set_y_orig: ndarray = np.array(test_dataset["test_set_y"][:])  # your test set labels

    classes: ndarray = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
