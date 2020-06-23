#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import os
import pyautogui
import tkinter as tk
root=tk.Tk()
canvas1 = tk.Canvas(root, width=180, height=170)
canvas1.pack()
entry1 = tk.Entry(root) 
entry2 = tk.Entry(root) 
canvas1.create_window(90,80, window=entry1)
canvas1.create_window(90,120, window=entry2)
def getSquareRoot ():  
    global msg
    global name
    msg= entry1.get()
    name=entry2.get()
button1=tk.Button(root,text="Enter Message and Name",command=getSquareRoot).pack()
root.mainloop()
webcam=cv2.VideoCapture(0)
cv2.namedWindow("drawing",cv2.WINDOW_AUTOSIZE)
while webcam.isOpened():
    ret,frame=webcam.read()
    cv2.putText(frame,msg,pyautogui.position(),cv2.FONT_ITALIC,2,(255,160,122),2)

    #length right-side
    #direction change
    cv2.imshow('drawing',frame)
    key=cv2.waitKey(100) & 0xFF
    if key == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif cv2.getWindowProperty('drawing',0)==-1: 
        break
    elif key == 32:
        # SPACE pressed
        img_name = "{}.png".format(name)
        #ret,frame=webcam.read()
        cv2.putText(frame,msg,pyautogui.position(),cv2.FONT_ITALIC,2,(255,160,122),3)

        #cv2.rectangle(frame,(3,3),(637,477),(255,215,185),80)
        #cv2.imshow('drawing',frame)
        cv2.imshow("image", frame)
        path="C:\\Users\\HP\\Desktop\\Project\\Save"
        cv2.imwrite(os.path.join(path,img_name),frame)
        #cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

webcam.release()
cv2.destroyAllWindows()


# In[ ]:




