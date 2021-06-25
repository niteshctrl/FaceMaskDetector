# Face Mask Detector

## Table of Contents
* [Setup and Demo](#Setup-and-Demo)
* [Description](#Description)
* [Dataset](#Dataset)
* [Failure Cases and Further Improvements](#Failure-Cases-and-Further-Improvements)
* [References and Credits](#References-and-Credits)


## Setup and Demo
* To install the dependencies in the current environment:
```
pip install requirements.txt
```
* Unmasked face will be bounded by a 'RED' colored bounding box while masked face with a 'GREEN'. Improperly worn mask will be bounded by 'BLUE' box. Keep the files 'haarcascade_frontalface_default.xml' and 'hypermodel_weights.h5' in the 'files' directory as in the repository and run the mask detector on the webcam by:
```
python run.py 
```


## Description
* The mask detection in this project is a two staged process with first one detecting faces and the second one classifying the detected faces into the three classes:'with_mask', 'without_mask' and 'mask_weared_incorrect'. 
* OpenCV's [HAARCASCADE FRONTAL FACE](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) is used for face detection.
* MobileNetV2 is used as the backend architecture for classification of the detected faces.
* Validation accuracy = 91.76%


## Dataset
* The dataset is available on [Kaggle](https://www.kaggle.com/andrewmvd/face-mask-detection) as this date(Jun 25, 2021) with a total of 853 annotated images in PASCAL VOC format with each image having multiple instances of faces belonging to 3 classes:'with_mask', 'without_mask' and 'mask_weared_incorrect'.
* Upon extraction, a total of 4072 face crops were found.
* A few samples in the dataset:
![Samples](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F793761%2Fd0744f78b0471c0605b98debd7b2d88d%2FUntitled.png?generation=1590132045583855&alt=media "Sample")


## Failure Cases and Further Improvements
* Currently this is a two-staged model with first stage responsible to detect faces and the second for classifying as masked vs unmasked face. The detector often fails to detect the masked face itself as HAARCASCADE FRONTAL FACE(Face Detector) has been trained on unmasked faces. This leads to failure of masked face detection at the end. However unmasked face is mostly detected correctly by the app. 
The possible solution could be to train a single end-to-end object detection model specifying 'masked-face', 'unmasked-face' and 'mask-worn-incorrect' as three objects. This would remove the confusion for the face detector model on masked faces.

## References and Credits:
1. Data Source - [Kaggle](https://www.kaggle.com/andrewmvd/face-mask-detection)
2. [XML parsing in Python](https://www.geeksforgeeks.org/xml-parsing-python/)
