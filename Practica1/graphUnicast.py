import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 300
tiempo_inicial = tiempo_final -25920000

while 1:
    ret = rrdtool.graph( "unicast.png",
                     "--start="+ str(tiempo_final),
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Unicast",
                     "DEF:entrada=traficoUnicast.rrd:inoctets:AVERAGE",
                     "DEF:salida=traficoUnicast.rrd:outoctets:AVERAGE",
                     "AREA:entrada#00FF00:Unicast",
                     "LINE1:salida#0000FF:Unicast\r")

    time.sleep(30)