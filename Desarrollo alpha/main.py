
from tkinter import *
from tkinter import ttk
import os
import sys
import shlex, subprocess
import re
import webbrowser
from tkinter import filedialog

#importando archivos py
#import inductores
from inductores import calculo_ind
#####################################################################


# ENVIANDO VARIABLES AL ARCHIVO INDUCTORES

def calculo_inductores ():
    banda1=ban1_combo.get()
    banda2=ban2_combo.get()
    banda3=ban3_combo.get()
    banda4=ban4_combo.get()
    banda5=ban5_combo.get()
    calculo_ind(banda1,banda2,banda3,banda4,banda5)
    
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


#funcion para buscar valor de capacitores comerciales
def buscar_cap():
    numero= codigo_cap.get()
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

        codigo_cap.set('ERROR')

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

    nada= None
	#CALCULANDO TOLERANCIA

    #creamos un diccionario para la tolerancia
    dic_tole={'B':'0.10pf','C':'0.25pf','D':'0.5pf','E':'0.5%','F':'1%', 'G':'2%', 'H':'3%', 'J':'5%', 'K':'10%', 'M':'20%','N':'30%',
    'P':'+100%, -0%','Z':'+80%, -20%'}
    tolerancia=tole_combo.get()
    tolerancia=dic_tole.get(tolerancia)
    #setiamos la entry de Tolerancia
    tole_cap.set(tolerancia)

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
   
    #validamos si no hay seleccion de capacitacia
    if (pn and pn.strip()) and (sn and sn.strip()):
    #si selecciono valores
    
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
            print (sn)
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
        #llamamos a la funcion sufijo
        c=fun_sufijo(sufijo, capacitancia)
        capacitancia=c
         #por defecto el valor es en pf
        capacitancia= str(capacitancia) + sufijo
        #setiamos la entry capacitancia con el valor capacitancia
        valor_cap.set(capacitancia)
        
    else:
        #No hay capacitancia seleccionada para calcular
        valor_cap.set(None)



 


#   CALCULO DE CAPACITORES PARALELO Y SERIE

def cap_paralelo ():
    cap1=paraleloc1.get()
    cap2=paraleloc2.get()
    #setiamos la firts entry
    paraleloc1.set(cap1+cap2)
    paraleloc2.set('  ')

def cap_serie ():
    cap1=seriec1.get()
    cap2=seriec2.get()
    #setiamos la firts entry
    seriec1.set((cap1*cap2)/(cap1+cap2))
    seriec2.set('  ')



 
########################################################################

#Funciones para la pestaña resisitencia
def buscar_res():
    valor_res= code_res.get()
    #validamos que lo ingresado sea numeros
    digit=valor_res.isdigit()

    print(valor_res)
    if  digit==False and re.match("^\d+?\.\d+?$",valor_res) is None:

        code_res.set('ERROR')
    
    elif float(valor_res) >1000000:
        code_res.set('ERROR')
        
    elif  float(valor_res) <0.99:
        code_res.set('ERROR')
 
    else:
        res_comercial=(1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.1,5.6,6.8,8.2,10,12,15,18,22,27,33,39,47,51,56,68,82,100,120,150,180,220,270,330,390,470,510,560,680,820,1000,1200,1500,1800,2200,2700,3300,3900,4700,
        5100,5600,6800,8200,10000,12000,15000,18000,22000,27000,33000,39000,47000,51000,56000,68000,82000,100000,120000,150000,180000,220000,330000,390000,470000,510000,560000,680000,820000,1000000)

        #convertimos a una lista string
        valor_res= float(valor_res)
        disponible=valor_res in res_comercial


        if disponible==True:
            #setiamos la entry
            res_up.set('This value is')
            res_down.set('Commercial')

        else:

            #numero mas cercano
            takeClosest= lambda num,collection:min(collection,key=lambda x:abs(num-x))
            Closest=takeClosest(valor_res,res_comercial)
            print(Closest)

            Nexposicion=res_comercial.index(Closest)


            if valor_res > Closest :
                res_down.set(Closest)
                Nexposicion=Nexposicion+1
                Nexposicion=res_comercial[Nexposicion]
                res_up.set(Nexposicion)

            else:
                Nexposicion=Nexposicion-1
                Nexposicion=res_comercial[Nexposicion]
                res_down.set(Nexposicion)
                res_up.set(Closest)




