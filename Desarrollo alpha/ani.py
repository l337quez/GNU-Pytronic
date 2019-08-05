# -*- coding: Utf-8 -*-
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

im = Image.open("xmas-walker.png")
# x=0
# y=0
# h=34 #alto
# a=100 #ancho

# class Image(object): 
    # def __init__(self, canvas, image, x, y, vx, vy): 
        # self.canvas = canvas 
        # self.image = image 
        # self.x = x 
        # self.y = y 
        # self.vx = vx 
        # self.vy = vy 
        # self.w = image.width() 
        # self.h = image.height() 
        # self.id = canvas.create_image(x, y, image=image, anchor=NW) 



# # caminar hacia la derecha
# def move ():
	# for x in range(0, 5):
		# cropped = im.crop((x, 44, h, 100))
		# tk_im = ImageTk.PhotoImage(cropped)
		# canvas.create_image(250, 250, image=tk_im)
		# time.sleep(1)
		# x=34 + x
		# h=34 + h


# if __name__ == "__main__": 
	# root = Tk()
	# ball = PhotoImage(file="/home/ronal/git/GNU-Pytronic/gnu-pytronic/Desarrollo alpha/c.gif") 
	# canvas = Canvas(root, width=WIDTH, height=HEIGHT) 
	# canvas.pack() 
	# images = [random_image(canvas, ball) for _ in range(1)] 
	# move() 
	# ventana =Tk()
	# ventana.mainloop()

def actualizar ():
	x=34 + x
	h=34 + h
	return x

for a in range(0, 5):
	if a==0:
		x=0
		h=34
		
	cropped = im.crop((x, 44, h, 100))
	tk_im = ImageTk.PhotoImage(cropped)
	canvas.create_image(250, 250, image=tk_im)
	actualizar()


ventana =Tk()
Boton_calcular=Button(ventana, text= "Calculate", command= actualizar).place(x=55, y=158)

ventana.mainloop()
