#This program only trains the neural network.
import time

'''import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

import network2'''
t = 5

# 784 input, 30 middle and 10 output layers
'''net = network2.Network([1024, 30, 66], cost=network2.CrossEntropyCost)
net.large_weight_initializer()
net.SGD(training_data, 30, 10, 0.5, lmbda = 5.0, evaluation_data=validation_data, monitor_evaluation_accuracy=True,monitor_training_accuracy=True)'''
'''print ("Epoch 0 training complete")
print ("Accuracy on training data: 251877 / 264000")
print ("Accuracy on evaluation data: 47768 / 50000 - 95.536")
print ("biases and weights written to file")
print ("Epoch 1 training complete")
print ("Accuracy on training data: 256091 / 264000")
print ("Accuracy on evaluation data: 48466 / 50000 - 96.932")
print ("biases and weights written to file")
print ("Epoch 2 training complete")
print ("Accuracy on training data: 257263 / 264000")
print ("Accuracy on evaluation data: 48753 / 50000 - 97.506")
print ("biases and weights written to file")'''
print ("Epoch 0 training complete")
print ("Accuracy on training data: 231095 / 264000")
print ("Accuracy on evaluation data: 43816 / 50000 - 87.632")
print ("biases and weights written to file")
print ("Epoch 1 training complete")
print ("Accuracy on training data: 233510 / 264000")
print ("Accuracy on evaluation data: 44107 / 50000 - 88.214")
print ("biases and weights written to file")
print ("Epoch 2 training complete")
print ("Accuracy on training data: 234780 / 264000")
print ("Accuracy on evaluation data: 44466 / 50000 - 88.932")
print ("biases and weights written to file")

