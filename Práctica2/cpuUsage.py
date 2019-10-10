import time
import rrdtool
from getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

#Datagramas entregados a usuarios UDP
#consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.7.1.0")


def iniciarCPU(comunidad, ip):
    tiempo = 0
    while 1:
        total_input_traffic = int(
            consultaSNMP(comunidad, ip, "1.3.6.1.4.1.2021.4.6.0"))
        total_output_traffic = int(
            consultaSNMP(comunidad, ip, "1.3.6.1.4.1.2021.4.6.0"))

        valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
        print (valor)
        rrdtool.update('cpuUsageBD.rrd', valor)
        rrdtool.dump('cpuUsageBD.rrd', 'cpuUsagebd.xml')

        time.sleep(1)
        tiempo += 1
        if tiempo == 1:
            break

    # if ret:
    #     print (rrdtool.error())
    #     time.sleep(300)