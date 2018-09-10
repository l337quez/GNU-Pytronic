#https://openclassrooms.com/forum/sujet/animer-des-sprite-17872
import os
import time
from tkinter import *
from PIL import Image, ImageTk
 
animation= Tk()
canvas= Canvas(animation, width= 800, height=600)
canvas.pack()
#canvas.create_polygon(10,10,10,10,60,50,35,35) 

# load the .gif image file
gif1 = PhotoImage(file="/home/ronal/git/GNU-Pytronic/gnu-pytronic/Desarrollo alpha/c.gif")

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image=gif1, anchor=NW)

for x in range (0, 140):
	canvas.move(1,5,0)
	animation.update()
	time.sleep(0.05)
    self.subframe = tkinter.Frame(master, height=50, borderwidth=2, relief='groove')
	self.subframe.pack(side='bottom')
	self.subframe2 = tkinter.Frame(self.subframe, height=50, borderwidth=2, relief='raised')
	self.subframe2.pack(side='right')
 
for x in range (0, 140):
	canvas.move(1,-5,0)
	animation.update()
	time.sleep(0.05)


def move_sprite(self, sprite, position):
	"""Moves a piece to destination, resetting origin square to empty"""
	file, rank = Ply.position_to_tuple(position)
	
	self.canvas.coords(sprite,  self.square_size * (file - 1), self.square_size * (rank - 1))
	self.sprites[position] = sprite

def clear_sprite(self, sprite):
	"""Removes sprite from canvas"""
	self.canvas.delete(sprite)


move_sprite
move_sprite
self.move_sprite(self.sprites[self.pickup], self.pickup)
