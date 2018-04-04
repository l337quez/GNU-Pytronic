

from tkinter import *
from tkinter import ttk
import os
import sys
import subprocess
import re
import webbrowser
from tkinter import filedialog
#####################################################################

global contador
contador=0
def select_image_cap(event):
    global contador
    #cambiador de imagenes IMAGEN DEL CAPACITOR, CERAMICO, Electrolitico...
    widget=event.widget
    selection=widget.curselection()

    #colocamos la imagen del capacitor ceramico como default
    if contador <2 :
        p_lis_cap=('Ceramico')
        ruta_cap=(PhotoImage(file="Sources/ceramico.png"),PhotoImage(file="Sources/poliester.png"),PhotoImage(file="Sources/tamtalio.png"),PhotoImage(file="Sources/electrolitico.png"),PhotoImage(file="Sources/plastico.png"))
        #setiamos la label del dibujo del capacitor
        label_dib_cap.config(image=ruta_cap[0])
        label_dib_cap.image = ruta_cap[0]
        grafic_tools = 1


    contador = contador +1;

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
        cap_comercial=(0.5,1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.6,6.8,8.2,10,12,15,18,22,27,33,39,47,56,68,82,100,120,150,180,220,270,330,390,470,560,680,820,1000,1200,1500,1800,2200,2700,3300,3900,4700,5600
        ,6800,8200,10000,12000,15000,18000,22000,27000,33000,39000,47000,56000,68000,82000,100000,120000,150000,180000,220000,330000,390000,470000,560000,680000,820000,1000000)
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


    elif pn=='p' or sn=='p':


        if pn== 'p':
            sn=float(sn)
            valor=0.1*sn

        elif sn=='p':
            tn=float(tn)
            pn=float(pn)
            valor=pn+(tn/10)
        capacitancia=float(valor)


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


#   CALCULO DE CAPACITORES PARALELO

def cap_paralelo ():
    cap1=paralelo1.get()
    cap2=paralelo2.get()
    cap_result=cap1+cap2
    #setiamos la firts entry
    paralelo1.set(cap_result)
    paralelo2.set('  ')

def cap_serie ():
    cap1=serie1.get()
    cap2=serie2.get()
    cap_result=cap1*cap2/cap1+cap2
    #setiamos la firts entry
    serie1.set(cap_result)
    serie2.set('  ')



#####################################################################
#Configuracion inicial
ventana =Tk()
ventana.title("GNU Pytronics")
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
notebook.add(pestana2,text='Inductors')
notebook.add(pestana3,text='About')


noteStyler = ttk.Style()
noteStyler.configure("TNotebook", background='gray', borderwidth=0)

COLOR_3 = 'black'
COLOR_4 = '#2E2E2E'
COLOR_5 = '#8A4B08'
COLOR_6 = '#DF7401'
noteStyler.configure("TNotebook.Tab", background="gray", foreground=COLOR_3, lightcolor=COLOR_6, borderwidth=2)


def personalData(event):
    if event.widget.index("current") == 0:
       print("One!")
    else:
       print("Not One!")
       #ttk.Frame(pestana1,os.system ('python capacitores.py'))


notebook.bind("<<NotebookTabChanged>>", personalData)

##############################################################################
#Pestaña About

Label(pestana3,text='GNU Pytronic software Desarrollado por Ronal Forero').place(x=20,y=60)
Label(pestana3,text='Licencia GPL V3').place(x=20,y=80)




def callback(event):
    webbrowser.open_new(r"https://github.com/l337quez/GNU-Pytronic")


link = Label(pestana3, text="GNU Pyttonics Repository", fg="blue", cursor="hand2")
link.place(x=20,y=100)
link.bind("<Button-1>", callback)

##############################################################################
#Pestaña HOME


##############################################################################
#Pestaña Capacitores

#definimos variables
codigo =StringVar() #codigo del capacitor
valor_cap =StringVar() #valor real del capacitor
volts_cap= StringVar() # voltaje del capacitor
tole_cap= StringVar()
list_tipo_cap= StringVar() #obtener el valor seleccionado en tipo de capacitor
cap_up=StringVar()
cap_down=StringVar()
serie1=DoubleVar()
serie2=DoubleVar()
paralelo1=DoubleVar()
paralelo2=DoubleVar()


#creamos demas objetos

#Entry
entry_codigo=Entry(pestana0,  width= 10, textvariable=codigo).place(x=114, y=225) #codigo del capacitor
entry_valor=Entry(pestana0,  width= 10, state='readonly', textvariable=valor_cap).place(x=10, y=160) #capacitancia
entry_volt=Entry(pestana0,  width= 10,state='readonly', textvariable=volts_cap).place(x=110, y=160) #voltaje
entry_tol=Entry(pestana0,  width= 10,state='readonly', textvariable=tole_cap).place(x=210, y=160) #tolerancia
entry_comerup=Entry(pestana0,  width= 10, state='readonly',textvariable=cap_up).place(x=330, y=210) #valor comercial disponible
entry_comerdown=Entry(pestana0,  width= 10, state='readonly',textvariable=cap_down).place(x=330, y=240) #valor comercial por debajo
entry_paralel1=Entry(pestana0,  width= 10,textvariable=paralelo1).place(x=10, y=330)
entry_paralel2=Entry(pestana0,  width= 10,textvariable=paralelo2).place(x=10, y=360)
entry_serie1=Entry(pestana0,  width= 10,textvariable=serie1).place(x=280, y=330)
entry_serie2=Entry(pestana0,  width= 10,textvariable=serie2).place(x=280, y=360)

