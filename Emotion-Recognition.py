import numpy as np
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Input, Dropout,Flatten, Conv2D
from tensorflow.keras.layers import BatchNormalization, Activation, MaxPooling2D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.utils import plot_model

from IPython.display import SVG, Image
img_size=48
batch_size=64
datagen_train=ImageDataGenerator(horizontal_flip=True)
train_generator=datagen_train.flow_from_directory("train/",
                                                 target_size=(img_size,img_size),
                                                 color_mode='grayscale',
                                                 batch_size=batch_size,
                                                 class_mode='categorical',
                                                 shuffle=True)

datagen_validation=ImageDataGenerator(horizontal_flip=True)
validation_generator=datagen_train.flow_from_directory("test/",
                                                 target_size=(img_size,img_size),
                                                 color_mode='grayscale',
                                                 batch_size=batch_size,
                                                 class_mode='categorical',
                                                 shuffle=True)
from tensorflow.keras.models import load_model
classifier=load_model('my_expression.h5')

from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
#we are starting our web cam
cv2.namedWindow("Emotion",cv2.WINDOW_AUTOSIZE)
webcam=cv2.VideoCapture(0)
def predictor(test_img):
    #test_img=image.load_img(path,target_size=(48,48))
    test_img=image.img_to_array(test_img)
    test_img=np.expand_dims(test_img,axis=0)
    result=classifier.predict(test_img)
    a=result.argmax()
    s=train_generator.class_indices
        #print(s)
    name=[]
    for i in s:
        name.append(i)
    for i in range(len(s)):
        if(i==a):
            q=name[i]
    return q
    
while(True):
    #capture frame by frame
    #ret is boolean veriable
    #frame capture images bcoz vedio is collection of images
    ret,frame=webcam.read()
    haar_face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    g_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces=haar_face_cascade.detectMultiScale(frame,scaleFactor=1.06,minNeighbors=5)
    print("faces found")
    #print(faces)
    for(x,y,w,h) in faces:
        
        crop=g_frame[y:y+h,x:x+w]
        roi=cv2.resize(crop,(48,48))
        path='s.jpg'
        #loaded_model_json = json_file.read()
        #loaded_model = model_from_json(loaded_model_json)
        cv2.imwrite(path,roi)
        name=predictor(roi)
        print(name)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,name,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0),2)
        
        
    cv2.imshow('Emotion',frame)
    if cv2.waitKey(1)== 27:
        # ESC pressed
        print("Escape hit, closing...")
        os.remove(path)
        break
    elif cv2.getWindowProperty('Emotion',0)==-1: 
        os.remove(path)
        break
    
#when everythong is done we realese the capture
webcam.release()
