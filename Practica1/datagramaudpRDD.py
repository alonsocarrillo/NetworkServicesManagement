import time
import rrdtool
from Practica1.getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

#Datagramas entregados a usuarios UDP
#consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.7.1.0")



while 1:
    total_input_traffic = int(
        consultaSNMP("aubuntu", "10.100.67.146", "1.3.6.1.2.1.7.1.0"))
    total_output_traffic = int(
        consultaSNMP("aubuntu", "10.100.67.146", "1.3.6.1.2.1.7.1.0"))

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print (valor)
    rrdtool.update('datagramaUDP.rrd', valor)
    rrdtool.dump('datagramaUDP.rrd', 'datagramaUDP.xml')

    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)