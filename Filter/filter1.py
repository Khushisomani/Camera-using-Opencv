#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os

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
webcam=cv2.VideoCapture(0)
cv2.namedWindow("drawing",cv2.WINDOW_AUTOSIZE)
while True:
    ret,frame=webcam.read()
    frame_RGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    #length right-side
    #direction change
    cv2.imshow('drawing',frame_RGB)
    key=cv2.waitKey(1) 
    if key%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif cv2.getWindowProperty('drawing',0)==-1: 
        break
    elif key%256 == 32:
        # SPACE pressed
        width1=640
        height1=480
        dim1=(width1,height1)
        resized1 = cv2.resize(frame_RGB, dim1)
        img_name = "{}.png".format(name)
        cv2.imshow('image',resized1)
        path="C:\\Users\\HP\\Desktop\\Project\\Save"
        cv2.imwrite(os.path.join(path,img_name),frame_RGB)
        #cv2.imwrite(img_name, frame_RGB)
        print("{} written!".format(img_name))
webcam.release()
cv2.destroyAllWindows()


# In[ ]:




