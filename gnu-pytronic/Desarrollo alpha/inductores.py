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
num_v=StringVar()
longitud=StringVar()
campo=StringVar()


#creamos demas objetos

#Entry
entry_codigo=Entry(ventana,  width= 10, textvariable=codigo).place(x=114, y=255) #codigo del capacitor
entry_valor=Entry(ventana,  width= 10, state='readonly', textvariable=valor_cap).place(x=10, y=190) #capacitancia
entry_volt=Entry(ventana,  width= 10,state='readonly', textvariable=volts_cap).place(x=110, y=190) #voltaje
entry_tol=Entry(ventana,  width= 10,state='readonly', textvariable=tole_cap).place(x=210, y=190) #tolerancia
entry_numerov=Entry(ventana,  width= 10,textvariable=num_v).place(x=140, y=130) #valor comercial disponible
entry_longitud=Entry(ventana,  width= 10,textvariable=longitud).place(x=10, y=130) #valor comercial por debajo
entry_campo=Entry(ventana,  width= 10,textvariable=campo).place(x=260, y=130) #valor comercial por debajo
entry_sensibilidad=Entry(ventana,  width= 10).place(x=380, y=130) #valor comercial por debajo
entry_sensibilidad=Entry(ventana,  width= 10).place(x=490, y=130) #valor comercial por debajo


#entry_aproximar=Entry(ventana,  width= 8).place(x=10, y=400) #aproximar valor



#Botones
#command= lambda:calculo_cap()
Boton_calcular=Button(ventana, text= "Calculate", command= calculo_cap).place(x=420, y=230)
Boton_buscar=Button(ventana, text= "Search", command=buscar_cap).place(x=252, y=250)
Boton_graficar=Button(ventana, text="Graficar").place(x=410, y=600)
Boton_guardar_data=Button(ventana, text="Guardar DATA", state='disabled').place(x=10, y=600)




#Labels
label_cchino=Label(ventana, text="Comercial value:").place(x=10, y=255)
label_tc=Label(ventana, text="Calculator of sensor output according to the coil:", font='bold').place(x=10, y=74)
label_voltaje=Label(ventana, text="N° of turns").place(x=140, y=110)
label_tole=Label(ventana, text="Magnetic Field").place(x=260, y=110)
label_ca=Label(ventana, text="Inductor Length").place(x=10, y=110)
label_ca=Label(ventana, text="M. Sensitivy").place(x=380, y=110)
label_ca=Label(ventana, text="Quiescent volt").place(x=490, y=110)






#COMBOBOX

#Combobox  convercion pf a uf...
combo=ttk.Combobox(ventana, width= 2)
combo.place(x=380, y=294)
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







ventana.mainloop()
