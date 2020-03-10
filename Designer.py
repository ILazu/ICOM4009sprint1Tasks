import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image

backgroundtxt=" "
Buildingtxt=" "
texture=" "


wall=1;

x1=0
x2=0
y1=0
y2=0
rep=0
z=5

root = tk.Tk()  # lib kinter

root.title("Designer")
root.geometry("1024x700")  # Width x Height

canva = tk.Canvas(root, width=1024, height=650)
canva.config(bg="white")
canva.pack()
label=Label(root,text="Coordinates").place(x=350,y=655)
text_widget = Text(root,width=20,height=1)
text_widget.pack()

####################################second window##############################################

top = Toplevel()#lib kinter
top.title("Map functions")
top.geometry("590x270")  # Width x Height


# XandY entry
Name = tk.Label(top, text="Name").place(x=0, y=40)
x1 = tk.Label(top, text="X1").place(x=0, y=70)
y1 = tk.Label(top, text="Y1").place(x=90, y=70)
x2 = tk.Label(top, text="X2").place(x=180, y=70)
y2 = tk.Label(top, text="Y2").place(x=270, y=70)
z = tk.Label(top, text="Height").place(x=360, y=70)
eb = tk.Entry(top, width=20)
ex1 = tk.Entry(top, width=10)
ey1 = tk.Entry(top, width=10)
ex2 = tk.Entry(top, width=10)
ey2 = tk.Entry(top, width=10)
ez = tk.Entry(top, width=10)


eb.place(x=40, y=40)
ex1.place(x=20, y=70)
ey1.place(x=110, y=70)
ex2.place(x=200, y=70)
ey2.place(x=290, y=70)
ez.place(x=400, y=70)

text_widget1 = tk.Text(top, width=60, height=8)
text_widget1.place(x=15, y=100)

def AddBuilding():
    global Buildingtxt,wall,text_widget1,eb
    temp="Building:  "
    Buildingtxt = "%s%s%s\n" % (Buildingtxt,temp,str(eb.get()))
    wall=1
    text_widget1.delete("1.0", END)


def Submit(): #submit
    global text_widget1,ex1,ex2,ey1,ey2,ez,Buildingtxt,texture,wall
    text_widget1.insert(INSERT, 'x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d\n' % (int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), int(ez.get())))
    line = canva.create_line(int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), width=3)
    temp= 'x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d, Texture '% (int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), int(ez.get()))
    Buildingtxt="%s%s%s\n" % (Buildingtxt,temp,texture)
    wall=wall+1

def Texture():
    global texture
    file_path = filedialog.askopenfilename()
    texture=file_path



def saveMap():
    global backgroundtxt,Buildingtxt
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    textToSave=backgroundtxt+Buildingtxt
    f.write(textToSave)
    f.close()




#buttons
building = tk.Button(top, text="Add Building", command=AddBuilding, width=14).place(x=180, y=35)
submit = tk.Button(top, text ="Submit", command=Submit, width=10).place(x=470, y=70)
texture = tk.Button(top, text="Add Texture", command=Texture, width=14).place(x=290, y=35)
save = tk.Button(top, text="Save", command=saveMap, width=10).place(x=470, y=15)


############################################################################################


def choose_bg():
    global canva,backgroundtxt
    file_path = filedialog.askopenfilename()
    backgroundtxt="Background: "+ file_path + "\n"
    render=ImageTk.PhotoImage(file=file_path)
    img=canva.create_image(0,0,image=render,anchor=NW)
    canva.config(image=img)
    canva.pack()



def pressed1(event):
    global text_widget
    text_widget.delete('1.0',END)
    text_widget.insert(INSERT, 'x = % d, y = % d ' % (event.x, event.y))




## function to be called when button-1 is double clocked
def double_click(event):
    global x1,y1,rep,canva,wall,texture,Buildingtxt
    print('draw x = % d, y = % d' % (event.x, event.y))
    if rep>0:
        line = canva.create_line(x1, y1, event.x, event.y, width=3)
        text_widget1.insert(INSERT, 'x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d\n' % (x1, y1, event.x, event.y, 5))
        temp = 'x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d, Texture ' % ( x1, y1, event.x, event.y, 5)
        Buildingtxt = "%s%s%s\n" % (Buildingtxt,temp, texture)
        rep=0
        wall=wall+1
    else:
        rep=rep+1
        x1=event.x
        y1=event.y




B = Button(root, text ="Choose Background", command=choose_bg).place(x=160,y=660)

# these lines are binding mouse
# buttons with the Frame widget
canva.bind('<Button-1>', pressed1)
canva.bind('<Double 1>', double_click)



root.mainloop()
