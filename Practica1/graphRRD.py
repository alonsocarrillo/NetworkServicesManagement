import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 300
tiempo_inicial = tiempo_final -25920000

while 1:
    ret = rrdtool.graph( "traficoRED.png",
                     "--start="+ str(tiempo_final),
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de RED de agente SNMP",
                     "DEF:entrada=trafico.rrd:inoctets:AVERAGE",
                     "DEF:salida=trafico.rrd:outoctets:AVERAGE",
                     "AREA:entrada#00FF00:In traffic",
                     "LINE1:salida#0000FF:Out traffic\r")

    time.sleep(30)