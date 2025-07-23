# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:46:22 2024

@author: admin
"""

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
loaded_model = load_model('C:/Users/HP/Desktop/Banana_Data/fruit_classifier_final.h5')

# Function to load and preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(64,64))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0
    return img

# Make predictions
def predict_image(img_path):
    img = preprocess_image(img_path)
    prediction = loaded_model.predict(img)
    return prediction

# Example usage:
image_path = 'C:/Users/HP/Downloads/fraise khdr.jpg'
prediction = predict_image(image_path)
print(prediction)  # This will give you the prediction result