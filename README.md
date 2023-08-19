# groupproject
Projects
# Car Detection using YOLO 🚗👁️

## Table of Contents
- [Introduction](#introduction) 📝
- [Installation](#installation) 💻
  - [Requirements](#requirements) 📦
  - [Installation Steps](#installation-steps) 🚀
- [Usage](#usage) 🚗
  - [Preparing Your Dataset](#preparing-your-dataset) 📂
  - [Configuring the Script](#configuring-the-script) ⚙️
  - [Running the Object Detection](#running-the-object-detection) ▶️
- [Dataset](#dataset) 📷
- [Results](#results) 📊
- [Contributing](#contributing) 🤝
- [License](#license) 📜
- [Acknowledgments](#acknowledgments) 🙏

  
## Introduction 📝
The Car Detection Using YOLO project is pleased to have you. Using the YOLO (You Only Look Once) object detection approach, this repository illustrates how to carry out automobile detection. For effective implementation, the project makes use of the Ultralytics library. The objective of object detection is to recognize and localize things of interest inside photographs. An important task in applications like autonomous driving, traffic analysis, and surveillance, car detection is the subject of this study.

## Installation 💻
### Requirements 📦
To run this project, you need:
- Python 3.x
- The following Python libraries:
  - numpy 🧮
  - pandas 🐼
  - cv2 (OpenCV) 📷
  - matplotlib 📈
  - PIL (Pillow) 🖼️
  - ultralytics 🚀
 
  
### Installation Steps 🚀
1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```bash
   git clone <https://github.com/singhjd/groupproject.git>

### Install Dependencies:
 Install the required Python packages using the following command:
 ```bash
pip install -r requirements.txt

### Download Pre-trained YOLO Weights:
Download the pre-trained YOLO weights file (e.g., yolov8l.pt) from the official Ultralytics repository and place it in the project directory.

## Usage 🚗
## Preparing Your Dataset 📂
Organize your dataset by placing images and a corresponding CSV file with bounding box annotations in the appropriate directories.
Ensure that your dataset directory structure looks like:
/car-detection-yolo
|-- dataset
   |-- images
      |-- image1.jpg
      |-- image2.jpg
      ...
   |-- annotations.csv



## Configuring the Script
Open the car_detection.py script.
Update the following variables to match your dataset:
CLASS_LABELS: A dictionary mapping class IDs to class labels.
IMAGE_PATHS: A list of image paths you want to perform object detection on.
You can also adjust the following parameters to customize object detection behavior:
conf: The confidence threshold for object detection. By default, it is set to 0.5, but you can vary it based on your needs. Increasing it might result in fewer detections with higher confidence.
iou: The IoU (Intersection over Union) threshold for object detection. Set to 0.7 by default, it determines the overlap required for two bounding boxes to be considered the same object. Adjust it to control the sensitivity of duplicate detection.
model_type: You have the option to choose from different YOLO variants, such as yolov8n, yolov8m, yolov8l, yolov8x. In this project, we've used yolov8l as it provided satisfactory results. You can experiment with these variants to find the one that suits your task best.
## Running the Object Detection
Execute the script to perform object detection:
bashCopy code
python car_detection.py 
The script will display annotated images with detected objects and print information about the detected objects.
## Dataset
The dataset used in this project is provided in the self-driving-cars directory. It includes images and a CSV file containing bounding box annotations for cars, trucks, persons, bicyclists, and lights.
The dataset is available at Kaggle Dataset Link.
## Object Detection
The object detection process is performed using the YOLO (You Only Look Once) model implemented using the Ultralytics library. YOLO is known for its real-time object detection capabilities. The code provided handles loading the model, processing images, and detecting objects.
## Results
The results of the object detection process can be observed in the annotated images displayed during script execution. Bounding boxes are drawn around detected objects, and relevant information such as class labels and confidence scores is printed.

## Contributing
Contributions to this project are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request. For major changes, please open an issue first to discuss your proposed changes.
## License
This project is licensed under the MIT License.
## Acknowledgments
We would like to acknowledge the creators of the Ultralytics library for their contribution to the ease of implementing object detection using YOLO.
