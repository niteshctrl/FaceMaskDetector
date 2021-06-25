# Face Mask Detector

## Table of Contents
* [Setup and Demo](#Setup-and-Demo)
* [Description](#Description)
* [Dataset](#Dataset)
* [Failure Cases and Further Improvements](#Failure-Cases-and-Further-Improvements)
* [References and Credits](#References-and-Credits)

## Setup and Demo
* To install the dependecies in the current environment
```
pip install requirements.txt
```

* Run the mask detector on the webcam
```
python run.py 
```

## Description

## Dataset

## Failure Cases and Further Improvements
* The detector often fails to detect the masked face itself as HAARCASCADE FRONTAL FACE(Face Detector) has been trained on unmasked faces. This leads to failure of masked face detection at the end. However unmasked face is mostly detected correctly by the app. 
The possible solution could be to train a single end-to-end object detection model specifying 'masked-face', 'unmasked-face' and 'mask-worn-incorrect' as three objects. This would remove the confusion for the face detector model on masked faces.

## References and Credits:
1. Data Source - [Kaggle](https://www.kaggle.com/andrewmvd/face-mask-detection)
2. [XML parsing in Python](https://www.geeksforgeeks.org/xml-parsing-python/)