#Funcion de busqueda de resistores SMD
def smd():
	
	
    smd_value=res_smd.get()
    #validamos letras minusculas
    smd_value=smd_value.upper()
    codeuno=smd_value[:2]
    ceros=smd_value[2:3]
    
    
    #creamos un diccionario
    dic_ceros={'Z':'0.001','Y':'0.01','R':'0.01','X':'0.1','S':'0.1','A':'1','B':'10','H':'10','C':'100','D':'1000','E':'10000','F':'1000000'}
	 

    dic_smd={'01':'100','02':'102','03':'105','04':'107','05':'110','06':'113','07':'115','08':'118','09':'121','10':'124','11':'127','12':'130',
			 '13':'133','14':'137', '15':'140', '16':'143', '17':'147','18':'150','19':'154','20':'158','21':'162','22':'165','23':'169','24':'174',
			 '25':'178','26':'182', '27':'187', '28':'191', '29':'196','30':'200','31':'205','32':'210','33':'215','34':'221','35':'226','36':'232',
			 '37':'237','38':'243', '39':'249', '40':'255', '41':'261','42':'267','43':'274','44':'280','45':'287','46':'294','47':'301','48':'309',
             '49':'316','50':'324', '51':'332', '52':'340', '53':'348','54':'357','55':'365','56':'374','57':'383','58':'392','59':'402','60':'412',
			 '61':'422','62':'432', '63':'442', '64':'453', '65':'464','66':'475','67':'487','68':'499','69':'511','70':'523','71':'536','72':'549',
			 '73':'562','74':'567', '75':'590', '76':'604', '77':'619','78':'634','79':'649','80':'665','81':'681','82':'698','83':'715','84':'732',
			 '85':'750','86':'768', '87':'787', '88':'806', '89':'825','90':'845','91':'866','92':'887','93':'909','94':'931','95':'953','96':'976'

			}   
    
 

    #validamos que lo ingresado sea numeros
    digit=ceros.isdigit()
    
    if digit==False:
	    codeuno=dic_smd.get(codeuno)
	    ceros=dic_ceros.get(ceros)
	    print(type(ceros))
	    ceros=ceros[1:]


    else:
		#(1x10)^ceros
	    ceros=str(10**int(ceros))
	    ceros=ceros[1:]
	    print(codeuno)
	    print(ceros)
	    print("entroo")

    valor=codeuno+ceros
    valor_smd=valor+ 'Ω'
    print(valor_smd)
    #setiamos la  entry de smd
    #res_smd.set(valor_smd)
    resultado_smd.set(valor_smd)



########################################################################
### Rutina de auto completado



# NOTAAAAA
# Si se desea poner autocompletado
# en otra cosa, hay que automatizar para que la variable lista tenga en valor deseado

    dic_smd={'01':'100','02':'102','03':'105','04':'107','05':'110','06':'113','07':'115','08':'118','09':'121','10':'124','11':'127','12':'130',
			 '13':'133','14':'137', '15':'140', '16':'143', '17':'147','18':'150','19':'154','20':'158','21':'162','22':'165','23':'169','24':'174',
			 '25':'178','26':'182', '27':'187', '28':'191', '29':'196','30':'200','31':'205','32':'210','33':'215','34':'221','35':'226','36':'232',
			 '37':'237','38':'243', '39':'249', '40':'255', '41':'261','42':'267','43':'274','44':'280','45':'287','46':'294','47':'301','48':'309',
             '49':'316','50':'324', '51':'332', '52':'340', '53':'348','54':'357','55':'365','56':'374','57':'383','58':'392','59':'402','60':'412',
			 '61':'422','62':'432', '63':'442', '64':'453', '65':'464','66':'475','67':'487','68':'499','69':'511','70':'523','71':'536','72':'549',
			 '73':'562','74':'567', '75':'590', '76':'604', '77':'619','78':'634','79':'649','80':'665','81':'681','82':'698','83':'715','84':'732',
			 '85':'750','86':'768', '87':'787', '88':'806', '89':'825','90':'845','91':'866','92':'887','93':'909','94':'931','95':'953','96':'976'

			}   

lista=['100','102','105','107','110','113','115','118','121','124','127','130','133','137','140','143','147','150','154','158','162','165','169',
'174', '178', '182','187','191','196','200','205','210','215','221','226','232','237','243','249','255','261','267','274','280','287','294','301',
'309','316','324','332','340', '348','357','365','374','383','392','402','412','422','432','442' ,'453','464','475','487','499','511','523','536',
'549','562','567','590','604','619','634','649','665','634','681','698','715','732','750','768','787','806','825','845','866','887','909','931',
'953','976']


