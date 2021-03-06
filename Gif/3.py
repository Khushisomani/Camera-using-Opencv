import cv2 
import numpy as np 
import os
from moviepy.editor import *
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
video = cv2.VideoCapture(0) 
cv2.namedWindow("Video",cv2.WINDOW_AUTOSIZE)  
cap = cv2.VideoCapture(0)   
# Define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
vid_name="C:\\Users\\HP\\Desktop\\Project\\Save\\"+name+'.avi'
out = cv2.VideoWriter(vid_name, fourcc, 20.0, (640, 480)) 
j=0
while True: 
    # reads frames from a camera  
    # ret checks return at each frame 
    ret, frame = cap.read()  
    out.write(frame)  
      
    # The original input frame is shown in the window  
    cv2.imshow('Video', frame)  
    j+=1
  
      
    # Wait for 'a' key to stop the program  
    if cv2.waitKey(1)==27: 
        break
    elif cv2.getWindowProperty('Video',0)==-1: 
        break
    elif j>60:
        break
  
# Close the window / Release webcam 
cap.release() 
out.release()  
  
# De-allocate any associated memory usage  
cv2.destroyAllWindows() 
kris_sven = (VideoFileClip(vid_name)
             .subclip(0,3)
             .resize(0.5)
             .crop(x1=50,x2=400)) # remove left-right borders
s="C:\\Users\\HP\\Desktop\\Project\\Save\\"+name+'.gif'
kris_sven.write_gif(s)
os.remove(vid_name)