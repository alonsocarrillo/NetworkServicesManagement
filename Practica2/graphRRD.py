import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 300
tiempo_inicial = tiempo_final -25920000

def graficarUDP():
    while 1:
        ret = rrdtool.graph( "datagramasUDP.png",
                         "--start="+ str(tiempo_final),
     #                    "--end","N",
                         "--vertical-label=Bytes/s",
                         "--title=Datagramas entregados a usuarios UDP",
                         "DEF:entrada=datagramaUDP.rrd:inoctets:AVERAGE",
                         "DEF:salida=datagramaUDP.rrd:outoctets:AVERAGE",
                         "AREA:entrada#00FF00:In traffic",
                         "LINE1:salida#0000FF:Out traffic\r")

        time.sleep(30)