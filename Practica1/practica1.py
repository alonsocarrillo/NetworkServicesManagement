from Practica1.getSNMP import consultaSNMP

print("---------- PRACTICA 1 ----------")
print("--------------------------------")

archivo = open("agentes.txt", "r")

misAgentes = []

for ag in archivo.readlines():
    #print(ag)
    misAgentes.append(ag)
    a = ag.split(',')
    num = a [0]
    com = a [1]
    dir = a [2]
    #print(agente)

archivo.close()


# Dispositivos que están en monitoreo
print(" --> Dispositivos que estan en monitoreo: \n")
for agente in misAgentes:
    a = agente.split(',')
    num = a[0]
    com = a[1]
    dir = a[2]
    print("Agente", num, "| Comunidad:", com, "Direccion:", dir)

# El status del monitoreo del agente (up or down)
print(" --> Status del monitoreo del agente: \n")
try:
    consulta = consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.1.1.0")
    print("Status del Agente: UP")
except:
    print ("Status del Agente: DOWN")

#Número de interfaces disponibles
print(" --> Número de interfaces disponibles: \n")
i = 1
res = ""

while res != "No":
    oid = "1.3.6.1.2.1.2.2.1.2." + str(i)
    res = consultaSNMP("acarrillo", "localhost", oid)
    if(res == "No"):
        print("")
    else:
        print(str(i)+" "+res)
    i = i + 1

#El status de actividad de cada puerto
print(" --> Status de actividad de cada puerto: \n")
i = 1
res = ""

while res != "No":
    oid = "1.3.6.1.2.1.2.2.1.10." + str(i)
    res = consultaSNMP("acarrillo", "localhost", oid)
    if(res == "No"):
        print("")
    else:
        if res != "0":
            print(str(i)+" "+"activo")
        else:
            print(str(i)+" "+"inactivo")
    i = i + 1





