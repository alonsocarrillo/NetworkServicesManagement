import time
import rrdtool
from Practica1.getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

#Mensajes ICMP echo que ha enviado el agente
#consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.5 ")


def iniciarSegmentos(comunidad, ip):
    tiempo = 0
    while 1:
        total_input_traffic = int(
            consultaSNMP(comunidad, ip, "1.3.6.1.2.1.5.10.0"))
        total_output_traffic = int(
            consultaSNMP(comunidad, ip, "1.3.6.1.2.1.5.10.0"))

        valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
        print (valor)
        rrdtool.update('traficoRED.rrd', valor)
        rrdtool.dump('traficoRED.rrd', 'traficoSeg.xml')

        time.sleep(1)
        tiempo += 1
        if tiempo == 1:
            break

    # if ret:
    #     print (rrdtool.error())
    #     time.sleep(300)