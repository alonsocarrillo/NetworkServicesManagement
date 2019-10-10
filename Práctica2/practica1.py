from getSNMP import consultaSNMP
from generarPDF import generarReportePDF
from cpuUsage import iniciarCPU
from ramUsage import iniciarRAM
from graphCPUUsage import graficarCPU
from graphCPUUsage import graficarRAM
from Detección import detectar
import threading
import time

print("---------- PRACTICA 2 ----------")
print("--------------------------------")

archivo = open("agentes.txt", "r")

misAgentes = []

for ag in archivo.readlines():
    #print(ag)
    misAgentes.append(ag)
    a = ag.split(',')
    com = a [0]
    dir = a [1]
    #print(agente)

archivo.close()

#AgregarUsuario
def agregarAgente():
    print("---------- Agregar Agente ----------")
    archivo = open("agentes.txt", "r")

    misAgentes = []

    for ag in archivo.readlines():
        misAgentes.append(ag)
        a = ag.split(',')

    archivo.close()

    idx = misAgentes[-1][0]
    ix = int(idx)
    index = ix + 1
    print("-> Nombre de la comunidad:")
    comunidad = input()
    print("-> Dirección IP:")
    direccion = input()

    archivo = open("agentes.txt", "a+")
    nuevoAgente = str(index)+","+comunidad+","+direccion
    archivo.write("\n"+nuevoAgente)
    print(nuevoAgente)
    archivo.close()

#EliminarUsuario
def eliminarAgente():
    print("---------- Eliminar Agente ----------")
    archivo = open("agentes.txt", "r")

    misAgentes = []

    for ag in archivo.readlines():
        misAgentes.append(ag)
        a = ag.split(',')
        print(a)

    archivo.close()
    print("¿Qué agente va a eliminar")
    e = int(input())
    e = e - 1;

    print("Ha seleccionado: "+misAgentes[e])
    print("¿Está seguro de querer eliminar este agente? (y/n)")
    el = input()

    if el == "y":
        print("Eliminando ...")
        misAgentes.remove(misAgentes[e])
        ags = misAgentes[-1]
        a = ags.split(',')
        print(misAgentes)

        param = int(misAgentes[-1][0]) -1
        print(param)

        file = open("agentes.txt", "w")
        for i in range(param):
            file.write(misAgentes[i])
        file.close()

        print("Se eliminó exitosamente")


    elif el == "n":
        print("Operación cancelada")
        print("Regresando a menú principal ... ")
        mostrarMenu()



#Menu Usuario
def mostrarMenu():
    print ("¡Buen día! Seleccione una opción")
    print("1. Agregar agente")
    print("2. Eliminar agente")
    print("3. Continuar con la ejecucion")
    s = input()


    if s == '1':
        agregarAgente()
    elif s == '2':
        eliminarAgente()
    elif s == '3':
        print("Continuando ...")

mostrarMenu()


#Selección del servidor
a1 = misAgentes[0].split(',')
com1 = a1[0]
dir1 = a1[1]

print(com1)
print(dir1)
ip1 = dir1[:-1]
print(ip1)

#Obtener información de:
#Agente 1
def obtenerAgenteUno(comunidad, ip):
    print("Empezando a recopilar informacion ...")
    while 1:
        # CPU Usage in porcentage
        iniciarCPU(comunidad, ip)
        iniciarRAM(comunidad, ip)
        obtenerAgenteUno(comunidad, ip)



def generarGrafica():
    print("Generando graficas ...")
    graficarCPU()
    graficarRAM()
    print("¡Graficas generadas!")




hilo1 = threading.Thread(name="AgenteUno", target=obtenerAgenteUno, args=(com1,ip1))
hilo2 = threading.Thread(name="Graficar", target=generarGrafica)


print("Empezo a ejecutar hilo1 <obtener agente>")
hilo1.start()
time.sleep(5)
print("Empezo a generar graficas hilo2")
hilo2.start()
print("Las imagenes han sido generadas con exito")
time.sleep(5)
generarReportePDF(com1,dir1)
detectar(com1,uReady,uSet,uGo,time)


# #Creacion de hilo para primer agente
# hilo1 = threading.Thread(name="AgenteUno", target=obtenerAgenteUno, args=(com1,ip1))
# hilo2 = threading.Thread(name="GenerarGraficas", target=generarGrafica)
#
# hilo1.start()
# time.sleep(60)
# hilo2.start()
# generarReportePDF(com1, ip1)
#
# #hilo2 = threading.Thread(name="AgenteDos", target=obtenerAgenteDos, args=(com2,ip2))



#Uso del CPU
# 1.3.6.1.4.1.2021.11.10.0

#Grafica del uso de memoria RAM
#1.3.6.1.4.1.2021.4.6.0

#Grafica del uso de disco duro
#1.3.6.1.4.1.2021.9.1.9.1 Investigar






