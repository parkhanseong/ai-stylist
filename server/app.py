from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin
import tensorflow as tf
import os
import cv2
import PIL
from PIL import Image
import numpy as np
# import os
import matplotlib.pyplot as plt
app = Flask(__name__)
CORS(app)

current_dir = os.path.dirname( os.path.abspath( __file__ ) )

@app.route("/", methods=['GET'])
def index():
    return jsonify(' >>> index >> ')

@app.route("/predict", methods=['POST'])
def predict(path, img_path):
    classes = []
    model = tf.keras.models.load_model(path)
    return classes[prediction[0]]

if __name__ == '__main__':
    app.run(port=5000)