from tkinter import *
import time
from PIL import Image, ImageTk

WIDTH = 800
HEIGHT = 500
SIZE = 50
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="grey")
canvas.pack()
color = 'black'
im = Image.open("xmas-walker.png")
x=0
h=34
class Ball:
    def __init__(self):

        cropped = im.crop((x, 44, h, 100))
        tk_im = ImageTk.PhotoImage(cropped)
        self.shape =canvas.create_image(250, 250, image=tk_im)    
        #self.shape = canvas.create_oval(0, 0, SIZE, SIZE, fill=color)
        self.speedx = 9 # changed from 3 to 9
        self.speedy = 9 # changed from 3 to 9
        self.active = True
        self.move_active()

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        x= x +0
        h= h + 34       

        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            tk.after(40, self.move_active) # changed from 10ms to 30ms

ball = Ball()
tk.mainloop()
