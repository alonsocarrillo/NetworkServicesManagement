import time
import rrdtool
from Practica1.getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

#Mensajes ICMP echo que ha enviado el agente
#consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.5.0 ") 1.3.6.1.2.1.5



while 1:
    total_input_traffic = int(
        consultaSNMP("ricardovargassagrero", "10.100.70.14", "1.3.6.1.2.1.5.10.0"))
    total_output_traffic = int(
        consultaSNMP("ricardovargassagrero", "10.100.70.14", "1.3.6.1.2.1.5.10.0"))

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print (valor)
    rrdtool.update('traficoicmp.rrd', valor)
    rrdtool.dump('traficoicmp.rrd', 'trafico.xml')

    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)