#Clase de Autocompletado
   
class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
        
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  
		
        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox(height=3, width= 10)
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    #+self.winfo_height()+27    --> +27 fue agregado porque el autocompletado salia encima del entry. originalmente no existe
                   #self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height()+27)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height()+27)
                    self.lb_up = True
                self.lb.delete(0, END)   
                #TOMANDO EL VALOOR, el valor seleccionado es str1     
                str1 = ''.join(words)
                str=len(str1)
				#guardamos el ultimo valor que suponesmo que sera menor que 7
				#Guardamos en la variable res_smd
                if str < 7:
                    res_smd.set(str1)
                    

                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 


    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]

########################################################################
#Fin de Rutina de Autocompletado
	
	

#Funcion calcular el codigo de colores
def calculo_color():
    #obtenmos el valor numerico
    valor_num=resistor_value.get()
    val1=valor_num[:1]
    val2=valor_num[1:2]
    val3=valor_num[2:]
    val4=valor_num[3:4]


    ceros=len(val3)
    #(1x10)^ceros
    ceros=str(10**int(ceros))
    # ceros=str(ceros)
    ceros=str(len(ceros[1:]))



    #Si es de 4 bandas
    # if len(valor_num)==4:
    #     ceros=int(val4)
    #     #(1x10)^ceros
    #     ceros=10**ceros


    #creamos un diccionario
    #Esta vez buscamos el numero y el contenido es el color
    color_value={'1':'brown','2':'red','3':'orange','4':'yellow','5':'green','6':'blue','violet':'7','gray':'8','9':'white','0':'black'}

    tole_res={'N/A':'20%','Silver':'10%','Golden':'5%','Red':'2%','Brown':'1%','Green':'0.5%', 'Blue':'0.25%','Violet':'0.10%','Gray':'0.05%'}

    #diccionario para setiar el combobox tolerancia segun la banda seleccionada
    combo_tole_dic={'20%':'1','10%':'2','5%':'3','Red':'2%','Brown':'1%','Green':'0.5%', 'Blue':'0.25%','Violet':'0.10%','Gray':'0.05%'}


    banda1=color_value.get(val1)
    banda2=color_value.get(val2)
    banda3=color_value.get(ceros)
    #setiamos el color de la banda1
    label_ban1.configure(bg=banda1)
    label_ban2.configure(bg=banda2)
    label_ban3.configure(bg=banda3)
    # label_ban5.configure(bg=banda5)
    



#Funcion para calcular Resistores
def calculo_res():
    banda1=ban1_combo.get()
    banda2=ban2_combo.get()
    banda3=ban3_combo.get()
    banda4=ban4_combo.get()
    banda5=ban5_combo.get()


    #creamos un diccionario
    color_value={'brown':'1','red':'2','orange':'3','yellow':'4','green':'5','blue':'6','violet':'7','gray':'8','white':'9','black':'0', '10' : 'golden', '100' : 'silver' }

    tole_res={'N/A':'20%','Silver':'10%','Golden':'5%','Red':'2%','Brown':'1%','Green':'0.5%', 'Blue':'0.25%','Violet':'0.10%','Gray':'0.05%'}

    #diccionario para setiar el combobox tolerancia segun la banda seleccionada
    combo_tole_dic={'20%':'1','10%':'2','5%':'3','Red':'2%','Brown':'1%','Green':'0.5%', 'Blue':'0.25%','Violet':'0.10%','Gray':'0.05%'}


    if banda4 == 'none':
        label_ban4.configure(state='disable')
        ban4=' '
        ventana.update()

    if banda5== 'Golden' :
        banda5= 'gold2'
        
    if  banda3  == 'golden':
        banda3 ='gold2'
        
    elif  banda4  == 'golden': 
        banda4 ='gold2'

    #setiamos el color de la banda1
    label_ban1.configure(bg=banda1)
    label_ban2.configure(bg=banda2)
    label_ban3.configure(bg=banda3)
    label_ban5.configure(bg=banda5)


    ban1=color_value.get(banda1)
    ban2=color_value.get(banda2)



    if  banda3 != 'gold2' and banda3 !='silver' and banda4 == 'none' :

        #banda3 multiplicador por ceros
        ban3=int(color_value.get(banda3))
        ban3=str(10**ban3)
        #asignamos solo los ceros
        ban3=ban3[1:]

