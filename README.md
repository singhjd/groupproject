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
   bashCopy code
   pip install -r <requirements.txt>

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

## Configuring the Script ⚙️
Open the **'car_detection.py'** script. Update the following variables to match your dataset:

**CLASS_LABELS:** A dictionary mapping class IDs to class labels.
**IMAGE_PATHS:** A list of image paths you want to perform object detection on.
You can also adjust the following parameters to customize object detection behavior:

**'conf':** The confidence threshold for object detection.
**'iou':** The IoU (Intersection over Union) threshold for object detection.
**'model_type':** Choose from different YOLO variants, such as yolov8n, yolov8m, yolov8l, yolov8x.

## Running the Object Detection ▶️
Execute the script to perform object detection:
bashCopy code
python car_detection.py 
The script will display annotated images with detected objects and print information about the detected objects.

## Dataset 📷
The dataset used in this project is provided in the self-driving-cars directory. It includes images and a CSV file containing bounding box annotations for cars, trucks, persons, bicyclists, and lights. The dataset is available at Kaggle.

## Results 📊
The annotated photos shown while the script is running can be used to observe the outcomes of the item detection process. Around items that are detected, bounding boxes are created, and pertinent details like class labels and confidence ratings are presented.

## Contributing 🤝
We encourage contributions to our endeavor! Please feel free to submit a pull request if you discover any problems or have suggestions for enhancements. Please open an issue first to discuss any significant modifications you'd like to make.

## License 📜

## Acknowledgments 🙏
We would like to thank the designers of the Ultralytics library for their contribution to the simplicity of using YOLO to create object detection.

