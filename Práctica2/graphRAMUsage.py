import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 300
tiempo_inicial = tiempo_final -25920000

def graficarRAM():
    print("Generando imagen")
    while 1:
        ret = rrdtool.graph( "IMG/ram.png",
                         "--start="+ str(tiempo_final),
     #                    "--end","N",
                         "--vertical-label=Bytes/s",
                         "--title=ICMP",
                         "DEF:entrada=ramUsageBD.rrd:inoctets:AVERAGE",
                         "DEF:salida=ramUsageBD.rrd:outoctets:AVERAGE",
                         "AREA:entrada#00FF00:RAM Usage",
                         "LINE1:salida#0000FF:RAM\r")

        time.sleep(30)