#Banda 4 activa con algun valor
    elif banda4 != 'none' :
        
        if banda4 == 'gold2':
            ban1=color_value.get(banda1)
            ban2=color_value.get(banda2)
            ban3=color_value.get(banda3)
            ban123= ban1 + ban2 + ban3
            ban123= str(float(ban123)/10)
            valor_resis=ban123+'Ω'
            #setiamos la entry del valor de resisitencia
            resistor_value.set(valor_resis)    
            
        elif banda4 == 'silver':  
            ban1=color_value.get(banda1)
            ban2=color_value.get(banda2)
            ban3=color_value.get(banda3)
            ban123= ban1 + ban2 + ban3
            ban123= str(float(ban123)/100)
            valor_resis=ban123+'Ω'
            #setiamos la entry del valor de resisitencia
            resistor_value.set(valor_resis)             
        
        else:              
            ban4=color_value.get(banda4)
            label_ban4.configure(bg=banda4)
            #banda 3 normal
            ban3=color_value.get(banda3)
            print(banda4)
            #banda4 multiplicador por ceros
            ban4=int(color_value.get(banda4))
            ban4=str(10**ban4)
            ban4=ban4[1:]
            valor_resis=ban1+ ban2 + ban3 + ban4 +'Ω'
            #setiamos la entry del valor de resisitencia
            resistor_value.set(valor_resis)
        

    
# si la banda 3 es silver o golden
    if banda3 == 'gold2':

        ban1=color_value.get(banda1)
        ban2=color_value.get(banda2)
        ban12= ban1 +ban2
        ban12= str(float(ban12)/10)
        valor_resis=ban12+'Ω'
        #setiamos la entry del valor de resisitencia
        resistor_value.set(valor_resis)

    elif banda3 == 'silver':
        ban1=color_value.get(banda1)
        ban2=color_value.get(banda2)
        ban12= ban1 +ban2
        ban12= str(float(ban12)/100)
        valor_resis=ban12+'Ω'
        #setiamos la entry del valor de resisitencia
        resistor_value.set(valor_resis)
        
    elif banda3 != 'gold2' and banda3 !='silver' and banda4 == 'none' :    
        valor_resis=ban1+ ban2 + ban3 + ban4 +'Ω'
        #setiamos la entry del valor de resisitencia
        resistor_value.set(valor_resis)

    #Setiamos la Tolerancia
    tolerancia=banda5
    print(tolerancia)
    #buscamos en el diccionario tole_res
    #tolerancia=tole_res.get(tolerancia)
    #tolera_combo.set(tolerancia)



#   CALCULO DE RESISTORES PARALELO Y SERIE

def res_serie ():
    res1=serier1.get()
    res2=serier2.get()
    #setiamos la firts entry
    serier1.set(res1+res2)
    serier2.set('  ')

def res_paralelo ():
    res1=paralelor1.get()
    res2=paralelor2.get()
    #setiamos la firts entry
    paralelor1.set((res1*res2)/(res1+res2))
    paralelor2.set('  ')


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
pestana3=ttk.Frame(notebook)
notebook.add(pestana,text='Home')
notebook.add(pestana0,text='Capacitors')
notebook.add(pestana1,text='Resistors')
#notebook.add(pestana2,text='Inductors')
notebook.add(pestana2,text='inductors')
notebook.add(pestana3,text='About')



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
    elif event.widget.index("current") == 3:
       pestanan= 3
       print("Inductors")       
    else:
       pestanan= 4
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
##############################################################################
# PESTAÑA ABOUT

#validando el sistema operativo windows o linux
operativo=sys.platform


if operativo=='linux':
	# INFORMACION DEL COMPUTADOR GNU LINUX
	sistema = subprocess.check_output("uname -o ", shell=True).strip();
	distri=subprocess.check_output("uname -r ", shell=True).strip();
	arch=subprocess.check_output("uname -m ", shell=True).strip();
	enblanco = str.encode("  ")
	result= sistema + enblanco + distri + enblanco +arch
	uname=StringVar()
	uname.set(result)
	Label(pestana3,text='Platform:',font='Helvetica 10 bold').place(x=20,y=40)
	Label(pestana3, textvariable=uname,font='Helvetica 10').place(x=87, y=40)
	
	#Tema tkinter para los objetos
	s=ttk.Style()
	s.theme_names()
	#"""======== if you are under win 8.1 you must see ..
	# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative') you can use for example 'clam' ===== """
	s.theme_use('clam')



