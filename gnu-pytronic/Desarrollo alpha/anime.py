# -*- coding: Utf-8 -*-
from tkinter import *
from tkinter import ttk
import random 


WIDTH = 300
HEIGHT =70


def random_speed(): 
    return random.choice([-1, 1]) * random.randrange(2, 4) 


def random_image(canvas, image): 
    """Place `image` on `canvas` with random pos and speed. 
    """ 
    return Image( 
        canvas, 
        image, 
        random.randrange(WIDTH-image.width()), 
        random.randrange(HEIGHT-image.height()), 
        random_speed(), 
        random_speed(), 
    ) 


class Image(object): 
    def __init__(self, canvas, image, x, y, vx, vy): 
        self.canvas = canvas 
        self.image = image 
        self.x = x 
        self.y = y 
        self.vx = vx 
        self.vy = vy 
        self.w = image.width() 
        self.h = image.height() 
        self.id = canvas.create_image(x, y, image=image, anchor=NW) 

    @property 
    def right(self): 
        return self.x + self.w 

    @property 
    def bottom(self): 
        return self.y + self.h 

    def move(self): 
        self.x += self.vx 
        self.y += self.vy 
        self.canvas.move(self.id, self.vx, self.vy) 
        if self.bottom > HEIGHT or self.y < 0: 
            self.vy = - self.vy 
        if self.right > WIDTH or self.x < 0: 
            self.vx = - self.vx 


def move(): 
    for image in images: 
        image.move() 
    root.after(20, move) 


if __name__ == "__main__": 
    root = Tk()
    ball = PhotoImage(file="/home/ronal/git/GNU-Pytronic/gnu-pytronic/Desarrollo alpha/c.gif") 
    canvas = Canvas(root, width=WIDTH, height=HEIGHT) 
    canvas.pack() 
    images = [random_image(canvas, ball) for _ in range(1)] 
    move() 
    ventana =Tk()
    ventana.mainloop()

