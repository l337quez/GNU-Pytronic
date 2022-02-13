class capacitor(str):
    def __init__(self, src_string):
        self._data = src_string

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