else :
	# INFORMACION DEL COMPUTADOR WINDOWS
	print ('esta en windows')
#nombre y version de windows con 
#WMIC OS Get Caption   
#arquitecuta con 
#WMIC OS Get Caption   

#texto informativo

Label(pestana3,text='GNU Pytronic',font='Helvetica 10 bold').place(x=20,y=60)
Label(pestana3,text=', software developed by Ronal Forero',font='Helvetica 10').place(x=108,y=60)
Label(pestana3,text='License:',font='Helvetica 10 bold').place(x=20,y=80)
Label(pestana3,text='GPL V.3',font='Helvetica 10').place(x=80,y=80)
Label(pestana3,text='Version:',font='Helvetica 10 bold').place(x=20,y=100)
Label(pestana3,text='Beta 0.1',font='Helvetica 10').place(x=80,y=100)
Label(pestana3,text='Version in development:',font='Helvetica 10 bold').place(x=20,y=120)
Label(pestana3,text='Alpha 0.2',font='Helvetica 10').place(x=180,y=120)
Label(pestana3,text='Contact:',font='Helvetica 10 bold').place(x=20,y=140)
Label(pestana3,text='L337.ronald@gmail.com',font='Helvetica 10').place(x=80,y=140)

#Colaboradores:
Label(pestana3,text='Collaborators:',font='Helvetica 10 bold').place(x=20,y=250)

#artistas
Label(pestana3,text='Artists:',font='Helvetica 10 bold').place(x=20,y=280)
Label(pestana3,text='Pablo Lopez (Icon Pytronic)',font='Helvetica 10').place(x=73,y=280)

#empaquetadores
Label(pestana3,text='Packager:',font='Helvetica 10 bold').place(x=20,y=300)
#Label(pestana3,text='Francisco de la Peña (RPM)',font='Helvetica 10').place(x=90,y=300)

#enlaces
def callback(event):
    webbrowser.open_new(r"https://ronaldl337.wordpress.com/tag/gnu-pytronic/")

link = Label(pestana3, text="GNU Pyttonics Repository", fg="blue", cursor="hand2")
link.place(x=20,y=160)
link.bind("<Button-1>", callback)

def callback(event):
    webbrowser.open_new(r"https://raw.githubusercontent.com/l337quez/GNU-Pytronic/master/other%20Sources/manual.pdf")

link = Label(pestana3, text="User manual", fg="blue", cursor="hand2")
link.place(x=20,y=180)
link.bind("<Button-1>", callback)

##############################################################################
#Pestaña HOME

#la imagen debe tener una dimencion de 600x407
banner=PhotoImage(file="Sources/banner.png")
banner_home=Label(pestana,image=banner).place(x=-1, y=20)


##############################################################################
#Pestaña inductors


#Definimos Variables
code_ind =StringVar() #valor de la resistencia comercial
inductor_value= StringVar()
ind_combo_tole=IntVar() #para setear el combobox de la tolerancia
int_smd=StringVar() #para valor de resistor SMD
resultado_int_smd=StringVar()

#Entry inductors

Entry(pestana2,  width= 10, textvariable=inductor_value).place(x=295, y=54) #value code

#Autocompletado para la entry de resistencias SMD  value code SMD
entry = AutocompleteEntry(lista, pestana2, width= 10)
entry.place(x=90, y=200)
#Entry(ventana,  width= 14, textvariable=res_smd).place(x=90, y=180) 
#entry_aproximar=Entry(ventana,  width= 8).place(x=10, y=400) #aproximar valor

#Botones inductors
Button(pestana2, text= "Calculate", command= calculo_inductores).place(x=383, y=110) #Boton calcular
Button(pestana2, text= "Solve", command= lambda:inductores.calculo_color).place(x=474, y=50) #Boton solve value resistor
Button(pestana2, text= "Solve",command= lambda:inductores.smd).place(x=200, y=196) #Boton solve value resistor SMD

#Labels inductors
ima_inductor=PhotoImage(file="Sources/inductor.png")
banner_home=Label(pestana2,image=ima_inductor).place(x=84, y=40)

smd_label= Label(pestana2, textvariable=resultado_int_smd).place(x=290, y=180)


