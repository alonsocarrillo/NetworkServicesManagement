import time
import rrdtool
from Practica1.getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

#packets con errores
#consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.2.2.1.11.1")

while 1:
    total_input_traffic = int(
        consultaSNMP("ricardovargassagrero", "10.100.70.14", "1.3.6.1.2.1.2.2.1.11.1"))
    total_output_traffic = int(
        consultaSNMP("ricardovargassagrero", "10.100.70.14", "1.3.6.1.2.1.2.2.1.11.1"))

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print (valor)
    rrdtool.update('traficov4.rrd', valor)
    rrdtool.dump('traficov4.rrd', 'traficov4.xml')

    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)