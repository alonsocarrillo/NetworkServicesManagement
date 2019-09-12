import time
import rrdtool
from Practica1.getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

#Paquetes de entrada Unicast
#consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.2.2.1.11") 'ricardovargassagrero', '10.100.70.14'



while 1:
    total_input_traffic = int(
        consultaSNMP("ricardovargassagrero", "10.100.70.14", "1.3.6.1.2.1.2.2.1.11.1"))
    total_output_traffic = int(
        consultaSNMP("ricardovargassagrero", "10.100.70.14", "1.3.6.1.2.1.2.2.1.11.1"))

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print (valor)
    rrdtool.update('traficoUnicast.rrd', valor)
    rrdtool.dump('traficoUnicast.rrd', 'traficou.xml')

    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)