label_tc=Label(pestana2, text="Color Code:").place(x=10, y=95)
Label(pestana2, text="Value:").place(x=250, y=54)
Label(pestana2, text="SMD Code:").place(x=10, y=200)
label_ban1=Label(pestana2,  height= 2)
label_ban1.place(x=110, y=50)
label_ban2=Label(pestana2,  height= 2)
label_ban2.place(x=130, y=50)
label_ban3=Label(pestana2,  height= 2)
label_ban3.place(x=150, y=50)
label_ban4=Label(pestana2,  height= 2)
label_ban4.place(x=170, y=50)
label_ban5=Label(pestana2, bg="gold2",  height= 2)
label_ban5.place(x=190, y=50)



#######COMBOBOX PARA inductors
#BANDA 1
ban1_combo=ttk.Combobox(pestana2, width= 6, height=3)
ban1_combo.place(x=10, y=115)
ban1_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white' )

#BANDA 2
ban2_combo=ttk.Combobox(pestana2, width= 6,height=3)
ban2_combo.place(x=80, y=115)
ban2_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white','black' )

#BANDA 3
ban3_combo=ttk.Combobox(pestana2, width= 6,height=3)
ban3_combo.place(x=150, y=115)
ban3_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white','black','golden','silver' )
#BANDA 4
ban4_combo=ttk.Combobox(pestana2, width= 6,height=3)
ban4_combo.place(x=220, y=115)
ban4_combo['values']=('none','brown','red','orange','yellow','green', 'blue','violet','gray','white','black','golden','silver'  )
ban4_combo.current(0)

#BANDA 5
ban5_combo=ttk.Combobox(pestana2, width= 6, height=3)
ban5_combo.place(x=290, y=115)
ban5_combo['values']=('Silver','Golden','Red','Brown','Green', 'Blue','Violet','Gray' )
ban5_combo.current(1)

#TOLERANCIA
tolera_combo=ttk.Combobox(pestana2, width= 6, height=3)
tolera_combo.place(x=390, y=54)
tolera_combo['values']=('20%','10%','5%','1%','0.5%', '0.25%','0.10%','0.05%' )
tolera_combo.current(2)



##############################################################################
##############################################################################
#Pestaña Capacitores

#definimos variables
## variables de Capacitores
codigo_cap =StringVar() #codigo del capacitor
valor_cap =StringVar() #valor real del capacitor
volts_cap= StringVar() # voltaje del capacitor
tole_cap= StringVar()
list_tipo_cap= StringVar() #obtener el valor seleccionado en tipo de capacitor
cap_up=StringVar()
cap_down=StringVar()
seriec1=DoubleVar()
seriec2=DoubleVar()
paraleloc1=DoubleVar()
paraleloc2=DoubleVar()


#variables de resistores
code_res =StringVar() #valor de la resistencia comercial
resistor_value= StringVar()
res_up=StringVar()
res_down=StringVar()
combo_tole=IntVar() #para setear el combobox de la tolerancia
res_smd=StringVar() #para valor de resistor SMD
resultado_smd=StringVar()
serier1=DoubleVar()
serier2=DoubleVar()
paralelor1=DoubleVar()
paralelor2=DoubleVar()

#creamos demas objetos

#Entry
#Entry Capacitor
entry_codigo=Entry(pestana0,  width= 10, textvariable=codigo_cap).place(x=10, y=225) #codigo del capacitor
entry_valor=Entry(pestana0,  width= 10, state='readonly', textvariable=valor_cap).place(x=10, y=160) #capacitancia
entry_volt=Entry(pestana0,  width= 10,state='readonly', textvariable=volts_cap).place(x=110, y=160) #voltaje
entry_tol=Entry(pestana0,  width= 10,state='readonly', textvariable=tole_cap).place(x=210, y=160) #tolerancia
entry_comerup=Entry(pestana0,  width= 10, state='readonly',textvariable=cap_up).place(x=280, y=210) #valor comercial disponible
entry_comerdown=Entry(pestana0,  width= 10, state='readonly',textvariable=cap_down).place(x=280, y=240) #valor comercial por debajo
Entry(pestana0,  width= 10,textvariable=paraleloc1).place(x=10, y=360)
Entry(pestana0,  width= 10,textvariable=paraleloc2).place(x=10, y=390)
Entry(pestana0,  width= 10,textvariable=seriec1).place(x=280, y=360)
Entry(pestana0,  width= 10,textvariable=seriec2).place(x=280, y=390)

#Entry Resistors
entry_codigo=Entry(pestana1,  width= 10, textvariable=code_res).place(x=10, y=295) #codigo del resisitor
Entry(pestana1,  width= 10, textvariable=resistor_value).place(x=295, y=54) #value code
Entry(pestana1,  width= 10, state='readonly',textvariable=res_up).place(x=220, y=280) #valor comercial disponible
Entry(pestana1,  width= 10, state='readonly',textvariable=res_down).place(x=220, y=310) #valor comercial por debajo
Entry(pestana1,  width= 10,textvariable=paralelor1).place(x=10, y=360) 
Entry(pestana1,  width= 10,textvariable=paralelor2).place(x=10, y=390)
Entry(pestana1,  width= 10,textvariable=serier1).place(x=280, y=360)
Entry(pestana1,  width= 10,textvariable=serier2).place(x=280, y=390)
#Autocompletado para la entry de resistencias SMD  value code SMD
entry = AutocompleteEntry(lista, pestana1, width= 10)
entry.place(x=90, y=200)
#Entry(pestana1,  width= 14, textvariable=res_smd).place(x=90, y=180) 
#entry_aproximar=Entry(ventana,  width= 8).place(x=10, y=400) #aproximar valor

#Botones
#Botones capacitores
Boton_calcular=Button(pestana0, text= "Calculate", command= calculo_cap).place(x=455, y=58)
Boton_buscar=Button(pestana0, text= "Search", command=buscar_cap).place(x=182, y=220)
Boton_graficar=Button(pestana0, text="Graficar").place(x=410, y=600)
Boton_guardar_data=Button(pestana0, text="Guardar DATA", state='disabled').place(x=10, y=570)
Boton_paralelo=Button(pestana0, text= "+", command=cap_paralelo).place(x=120, y=360)
Boton_serie=Button(pestana0, text= "+", command=cap_serie).place(x=390, y=360)

#Botones resistores
Button(pestana1, text= "Calculate", command= calculo_res).place(x=383, y=110) #Boton calcular
Button(pestana1, text= "Solve", command= calculo_color).place(x=474, y=50) #Boton solve value resistor
Button(pestana1, text= "Solve",command= smd).place(x=200, y=196) #Boton solve value resistor SMD
Button(pestana1, text= "Search", command=buscar_res).place(x=130, y=288) #Boton buscar
Button(pestana1, text= "+", command=res_paralelo).place(x=120, y=360) #Boton_paralelo
Button(pestana1, text= "+", command=res_serie).place(x=390, y=360) #Boton serie


#Labels
#Labels Capacitores
label_cchino=Label(pestana0, text="Parallel Capacitors:").place(x=10, y=340)
label_cchino=Label(pestana0, text="Serial Capacitors:").place(x=280, y=340)
label_cchino=Label(pestana0, text="Comercial value:").place(x=10, y=205)
label_tc=Label(pestana0, text="Type of Capacitor:").place(x=10, y=44)
label_voltaje=Label(pestana0, text="Voltage").place(x=110, y=138)
label_tole=Label(pestana0, text="Tolerance").place(x=210, y=138)
label_ca=Label(pestana0, text="Capacitance").place(x=10, y=138)
label_code=Label(pestana0, text="Capacitor code:").place(x=140, y=44)
Label(pestana0, text="Volts").place(x=140, y=84)
Label(pestana0, text="Capacitance").place(x=231, y=84)
Label(pestana0, text="Tolerance").place(x=342, y=84)
#label dibujo de capacitor
label_dib_cap=Label(pestana0)
label_dib_cap.place(x=450, y=110)


#Labels RESISTORES
ima_resistor=PhotoImage(file="Sources/resistencia.png")
banner_home=Label(pestana1,image=ima_resistor).place(x=84, y=40)

smd_label= Label(pestana1, textvariable=resultado_smd).place(x=290, y=180)

Label(pestana1, text="Parallel Resistors:").place(x=10, y=340)
Label(pestana1, text="Serial Resistors:").place(x=280, y=340)
label_cchino=Label(pestana1, text="Comercial value:").place(x=10, y=273)
label_tc=Label(pestana1, text="Color Code:").place(x=10, y=95)
Label(pestana1, text="Value:").place(x=250, y=54)
Label(pestana1, text="SMD Code:").place(x=10, y=200)
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

