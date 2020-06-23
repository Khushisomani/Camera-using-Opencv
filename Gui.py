def Camera():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Camera.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def Video():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Video.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def border1():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Border\\border1.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def border2():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Border\\border2.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def border3():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Border\\border3.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def border4():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Border\\border4.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def border5():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Border\\border5.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def border6():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Border\\border6.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def border7():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Border\\border7.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def filter1():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Filter\\filter1.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def filter2():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Filter\\filter2.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def filter3():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Filter\\filter3.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def filter4():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Filter\\filter4.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def filter5():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Filter\\filter5.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def filter6():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Filter\\filter6.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def filter7():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Filter\\filter7.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def Face():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\MakeUp\\Face.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def Eyebrow():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\MakeUp\\eyebrow.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def Eyes():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\MakeUp\\eyes.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def Lips():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\MakeUp\\lips.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def gif1():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Gif\\1.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def gif2():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Gif\\3.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def Emotion():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Emotion-Recognition.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad
def Text1():
    import tkinter as tk
    import os
    filename = 'python C:\\Users\\HP\\Desktop\\Project\\Text.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('jupyter notebook '+filename) #Open in notepad

def print_path():
    import tkinter
    from tkinter import filedialog
    f = tkinter.filedialog.askopenfilename(
        parent=mainwindow, initialdir='C:\\Users\\HP\\Desktop\\Project\\Save',
        title='Choose file',
        filetypes=[('png images', '.png')]
        )
from tkinter import *
import tkinter as tk

mainwindow=Tk()

def window():
    Toplevel(mainwindow)
    

'''root = tk.Tk()
tk.Button(root, text="Python File", command=callback).pack()'''

mainwindow.geometry("570x390")
# create the canvas, size in pixels

canvas = Canvas(width=200,height=250,bg='snow')

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

# load the .gif image file
img = PhotoImage(file="C:\\Users\\HP\\Desktop\\Project\\1.gif")    

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(40, 60,anchor=NW,image=img)

#rightFrame=Frame(mainwindow)
#rightFrame.grid(row=50,column=10)

button1=Button(mainwindow,text='Camera',bg='azure',padx=7,activebackground='white',command=Camera)
button1.pack(side=tk.LEFT)
button2=Button(mainwindow,text='Video',bg='gray',padx=7,command=Video)
button2.pack(side=tk.LEFT)
button3= Menubutton(mainwindow,text='Border',bg='beige',justify='center',padx=10,bd=3)
button3.pack(side=tk.LEFT)
button3.menu =  Menu (button3, tearoff = 0 )
button3["menu"] =button3.menu
button3.menu.add_checkbutton ( label="border1",command=border1)
button3.menu.add_checkbutton ( label="border2",command=border2)
button3.menu.add_checkbutton ( label="border3",command=border3)
button3.menu.add_checkbutton ( label="border4",command=border4)
button3.menu.add_checkbutton ( label="border5",command=border5)
button3.menu.add_checkbutton ( label="border6",command=border6)
button3.menu.add_checkbutton ( label="border7",command=border7)
button4= Menubutton(mainwindow,text='Filter',bg='darkgray',justify='center',padx=10,bd=3)
button4.pack(side=tk.LEFT)
button4.menu =  Menu (button4, tearoff = 0 )
button4["menu"] =button4.menu
button4.menu.add_checkbutton ( label="filter1",command=filter1)
button4.menu.add_checkbutton ( label="filter2",command=filter2)
button4.menu.add_checkbutton ( label="filter3",command=filter3)
button4.menu.add_checkbutton ( label="filter4",command=filter4)
button4.menu.add_checkbutton ( label="filter5",command=filter5)
button4.menu.add_checkbutton ( label="filter6",command=filter6)
button4.menu.add_checkbutton ( label="filter7",command=filter7)
button5= Menubutton(mainwindow,text='MakeUp',bg='pink',justify='center',padx=10,bd=3)
button5.pack(side=tk.LEFT)
button5.menu =  Menu (button5, tearoff = 0 )
button5["menu"] =button5.menu
button5.menu.add_checkbutton (label="Face",command=Face)
button5.menu.add_checkbutton ( label="Eyebrow",command=Eyebrow)
button5.menu.add_checkbutton ( label="Eyes",command=Eyes)
button5.menu.add_checkbutton ( label="Lips",command=Lips)
button6= Menubutton(mainwindow,text='Gif',bg='teal',justify='center',padx=10,bd=3)
button6.pack(side=tk.LEFT)
button6.menu =  Menu (button6, tearoff = 0 )
button6["menu"] =button6.menu
button6.menu.add_checkbutton ( label="Half-Freeze",command=gif1)
button6.menu.add_checkbutton ( label="Repeat",command=gif2)
button7=Button(mainwindow,text='Emotion-Recognition',bg='lavender',padx=7,command=Emotion)
button7.pack(side=tk.LEFT)
button8=Button(mainwindow,text='Text',bg='Teal',padx=7,command=Text1)
button8.pack(side=tk.LEFT)
button9=Button(mainwindow,text='Photos',bg='linen', padx=7,command=print_path)
button9.pack(side=tk.LEFT)
mainwindow.mainloop()