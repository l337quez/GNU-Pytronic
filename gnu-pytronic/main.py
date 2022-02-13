# iconos
# https://material.io/resources/icons/?icon=bookmark_border&style=baseline

from pymongo import MongoClient

import sys
import os.path, time
import re
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets,QtGui
from PySide2.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox, QGridLayout, QGroupBox
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon 
from PySide2.QtGui import *
import json


# class MainWindow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         #QMainWindow.__init__(self)
#         super(MainWindow, self).__init__(*args, **kwargs)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowIcon(QIcon('pytronics.png')) 
        layout = QGridLayout()
        #layout = QHBoxLayout() #HOrizontal
        self.setLayout(layout)
        #label1 = QLabel("Widget in Tab 1.")
        #label2 = QLabel("Widget in Tab 2.")
        pushButton1 = QPushButton("PyQt5 button")
        tabwidget = QTabWidget()
        home=tabwidget.addTab(Home(), "Inicio") #Home
        capacitors=tabwidget.addTab(Capacitors(), "Capacitors") 
        datasheet=tabwidget.addTab(Datasheets(), "Datasheets") 
        help=tabwidget.addTab(Help(), "Ayuda") #Help
        #agregamos los iconos a las pestañas
        tabwidget.setTabIcon(home, QtGui.QIcon('home.png'))
        tabwidget.setTabIcon(help, QtGui.QIcon('help.png'))

        #layout.addWidget(tabwidget, 0, 0)
        layout.addWidget(tabwidget)
        #sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #sizePolicy.setHeightForWidth(True)
        #self.setSizePolicy(sizePolicy)


        

 
############ 
 
 
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





############ PESTAÑA CAPACITORS    

