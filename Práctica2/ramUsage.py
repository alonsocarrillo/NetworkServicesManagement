import time
import rrdtool
from getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0



def iniciarRAM(comunidad, ip):
    tiempo = 0
    while 1:
        total_input_traffic = int(
            consultaSNMP(comunidad, ip, "1.3.6.1.4.1.2021.4.6.0"))
        total_output_traffic = int(
            consultaSNMP(comunidad, ip, "1.3.6.1.4.1.2021.4.6.0"))

        valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
        print (valor)
        rrdtool.update('ramUsageBD.rrd', valor)
        rrdtool.dump('ramUsageBD.rrd', 'ramUsge.xml')

        time.sleep(1)
        tiempo += 1
        if tiempo == 1:
            print("Termino de guardar la info")
            break

    # if ret:
    #     print (rrdtool.error())
    #     time.sleep(300)