#!/usr/bin/env python
# coding: utf-8

# In[3]:
import cv2
import os
from PIL import Image
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

#img_counter = 0

while True:
    ret, frame = cam.read()
    image = Image.fromarray(frame)
    p=image.rotate(-18, expand=True)
    opencv=numpy.array(p)
    cv2.imshow('test',opencv)
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
        image = Image.fromarray(frame)
        p=image.rotate(-18, expand=True)
        opencv=numpy.array(p)
        cv2.imshow('image',opencv)
        path="C:\\Users\\HP\\Desktop\\Project\\Save"
        cv2.imwrite(os.path.join(path,img_name),opencv)
        print("{} written!".format(img_name))
        

cam.release()

cv2.destroyAllWindows() 


# In[ ]:




