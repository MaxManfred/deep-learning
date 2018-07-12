import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from numpy.core.multiarray import ndarray
from scipy import ndimage
from utils import load_dataset

# %matplotlib inline

# Loading the data (cat/non-cat)
train_set_y: ndarray
train_set_x_orig: ndarray
test_set_x_orig: ndarray
test_set_y: ndarray
classes: ndarray
train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

# Example of a picture
index = 15
plt.imshow(train_set_x_orig[index])
print(
    "y = " + str(train_set_y[:, index]) + ", it's a '" +
    classes[np.squeeze(train_set_y[:, index])].decode("utf-8") + "' picture."
)
