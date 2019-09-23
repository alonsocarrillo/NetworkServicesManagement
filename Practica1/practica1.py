from Practica1.getSNMP import consultaSNMP
from Practica1.unicast import iniciarUnicast
from Practica1.ipv4 import iniciarIPv4
from Practica1.icmp import iniciarICMP
from Practica1.segmentosRec import iniciarSegmentos
from Practica1.datagramasUDP import iniciarUDP
from Practica1.graphUnicast import graficarUnicast
from Practica1.graphIPV4 import graficarIPv4
from Practica1.graphICMP import graficarICMP
from Practica1.graphSegRRD import graficarSegmentos
from Practica1.graphRRD import graficarUDP
from Practica1.generarPDF import generarReportePDF
import threading
import time

print("---------- PRACTICA 1 ----------")
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


# Dispositivos que están en monitoreo

nmr = 1

print(" --> Dispositivos que estan en monitoreo: \n")
for agente in misAgentes:
    a = agente.split(',')
    num = nmr
    com = a[0]
    dir = a[1]
    print("Agente", num, "| Comunidad:", com, "Dirección:", dir)
    nmr = nmr + 1

#Selección de primer agente
a1 = misAgentes[0].split(',')
com1 = a1[0]
dir1 = a1[1]

#Selección de segundo agente
a2 = misAgentes[1].split(',')
com2 = a2[0]
dir2 = a2[1]

print(com1)
print(dir1)

print(com2)
print(dir2)

# El status del monitoreo del agente (up or down)
# Primer agente
print(" --> Status del monitoreo del agente: \n")
print("Primer agente "+com1)

ip1 = dir1[:-1]

c = consultaSNMP(com1, ip1,"1.3.6.1.2.1.1.1.0")
consulta = str(c)
consulta = consulta[:2]

if consulta == "No":
    print("Estado del agente "+ com1 +" DOWN")
else:
    print("Estado del agente "+ com1 +" UP")


#Segundo agente
print("Segundo agente "+com2)

ip2 = dir2[:-1]

c2 = consultaSNMP(com2, ip2,"1.3.6.1.2.1.1.1.0")
consulta2 = str(c2)
consulta2 = consulta2[:2]

if consulta2 == "No":
    print("Estado del agente "+ com2 +" DOWN")
else:
    print("Estado del agente "+ com2 +" UP")


#Número de interfaces disponibles
print(" --> Número de interfaces disponibles: \n")
i = 1
res = ""


print("--- Primer agente ---")
while res != "No":
    oid = "1.3.6.1.2.1.2.2.1.2." + str(i)
    res = consultaSNMP(com1,ip1, oid)
    if(res == "No"):
        print("")
    else:
        print(str(i)+" "+res)
    i = i + 1

i = 1
res = ""
print("--- Segundo agente ---")
while res != "No":
    oid = "1.3.6.1.2.1.2.2.1.2." + str(i)
    res = consultaSNMP(com2,ip2, oid)
    if(res == "No"):
        print("")
    else:
        print(str(i)+" "+res)
    i = i + 1

#El status de actividad de cada puerto
print(" --> Status de actividad de cada puerto: \n")
i = 1
res = ""

print("--- Primer agente ---")
while res != "No":
    oid = "1.3.6.1.2.1.2.2.1.10." + str(i)
    res = consultaSNMP(com1, ip1, oid)
    if(res == "No"):
        print("")
    else:
        if res != "0":
            print(str(i)+" "+"activo")
        else:
            print(str(i)+" "+"inactivo")
    i = i + 1

i = 1
res = ""
print("--- Segundo agente ---")
while res != "No":
    oid = "1.3.6.1.2.1.2.2.1.10." + str(i)
    res = consultaSNMP(com2, ip2, oid)
    if(res == "No"):
        print("")
    else:
        if res != "0":
            print(str(i)+" "+"activo")
        else:
            print(str(i)+" "+"inactivo")
    i = i + 1



#Obtener información de:
#Agente 1
def obtenerAgenteUno(comunidad, ip):
    print("Empezando a recopilar informacion ...")
    while 1:
        # Paquetes UNICAST que ha recibido la interfaz
        print("UNICAST")
        iniciarUnicast(comunidad,ip)
        # Paquetes recibidos a protocolos IPv4, incluyendo los que tienen errores
        print("IPV4")
        iniciarIPv4(comunidad, ip)
        #Mensajes ICMP echo que ha enviado el agente
        print("ICMP")
        iniciarICMP(comunidad, ip)
        #Segmentos recibidos, incluyendo los que se han recibido con errores
        print("SEGMENTOS")
        iniciarSegmentos(comunidad, ip)
        #Datagramas entregados a usuarios UDP
        print("UDP")
        #iniciarUDP(comunidad, ip)
        obtenerAgenteUno(comunidad, ip)


def generarGrafica():
    print("Generando graficas ...")
    graficarUnicast()
    graficarIPv4()
    graficarICMP()
    graficarSegmentos()
    graficarUDP()
    print("¡Graficas generadas!")


#obtenerAgenteUno(com1,ip1)
#print("¡Informacion recopilada exitosamente!")


#Creacion de hilo para primer agente
hilo1 = threading.Thread(name="AgenteUno", target=obtenerAgenteUno, args=(com1,ip1))
hilo2 = threading.Thread(name="GenerarGraficas", target=generarGrafica)

hilo1.start()
time.sleep(60)
hilo2.start()
generarReportePDF(com1, ip1)

#hilo2 = threading.Thread(name="AgenteDos", target=obtenerAgenteDos, args=(com2,ip2))










