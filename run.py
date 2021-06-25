# Inference

import cv2
import numpy as np
from model import model_arch
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


model_weights_file = 'files/hypermodel_weights.h5'


def infer():
    face_detector = cv2.CascadeClassifier('files/haarcascade_frontalface_default.xml')
    mask_detector = model_arch()
    mask_detector.load_weights(model_weights_file)
    vid = cv2.VideoCapture(0)

    while(True):
        _, frame = vid.read()
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(grey, 1.1, 4)
        
        try:
            for (x,y,w,h) in faces:
                crop = cv2.resize(frame[y:y+h, x:x+w], (224,224))
                crop = preprocess_input(crop)                
                crop = crop.reshape(1,224,224,3)
                prediction = mask_detector.predict(crop)
                arg_pred = np.argmax(prediction[0])
                if arg_pred == 1: # With Mask
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1)
                elif arg_pred == 0: # Incorrect Worn Mask
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 1)
                else: # Without Mask
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
        except:
            pass

        cv2.imshow('Frame', frame)

        k = cv2.waitKey(30) & 0xff  # Esc for quiting the app
        if k==27:
            break
    vid.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    infer()