Label(pestana1, text="Band 1").place(x=10, y=135)
Label(pestana1, text="Band 2").place(x=80, y=135)
Label(pestana1, text="Band 3").place(x=150, y=135)
Label(pestana1, text="Band 4").place(x=220, y=135)
Label(pestana1, text="Tolerance").place(x=290, y=135)

#COMBOBOX

#   COMBOBOX PARA Capacitores

#combobox codigo de voltaje
vol_combo=ttk.Combobox(pestana0, width= 3, height=3)
vol_combo.place(x=140, y=64)
vol_combo['values']=('0G','0L','0J','1A','1C','1E','1H','1J','1K','2A','2Q','2B','2C','2Z', '2D', '2P', '2E','2F','2V','2G','2W','2H','2J','3A' )


pn_combo=ttk.Combobox(pestana0, width= 3,height=3)
pn_combo.place(x=210, y=64)
pn_combo['values']=('n','p','0','0.5','1','1.2','1.5','1.8','2','2.2','2.7','3','3.3','3.9','4','4.7','5','6','7','8','9')


sn_combo=ttk.Combobox(pestana0, width= 2,height=3)
sn_combo.place(x=255, y=64)
sn_combo['values']=('n','p','0','1','2','3','4','5','6','7','8','9')


cero_combo=ttk.Combobox(pestana0, width= 2,height=3)
cero_combo.place(x=292, y=64)
cero_combo['values']=('n','0','1','2','3','4','5','6','7','8','9')


#Combobox  TOLERANCIA
tole_combo=ttk.Combobox(pestana0, width= 2, height=3)
tole_combo.place(x=355, y=64)
tole_combo['values']=('B','C','D','E','F','G','H','J','K','M','N','P','Z')


#Combobox  convercion pf a uf...
combo=ttk.Combobox(pestana0, width= 2)
combo.place(x=410, y=64)
combo['values']=('f','mf','uf','pf','nf')
combo.current(2)

#Combobox  convercion pf a uf imput comercial...
in_combo=ttk.Combobox(pestana0, width= 2)
in_combo.place(x=110, y=225)
in_combo['values']=('f','mf','uf','pf','nf')
in_combo.current(3)






#######COMBOBOX PARA RESISTORES
#BANDA 1
ban1_combo=ttk.Combobox(pestana1, width= 6, height=3)
ban1_combo.place(x=10, y=115)
ban1_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white' )

#BANDA 2
ban2_combo=ttk.Combobox(pestana1, width= 6,height=3)
ban2_combo.place(x=80, y=115)
ban2_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white','black' )

#BANDA 3
ban3_combo=ttk.Combobox(pestana1, width= 6,height=3)
ban3_combo.place(x=150, y=115)
ban3_combo['values']=('brown','red','orange','yellow','green', 'blue','violet','gray','white','black','golden','silver' )
#BANDA 4
ban4_combo=ttk.Combobox(pestana1, width= 6,height=3)
ban4_combo.place(x=220, y=115)
ban4_combo['values']=('none','brown','red','orange','yellow','green', 'blue','violet','gray','white','black','golden','silver'  )
ban4_combo.current(0)

#BANDA 5
ban5_combo=ttk.Combobox(pestana1, width= 6, height=3)
ban5_combo.place(x=290, y=115)
ban5_combo['values']=('Silver','Golden','Red','Brown','Green', 'Blue','Violet','Gray' )
ban5_combo.current(1)

#TOLERANCIA
tolera_combo=ttk.Combobox(pestana1, width= 6, height=3)
tolera_combo.place(x=390, y=54)
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
list_tc.place(x=10, y=62.5)
#barra de scroll para el listbox
scrollbar_list_tc= Scrollbar(pestana0, width= 12.5, orient="vertical")
scrollbar_list_tc.config(command=list_tc.yview)
scrollbar_list_tc.place(x=110.3, y=64.9)
list_tc.config(yscrollcommand=scrollbar_list_tc.set)
list_tc.select_set(0)
#list_tc.selectedindex = 0
list_tc.event_generate("<<ListboxSelect>>")
list_tc.bind('<<ListboxSelect>>',select_image_cap)





########################################################################
ventana.geometry("600x450+0+0")
#icono del software 
ventana.call('wm','iconphoto',ventana._w,PhotoImage(file='pytronics.png'))

ventana.resizable(False, False)
ventana.mainloop()
