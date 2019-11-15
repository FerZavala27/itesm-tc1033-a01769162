with open ("datos_vuelos.csv", "r") as archivo:
    lines=archivo.readlines()
    dmp={}
    dmp1={}
    dicpor={}
    #l= cada linea en especific
    for l in lines:
        datos=l.split(",")
        pais=datos[0][0:5]
        mes=datos[1][3:5]
        if mes in dmp:
            dmp[mes]+=1
        else:
            dmp[mes]=1
        if mes not in dmp1:
            dmp1[mes]={} 
        if pais in dmp1[mes]:
            dmp1[mes][pais]+=1
        else:
            dmp1[mes][pais]=1
    f=open("resultados.csv","w+")
    for mes in dmp1:
        for pais in dmp1[mes]:
            por=(dmp1[mes][pais]/dmp[mes])*100
            if por>=20:
                
                f.write(mes+","+pais+","+str(por)+"\n")
    f.close()
        
#prueba
