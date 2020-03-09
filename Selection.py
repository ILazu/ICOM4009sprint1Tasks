import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image


class interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1028x768")
        self.config(bg="green" ,bd=25,relief="sunken")
        self.myframe=Frame(self)
        self.myframe.pack()
        self.myframe.config(bg="grey", width=1000, height=750)

        #canvas = tk.Canvas(bg="grey",width=400,height=400)
        #canvas.pack()
        self.B1 = tk.Button(self, text="StartGame", width=16)
        self.B1.place(x=750, y=600)
        self.B1.bind('<Button-1>', self.hide_me)

        self.B2 = tk.Button(self, text="Designer", width=16)
        self.B2.place(x=750, y=650)
        self.B2.bind('<Button-1>',self.hide_me)




    def hide_me(self, event):
        self.Designer()
        self.B1.place_forget()
        self.B2.place_forget()
    def Designer(self):
        self.destroy()
        exec(open("./Designer.py").read())

    def saveMap(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        textToSave = "something"  # placeholder to avoid errors
        f.write(textToSave)
        f.close()


        

    def StartGame(self):  # re center and delete
            print("not yet")


if __name__ == "__main__":
    interfaz().mainloop()
