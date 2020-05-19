
from tkinter import *
from tkinter import ttk
import os
import sys
import subprocess
import re
import webbrowser
from tkinter import filedialog

#####################################################################



 
########################################################################

#INDUCTORES SMD
#https://www.youtube.com/watch?v=b37zyN8WZiE
#http://www.inprocorp.co.kr/powerinductor.pdf

#http://www.incb.com.mx/index.php/articulos/9-articulos-tecnicos-y-proyectos/942-como-calcular-y-enrollar-pequenos-inductores-art170s
#http://www.lu1cgb.com.ar/Inductores.htm


#Funciones para la pestaña resisitencia
def buscar_res():
    valor_res= code_res.get()
    #validamos que lo ingresado sea numeros
    digit=valor_res.isdigit()


    if  digit==False and re.match("^\d+?\.\d+?$",valor_res) is None:

        codigo.set('ERROR')

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
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
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





#####################################################################
#Construyendo la ventana
ventana = Tk()
ventana.title("GNU Pytronics") #Titulo de la ventana
#Dimencion de la ventana
ventana.geometry("600x450+0+0")







#definimos variables



#variables de resistores
code_res =StringVar() #valor de la resistencia comercial
resistor_value= StringVar()
res_up=StringVar()
res_down=StringVar()
combo_tole=IntVar() #para setear el combobox de la tolerancia
res_smd=StringVar() #para valor de resistor SMD
resultado_smd=StringVar()


#creamos demas objetos

#Entry
#Entry Capacitor


#Entry Resistors

Entry(ventana,  width= 10, textvariable=resistor_value).place(x=295, y=54) #value code


#Entry(ventana,  width= 14, textvariable=res_smd).place(x=90, y=180) 
#entry_aproximar=Entry(ventana,  width= 8).place(x=10, y=400) #aproximar valor

#Botones

#Botones resistores
Button(ventana, text= "Calculate", command= calculo_res).place(x=383, y=110) #Boton calcular



#Labels
#Labels Capacitores


#Labels RESISTORES
ima_resistor=PhotoImage(file="Sources/inductor.png")
banner_home=Label(ventana,image=ima_resistor).place(x=84, y=40)

smd_label= Label(ventana, textvariable=resultado_smd).place(x=290, y=180)


label_tc=Label(ventana, text="Color Code:").place(x=10, y=95)
Label(ventana, text="Value:").place(x=250, y=54)

label_ban1=Label(ventana,  height= 2)
label_ban1.place(x=110, y=50)
label_ban2=Label(ventana,  height= 2)
label_ban2.place(x=130, y=50)
label_ban3=Label(ventana,  height= 2)
label_ban3.place(x=150, y=50)
label_ban4=Label(ventana,  height= 2)
label_ban4.place(x=170, y=50)
label_ban5=Label(ventana, bg="gold2",  height= 2)
label_ban5.place(x=190, y=50)

#COMBOBOX






#######COMBOBOX PARA RESISTORES
#BANDA 1





#########################################################################



ventana.mainloop()
