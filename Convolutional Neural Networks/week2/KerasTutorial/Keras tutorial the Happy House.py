# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 16:35:19 2018

@author: ZSQ
"""

"""
Keras tutorial - the Happy House
"""

import numpy as np
from keras import layers
from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
from keras.layers import AveragePooling2D, MaxPooling2D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
from keras.models import Model
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
import pydot
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
from kt_utils import *

import keras.backend as K
K.set_image_data_format('channels_last')
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

import os

os.environ["CUDA_VISIBLE_DEVICES"] = "2" 

"""
-------------------------------------------------------------------------------
Stage 1 : The Happy House
-------------------------------------------------------------------------------
"""
X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset()

# Normalize image vectors
X_train = X_train_orig/255.
X_test = X_test_orig/255.

# Reshape
Y_train = Y_train_orig.T
Y_test = Y_test_orig.T

print ("number of training examples = " + str(X_train.shape[0]))
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_train shape: " + str(X_train.shape))
print ("Y_train shape: " + str(Y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))


"""
-------------------------------------------------------------------------------
Stage 2: Building a model in Keras
-------------------------------------------------------------------------------
"""

def HappyModel(input_shape):
    """
    Implementation of the HappyModel.
    
    Arguments:
    input_shape -- shape of the images of the dataset

    Returns:
    model -- a Model() instance in Keras
    """
    
    ### START CODE HERE ###
    # Feel free to use the suggested outline in the text above to get started, and run through the whole
    # exercise (including the later portions of this notebook) once. The come back also try out other
    # network architectures as well. 
        # Define the input placeholder as a tensor with shape input_shape. Think of this as your input image!
    X_input = Input(input_shape)
    
    # Zero-Padding: pads the border of X_input with zeroes
    X = ZeroPadding2D((3, 3))(X_input)
    
    # CONV -> BN -> RELU Block applied to X
    X = Conv2D(32, (7, 7), strides=(1, 1), name = 'conv0')(X)
    X = BatchNormalization(axis= 3, name='bn0')(X)
    X = Activation('relu')(X)
    
    # MAXPOOL
    X = MaxPooling2D((2, 2), name='max_pool')(X)
    
    # FLATTEN X (means convert it to a vector) + FULLYCONNECTED
    X = Flatten()(X)
    X = Dense(1, activation='sigmoid', name='fc')(X)
    
    # Create model. This creates your Keras model instance, you'll use this instance to train/test the model.
    model = Model(inputs = X_input, outputs=X, name='HappyModel')
    
    return model


### START CODE HERE ### (1 line)
happyModel = HappyModel((64,64,3))
### END CODE HERE ###

### START CODE HERE ### (1 line)
happyModel.compile(optimizer='adam', loss="binary_crossentropy", metrics=['accuracy'])
### END CODE HERE ###   

### START CODE HERE ### (1 line)
happyModel.fit(x=X_train, y=Y_train, epochs=10, batch_size=20)
### END CODE HERE ###  
    
    
### START CODE HERE ### (1 line)
preds = happyModel.evaluate(x=X_test, y=Y_test,)
### END CODE HERE ###
print()
print ("Loss = " + str(preds[0]))
print ("Test Accuracy = " + str(preds[1]))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


