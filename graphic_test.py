#https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

from tkinter import *

# Esempio di GUI

# def GUISelf():
#     w1=Tk()
#     w1.title("FEM")
#     # Width, height in pixels
#     f1=Frame(w1, height=500, width=1000)
#     #b = Button(f1, text='asldkf')
#     #b.pack()
#     f1.pack()
#     w1.mainloop()

# GUISelf()


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)


root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_window(500, 400)
create_circle(20, 0, 200, myCanvas)
create_circle(50, 25, 10, myCanvas)
h1 = myCanvas.create_line(0,10,screen_width,0)
root.state("zoomed")
root.mainloop()