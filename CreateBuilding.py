import tkinter as tk
from PIL import ImageTk,Image

import 3DPlane as sp
import cartesianPlane as cp

root = tk.Tk()#lib kinter
root.title("Building Creator")
root.geometry("800x600")  # Width x Height
canvas=tk.Canvas(root,width=800,height=600)
canvas.pack()

#instancias
cplane=cp.cartesianPlane(0,0)
getx=cplane.getX
gety=cplane.getY

i=1

# XandY entry
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root)

if polar==False:
    e1.place(x=15, y=470)
    e2.place(x=215, y=470)



def draw(x,y,a1,a2):# dibujo
    global p1,p2
    line = canvas.create_line(a1,a2,x,y,width=3)
    p1=x
    p2=y
    
def building():
    

#buttons
B = tk.Button(root, text ="Draw Building", command=building).place(x=160,y=420)





root.mainloop()
