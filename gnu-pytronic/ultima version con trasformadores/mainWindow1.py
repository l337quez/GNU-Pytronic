import tkinter as tk
import os
import sys
import shlex, subprocess
import re
import webbrowser
from tkinter import filedialog
#Estilos para tkinter
from ttkthemes import ThemedStyle
#para abrir ventan transformadores
#import transformadores as sW

import secondWindow as sW

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Titulo de la ventana
        self.title("GNU Pytronic")
        #icono del software
        #self.iconbitmap("pytronics.ico")
        #Geometria y posicion de la ventana
        self.geometry("600x450+120+120")


        #Organizando las pestañas
        notebook=ttk.Notebook(ventana)
        notebook.pack(fill='both',expand='yes')
        pestana=ttk.Frame(notebook)
        pestana0=ttk.Frame(notebook)
        pestana1=ttk.Frame(notebook)
        pestana2=ttk.Frame(notebook)
        pestana3=ttk.Frame(notebook)
        notebook.add(pestana,text='Home')
        notebook.add(pestana0,text='Capacitors')
        notebook.add(pestana1,text='Resistors')
        notebook.add(pestana2,text='More...')
        notebook.add(pestana3,text='About')


        noteStyler = ttk.Style()
        noteStyler.configure("TNotebook", background='gray', borderwidth=0)

        COLOR_3 = 'black'
        COLOR_4 = '#2E2E2E'
        COLOR_5 = '#8A4B08'
        COLOR_6 = '#DF7401'
        noteStyler.configure("TNotebook.Tab", background="gray", foreground=COLOR_3, lightcolor=COLOR_6, borderwidth=2)
        
        
        tk.Button(self, text = "New Window", command = self.new_window).pack()
        tk.Button(self, text = "Close Window", command = self.close).pack()

        self._second_window = None

    def new_window(self):
        # This prevents multiple clicks opening multiple windows
        if self._second_window is not None:
            return

        self._second_window = sW.SubWindow(self)

    def close(self):
        # Destory the 2nd window and reset the value to None
        if self._second_window is not None:
            self._second_window.destroy()
            self._second_window = None







#########################################################################
# Llammos a la clase principal

if __name__ == '__main__':
    ventana = MainWindow()
    ventana.resizable(False, False)

    #Tema tkinter para los objetos
    style = ThemedStyle(ventana)
    style.set_theme("alt")
    
    ventana.mainloop()

