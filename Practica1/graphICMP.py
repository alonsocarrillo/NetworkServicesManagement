import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 300
tiempo_inicial = tiempo_final -25920000

while 1:
    ret = rrdtool.graph( "icmp.png",
                     "--start="+ str(tiempo_final),
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=ICMP",
                     "DEF:entrada=trafico.rrd:inoctets:AVERAGE",
                     "DEF:salida=trafico.rrd:outoctets:AVERAGE",
                     "AREA:entrada#00FF00:ICMP echo incluyendo errores",
                     "LINE1:salida#0000FF:ICMP\r")

    time.sleep(30)