#entry_aproximar=Entry(ventana,  width= 8).place(x=10, y=400) #aproximar valor



#Botones
#command= lambda:calculo_cap()
Boton_calcular=Button(pestana0, text= "Calculate", command= calculo_cap).place(x=420, y=58)
Boton_buscar=Button(pestana0, text= "Search", command=buscar_cap).place(x=252, y=220)
Boton_graficar=Button(pestana0, text="Graficar").place(x=410, y=600)
Boton_guardar_data=Button(pestana0, text="Guardar DATA", state='disabled').place(x=10, y=570)
Boton_paralelo=Button(pestana0, text= "+", command=cap_paralelo).place(x=120, y=330)
Boton_serie=Button(pestana0, text= "+", command=cap_serie).place(x=390, y=330)



#Labels
label_cchino=Label(pestana0, text="Parallel Capacitors:").place(x=10, y=310)
label_cchino=Label(pestana0, text="Serial Capacitors:").place(x=280, y=310)
label_cchino=Label(pestana0, text="Comercial value:").place(x=10, y=225)
label_tc=Label(pestana0, text="Type of Capacitor:").place(x=10, y=44)
label_voltaje=Label(pestana0, text="Voltage").place(x=110, y=138)
label_tole=Label(pestana0, text="Tolerance").place(x=210, y=138)
label_ca=Label(pestana0, text="Capacitance").place(x=10, y=138)
label_code=Label(pestana0, text="Capacitor code:").place(x=140, y=44)
#label dibujo de capacitor
label_dib_cap=Label(pestana0)
label_dib_cap.place(x=450, y=110)
#label logo de pytronic
#label_logo=Label(ventana, image=PhotoImage(file="Sources/pytronic.png")).place(x=1, y=1)






#COMBOBOX

#combobox codigo de voltaje
vol_combo=ttk.Combobox(pestana0, width= 3, height=3)
vol_combo.place(x=140, y=64)
vol_combo['values']=('0G','0L','0J','1A','1C','1E','1H','1J','1K','2A','2Q','2B','2C','2Z', '2D', '2P', '2E','2F','2V','2G','2W','2H','2J','3A' )


pn_combo=ttk.Combobox(pestana0, width= 3,height=3)
pn_combo.place(x=200, y=64)
pn_combo['values']=('n','p','0','0.5','1','1.2','1.5','1.8','2','2.2','2.7','3','3.3','3.9','4','4.7','5','6','7','8','9')


sn_combo=ttk.Combobox(pestana0, width= 2,height=3)
sn_combo.place(x=245, y=64)
sn_combo['values']=('n','p','0','1','2','3','4','5','6','7','8','9')


cero_combo=ttk.Combobox(pestana0, width= 2,height=3)
cero_combo.place(x=282, y=64)
cero_combo['values']=('n','0','1','2','3','4','5','6','7','8','9')


#Combobox  TOLERANCIA
tole_combo=ttk.Combobox(pestana0, width= 2, height=3)
tole_combo.place(x=335, y=64)
tole_combo['values']=('B','C','D','E','F','G','H','J','K','M','N','P','Z')


#Combobox  convercion pf a uf...
combo=ttk.Combobox(pestana0, width= 2)
combo.place(x=380, y=64)
combo['values']=('f','mf','uf','pf','nf')
combo.current(2)



#Combobox  convercion pf a uf imput comercial...
in_combo=ttk.Combobox(pestana0, width= 2)
in_combo.place(x=209, y=225)
in_combo['values']=('f','mf','uf','pf','nf')
in_combo.current(3)

#Combobox  convercion pf a uf ouput comercial...
ou_combo=ttk.Combobox(pestana0, width= 2)
ou_combo.place(x=427, y=225)
ou_combo['values']=('f','mf','uf','pf','nf')
ou_combo.current(3)



#Listbox
list_tc=Listbox(pestana0,width= 14, height=2)
list_tc.insert(0,"Ceramico")
list_tc.insert(1,"Poliester")
list_tc.insert(2,"Tamtalio")
list_tc.insert(3,"Electrolitico")
list_tc.insert(4,"Plastico")
list_tc.insert(4,"Polipropileno")
list_tc.place(x=10, y=62)
scrollbar_list_tc= Scrollbar(pestana0, width= 12, orient="vertical")
scrollbar_list_tc.config(command=list_tc.yview)
scrollbar_list_tc.place(x=112, y=67)
list_tc.config(yscrollcommand=scrollbar_list_tc.set)
list_tc.select_set(0)
#list_tc.selectedindex = 0
list_tc.event_generate("<<ListboxSelect>>")
list_tc.bind('<<ListboxSelect>>',select_image_cap)




















ventana.geometry("600x450+0+0")
ventana.mainloop()
