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
        #print(e)
        #print(param)
        #i = e

        #for agnt in misAgentes[i:param]:
            #print(agnt)
            #od = agnt[0]
            #old = str(od)
            #nw = int(agnt[0]) - 1
            #new = str(nw)
            #print(old)
            #print(new)
            #misAgentes[i][0] = ""+new
            #print(misAgentes[i][0])
            #misAgentes[i][0].replace(old, new)
            #print("I --- " + str(i))
            #old = misAgentes[e][0]
            #print("Old")
            #print(old)
            #new = str(e)
            #misAgentes[e][0].replace(old,new)
            #i+=1
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
    s = input()


    if s == '1':
        agregarAgente()
    elif s == '2':
        eliminarAgente()




mostrarMenu()








