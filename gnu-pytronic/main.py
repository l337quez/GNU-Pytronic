# iconos
# https://material.io/resources/icons/?icon=bookmark_border&style=baseline
import sys
import os.path, time
import re
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets,QtGui
from PySide2.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from PySide2.QtGui import *



# class MainWindow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         #QMainWindow.__init__(self)
#         super(MainWindow, self).__init__(*args, **kwargs)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowIcon(QIcon('save-impression.png')) 
        layout = QGridLayout()
        #layout = QHBoxLayout() #HOrizontal
        self.setLayout(layout)
        label1 = QLabel("Widget in Tab 1.")
        label2 = QLabel("Widget in Tab 2.")
        pushButton1 = QPushButton("PyQt5 button")
        tabwidget = QTabWidget()
        home=tabwidget.addTab(Home(), "Casa") #Home
        help=tabwidget.addTab(Help(), "Ayuda") #Help
        #agregamos los iconos a las pestañas
        tabwidget.setTabIcon(home, QtGui.QIcon('home.png'))
        tabwidget.setTabIcon(help, QtGui.QIcon('help.png'))

        #layout.addWidget(tabwidget, 0, 0)
        layout.addWidget(tabwidget)
        

 
 
 
 
############ PESTAÑA HOME
        
class Home(QWidget):
    def __init__(self):
        super().__init__()
        
        
        ############  Label
        pixmap = QtGui.QPixmap("Sources/banner.png")
        label = QtWidgets.QLabel()
        label.setPixmap(pixmap)    
        label.show()



        

        #SETIAMOS LOS OBJETOS EN EL LAYOUT
        # LeftToRight, RightToLeft, TopToBottom, BottomToTop, Down, Up 

        hbox = QHBoxLayout(self) #HOrizontal
        hbox.addWidget(label)


        #https://www.tutorialspoint.com/pyqt/pyqt_qboxlayout_class.htm


        #vbox.addLayout(hbox)
     



        #layout2.addWidget(b_Valtura)
        #layout2.addWidget(self.label)
        #layout2.addStretch(0)
        #layout1.addLayout(layout2)
        #layout1.addLayout(layout2)#siguiente fila
        #layout1.addWidget(a_Capa)
        #layout1.addLayout(layout2)#siguiente fila
        #layout1.addWidget(self.line)
        #layout1.addLayout(layout2)#siguiente fila
        #layout1.addWidget(n_capa)
        #layout1.addLayout(layout2)#siguiente fila
        #layout1.addWidget(self.line1)
        #layout1.addLayout(layout2)#siguiente fila
        #self.setLayout(layout2)
        #layout1.addLayout(layout2,3) #siguiente fila
        #layout1.addWidget(b_infoc)
        #layout1.addWidget(b_VerInfo)
        #layout1.addWidget(self.b_rec)
        #layout2.addLayout(layout1)



        #self.setLayout(layout1)
        

        # layout = QGridLayout()
        # layout.addWidget(self.button)
        # layout.addWidget(self.label_ng,0,1)
        # layout.addWidget(label)
        # layout.addWidget(a_Capa,2,0)
        # layout.addWidget(self.line,2,1)
        # layout.addWidget(n_capa,2,2)
        # layout.addWidget(self.line1,2,3)
        # layout.addWidget(b_Valtura,3,0)
        # layout.addWidget(b_infoc,3,1)
        # layout.addWidget(b_VerInfo,4,0)
        # layout.addWidget(self.b_rec,4,1)
        # self.setLayout(layout)
        
        
        
        
############  FUNCIONES
        
#FUNCION CARGAR EL ARCHIVO GCODE        
    def load_file_gcode(self):
        #cambiamos el icono del boton
        self.button.setIcon(QIcon('open.png'))
        
        fname = QtWidgets.QFileDialog.getOpenFileName(self,filter="GCODE Files (*.gcode)")
        ruta_load=fname[0]
        ruta_load_str=''.join(ruta_load)
        #print(ruta_load)
        #leemos el archivo GCODE
        leer_file=open(ruta_load,'r')
        texto=leer_file.read()
        leer_file.close()
        
        #w+ son permisos de escritura  o de write
        #creamos el txt como archivo oculto antecediendo el punto
        RUTA= open('.ruta.txt', 'w+')
        #escribimos en el txt
        RUTA.write(ruta_load_str)
        RUTA.close()
        
        #MOSTRAMOS UNA ETIQUETA CON EL NOMBRE DEL ARCHIVO SELECCIONADO
        #r+ para leer
        RUTA= open('.ruta.txt', 'r+')
        #Leemos en el txt
        ngcode= RUTA.read()
        RUTA.close()
        print(ngcode)
        p_ngcode=ngcode.rindex("/")
        self.label_ng.setText(str(ngcode[p_ngcode+1:]))
        #.rindex("/") #posicion donde esta el ultimo / y luego sigue el nombre   









############ PESTAÑA HELP    
class Help(QWidget):
    def __init__(self):
        super().__init__()
        title= QLabel("Acerca de")
        title.setStyleSheet("QLabel { font-weight: bold;} ")
        version= QLabel("GNU SAP3D  Version Beta 0.3 ")
        devp= QLabel("Desarrollador: ")
        name= QLabel("Ronal Forero")
        mail= QLabel("L337.ronald@gmail.com")
        lic=QLabel("Licencia: ")
        lic_type=QLabel("GPL-V3")
        title1= QLabel("Empaquetadores")
        title1.setStyleSheet("QLabel { font-weight: bold;} ")
        title_w=QLabel("Windows (.exe): ")
        exe=QLabel("Ernesto Burgos")
        exe_mail=QLabel("hdst.bur@gmail.com")
        nada=QLabel("   ")
        #Acomodamos los Widfet con la malla (grid)
        layout = QGridLayout()
        #layout = QHBoxLayout() #HOrizontal




        #Agregamos los componentes
       #layout.addWidget(objeto,int fila, int columna,Qt::Alignment alignment = 0)        
        layout.addWidget(title,0,0)
        layout.addWidget(version)
        layout.setColumnMinimumWidth (2, 0)
        layout.addWidget(devp)
        #setColumnStretch(int column, int stretch)
        #setRowStretch(int row, int stretch)
        #layout.setRowStretch(1,2)
        #layout.setColumnStretch(2, 2)
        layout.addWidget(name,2,1)
        layout.addWidget(mail,3,1)
        layout.addWidget(lic,4,0)
        layout.addWidget(lic_type)
        layout.addWidget(title1,5,0)
        layout.addWidget(title_w,6,0)
        layout.addWidget(exe,6,1)
        layout.addWidget(exe_mail,7,1)
        layout.setRowStretch(8,1)
        layout.setColumnStretch(8, 22)
        self.setLayout(layout)        
        




app = QApplication(sys.argv)
screen = Window()
# Tamaño de la ventana
screen.resize(600,450)
screen.setWindowTitle("GNU Save Printing 3D") 
screen.show()
sys.exit(app.exec_())






