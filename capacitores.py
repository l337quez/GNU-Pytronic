#!/usr/bin/python
#Programa de comunicacion UART para Ings Electronicos
#pacman -S tk
#leer https://github.com/almost/picprogrammer/blob/master/picpro.py
#guia de tkinter http://guia-tkinter.readthedocs.io/es/develop/
import sys
import subprocess
import re
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from serial.tools.list_ports import comports
##############################################
#Configuracion inicial



# global Boton_quemar_pic

# def __init__(self,portada):

# def inicio():
#     ruta_portada_default=PhotoImage(file="banner-of.png")
#     portada.config(image=ruta_portada_default)
#     portada.image = ruta_portada_default
#     return

##############################################



#FUNCIONES
#Funcion de inicio de botones, labels etc.. deshabilitados, valores iniciales
def object_disables ():
    Boton_quemar_pic.state(["!disable"])


    return





#Funcion que nos indica el intem seleccionado con el cursor en listbox ceramico, tamtalio...
def select_image_cap(event):

    #cambiador de imagenes IMAGEN DEL CAPACITOR, CERAMICO, Electrolitico...
    widget=event.widget
    selection=widget.curselection()
    #obtenemos en string el item seleccionado en el listbox
    piked= widget.get(selection[0])
    #usamos una lista
    lis_cap=['Ceramico', 'Poliester', 'Tamtalio', 'Electrolitico', 'Plastico', 'Polipropileno']
    #buscamos en la lista el valor de piked y obtenemos la posicion
    p_lis_cap=lis_cap.index(piked)
    ruta_cap=(PhotoImage(file="Sources/ceramico.png"),PhotoImage(file="Sources/poliester.png"),PhotoImage(file="Sources/tamtalio.png"),PhotoImage(file="Sources/electrolitico.png"),PhotoImage(file="Sources/plastico.png"))
    #setiamos la label del dibujo del capacitor
    label_dib_cap.config(image=ruta_cap[p_lis_cap])
    label_dib_cap.image = ruta_cap[p_lis_cap]
    grafic_tools = 1 #activamos herramientas de graficacion


#funcion para buscar valor de capacitores comerciales
def buscar_cap():
    numero= codigo.get()
    #validamos que lo ingresado sea numeros
    digit=numero.isdigit()


    if  digit==False and re.match("^\d+?\.\d+?$",numero) is None:

        codigo.set('ERROR')

    else:
        cap_comercial=(0.5,1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.6,6.8,8.2)
        #convertimos a una lista string
        numero= float(numero)
        disponible=numero in cap_comercial


        if disponible==True:
            #setiamos la entry
            cap_up.set('This value is')
            cap_down.set('Commercial')

        else:

            #numero mas cercano
            takeClosest= lambda num,collection:min(collection,key=lambda x:abs(num-x))
            Closest=takeClosest(numero,cap_comercial)
            print(Closest)

            Nexposicion=cap_comercial.index(Closest)


            if numero > Closest :
                cap_down.set(Closest)
                Nexposicion=Nexposicion+1
                Nexposicion=cap_comercial[Nexposicion]
                cap_up.set(Nexposicion)

            else:
                Nexposicion=Nexposicion-1
                Nexposicion=cap_comercial[Nexposicion]
                cap_down.set(Nexposicion)
                cap_up.set(Closest)



            #numero=numero+0.1

#            if numero>buscando
#                lnumber=numero
#                i=i+1
#            elif numero<buscando
#                nu=buscando #number up
#                nd=lnumber #number down
#                if numero<cap_comercial[i+1]


        #else:
        #    up=numero
        #    down=numero
        #    while up <= numero and down>= numero  :
        #        up=up+0.1
        #        down=down-0.1
        #        if up <= numero and down== numero :
        #            break








        #tipo_cap= list_tipo_cap.get()
        #tamaño=len(numero)



#def fun_sufijo(sufijo, capacitancia):
def fun_sufijo(*args):
    sufijo=args[0]
    capacitancia=args[1]
    # capcitancia por defecto en pf

    if sufijo == "nf":
        c=capacitancia/1000

    elif sufijo == "uf":
        c=capacitancia/1000000

    elif sufijo == "mf":
        c=capacitancia/1000000000

    elif sufijo == "f":
        c=capacitancia/1000000000000

    #else sufijo = "pf"
    else :
        c = capacitancia
        #retornar capacitancia y el sufijo que lo llame
    return c

