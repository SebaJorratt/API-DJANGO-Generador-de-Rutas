import math
import numpy as np
import time as calculoTiempos

def algoritmo(cl):
    
    start = calculoTiempos.time()
    print("The time used to execute this is given below")

    Codigos = []
    tip = []
    sectores = []
    demandas = []
    longitudes = []
    latitudes = []
    clientes = []
    zonasF = []
    zonas = ['Tierras Blancas', 'Ovalle', 'La Florida', 'Pampa Sur', 'Coquimbo', 'Monte Patria', 'Punitaqui', 'Cerrillos', 'La Serena', 'Pampa Norte', 'Valle del Elqui', 'La Herradura', 'Andacollo', 'La Cantera', 'Pan de Azucar', 'Las Compañias', 'Tongoy']
    nodos = []
    macrozonasF = []

    for i in range(len(cl)):
        demandas.append(float(cl[i]['demanda']))
        Codigos.append(cl[i]['codigo'])
        sectores.append(cl[i]['sector'])
        tip.append(cl[i]['tipo'])
        longitudes.append(cl[i]['longitud'])
        latitudes.append(cl[i]['latitud'])
        zonasF.append(cl[i]['zona'])
        macrozonasF.append(cl[i]['macrozona'])
        clientes.append(i)
        nodos.append(i)

    arcos = [(i,j) for i in nodos for j in nodos if i!=j ]

    import math
    distancia = {(i,j): 6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i]))) for i in nodos for j in nodos if i!=j}
    time = {}
    traslado = {}
    for i in nodos: 
        for j in nodos:
                if i != j:
                    
                    if zonasF[i] == "Ovalle" or zonasF[i] =="Combarbala" or zonasF[i] =="Punitaqui" or zonasF[i] =="Cerrillos" or zonasF[i] =="Monte Patria" or  zonasF[i] == "Tulahuen" or zonasF[i] =="Valle del Elqui"  and zonasF[j] == "deposito":   
                            
                            time[(i,j)] = (60/100)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))
                            traslado[(i,j)] = (60/100)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))
                    
                    elif zonasF[i] == "deposito" and zonasF[j] == "Ovalle" or zonasF[i] =="Combarbala" or zonasF[i] =="Punitaqui" or zonasF[i] =="Punitaqui" or zonasF[i] =="Cerrillos" or zonasF[i] =="Monte Patria" or zonasF[i] == "Tulahuen" or zonasF[i] =="Valle del Elqui" :
                        
                            time[(i,j)] = (60/100)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))
                            traslado[(i,j)] = (60/100)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))
                    
                    elif zonasF[i] == "Andacollo"  and zonasF[j] == "deposito":   
                            
                            time[(i,j)] = (60/75)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))
                            traslado[(i,j)] = (60/75)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))
                    
                    elif zonasF[i] == "deposito" and zonasF[j] == "Andacollo" :
                        
                            time[(i,j)] = (60/75)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))
                            traslado[(i,j)] = (60/75)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))
                    
                
                
                    else:
                            time[(i,j)] =  (60/50)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i]))) 
                            traslado[(i,j)]  =   (60/50)*6371*math.acos(math.cos(math.radians(90-latitudes[j]))*math.cos(math.radians(90-latitudes[i]))+math.sin(math.radians(90-latitudes[j]))*math.sin(math.radians(90-latitudes[i]))*math.cos(math.radians(longitudes[j]-longitudes[i])))

    ts = 120
    tt = 12
    n = []
    for i in range(len(nodos)):
        for j in range(len(nodos)):
            if i == j:
                n.append(0)
            else:
                if tip[i] == "Supermercados":
                    time[(i,j)] = time[(i,j)] + ts
                
                else:
                        if tip[i] == "Tradicional" or tip[i] == "Foodservice" or  tip[i] == "Grandes Clientes":
                            time[(i,j)] = time[(i,j)] + tt       
    
    supe = []
    dec = []
    # Parametros pot Zonas
    solucion = []
    SolucionF = []
    lista = []
    zon = []
    tipo_ord = []
    ruta = []
    for x in range(len(zonas)):
        s = []    
        Lat = []    
        Long  = []
        Dem = []
        Sec = [] 
        Tip = []
        nodos = []   
        jep = []    
        macro = []
        for j in range(len(zonasF)):
            if zonas[x] == zonasF[j] :
                
                Lat.append(latitudes[j])
                Long.append(longitudes[j])
                Dem.append(demandas[j])
                nodos.append(j)
                macro.append(macrozonasF[i])
                Sec.append(sectores[j])
                jep.append(clientes[j])
                Tip.append(tip[j])
        
        #print(jep)
    ##############################################################################################  
        
    #Equilibrio de Cargas    

        if sum(Dem) > 0:
            C = math.ceil(sum(Dem)/5000) 
            Q = sum(Dem)/C
            
            if Q >= 4000:
                Q = 5000
            else:
                Q = Q + 1000
        
        else:
            Q = 0
        
    #############################################################################################  

    #Orden de Pararametros segun angulo menor

        angulos = []
        
        for i in range(len(Lat)):
            ang = np.arctan2((Lat[i]-latitudes[0]),(Long[i]-longitudes[0]))
            angulos.append(ang)
        
        angulos.sort(reverse=True)

        angulo = []
        for i in range(len(Lat)):
            ang = np.arctan2((Lat[i]-latitudes[0]),(Long[i]-longitudes[0]))
            angulo.append(ang)


            
        longitudes_ord = []
        latitudes_ord =[]
        clientes_ord = []
        demanda_ord = []
        sectores_ord = []
        tipos_ord = []
        macro_ord = []
        for i in range(len(Lat)):
            for j in range(len(Lat)):
                if angulos[i] == angulo[j]:
                        longitudes_ord.append(Long[j])
                        latitudes_ord.append(Lat[j])
                        clientes_ord.append(jep[j])
                        demanda_ord.append(Dem[j])
                        sectores_ord.append(Sec[j])
                        tipos_ord.append(Tip[j])
                        macro_ord.append(macro[j])
                else:
                    continue

        
        for i in range(len(tipos_ord)):
            if tipos_ord[i] == "Supermercados":
                supe.append(sectores_ord[i])
                dec.append(demanda_ord[i])
        
        

        vehiculos = 17


        dem = 0
        aux = [0]
        aux2 = []
        contador = 0
        rec = 0
        
        for i in range(len(Dem)):
            
            
            if  tipos_ord[i] != "Supermercados"  and demanda_ord[i] > 1200:
                        solucion.append([0,clientes_ord[i],0])
                        lista.append([0,clientes_ord[i],0])
                        zon.append(x)
            
            else:
                        if tipos_ord[i] == "Supermercados":
                            contador = contador + 1

                        if i != 0:

                            rec = rec + time[(clientes_ord[i-1],clientes_ord[i])]
                        else:
                            rec = rec + time[(0,clientes_ord[i])]





                        dem = dem + demanda_ord[i]
                        if (dem <= 5000 or zonas[x] == "Tierras Blancas") and contador<3 and (rec + time[(clientes_ord[i]),0] <=620 or zonas[x] == "Tierras Blancas"):
                            aux.append(clientes_ord[i])
        

                            aux2.append((clientes_ord[i]))
                        else:
                            contador = 0
                            rec = 0
                            aux.append(0)
                            #print(time[(clientes_ord[i-1],0)])
                            s.append(aux)
                            ruta.append(zonas[x])
                            zon.append(x)
                            lista.append(aux)
                            dem = demanda_ord[i]
                            if tipos_ord[i] == "Supermercados":
                                contador = contador + 1
                                
                            aux = [0]
                            aux2 = []
                            aux.append(clientes_ord[i])

                            rec = rec + time[(0,clientes_ord[i])]

        
        
        aux.append(0)
        s.append(aux)
        zon.append(x)
        lista.append(aux)
        solucion.append(s)
        
    

        for i in range(len(tipos_ord)):
            if tipos_ord[i] != []:
                tipo_ord.append(tipos_ord[i])
 
    orden = []
    for i in range(len(lista)):
        if sum(lista[i]) > 0:
            SolucionF.append(lista[i])
            orden.append(zon[i])

    d = []
    for i in range(len(SolucionF)):
        dem = 0
        
        for j in range(len(SolucionF[i])):
            dem = dem + demandas[SolucionF[i][j]]
        d.append(dem)

    t = []
    suma = 0
    for i in range(len(SolucionF)):
                if suma != 0:
                    suma = 0
                for j in range(len(SolucionF[i])):
                        if j == len(SolucionF[i]) - 1:
                            suma = suma + 0
                        else:
                            
                            m = time[SolucionF[i][j],SolucionF[i][j+1]]
                        
                        suma = suma + m
                t.append(suma)

    CantS = []
    for i in range(len(SolucionF)):
        cont = 0
        for j in range(len(SolucionF[i])):
            if tip[SolucionF[i][j]] == "Supermercados":
                cont = cont +1
        CantS.append(cont)

    ruta = []

    for i in range(len(SolucionF)):
        ruta.append(zonasF[SolucionF[i][-2]])

    CantS = []

    for i in range(len(SolucionF)):
        cont = 0
        for j in range(len(SolucionF[i])):
            if tip[SolucionF[i][j]] == "Supermercados":
                cont = cont +1
        CantS.append(cont)

    ruta = []

    for i in range(len(SolucionF)):
        ruta.append(zonasF[SolucionF[i][1]])

    for i in range(len(SolucionF)):
        pos = -9999999
        maxC =  -99999999
        for j in range(len(SolucionF)):
            
            if ruta[i] == ruta[j] and i != j:
                
                if d[i] < 4000 and i != j and SolucionF[j] != []:
                    if d[i] + d[j] <= 5000 and CantS[i] + CantS[j] <= 2 and t[i] + t[j] <= 620:
                        if d[i] + d[j] > maxC :
                            maxC = d[i] + d[j]
                            pos = j
                        
        if maxC > 0 and maxC != 99999999 :
                SolucionF[i].pop(len(SolucionF[i])-1)
                for k in range(1,len(SolucionF[pos])-1):
                            SolucionF[i].append(SolucionF[pos][k])

                d[i] = d[i] + d[pos]
                CantS[i] = CantS[i] + CantS[pos]
                t[i] = t[i] + t[pos] 
                ruta[pos] = "xxxxxxxxxx"
                SolucionF[pos] = []

                d[pos] = 10000
                t[pos] = 1000
                SolucionF[i].append(0)  
                CantS[pos] = 100

    tf = []

    for i in range(len(t)):
        if t[i] != 1000:
            tf.append(t[i])

    demF = []

    for i in range(len(d)):
        if d[i] != 10000:
            demF.append(d[i])

    CantSuper = []
    for i in range(len(d)):
        if CantS[i] != 100:
            CantSuper.append(CantS[i])

    SolucionFinal = []
    for i in range(len(SolucionF)):
        if SolucionF[i] != []:
            SolucionFinal.append(SolucionF[i])

    for i in range(len(CantSuper)):
    
        if CantSuper[i] == 1:

                    for j in range(len(SolucionFinal[i])):
                        aux = SolucionFinal[i][1]
                        if tip[SolucionFinal[i][j]] == "Supermercados":
                            SolucionFinal[i][1] = SolucionFinal[i][j]
                            SolucionFinal[i][j] = aux

        if CantSuper[i] == 2:

                for j in range(len(SolucionFinal[i])):
                        aux2 = SolucionFinal[i][1]
                        
                        if tip[SolucionFinal[i][j]] == "Supermercados":
                            SolucionFinal[i][1] = SolucionFinal[i][j]
                            SolucionFinal[i][j] = aux2
                            break
            
                for z in range(2,len(SolucionFinal[i])):
                        aux3 = SolucionFinal[i][2]
                        if tip[SolucionFinal[i][z]] == "Supermercados":
                                    SolucionFinal[i][2] = SolucionFinal[i][z]
                                    SolucionFinal[i][z] = aux3
        if CantSuper[i] == 0:
                    continue

    d = []
    suma = 0
    for i in range(len(SolucionFinal)):
                if suma != 0:
                    suma = 0
                for j in range(len(SolucionFinal[i])):
                        if j == len(SolucionFinal[i]) - 1:
                            suma = suma + 0
                        else:
                            
                            m = distancia[SolucionFinal[i][j],SolucionFinal[i][j+1]]
                        
                        suma = suma + m
                d.append(suma)

    Nodos= []
    Nod = []

    for i in range(len(CantSuper)):
        if CantSuper[i] == 1:
            
            if len(SolucionFinal[i])  <= 3:
                Nodos.append(SolucionFinal[i])
                Nodos[i].pop()
                Nod.append(0)
        
            else:
                
                a1 = []
                b1 = []
                for j in range(len(SolucionFinal[i])-1):

                    if j > 0 :
                        a1.append(SolucionFinal[i][j])

                    else:
                        b1.append(0)

                Nodos.append(a1) 

                Nod.append(b1)
            
            
            
        if CantSuper[i] == 2:
            if len(SolucionFinal[i])  <= 4 :
                Nodos.append(SolucionFinal[i])
                Nodos[i].pop()
                Nod.append(0)
            else:
                a2 = []
                b2 = []
                for j in range(len(SolucionFinal[i])-1):
                    if j > 1:
                        a2.append(SolucionFinal[i][j])

                    else:
                        b2.append(SolucionFinal[i][j])

                Nodos.append(a2) 
                Nod.append(b2)
            
            
        if CantSuper[i] == 0:
            
            a = []
            
            for j in range(len(SolucionFinal[i])-1):
                a.append(SolucionFinal[i][j])
            
            Nodos.append(a)
            Nod.append(0)

    SolFinal = []
    for i in range(len(Nodos)):
            starting_node= Nodos[i][0]
            NN=[starting_node]
            while len(NN)<=len(Nodos[i])-1:
                    k=NN[-1]
                    nn={(k,Nodos[i][j]): distancia[(k,Nodos[i][j])] for j in range(len(Nodos[i])) if Nodos[i][j] !=k and  Nodos[i][j]not in NN}
                    nn.items()
                
                    new=min(nn.items(), key=lambda x: x[1]) 
                    NN.append(new[0][1])
        
            NN.append(0)
            SolFinal.append(NN)

    for i in range(len(Nod)):
        if Nod[i] != 0:
            SolFinal[i] = Nod[i] + SolFinal[i]

    t2 = []
    suma = 0
    for i in range(len(SolFinal)):
                if suma != 0:
                    suma = 0
                for j in range(len(SolFinal[i])):
                        if j == len(SolFinal[i]) - 1:
                            suma = suma + 0
                        else:
                            
                            m = time[SolFinal[i][j],SolFinal[i][j+1]]
                
                            suma = suma + m
                t2.append(suma)

    sumaDemandas = []
    for i in range(len(SolFinal)):
        dem = 0
        
        for j in range(len(SolFinal[i])):
            dem = dem + demandas[SolFinal[i][j]]
        sumaDemandas.append(dem)

    for i in range(len(SolFinal)):
        dem = 0
        
        for j in range(len(SolFinal[i])):
            dem = dem + demandas[SolFinal[i][j]]

    Macroruta = []

    for i in range(len(SolFinal)):
        Macroruta.append(macrozonasF[SolFinal[i][-2]])

    ordFinal = []

    for i in range(len(SolFinal)):
        pos = -9999999
        maxC =  99999999
        for j in range(len(SolFinal)):
            
            if sumaDemandas[i] < 4000 and i != j and SolFinal[j] != []:
                if sumaDemandas[i] + sumaDemandas[j] <= 5000 and CantSuper[i] + CantSuper[j] <= 2 and t2[i] + t2[j] <= 680 and (Macroruta[i] == Macroruta[j] or Macroruta[j] == "Andacollo" or  Macroruta[j] == "Tierras Blancas"):  
                    if traslado[(SolFinal[i][len(SolFinal[i])-2],SolFinal[j][1])] < maxC :
                        maxC = traslado[(SolFinal[i][len(SolFinal[i])-2],SolFinal[j][1])] 
                        pos = j
                        
        if maxC > 0 and maxC != 99999999 :
                SolFinal[i].pop(len(SolFinal[i])-1)
                for k in range(1,len(SolFinal[pos])-1):
                            SolFinal[i].append(SolFinal[pos][k])

                sumaDemandas[i] = sumaDemandas[i] + sumaDemandas[pos]
                CantSuper[i] = CantSuper[i] + CantSuper[pos]
                t2[i] = t2[i] + t2[pos] 

                SolFinal[pos] = []
                sumaDemandas[pos] = 10000000
                t2[pos] = 1000
                SolFinal[i].append(0)  
                CantSuper[pos] = 100

    tFinal = []

    for i in range(len(t2)):
        if t2[i] != 1000:
            tFinal.append(t2[i])

    cFinal = []

    for i in range(len(CantSuper)):
        if CantSuper[i] != 100:
            cFinal.append(CantSuper[i])

    cap = []
    for i in range(len(SolucionFinal)):
        dem = 0
        
        for j in range(len(SolucionFinal[i])):
            dem = dem + demandas[SolucionFinal[i][j]]
        cap.append(5000-dem)
        sumaDemandas.append(dem)


    SoluFinal = []
    for i in range(len(SolFinal)):
        if SolFinal[i] != []:
            SoluFinal.append(SolFinal[i])

    deman = []
    for i in range(len(SoluFinal)):
        dem = 0
        
        for j in range(len(SoluFinal[i])):
            dem = dem + demandas[SoluFinal[i][j]]
        deman.append(dem)

    cap = []
    for i in range(len(SoluFinal)):
        dem = 0
        
        for j in range(len(SoluFinal[i])):
            dem = dem + demandas[SoluFinal[i][j]]
        cap.append(5000-dem)
        sumaDemandas.append(dem)

    for i in range(len(cFinal)):
        if cFinal[i] == 1:

                    for j in range(len(SoluFinal[i])):
                        aux = SoluFinal[i][1]
                        if tip[SoluFinal[i][j]] == "Supermercados":
                            SoluFinal[i][1] = SoluFinal[i][j]
                            SoluFinal[i][j] = aux

        if cFinal[i] == 2:

                for j in range(len(SoluFinal[i])):
                        aux2 = SoluFinal[i][1]
                        
                        if tip[SoluFinal[i][j]] == "Supermercados":
                            SoluFinal[i][1] = SoluFinal[i][j]
                            SoluFinal[i][j] = aux2
                            break
            
                for z in range(2,len(SoluFinal[i])):
                        aux3 = SoluFinal[i][2]
                        if tip[SoluFinal[i][z]] == "Supermercados":
                                    SoluFinal[i][2] = SoluFinal[i][z]
                                    SoluFinal[i][z] = aux3
        if cFinal[i] == 0:
                    continue

    Nodos= []
    Nod = []

    for i in range(len(cFinal)):
        if cFinal[i] == 1:
            
            if len(SoluFinal[i])  <= 3:
                Nodos.append(SoluFinal[i])
                Nodos[i].pop()
                Nod.append(0)
        
            else:
                
                a1 = []
                b1 = []
                for j in range(len(SoluFinal[i])-1):

                    if j > 0 :
                        a1.append(SoluFinal[i][j])

                    else:
                        b1.append(0)

                Nodos.append(a1) 

                Nod.append(b1)
            
            
            
        if cFinal[i] == 2:
            if len(SoluFinal[i])  <= 4 :
                Nodos.append(SoluFinal[i])
                Nodos[i].pop()
                Nod.append(0)
            else:
                a2 = []
                b2 = []
                for j in range(len(SoluFinal[i])-1):
                    if j > 1:
                        a2.append(SoluFinal[i][j])

                    else:
                        b2.append(SoluFinal[i][j])

                Nodos.append(a2) 
                Nod.append(b2)
            
            
        if cFinal[i] == 0:
            
            a = []
            
            for j in range(len(SoluFinal[i])-1):
                a.append(SoluFinal[i][j])
            
            Nodos.append(a)
            Nod.append(0)

    SolucionRutas = []
    for i in range(len(Nodos)):
            starting_node= Nodos[i][0]
            NN=[starting_node]
            while len(NN)<=len(Nodos[i])-1:
                    k=NN[-1]
                    nn={(k,Nodos[i][j]): distancia[(k,Nodos[i][j])] for j in range(len(Nodos[i])) if Nodos[i][j] !=k and  Nodos[i][j]not in NN}
                    nn.items()
                    new=min(nn.items(), key=lambda x: x[1]) 
                    NN.append(new[0][1])
                

            NN.append(0)
            SolucionRutas.append(NN)


    for i in range(len(Nod)):
        if Nod[i] != 0:
            SolucionRutas[i] = Nod[i] + SolucionRutas[i]

    for i in range(len(SolucionRutas)):
        if cFinal[i] == 2 and len(SolucionRutas[i]) > 5:
            if zonasF[SolucionRutas[i][2]] != zonasF[SolucionRutas[i][3]] and zonasF[SolucionRutas[i][1]] == zonasF[SolucionRutas[i][3]]:
                cambio = SolucionRutas[i][1]
                SolucionRutas[i][1] = SolucionRutas[i][2]
                SolucionRutas[i][2] = cambio

    cantidad = []

    for i in range(len(SolucionRutas)):
        cont = 0
        for j in range(len(SolucionRutas[i])):
            if SolucionRutas[i][j] != 0:
            
                if tip[SolucionRutas[i][j]] != "Supermercados" :
                    cont = cont + 1
                else:
                    cont = cont + 12
        cantidad.append(cont)


    deman = []
    for i in range(len(SolucionRutas)):
        dem = 0
        
        for j in range(len(SolucionRutas[i])):
            dem = dem + demandas[SolucionRutas[i][j]]
        deman.append(dem)


    tiempo = []
    suma = 0
    for i in range(len(SolucionRutas)):
                if suma != 0:
                    suma = 0
                for j in range(len(SolucionRutas[i])):
                        if j == len(SolucionRutas[i]) - 1:
                            suma = suma + 0
                        else:
                            
                            m = time[SolucionRutas[i][j],SolucionRutas[i][j+1]]
                
                            suma = suma + m
                tiempo.append(suma)

    distan = []
    suma = 0
    for i in range(len(SolucionRutas)):
                if suma != 0:
                    suma = 0
                for j in range(len(SolucionRutas[i])):
                        if j == len(SolucionRutas[i]) - 1:
                            suma = suma + 0
                        else:
                            
                            m = distancia[SolucionRutas[i][j],SolucionRutas[i][j+1]]
                
                            suma = suma + m
                distan.append(suma)

    '''a = 0
    for i in range(len(SolucionRutas)):
        print("RUTA", i+1)
        for j in range(len(SolucionRutas[i])):
            print(sectores[SolucionRutas[i][j]],demandas[SolucionRutas[i][j]],SolucionRutas[i][j])
            if sectores[SolucionRutas[i][j]] != "sucursal":
                a = a +1
            
        print("CANTIDAD =",cantidad[i])
        print("DEMANDA =", deman[i])
        print("TIEMPO =",tiempo[i])
        print("DISTANCIA =", distan[i])
        print("===============================") '''

    end = calculoTiempos.time()
    print(end - start)
        
    return SolucionRutas
    #return [[0, 30, 8, 6, 16, 9, 19, 23, 25, 27, 7, 3, 12, 20, 2, 26, 10, 13, 28, 22, 18, 0],[0, 29, 24, 5, 11, 1, 4, 17, 21, 14, 15, 0]] #Resultado de vecino mas cercano
    #return [[0, 13, 26, 28, 10, 30, 9, 16, 19, 20, 2, 3, 7, 25, 27, 12, 22, 18, 23, 8, 6, 0], [0, 29, 1, 4, 17, 21, 14, 15, 11, 5, 24, 0]] #Resultado del algoritmo genético
