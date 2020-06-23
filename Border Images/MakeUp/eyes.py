#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
from PIL import Image, ImageDraw
import face_recognition
import numpy
import tkinter as tk
root= tk.Tk()
canvas1 = tk.Canvas(root, width=150, height=100)
canvas1.pack()
entry1 = tk.Entry (root) 
canvas1.create_window(70,80, window=entry1)
def getSquareRoot ():  
    global name
    name= entry1.get()
button1=tk.Button(root,text="Enter Name",command=getSquareRoot).pack()
root.mainloop()
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif cv2.getWindowProperty('test',0)==-1: 
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}.png".format(name)
        cv2.imwrite(img_name, frame)

# Load the jpg file into a numpy array
        image = face_recognition.load_image_file(img_name)
        os.remove(img_name)

# Find all facial features in all the faces in the image
        face_landmarks_list = face_recognition.face_landmarks(image)

        pil_image = Image.fromarray(image)
        for face_landmarks in face_landmarks_list:
                d = ImageDraw.Draw(pil_image, 'RGBA')


                # Sparkle the eyes
                d.polygon(face_landmarks['left_eye'], fill=(255,20,147, 15))
                d.polygon(face_landmarks['right_eye'], fill=(255,20,147, 15))

                # Apply some eyeliner
                d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=1)
                d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=1)

        #pil_image.show()
        opencv=numpy.array(pil_image)
        #cv2.imshow('Image',opencv)
        frame_RGB=cv2.cvtColor(opencv,cv2.COLOR_BGR2RGB)
        cv2.imshow("image", frame_RGB)
        path="C:\\Users\\HP\\Desktop\\Project\\Save"
        cv2.imwrite(os.path.join(path,img_name),frame_RGB)
        #cv2.imwrite(img_name,frame_RGB)
        print("{} written!".format(img_name))
        #img_counter += 1

cam.release()

cv2.destroyAllWindows() 


# In[ ]:




