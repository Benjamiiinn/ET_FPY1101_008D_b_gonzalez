import random
import statistics as st
import csv

trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
sueldos=[]

def menu(titulo,lista):
    print('=================================')
    print(titulo.upper())
    print('=================================')
    while True:
        i=1
        for item in lista:
            print(i,'.-',item)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('La opción debe estar entre 1 y ',i)
        else:
            print('Debe Ingresar un Número')

def sueldos_random():
    global sueldos
    sueldos=[random.randint(300000,2500000) for _ in range(10)]
    print("SUELDOS ASIGNADOS ALEATORIAMENTE")

def ordenar_sueldos():
    global sueldos
    sueldos.sort()
    print("SUELDOS CLASIFICADOS CORRECTAMENTE")

def ver_clasificacion():
    global trabajadores, sueldos

    if not sueldos:
        print("¡PRIMERO DEBES ASIGNAR LOS SUELDOS ALEATORIAMENTE!")
        return
    
    sueldos_menor_800k=[]
    sueldos_entre_800_2m=[]
    sueldos_mayor_2m=[]

    for i in range(len(trabajadores)):
        nombre=trabajadores[i]
        sueldo=sueldos[i]

        if sueldo<800000:
            sueldos_menor_800k.append((nombre,sueldo))
        elif sueldo>=800000 and sueldo<=2000000:
            sueldos_entre_800_2m.append((nombre,sueldo))
        else:
            sueldos_mayor_2m.append((nombre,sueldo))

    print("Sueldos menores a 800.000")
    print("TOTAL: ",len(sueldos_menor_800k))
    print("Nombre empleado  Sueldo")
    for nombre,sueldo in sueldos_menor_800k:
        print(nombre,"$" ,sueldo)
    
    print("Sueldos entre 800.000 y 2.000.000")
    print("TOTAL: ",len(sueldos_entre_800_2m))
    print("Nombre empleado  Sueldo")
    for nombre,sueldo in sueldos_entre_800_2m:
        print(nombre,"$" , sueldo)
    
    print("Sueldos superiores a 2.000.000")
    print("TOTAL: ",len(sueldos_mayor_2m))
    print("Nombre empleado  Sueldo")
    for nombre,sueldo in sueldos_mayor_2m:
        print(nombre,"$" , sueldo)

def total_sueldos():
    global sueldos
    return print("TOTAL SUELDOS: $",sum(sueldos))

def estadisticas():
    global sueldos, trabajadores

    if not sueldos:
        print("¡PRIMERO DEBES ASIGNAR LOS SUELDOS ALEATORIAMENTE!")
        return
    
    sueldo_mas_alto=max(sueldos)
    sueldo_minimo=min(sueldos)
    promedio=st.mean(sueldos)
    media_geo=st.geometric_mean(sueldos)
    print("SUELDO MAS ALTO: $",sueldo_mas_alto)
    print("SUELDO MAS BAJO: $",sueldo_minimo)
    print("PROMEDIO DE LOS SUELDOS: $",promedio)
    print("MEDIA GEOMETRICA DE LOS SUELDOS: $",media_geo)

def dscto_salud(sueldo):
    return sueldo*0.07

def dscto_afp(sueldo):
    return sueldo*0.12

def sueldo_liquido(sueldo):
    return sueldo-sueldo*0.07-sueldo*0.12

def reporte_sueldo():
    global trabajadores, sueldos
    datos={"Nombre":trabajadores,"Sueldo Base":sueldos,"Descuento Salud":dscto_salud,"Descuento AFP":dscto_afp,"Sueldo Liquido":sueldo_liquido}
    with open('reporte_sueldo.csv', mode='w', newline='') as archivo:
            writer=csv.writer(archivo)
            writer.writerow(datos)

while True:
    opc=menu('menu principal',['Asignar Sueldos Aleatorios',"Clasificar Sueldos",'Ver Estadisticas',"Reporte de Sueldos"])
    if opc==1:
        sueldos_random()
    elif opc==2:
        ordenar_sueldos()
        ver_clasificacion()
        total_sueldos()
    elif opc==3:
        estadisticas()
    elif opc==4:
        reporte_sueldo()
    else:
        print("Finalizando programa...")
        print("Desarrollado por Benjamin Gonzalez")
        print("RUT 21.719.226-9")
        break