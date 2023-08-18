import numpy as np
import pandas as pd
import cv2
from sklearn.utils import shuffle
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from PIL import Image
from IPython.display import display
from ultralytics import YOLO


import warnings
warnings.simplefilter('ignore')

CLASS_LABELS = {
    1: 'car',
    2: 'truck',
    3: 'person',
    4: 'bicyclist',
    5: 'light'
}

IMAGE_PATHS = [
    "/kaggle/input/self-driving-cars/images/1478019960680764792.jpg",
    "/kaggle/input/self-driving-cars/images/1478019964687995430.jpg"
]

def load_dataset(csv_path):
    df = pd.read_csv(csv_path)
    return shuffle(df)

def load_images_and_boxes(df, base_path):
    boxes = {}
    images = {}
    
    for class_id, label in CLASS_LABELS.items():
        first_row = df[df['class_id'] == class_id].iloc[0]
        image = cv2.imread(base_path + first_row['frame'])
        images[class_id] = image
        boxes[class_id] = [
            first_row['xmin'], first_row['xmax'], first_row['ymin'], first_row['ymax']
        ]
    
    return images, boxes


