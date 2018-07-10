
#funcion para buscar valor de capacitores comerciales
def buscar_cap():
    numero= codigo.get()
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