#Funcion para calcular capacitores
def calculo_cap():

    #CALCULADO LOS VOLTIOS
    #creamos un diccionario
    dic_volt={'0G':'4VDC','0L':'5.5VDC','0J':'6.3VDC','1A':'10VDC','1C':'16VDC','1E':'25VDC','1H':'50VDC','1J':'63VDC','1K':'80VDC','2A':'100VDC','2Q':'110VDC','2B':'125VDC',
    '2C':'160VDC','2Z':'180VDC', '2D':'200VDC', '2P':'220VDC', '2E':'250VDC','2F':'315VDC','2V':'350VDC','2G':'400VDC','2W':'450VDC','2H':'500VDC','2J':'630VDC','3A':'1000VDC' }

    volts=vol_combo.get()
    #buscamos el codigo referente al voltaje en el diccionario y le asignamos el valor a volts
    volts=dic_volt.get(volts)
    #setiamos la entry de Voltaje
    volts_cap.set(volts)

    #CALCULANDO LA CAPACITANCIA
    pn=pn_combo.get() #primer numero
    sn=sn_combo.get() #segundo numero
    tn=cero_combo.get() #tercer numero

    if pn=='n'or sn=='n' or tn=='n':
        if pn=='n':
            valor = sn+tn #concatenamos caracteres
            ceros= '0'

        elif sn=='n':
            valor=pn+tn
            ceros='00'

        elif ceros=='n':
            valor=pn+sn
            ceros='000'

        capacitancia=float(valor+ceros)
        print(capacitancia)
    #if sn=='p':



    else:
        valor= pn+sn
        valor=float(valor)

#    if ceros == 'None':
#        ceros=1
#    else:
        ceros=int(tn)
        #(1x10)^ceros
        ceros=10**ceros
        #multiplicamos el valor con el numero multiplicador
        capacitancia= valor*ceros

    #validamos el sufijo
    sufijo=combo.get()
    print(capacitancia)
    #llamamos a la funcion sufijo
    c=fun_sufijo(sufijo, capacitancia)
    capacitancia=c
    print(capacitancia)
    #por defecto el valor es en pf
    capacitancia= str(capacitancia) + sufijo
    #setiamos la entry capacitancia con el valor capacitancia
    valor_cap.set(capacitancia)



    #CALCULANDO TOLERANCIA

    #creamos un diccionario para la tolerancia
    dic_tole={'B':'0.10pf','C':'0.25pf','D':'0.5pf','E':'0.5%','F':'1%', 'G':'2%', 'H':'3%', 'J':'5%', 'K':'10%', 'M':'20%','N':'30%',
    'P':'+100%, -0%','Z':'+80%, -20%'}
    tolerancia=tole_combo.get()
    tolerancia=dic_tole.get(tolerancia)
    #setiamos la entry de Tolerancia
    tole_cap.set(tolerancia)



#########################################################
#Construyendo la ventana
ventana = Tk()
ventana.title("GNU Pytronics") #Titulo de la ventana
#Dimencion de la ventana
ventana.geometry("600x450+0+0")



#definimos variables
codigo =StringVar() #codigo del capacitor
valor_cap =StringVar() #valor real del capacitor
volts_cap= StringVar() # voltaje del capacitor
tole_cap= StringVar()
list_tipo_cap= StringVar() #obtener el valor seleccionado en tipo de capacitor
cap_up=StringVar()
cap_down=StringVar()

#creamos demas objetos

#Entry
entry_codigo=Entry(ventana,  width= 10, textvariable=codigo).place(x=114, y=255) #codigo del capacitor
entry_valor=Entry(ventana,  width= 10, state='readonly', textvariable=valor_cap).place(x=10, y=190) #capacitancia
entry_volt=Entry(ventana,  width= 10,state='readonly', textvariable=volts_cap).place(x=110, y=190) #voltaje
entry_tol=Entry(ventana,  width= 10,state='readonly', textvariable=tole_cap).place(x=210, y=190) #tolerancia
entry_comerup=Entry(ventana,  width= 10, state='readonly',textvariable=cap_up).place(x=330, y=240) #valor comercial disponible
entry_comerdown=Entry(ventana,  width= 10, state='readonly',textvariable=cap_down).place(x=330, y=270) #valor comercial por debajo
entry_paralel1=Entry(ventana,  width= 10,textvariable=cap_down).place(x=10, y=360)
entry_paralel2=Entry(ventana,  width= 10,textvariable=cap_down).place(x=10, y=390)
entry_serie1=Entry(ventana,  width= 10,textvariable=cap_down).place(x=280, y=360)
entry_serie2=Entry(ventana,  width= 10,textvariable=cap_down).place(x=280, y=390)

