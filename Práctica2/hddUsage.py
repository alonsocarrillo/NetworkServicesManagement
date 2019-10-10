import time
import rrdtool
from getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

##RAM
# almacenTotal = int(consultaSNMP(comunidad,ip,'1.3.6.1.2.1.25.2.3.1.5.36'))
# almacenUsado = int(consultaSNMP(comunidad,ip,'1.3.6.1.2.1.25.2.3.1.6.36'))


def iniciarHDD(comunidad, ip):
    tiempo = 0
    while 1:
        total_input_traffic = int(
            consultaSNMP(comunidad, ip, "1.3.6.1.2.1.25.2.3.1.5.36"))
        total_output_traffic = int(
            consultaSNMP(comunidad, ip, "1.3.6.1.2.1.25.2.3.1.5.36"))

        valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
        print (valor)
        rrdtool.update('hddUsageBD.rrd', valor)
        rrdtool.dump('hddUsageBD.rrd', 'hddUsagebd.xml')

        time.sleep(1)
        tiempo += 1
        if tiempo == 1:
            break

    # if ret:
    #     print (rrdtool.error())
    #     time.sleep(300)