class Capacitors(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button_cap_paralelo = QtWidgets.QPushButton("+", self)
        self.button_cap_paralelo.clicked.connect(self.cap_paralelo)
        self.button_cap_paralelo.setStyleSheet("padding: 8px;")
        
        
        self.button_cap_serie = QtWidgets.QPushButton("+", self)
        self.button_cap_serie.clicked.connect(self.cap_serie)
        self.button_cap_serie.setStyleSheet("padding: 8px;")
        
        self.groupbox = QGroupBox("GroupBox Example")
        #self.groupbox.setCheckable(True)
                
        #label titulo + serie
        self.label_tp = QtWidgets.QLabel("Paralel Capacitors",self)
        self.label_tp.setStyleSheet("border :0px solid blue;padding :0px; margin:0px; content:-12px")
        self.label_tp.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        #self.label_tp.setText("Paralel Capacitors")
        #self.label_tp.setStyleSheet("QLabel { font-weight: light;} ")
        
        #label titulo + paralelo
        self.label_ts = QtWidgets.QLabel("Serial Capacitors",self)
        self.label_ts.setStyleSheet("border :0px solid blue;padding :0px; margin:0px; content:-12px")
        self.label_ts.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #self.label_ts.setText("Serial Capacitors")
        
        #Value cap 1 //
        self.cap1_p = QLineEdit(self)
        #self.cap1.textChanged.connect(self.press)
        self.cap1_p.setPlaceholderText("capacitor 1") 
        #self.cap2_s.setText("capacitor 1") 
        #self.cap1_p.setMaxLength(2)
        #self.cap1_p.returnPressed.connect("Oleee")
        #self.cap1_p.mousePressEvent.connect(self.doSomething)


        #Value cap 2 // 
        self.cap2_p = QLineEdit(self)
        self.cap2_p.setPlaceholderText("capacitor 2") 
        
        #Value cap 1 serie
        self.cap1_s = QLineEdit(self)
        self.cap1_s.setPlaceholderText("capacitor 1") 
        
        #Value cap 2 serie 
        self.cap2_s = QLineEdit(self)
        self.cap2_s.setPlaceholderText("capacitor 2") 
        
        #Rango de valor comercial
        self.comercial_value_up = QLineEdit(self)
        self.comercial_value_up.setPlaceholderText("value up") 
        self.comercial_value_down = QLineEdit(self)
        self.comercial_value_down.setPlaceholderText("value down") 
        self.btn_search_comercial= QtWidgets.QPushButton("Search", self)
        self.btn_search_comercial.clicked.connect(self.search_cap_comercial)
        self.search_value = QLineEdit(self)
        self.search_value.setPlaceholderText("search value") 
        #self.list_convert_comercial= QtWidgets.QListWidget()
        self.list_convert_comercial= QComboBox(self)   
        # Agregamos items
        self.list_convert_comercial.addItem("f")
        self.list_convert_comercial.addItem("mf")
        self.list_convert_comercial.addItem("uf")
        self.list_convert_comercial.addItem("nf")
        self.list_convert_comercial.addItem("pf")
        #for i in range(1,6):
            #list_convert_comercial.addItem(str(i))
        self.list_convert_comercial.setCurrentIndex(4)

            
        # Resultados
        self.capacitance_value = QLineEdit(self)
        self.volts_value = QLineEdit(self)
        self.tolerance_value = QLineEdit(self)
        
        self.lb_capacitance = QtWidgets.QLabel("Capacitance")
        self.lb_capacitance.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.lb_volt = QtWidgets.QLabel("Voltaje")
        self.lb_volt.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.lb_tole = QtWidgets.QLabel("Tolerance")
        self.lb_tole.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        self.code_volts= QComboBox(self)
        self.code_volts.addItem("0G")
        self.code_volts.addItem("0L")
        self.code_volts.addItem("0J")
        self.code_volts.addItem("1A")
        self.code_volts.addItem("1C")
        self.code_volts.addItem("1E")
        self.code_volts.addItem("1H")
        self.code_volts.addItem("1J")
        self.code_volts.addItem("1K")
        self.code_volts.addItem("2A")
        self.code_volts.addItem("2Q")
        self.code_volts.addItem("2B")
        self.code_volts.addItem("2C")
        self.code_volts.addItem("2Z")
        self.code_volts.addItem("2D")
        self.code_volts.addItem("2P")
        self.code_volts.addItem("2E")
        self.code_volts.addItem("2F")
        self.code_volts.addItem("2V")
        self.code_volts.addItem("2G")
        self.code_volts.addItem("2W")
        self.code_volts.addItem("2H")
        self.code_volts.addItem("2J")
        self.code_volts.addItem("3A")
        self.code_volts.setCurrentIndex(-1)
        
        
        self.code1_capac= QComboBox(self)
        self.code1_capac.addItem('n')
        self.code1_capac.addItem('p')
        self.code1_capac.addItem('0')
        self.code1_capac.addItem('0.5')
        self.code1_capac.addItem('1')
        self.code1_capac.addItem('1.2')
        self.code1_capac.addItem('1.5')
        self.code1_capac.addItem('1.8')
        self.code1_capac.addItem('2')
        self.code1_capac.addItem('2.2')
        self.code1_capac.addItem('2.7')
        self.code1_capac.addItem('3.3')
        self.code1_capac.addItem('3.9')
        self.code1_capac.addItem('4')
        self.code1_capac.addItem('4.7')
        self.code1_capac.addItem('5')
        self.code1_capac.addItem('6')
        self.code1_capac.addItem('7')
        self.code1_capac.addItem('8')
        self.code1_capac.addItem('9')
        self.code1_capac.setCurrentIndex(-1)

        
        self.code2_capac= QComboBox(self)    
        self.code2_capac.addItem('n')
        self.code2_capac.addItem('p')
        self.code2_capac.addItem('0')
        self.code2_capac.addItem('1')
        self.code2_capac.addItem('2')
        self.code2_capac.addItem('3')
        self.code2_capac.addItem('4')
        self.code2_capac.addItem('5')
        self.code2_capac.addItem('6')
        self.code2_capac.addItem('7')
        self.code2_capac.addItem('8')
        self.code2_capac.addItem('9')
        self.code2_capac.setCurrentIndex(-1)

        self.code3_capac= QComboBox(self)   
        self.code3_capac.addItem('n')
        self.code3_capac.addItem('p')
        self.code3_capac.addItem('0')
        self.code3_capac.addItem('1')
        self.code3_capac.addItem('2')
        self.code3_capac.addItem('3')
        self.code3_capac.addItem('4')
        self.code3_capac.addItem('5')
        self.code3_capac.addItem('6')
        self.code3_capac.addItem('7')
        self.code3_capac.addItem('8')
        self.code3_capac.addItem('9')
        self.code3_capac.setCurrentIndex(-1)

        self.code_tole= QComboBox(self)             
        self.code_tole.addItem('B')
        self.code_tole.addItem('C')
        self.code_tole.addItem('D')
        self.code_tole.addItem('E')
        self.code_tole.addItem('F')
        self.code_tole.addItem('G')
        self.code_tole.addItem('H')
        self.code_tole.addItem('J')
        self.code_tole.addItem('K')
        self.code_tole.addItem('M')
        self.code_tole.addItem('N')
        self.code_tole.addItem('P')
        self.code_tole.addItem('Z')
        self.code_tole.setCurrentIndex(-1)

        self.convert_cap0= QComboBox(self)   
        self.convert_cap0.addItem("f")
        self.convert_cap0.addItem("mf")
        self.convert_cap0.addItem("uf")
        self.convert_cap0.addItem("nf")
        self.convert_cap0.addItem("pf")
        self.convert_cap0.setCurrentIndex(2)

        
        
        self.button_calculate = QtWidgets.QPushButton("Calculate", self)
        #self.button_calculate.clicked.connect(self.cap_serie)
        #self.button_calculate.setStyleSheet("padding: 8px;")
        
        self.code = QtWidgets.QLabel("Capacitor code")
        self.code.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        vbox = QVBoxLayout(self) #Vertical
        


        #hbox9 = QHBoxLayout(self) #HOrizontal
        #hbox9.addWidget(self.comercial_value_up)
        #vbox.addLayout(hbox9)
        
        hbox8 = QHBoxLayout(self) #HOrizontal
        hbox8.addWidget(self.code)
        vbox.addLayout(hbox8)

        #vbox.addStretch(5) # space Vertical
        hbox7 = QHBoxLayout(self) #HOrizontal
        #vbox.addWidget(self.groupbox)  
        hbox7.addWidget(self.code_volts)  
        hbox7.addStretch(3)
        hbox7.addWidget(self.code1_capac)     
        hbox7.addWidget(self.code2_capac)     
        hbox7.addWidget(self.code3_capac) 
        hbox7.addStretch(3)
        hbox7.addWidget(self.code_tole)  
        hbox7.addStretch(3)
        hbox7.addWidget(self.convert_cap0)    
        hbox7.addStretch(3)
        hbox7.addWidget(self.button_calculate)     
        #self.groupbox.setLayout(vbox)
        #vbox.addLayout(self.groupbox)
        vbox.addLayout(hbox7)
       
       
        hbox6 = QHBoxLayout(self) #HOrizontal
        hbox6.addWidget(self.lb_capacitance)
        hbox6.addWidget(self.lb_volt)
        hbox6.addWidget(self.lb_tole)     
        vbox.addLayout(hbox6)
                        
        hbox5 = QHBoxLayout(self) #HOrizontal
        hbox5.addStretch(5)
        hbox5.addWidget(self.capacitance_value)
        hbox5.addStretch(3)
        hbox5.addWidget(self.volts_value)
        hbox5.addStretch(3)
        hbox5.addWidget(self.tolerance_value)
        hbox5.addStretch(5)
        vbox.addLayout(hbox5)
        

        #hbox4 = QHBoxLayout(self) #HOrizontal
        #hbox4.addStretch(12)
        #hbox4.addWidget(self.comercial_value_up)
        #vbox.addLayout(hbox4)
        
        #layout = QtWidgets.QHBoxLayout()
        #sublayout = QtWidgets.QGridLayout()
        #layout.addLayout(sublayout)
        
        hbox2 = QHBoxLayout(self) #HOrizontal
        sublayout2 = QtWidgets.QGridLayout()
        hbox2.addWidget(self.search_value)
        hbox2.addWidget(self.list_convert_comercial)
        hbox2.addWidget(self.btn_search_comercial)
        hbox2.addStretch(2)
        sublayout2.addWidget(self.comercial_value_up,0,0) # object, row, column
        sublayout2.addWidget(self.comercial_value_down,1,0) # object, row, column
        hbox2.addLayout(sublayout2)
        hbox2.addStretch(6)
        vbox.addLayout(hbox2)
        
        #vbox.addWidget(self.label_ts)#Vertical
        #vbox.setContentsMargins(-1,-1,-1,-1)
        
    
        hbox1 = QHBoxLayout(self) #HOrizontal
        sublayout1 = QtWidgets.QGridLayout()
        sublayout1.addWidget(self.label_tp,0,0) 
        sublayout1.addWidget(self.label_ts,0,1) 
        #hbox1.addStretch(1) # Agregamos un espacio 
        hbox1.addLayout(sublayout1)
        vbox.addLayout(hbox1)
        
        

        hbox01 = QHBoxLayout(self) #HOrizontal
        hbox01.addWidget(self.label_tp)
        hbox01.addStretch(10) # Agregamos un espacio
        hbox01.addWidget(self.label_ts)
        hbox01.addStretch(2)
        vbox.addLayout(hbox01)
        

        hbox = QHBoxLayout(self) #HOrizontal      
        hbox.addWidget(self.cap1_p)
        hbox.addWidget(self.button_cap_paralelo)
        hbox.addStretch(3) # Agregamos un espacio 
        hbox.addWidget(self.cap1_s)
        hbox.addWidget(self.button_cap_serie)
        vbox.addLayout(hbox)

                
        # Ultima fila       
        hbox0 = QHBoxLayout(self) #HOrizontal
        hbox0.addWidget(self.cap2_p)
        hbox0.addStretch(10) 
        hbox0.addWidget(self.cap2_s)
        hbox0.addStretch(1) 
        vbox.addLayout(hbox0)
        
        vbox.setSpacing(0)
        #self.setLayout(vbox)    
        

        
        # VER ESTE tutorial
        #https://books.google.co.ve/books?id=wHDtDwAAQBAJ&pg=PA78&lpg=PA78&dq=pyside2+QVBoxLayout&source=bl&ots=d-ujt4_Puh&sig=ACfU3U1ZL-akiIvcAHQBdrHpVJY5JBDcIA&hl=es-419&sa=X&ved=2ahUKEwjix8_wiPvyAhXPRDABHTkxAukQ6AF6BAggEAM#v=onepage&q=pyside2%20QVBoxLayout&f=false

        
    def press(self):
        print("Hi World")
        self.cap1.clear()
        
    def cap_paralelo (self):
        cap1_get = self.cap1_p.text()
        cap2_get = self.cap2_p.text()
        if (cap1_get.isdigit() and cap2_get.isdigit()): 
            #setiamos la firts entry
            self.cap1_p.setText(str(float(cap1_get)+ float(cap2_get))) 
            self.cap2_p.setText("") 
        else:
            self.cap1_p.setText("Error, no is number") 
            self.cap2_p.setText("") 


    def cap_serie (self):
        cap1_get = self.cap1_s.text()
        cap2_get = self.cap2_s.text()
        if (cap1_get.isdigit() and cap2_get.isdigit()): 
            cap1_get = float(cap1_get)
            cap2_get = float(cap2_get)
            #setiamos la firts entry
            self.cap1_s.setText(str((cap1_get*cap2_get)/(cap1_get+cap2_get))) 
            self.cap2_s.setText("") 
        else:
            self.cap1_s.setText("Error, no is number") 
            self.cap2_s.setText("") 


    # Funcion para calcular el valor convertido dependiendo del prefijo
    def conver_cap(self,prefijo,value):
        if prefijo == "pf":
            #pass
            return [value, None, prefijo]
        
        elif prefijo == "nf":
            divide=value/1000
            multiply=value*1000
            ceros = 1000
            print(divide)
            
        elif prefijo == "uf":
            divide=value/1000000
            multiply=value*1000000
            ceros = 1000000
            print("entrooo a uf")
            
        elif prefijo == "mf":
            divide=value/1000000000
            multiply=value*1000000000
            ceros = 1000000000
            print(divide)
            
        elif prefijo == "f":
            divide=value/1000000000000
            multiply=value*1000000000000
            ceros = 1000000000000
        
        return [divide,multiply,prefijo,ceros]
            

    def search_cap_comercial(self):
        numero= self.search_value.text()
        #numero= codigo_cap.get()
        #validamos que lo ingresado sea numeros
        digit=numero.isdigit()

        
        # #validamos el sufijo
        # sufijo_in=in_combo.get()
        # sufijo_out=out_combo.get()

        # print(capacitancia)
        # #llamamos a la funcion sufijo
        # c=fun_sufijo(sufijo, capacitancia)
        # capacitancia=c
        # print(capacitancia)
        # #por defecto el valor es en pf
        # capacitancia= str(capacitancia) + sufijo
        # #setiamos la entry capacitancia con el valor capacitancia
        # valor_cap.set(capacitancia)
        
        #Diccionario de sufijo de capacitores
        #sufi_cap={'f':'1//1000000000000','mf':'1/1000000000','uf':'/1000000','nf':'/1000','pf':'1'}
        if  digit==False and re.match("^\d+?\.\d+?$",numero) is None:
            self.search_value.text('ERROR')

        else:
            #self.search_value.setText(numero + " " + "pf" )
            
            cap_comercial=(0.5,1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.6,6.8,8.2,10,12,15,18,22,27,33,39,47,56,68,82,100,120,150,180,220,270,330,390,470,560,680,820,1000,1200,1500,1800,2200,2700,3300,3900,4700,5600,6800,8200,10000,12000,15000,18000,22000,27000,33000,39000,47000,56000,68000,82000,100000,120000,150000,180000,220000,330000,390000,470000,560000,680000,820000,1000000)
            #convertimos a una lista string
            numero= float(numero)
            
            #El array tiene valores de pico faradios
            prefijo= str(self.list_convert_comercial.currentText())
            #conversor=in_combo.get()
            print("conversor",prefijo)        
            print("numero",numero)        
            
            #if conversor == "pf":
                #pass
            
            #elif conversor == "nf":
                #numero=numero/1000
                #numero=numero*1000
                #print(numero)
                
            #elif conversor == "uf":
                #numero=numero*1000000
                #print(numero)
                
            #elif conversor == "mf":
                #numero=numero*1000000000
                #print(numero)
                
            #elif conversor == "f":
                #numero=numero*1000000000000
                #print("numero",numero)
            
            value_cap = self.conver_cap(prefijo,numero)
            #print(value_cap[0],"valor de la funcioooooooooooooon")
            #print("tipoo",type(value_cap[0]))
            
            disponible= numero in cap_comercial
            print("respuesta si esta disponible: ", disponible)
    #             #creamos un diccionario para la tolerancia
    #     dic_tole={'B':'0.10pf','C':'0.25pf','D':'0.5pf','E':'0.5%','F':'1%', 'G':'2%', 'H':'3%', 'J':'5%', 'K':'10%', 'M':'20%','N':'30%',
    #     'P':'+100%, -0%','Z':'+80%, -20%'}
    #     tolerancia=tole_combo.get()
    #     tolerancia=dic_tole.get(tolerancia)
    #     #setiamos la entry de Tolerancia
    #     tole_cap.set(tolerancia)
    #     in_combo
            if disponible==True:
                #setiamos la entry
                self.comercial_value_up.setText('This value is')
                self.comercial_value_down.setText('Commercial')
                
            else:
                #numero mas cercano
                takeClosest= lambda num,collection:min(collection,key=lambda x:abs(num-x))
                
                ################## METER ESTO EN EL if numero > Closest : Y ELSE
                # Devolvemos respuesta en el prefijo seleccionado
                #if conversor == "pf":
                    #pass
                
                #elif conversor == "nf":
                    #numero=numero/1000
                    #print(numero)
                    
                #elif conversor == "uf":
                    #numero=numero/1000000
                    #print("entrooo a uf")
                    
                #elif conversor == "mf":
                    #numero=numero/1000000000
                    #print(numero)
                    
                #elif conversor == "f":
                    #numero=numero/1000000000000
                
                
                Closest=takeClosest(numero,cap_comercial) #estaba esteee

                #if (value_cap[1] == None):
                    #Closest=takeClosest(value_cap[0],cap_comercial) #estaba esteee
                
                #else:
                    #Closest=takeClosest(value_cap[0],cap_comercial)
                    #print("Closest 1",Closest)    
                    
                    
                print("Closest MAYOOOR",Closest)
                print(value_cap[1],"value_cap[1]")
                print(value_cap[0],"value_cap[0]")
                Nexposicion = cap_comercial.index(Closest)

                if numero > Closest :
                    print("entrooo 1111")
                    Nexposicion=Nexposicion+1
                    Nexposicion=cap_comercial[Nexposicion]
                    print("Nexposicion  MENOOOR",Nexposicion)
                    if (value_cap[2] != "pf"):
                        self.comercial_value_down.setText(str(Closest/value_cap[3]) + " " + value_cap[2])
                        Nexposicion=Nexposicion/value_cap[3]
                        self.comercial_value_up.setText(str(Nexposicion) + " " +  value_cap[2])
                    else:
                        self.comercial_value_down.setText(str(Closest))
                        self.comercial_value_up.setText(str(Nexposicion))

                else:
                    print("entrooo 222")
                    Nexposicion=Nexposicion-1
                    Nexposicion=cap_comercial[Nexposicion]
                    if (value_cap[2] != "pf"):
                        self.comercial_value_down.setText(str(takeClosest(value_cap[0],cap_comercial) ) + " " + value_cap[2])
                        Nexposicion=Nexposicion/value_cap[3]
                        self.comercial_value_up.setText(str(Nexposicion))
                    else:
                        self.comercial_value_down.setText(str(Nexposicion/value_cap[3]) + " " + value_cap[2])
                        self.comercial_value_up.setText(str(Closest))

        #title= QLabel("Acerca de")
        #title.setStyleSheet("QLabel { font-weight: bold;} ")
        #version= QLabel("GNU Pytronic  Version Beta 0.3 ")
        #devp= QLabel("Desarrollador: ")
        #name= QLabel("Ronal Forero")
        #mail= QLabel("L337.ronald@gmail.com")
        #lic=QLabel("Licencia: ")
        #lic_type=QLabel("GPL-V3")
        #title1= QLabel("Empaquetadores")
        #title1.setStyleSheet("QLabel { font-weight: bold;} ")
        #title_w=QLabel("Windows (.exe): ")
        #exe=QLabel("Ernesto Burgos")
        #exe_mail=QLabel("hdst.bur@gmail.com")
        #nada=QLabel("   ")
        #Acomodamos los Widfet con la malla (grid)
        #layout = QGridLayout()
        #layout = QHBoxLayout() #HOrizontal


############ PESTAÑA DATASHEETS    
class Datasheets(QWidget):
    def __init__(self):
        super().__init__()
        # el listado son las colecciones
        self.db = Database()
        print("listado --->",self.db.db.list_collection_names())

        self.picture = QPixmap("BS250.png")
        self.label = QLabel()
        self.label.setPixmap(self.picture)
        self.label.setGeometry(QtCore.QRect(10, 40, self.picture.width(), self.picture.height()))
        
        self.categories_devices = QListWidget()
        for i in self.db.db.list_collection_names():
            self.categories_devices.addItem(i)
            print("dento del array",i)
            
        self.devices = QListWidget()
        #print("--->",self.db.col.find({}, {"name":1}))
        
        # ESTA IMPRIMIENTO CUANTAS VECES COMO CAPOS TENGA EL DOCUMENTO Y DEBERIA SER CUANTOS DOCUMENTOS HAYAN.
        for document in self.db.col.find({}):
            self.devices.addItem(document['name'])
            print("dento de la coleccion",document)
            print("tipo ->",type(document))
            print ("el nmbreeee --->", document['name'])

            
            #app_json = json.dumps(document, sort_keys=True)
            #print(app_json)
            
            #for name in document:
                #print ("el nmbreeee --->", name)

        #print("afuera",json.dumps(document))
        
        vbox = QVBoxLayout(self) #Vertical
        
        hbox0 = QHBoxLayout(self) #HOrizontal
        hbox0.addWidget(self.categories_devices)
        hbox0.addWidget(self.devices)
        hbox0.addWidget(self.label)
        vbox.addLayout(hbox0)
        
        # separacion
        vbox.addStretch(2)
        
        #hbox1 = QHBoxLayout(self) #HOrizontal
        #vbox.addLayout(hbox1)
        
        
############ PESTAÑA DATABASE    
class Database(QWidget):
    def __init__(self):
        ######################################
        # Base de datos pruebas
        self.client = MongoClient('localhost')
        self.db = self.client['pytronics_devices']  #sino esta creada la db, la crea
        self.col = self.db['mosfets']
        self.col.insert_one({
            'name': 'BS250',
            'package': 'TO-92',
            'image': 'BS250.png',
            'vds': -45,
            'vgs': '± 25',
            'rds(on)':14,
            'id': -0.18,
            'idm': 2.2,
            'pd': 0.83,
            'v(br)dss': -45,
            'qg(max)': 1.8,
            'vgs(th)': '-1 to -3.5',
            'tj': -55,
            'tstg': 150,
            'similar_products': ['BSP254A', 'TP0610KL'],
            'maintainer_email': 'l337.ronald@gmail.com',
            'maintainer_name': 'Ronal Forero',
            'datasheet': 'https://pdf1.alldatasheet.es/datasheet-pdf/view/95978/GE/BS250/+748J9UDwZCy-N9+/datasheet.pdf'
            })
        print(self.client.list_database_names())
        print(self.db.list_collection_names())

        ######################################
        
############ PESTAÑA HELP    
class Help(QWidget):
    def __init__(self):
        super().__init__()
        title= QLabel("Acerca de")
        title.setStyleSheet("QLabel { font-weight: bold;} ")
        version= QLabel("GNU Pytronic  Version Beta 1.1 ")
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
screen.setFixedSize(640, 480) #block resize windows
screen.setWindowTitle("GNU Pytronic") 
screen.show()
sys.exit(app.exec_())






