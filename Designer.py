import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image

backgroundtxt=""
Buildingtxt=""



x1=0
x2=0
y1=0
y2=0
rep=0
z=5
#exec(open("./textfile.py").read())
root = tk.Tk()  # lib kinter
root.title("Designer")
root.geometry("1028x768")  # Width x Height
canva = tk.Canvas(root, width=1028, height=720)
canva.config(bg="white")
canva.pack()
label=Label(root,text="Coordinates").place(x=350,y=725)
text_widget = Text(root,width=20,height=1)
text_widget.pack()



def choose_bg():
    global canva,backgroundtxt
    file_path = filedialog.askopenfilename()
    backgroundtxt="Background: "+ file_path + "\n"
    render=ImageTk.PhotoImage(file=file_path)
    img=canva.create_image(0,0,image=render,anchor=NW)
    canva.config(image=img)
    canva.pack()

def addBuilding():
    global Buildingtxt
    Buildingtxt="Building:"+"stefani"+"\n"
def pressed1(event):
    global text_widget
    text_widget.delete('1.0',END)
    text_widget.insert(INSERT, 'x = % d, y = % d ' % (event.x, event.y))


# function to be called when button-3 of mouse is pressed
def pressed3(event):
    print('Button-3 pressed at x = % d, y = % d' % (event.x, event.y))


## function to be called when button-1 is double clocked
def double_click(event):
    global x1,y1,rep,canva
    print('draw x = % d, y = % d' % (event.x, event.y))
    if rep>0:
        line = canva.create_line(x1, y1, event.x, event.y, width=3)
        rep=0
    else:
        rep=rep+1
        x1=event.x
        y1=event.y

def saveMap():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    textToSave =backgroundtxt+Buildingtxt
    f.write(textToSave)
    f.close()


B = Button(root, text ="Choose Background", command=choose_bg).place(x=160,y=730)

# these lines are binding mouse
# buttons with the Frame widget
canva.bind('<Button-1>', pressed1)
canva.bind('<Button-3>', pressed3)
canva.bind('<Double 1>', double_click)



root.mainloop()