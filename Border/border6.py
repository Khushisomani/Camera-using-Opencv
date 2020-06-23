#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import os
from PIL import Image, ImageDraw
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
back = cv2.imread('C:\\Users\\HP\\Desktop\\Project\\Border Images\\3.jpg',1) 
cam = cv2.VideoCapture(0)
cv2.namedWindow("test",cv2.WINDOW_AUTOSIZE)
while True:
    ret, frame = cam.read()
    width1=640
    height1=480
    dim1=(width1,height1)
    resized1 = cv2.resize(back, dim1)
    img = cv2.addWeighted(resized1, 0.5, frame, 0.6, 2) 
    cv2.imshow("test",img)
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
        #cv2.imwrite(img_name, frame)

        width1=640
        height1=480
        dim1=(width1,height1)
        resized1 = cv2.resize(back, dim1)
    

        img = cv2.addWeighted(resized1, 0.5, frame, 0.5, 2) 
  
        # Show the image 
        cv2.imshow('image', img)        
        
        path="C:\\Users\\HP\\Desktop\\Project\\Save"
        cv2.imwrite(os.path.join(path,img_name),img)
        #cv2.imwrite(img_name,img)
        print("{} written!".format(img_name))
        #img_counter += 1

cam.release()

cv2.destroyAllWindows() 


# In[ ]:




