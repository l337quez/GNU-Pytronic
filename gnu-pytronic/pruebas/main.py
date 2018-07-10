
from tkinter import *
from tkinter import ttk
import os
import sys
import subprocess
import re
import webbrowser
from tkinter import filedialog


#importamos librerias create by Ronal Forero
import p_resistors
import p_capacitors


#####################################################################

#Funcion sufijo para hacer converciones Mega, kilo, micro, pico
# para capacitores y resistencias

# def sufijo():
	# # #sufijo es una variable que contiene el valor del combobox
	
	# sufijo_cap=["pF","nF","uF","mF","F"]
	# sufijo_res=["Ω","KΩ","MΩ","GΩ"]
	

    # if sufijo == "nf" :
        # c=capacitancia/1000

    # elif sufijo == "uf":
        # c=capacitancia/1000000

    # elif sufijo == "mf":
        # c=capacitancia/1000000000

    # elif sufijo == "f":
        # c=capacitancia/1000000000000

    # #else sufijo = "pf"
    # else :
        # c = capacitancia
        # #retornar capacitancia y el sufijo que lo llame
        	
	
	# if sufijo =="MΩ": // mega ohm
		# r=resistencia*1000000
	
	# elif sufijo =="KΩ": // kilo ohm
		# r=resistencia*1000
	
	# else sufijo =="Ω": //ohm
		# r=resistencia
		
    # return c







#####################################################################
#Configuracion inicial
ventana =Tk()
ventana.title("GNU Pytronic")

#Organizando las pestañas
notebook=ttk.Notebook(ventana)
notebook.pack(fill='both',expand='yes')
pestana=ttk.Frame(notebook)
pestana0=ttk.Frame(notebook)
pestana1=ttk.Frame(notebook)
#pestana2=ttk.Frame(notebook)
pestana2=ttk.Frame(notebook)
notebook.add(pestana,text='Home')
notebook.add(pestana0,text='Capacitors')
notebook.add(pestana1,text='Resistors')
#notebook.add(pestana2,text='Inductors')
notebook.add(pestana2,text='About')


noteStyler = ttk.Style()
noteStyler.configure("TNotebook", background='gray', borderwidth=0)

COLOR_3 = 'black'
COLOR_4 = '#2E2E2E'
COLOR_5 = '#8A4B08'
COLOR_6 = '#DF7401'
noteStyler.configure("TNotebook.Tab", background="gray", foreground=COLOR_3, lightcolor=COLOR_6, borderwidth=2)

#Funcion para saber en que pesta#a esta el usuario
def personalData(event):
    if event.widget.index("current") == 0:
       pestanan= 0
       print("Home")
    elif event.widget.index("current") == 1:
       pestanan= 1
       print("Capacitor")
       #setiamos la label del dibujo del capacitor
       defaul_c=PhotoImage(file="Sources/ceramico.png")
       label_dib_cap.config(image=defaul_c)
       label_dib_cap.image =defaul_c
       grafic_tools = 1
    elif event.widget.index("current") == 2:
       pestanan= 2
       print("Resistors")
    else:
       pestanan= 3
       print("About")
    #else:
    #   print("Not One!")
       #ttk.Frame(pestana1,os.system ('python capacitores.py'))

    return

notebook.bind("<<NotebookTabChanged>>", personalData)



#////////////////////////////////////////////
#Selecion de imagen del capacitor en el listbox

def select_image_cap(event):
    #cambiador de imagenes IMAGEN DEL CAPACITOR, CERAMICO, Electrolitico...
    widget=event.widget
    selection=widget.curselection()

    #obtenemos en string el item seleccionado en el listbox
    piked= widget.get(selection[0])
    #usamos una lista
    lis_cap=['Ceramic', 'Polyester', 'Tamtalio', 'Electrolityc', 'Mica', 'Polypropilene']
    #buscamos en la lista el valor de piked y obtenemos la posicion
    p_lis_cap=lis_cap.index(piked)
    ruta_cap=(PhotoImage(file="Sources/ceramico.png"),PhotoImage(file="Sources/poliester.png"),PhotoImage(file="Sources/tamtalio.png"),PhotoImage(file="Sources/electrolitico.png"),PhotoImage(file="Sources/plastico.png"))
    #setiamos la label del dibujo del capacitor
    label_dib_cap.config(image=ruta_cap[p_lis_cap])
    label_dib_cap.image = ruta_cap[p_lis_cap]
    grafic_tools = 1 #activamos herramientas de graficacion







##############################################################################
#Pestaña About

Label(pestana2,text='GNU Pytronic',font='Helvetica 10 bold').place(x=20,y=60)
Label(pestana2,text=', software developed by Ing.Ronal Forero',font='Helvetica 10').place(x=108,y=60)
Label(pestana2,text='License:',font='Helvetica 10 bold').place(x=20,y=80)
Label(pestana2,text='GPL V3',font='Helvetica 10').place(x=80,y=80)
Label(pestana2,text='Version:',font='Helvetica 10 bold').place(x=20,y=100)
Label(pestana2,text='1.0',font='Helvetica 10').place(x=80,y=100)
Label(pestana2,text='Version in development:',font='Helvetica 10 bold').place(x=20,y=120)
Label(pestana2,text='Alpha 1.1',font='Helvetica 10').place(x=180,y=120)
Label(pestana2,text='Contact:',font='Helvetica 10 bold').place(x=20,y=140)
Label(pestana2,text='L337.ronald@gmail.com',font='Helvetica 10').place(x=80,y=140)



def callback(event):
    webbrowser.open_new(r"https://ronaldl337.wordpress.com/tag/gnu-pytronic/")

link = Label(pestana2, text="GNU Pyttonics Repository", fg="blue", cursor="hand2")
link.place(x=20,y=160)
link.bind("<Button-1>", callback)

def callback(event):
    webbrowser.open_new(r"https://github.com/l337quez/GNU-Pytronic/raw/master/other%20Sources/manual.odt")

link = Label(pestana2, text="User manual", fg="blue", cursor="hand2")
link.place(x=20,y=180)
link.bind("<Button-1>", callback)

##############################################################################
#Pestaña HOME

banner=PhotoImage(file="Sources/banner.png")
banner_home=Label(pestana,image=banner).place(x=0, y=20)


##############################################################################
#Pestaña Capacitores

#definimos variables
## variables de Capacitores
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


#variables de resistores
code_res =StringVar() #valor de la resistencia comercial
resistor_value= StringVar()
res_up=StringVar()
res_down=StringVar()
combo_tole=IntVar() #para setear el combobox de la tolerancia
res_smd=StringVar() #para valor de resistor SMD

#creamos demas objetos

#Entry
#Entry Capacitor
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

#Entry Resistors
entry_codigo=Entry(pestana1,  width= 10, textvariable=code_res).place(x=114, y=255) #codigo del capacitor
Entry(pestana1,  width= 10, textvariable=resistor_value).place(x=295, y=64) #value code
#Entry(pestana1,  width= 14, textvariable=res_smd).place(x=90, y=180) #value code SMD
Entry(pestana1,  width= 10, state='readonly',textvariable=res_up).place(x=330, y=240) #valor comercial disponible
Entry(pestana1,  width= 10, state='readonly',textvariable=res_down).place(x=330, y=270) #valor comercial por debajo
paralel1=Entry(pestana1,  width= 10).place(x=10, y=360)
paralel2=Entry(pestana1,  width= 10).place(x=10, y=390)
serie1=Entry(pestana1,  width= 10).place(x=280, y=360)
serie2=Entry(pestana1,  width= 10).place(x=280, y=390)
#entry_aproximar=Entry(ventana,  width= 8).place(x=10, y=400) #aproximar valor



#Botones
#Botones capacitores
Boton_calcular=Button(pestana0, text= "Calculate", command= p_capacitors.calculo_cap).place(x=420, y=58)
Boton_buscar=Button(pestana0, text= "Search", command=p_capacitors.buscar_cap).place(x=252, y=220)
Boton_graficar=Button(pestana0, text="Graficar").place(x=410, y=600)
Boton_guardar_data=Button(pestana0, text="Guardar DATA", state='disabled').place(x=10, y=570)
Boton_paralelo=Button(pestana0, text= "+", command=p_capacitors.cap_paralelo).place(x=120, y=330)
Boton_serie=Button(pestana0, text= "+", command=p_capacitors.cap_serie).place(x=390, y=330)

