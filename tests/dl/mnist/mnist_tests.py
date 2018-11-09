import unittest

from keras.datasets import mnist
from keras.layers import Dense
# import mnist dataset
from keras.models import Sequential
from keras.utils import to_categorical


class TestMNIST(unittest.TestCase):

    def test_keras_on_mnist(self):
        # load MNIST data set in Keras
        (training_samples, training_labels), (test_samples, test_labels) = mnist.load_data()

        print('\n')
        print('Training samples shape', training_samples.shape)
        print('Training labels shape', training_labels.shape)

        print('Test samples shape', test_samples.shape)
        print('Test label shape', test_labels.shape)

        # create deep net
        neural_network = Sequential()
        neural_network.add(Dense(512, activation='relu', input_shape=(28 * 28,)))
        neural_network.add(Dense(10, activation='softmax'))

        # specify optimization process
        neural_network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

        # reshape training and test samples for creating 1D feature vectors
        training_samples = training_samples.reshape((60000, 28 * 28))
        training_samples = training_samples.astype('float32') / 255

        test_samples = test_samples.reshape((10000, 28 * 28))
        test_samples = test_samples.astype('float32') / 255

        # one-hot-encode training and test labels
        training_labels = to_categorical(training_labels)
        test_labels = to_categorical(test_labels)

        # train the network
        neural_network.fit(training_samples, training_labels, epochs=5, batch_size=128)

        # evaluate network accuracy on test data
        test_loss, test_accuracy = neural_network.evaluate(test_samples, test_labels)
        print('Test loss: {} - Test accuracy: {}'.format(test_loss, test_accuracy))


if __name__ == '__main__':
    unittest.main()