#entry_aproximar=Entry(ventana,  width= 8).place(x=10, y=400) #aproximar valor



#Botones
#command= lambda:calculo_cap()
Boton_calcular=Button(ventana, text= "Calculate", command= calculo_cap).place(x=420, y=88)
Boton_buscar=Button(ventana, text= "Search", command=buscar_cap).place(x=252, y=250)
Boton_graficar=Button(ventana, text="Graficar").place(x=410, y=600)
Boton_guardar_data=Button(ventana, text="Guardar DATA", state='disabled').place(x=10, y=600)
Boton_paralelo=Button(ventana, text= "+", command=buscar_cap).place(x=120, y=360)
Boton_serie=Button(ventana, text= "+", command=buscar_cap).place(x=390, y=360)



#Labels
label_cchino=Label(ventana, text="Parallel Capacitors:").place(x=10, y=340)
label_cchino=Label(ventana, text="Serial Capacitors:").place(x=280, y=340)
label_cchino=Label(ventana, text="Comercial value:").place(x=10, y=255)
label_tc=Label(ventana, text="Type of Capacitor:").place(x=10, y=74)
label_voltaje=Label(ventana, text="Voltage").place(x=110, y=170)
label_tole=Label(ventana, text="Tolerance").place(x=210, y=170)
label_ca=Label(ventana, text="Capacitance").place(x=10, y=170)
label_code=Label(ventana, text="Capacitor code:").place(x=140, y=74)
#label dibujo de capacitor
label_dib_cap=Label(ventana)
label_dib_cap.place(x=450, y=140)
#label logo de pytronic
#label_logo=Label(ventana, image=PhotoImage(file="Sources/pytronic.png")).place(x=1, y=1)






#COMBOBOX

#combobox codigo de voltaje
vol_combo=ttk.Combobox(ventana, width= 3, height=3)
vol_combo.place(x=140, y=94)
vol_combo['values']=('0G','0L','0J','1A','1C','1E','1H','1J','1K','2A','2Q','2B','2C','2Z', '2D', '2P', '2E','2F','2V','2G','2W','2H','2J','3A' )


pn_combo=ttk.Combobox(ventana, width= 3,height=3)
pn_combo.place(x=200, y=94)
pn_combo['values']=('n','0','0.5','1','1.2','1.5','1.8','2','2.2','2.7','3','3.3','3.9','4','4.7','5','6','7','8','9')


sn_combo=ttk.Combobox(ventana, width= 2,height=3)
sn_combo.place(x=245, y=94)
sn_combo['values']=('n','p','0','1','2','3','4','5','6','7','8','9')


cero_combo=ttk.Combobox(ventana, width= 2,height=3)
cero_combo.place(x=282, y=94)
cero_combo['values']=('n','0','1','2','3','4','5','6','7','8','9')


#Combobox  TOLERANCIA
tole_combo=ttk.Combobox(ventana, width= 2, height=3)
tole_combo.place(x=335, y=94)
tole_combo['values']=('B','C','D','E','F','G','H','J','K','M','N','P','Z')


#Combobox  convercion pf a uf...
combo=ttk.Combobox(ventana, width= 2)
combo.place(x=380, y=94)
combo['values']=('f','mf','uf','pf','nf')
combo.current(2)



#Combobox  convercion pf a uf imput comercial...
in_combo=ttk.Combobox(ventana, width= 2)
in_combo.place(x=209, y=255)
in_combo['values']=('f','mf','uf','pf','nf')
in_combo.current(2)

#Combobox  convercion pf a uf ouput comercial...
ou_combo=ttk.Combobox(ventana, width= 2)
ou_combo.place(x=427, y=255)
ou_combo['values']=('f','mf','uf','pf','nf')
ou_combo.current(2)



#Listbox
list_tc=Listbox(ventana,width= 14, height=2)
list_tc.insert(0,"Ceramico")
list_tc.insert(1,"Poliester")
list_tc.insert(2,"Tamtalio")
list_tc.insert(3,"Electrolitico")
list_tc.insert(4,"Plastico")
list_tc.insert(4,"Polipropileno")
list_tc.place(x=10, y=92)
scrollbar_list_tc= Scrollbar(ventana, width= 10, orient="vertical")
scrollbar_list_tc.config(command=list_tc.yview)
scrollbar_list_tc.place(x=112, y=97)
list_tc.config(yscrollcommand=scrollbar_list_tc.set)
list_tc.select_set(0)
#list_tc.selectedindex = 0
list_tc.event_generate("<<ListboxSelect>>")
list_tc.bind('<<ListboxSelect>>',select_image_cap)



ventana.mainloop()