#Botones resistores
Button(pestana1, text= "Calculate", command= p_resistors.calculo_res).place(x=464, y=104) #Boton calcular
Button(pestana1, text= "Solve", command= p_resistors.calculo_color).place(x=464, y=60) #Boton solve value resistor
Button(pestana1, text= "Solve",command= p_resistors.smd).place(x=230, y=176) #Boton solve value resistor SMD
Button(pestana1, text= "Search", command=p_resistors.buscar_res).place(x=240, y=250) #Boton buscar
Button(pestana1, text= "+").place(x=120, y=360) #Boton_paralelo
Button(pestana1, text= "+").place(x=390, y=360) #Boton serie


#Labels
#Labels Capacitores
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


#Labels RESISTORES
ima_resistor=PhotoImage(file="Sources/resistencia.png")
banner_home=Label(pestana1,image=ima_resistor).place(x=84, y=40)

Label(pestana1, text="Parallel Resistors:").place(x=10, y=340)
Label(pestana1, text="Serial Resistors:").place(x=280, y=340)
label_cchino=Label(pestana1, text="Comercial value:").place(x=10, y=255)
label_tc=Label(pestana1, text="Color Code:").place(x=10, y=110)
Label(pestana1, text="Value:").place(x=250, y=64)
Label(pestana1, text="SMD Code:").place(x=10, y=180)
label_ban1=Label(pestana1,  height= 2)
label_ban1.place(x=110, y=50)
label_ban2=Label(pestana1,  height= 2)
label_ban2.place(x=130, y=50)
label_ban3=Label(pestana1,  height= 2)
label_ban3.place(x=150, y=50)
label_ban4=Label(pestana1,  height= 2)
label_ban4.place(x=170, y=50)
label_ban5=Label(pestana1, bg="gold2",  height= 2)
label_ban5.place(x=190, y=50)

#COMBOBOX

#   COMBOBOX PARA Capacitores

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






#######COMBOBOX PARA RESISTORES
#BANDA 1
ban1_combo=ttk.Combobox(pestana1, width= 6, height=3)
ban1_combo.place(x=90, y=110)
ban1_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white' )

#BANDA 2
ban2_combo=ttk.Combobox(pestana1, width= 6,height=3)
ban2_combo.place(x=160, y=110)
ban2_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white','black' )

#BANDA 3
ban3_combo=ttk.Combobox(pestana1, width= 6,height=3)
ban3_combo.place(x=230, y=110)
ban3_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white','black' )
#BANDA 4
ban4_combo=ttk.Combobox(pestana1, width= 6,height=3)
ban4_combo.place(x=300, y=110)
ban4_combo['values']=('none','brown','red','orange','yellow','green', 'blue','violet','gray','white','black' )
ban4_combo.current(0)

#BANDA 5
ban5_combo=ttk.Combobox(pestana1, width= 6, height=3)
ban5_combo.place(x=370, y=110)
ban5_combo['values']=('Silver','Golden','Red','Brown','Green', 'Blue','Violet','Gray' )
ban5_combo.current(1)

#TOLERANCIA
tolera_combo=ttk.Combobox(pestana1, width= 6, height=3)
tolera_combo.place(x=390, y=64)
tolera_combo['values']=('20%','10%','5%','1%','0.5%', '0.25%','0.10%','0.05%' )
tolera_combo.current(2)




#Listbox
list_tc=Listbox(pestana0,width= 14, height=2)
list_tc.insert(0,"Ceramic")
list_tc.insert(1,"Polyester")
list_tc.insert(2,"Tamtalio")
list_tc.insert(3,"Electrolityc")
list_tc.insert(4,"Mica")
list_tc.insert(4,"Polypropylene")
list_tc.place(x=10, y=62)
#barra de scroll para el listbox
scrollbar_list_tc= Scrollbar(pestana0, width= 12, orient="vertical")
scrollbar_list_tc.config(command=list_tc.yview)
scrollbar_list_tc.place(x=112, y=67)
list_tc.config(yscrollcommand=scrollbar_list_tc.set)
list_tc.select_set(0)
#list_tc.selectedindex = 0
list_tc.event_generate("<<ListboxSelect>>")
list_tc.bind('<<ListboxSelect>>',select_image_cap)





#########################################################################
ventana.geometry("600x450+0+0")
#icono del software
ventana.call('wm','iconphoto',ventana._w,PhotoImage(file='pytronics.png'))

#Tema tkinter para los objetos
s=ttk.Style()
s.theme_names()
#"""======== if you are under win 8.1 you must see ..
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative') you can use for example 'clam' ===== """
s.theme_use('clam')
ventana.mainloop()
