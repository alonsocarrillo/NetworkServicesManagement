print("---------- PRACTICA 1 ----------")
print("--------------------------------")

archivo = open("agentes.txt", "r")

misAgentes = []

for ag in archivo.readlines():
    #print(ag)
    misAgentes.append(ag)
    #agente = ag.split(',')
    #agentes = agente [0]
    #comunidad = agente[1]
    #direccion = agente[2]
    #print(agente)


print(misAgentes[1])



archivo.close()