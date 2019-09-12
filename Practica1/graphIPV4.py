import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 300
tiempo_inicial = tiempo_final -25920000

while 1:
    ret = rrdtool.graph( "ipv4.png",
                     "--start="+ str(tiempo_final),
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=ICMP",
                     "DEF:entrada=traficov4.rrd:inoctets:AVERAGE",
                     "DEF:salida=traficov4.rrd:outoctets:AVERAGE",
                     "AREA:entrada#00FF00:IPv4",
                     "LINE1:salida#0000FF:IPv4\r")

    time.sleep(30)