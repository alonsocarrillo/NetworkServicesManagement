import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 300
tiempo_inicial = tiempo_final -25920000

def graficarCPU():
    while 1:
        ret = rrdtool.graph( "IMG/cpu.png",
                         "--start="+ str(tiempo_final),
     #                    "--end","N",
                         "--vertical-label=Bytes/s",
                         "--title=ICMP",
                         "DEF:entrada=cpuUsageBD.rrd:inoctets:AVERAGE",
                         "DEF:salida=cpuUsageBD.rrd:outoctets:AVERAGE",
                         "AREA:entrada#00FF00:RAM Usage",
                         "LINE1:salida#0000FF:RAM\r")

        time.sleep(30)

