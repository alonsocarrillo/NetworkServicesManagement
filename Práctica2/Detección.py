
import rrdtool
from path import *
import time
from Notify import send_alert_attached
def detectar(numAgente,uReady,uSet,uGo,horaConsulta):
    flagEnviado = False
    while 1:
        tiempo_final = int(rrdtool.last(rrdpath+str(numAgente)+"trend.rrd"))
        tiempo_inicial = tiempo_final - 300

        while 1:
            ret = rrdtool.graph("IMG/cpu.png",
                                "--start=" + str(tiempo_final),
                                #                    "--end","N",
                                "--vertical-label=Bytes/s",
                                "--title=ICMP",
                                "DEF:entrada=cpuUsageBD.rrd:inoctets:AVERAGE",
                                "DEF:salida=cpuUsageBD.rrd:outoctets:AVERAGE",
                                "AREA:entrada#00FF00:RAM Usage",
                                "LINE1:salida#0000FF:RAM\r")

            time.sleep(30)

        ret1 = rrdtool.graphv( pngpath+str(numAgente)+"ram.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--title","Carga de RAM",
                         "--vertical-label=Uso de CPU (%)",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "DEF:carga="+rrdpath+str(numAgente)+rrdname+":RAMload:AVERAGE",
                         "CDEF:umbralReady=carga,"+str(uReady)+",LT,0,carga,IF",
                         "CDEF:umbralSet=carga,"+str(uSet)+",LT,0,carga,IF",
                         "CDEF:umbralGo=carga,"+str(uGo)+",LT,0,carga,IF",
                         "VDEF:cargaMAX=carga,MAXIMUM",
                         "VDEF:cargaMIN=carga,MINIMUM",
                         "VDEF:cargaSTDEV=carga,STDEV",
                         "VDEF:cargaLAST=carga,LAST",
                         "AREA:carga#00FF00:Carga de la RAM",
                         "AREA:umbralReady#FFEC01:Tráfico de carga mayor que "+str(uReady),
                         "AREA:umbralSet#FF9F00:Tráfico de carga mayor que "+str(uSet),
                         "AREA:umbralGo#FF0000:Tráfico de carga mayor que "+str(uGo),#
                         "HRULE:"+str(uReady)+"#00FF00:Umbral 1 - "+str(uReady)+"%",
                         "HRULE:"+str(uSet)+"#FFEC01:Umbral "+str(uReady+1)+" - "+str(uSet)+"%",
                         "HRULE:"+str(uGo)+"#FF9F00:Umbral "+str(uSet+1)+" - "+str(uGo)+"%",
                         "PRINT:cargaLAST:%6.2lf %S",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )
        ultimo_valor_RAM=float(ret1['print[0]'])
        #print(ret1)
        if (time.time()- 300) >= horaConsulta:
            horaConsulta = time.time() + 300
            if flagEnviado == True:
                flagEnviado = False


        if flagEnviado == False:
            if ultimo_valor_RAM>uReady or ultimo_valor_RAM>uSet or ultimo_valor_RAM>uGo:
                flagEnviado = True
                print("Sobrepasa Umbral línea base de la RAM, enviando correo")
                send_alert_attached("Sobrepasa Umbral línea base de la RAM ALONSO CARRILLO RUÍZ",
                                    pngpath+str(numAgente)+"ram.png")
        time.sleep(10)

        ret2 = rrdtool.graphv(pngpath + str(numAgente) + "hdd.png",
                              "--start", str(tiempo_inicial),
                              "--end", str(tiempo_final),
                              "--title", "Disco Duro",
                              "--vertical-label=Uso de hdd (%)",
                              '--lower-limit', '0',
                              '--upper-limit', '100',
                              "DEF:carga=" + rrdpath + str(numAgente) + rrdname + ":HDDload:AVERAGE",
                              "CDEF:umbralReady=carga," + str(uReady) + ",LT,0,carga,IF",
                              "CDEF:umbralSet=carga," + str(uSet) + ",LT,0,carga,IF",
                              "CDEF:umbralGo=carga," + str(uGo) + ",LT,0,carga,IF",
                              "VDEF:cargaMAX=carga,MAXIMUM",
                              "VDEF:cargaMIN=carga,MINIMUM",
                              "VDEF:cargaSTDEV=carga,STDEV",
                              "VDEF:cargaLAST=carga,LAST",
                              "AREA:umbralReady#FFEC01:Tráfico de carga mayor que " + str(uReady),
                              "AREA:umbralSet#FF9F00:Tráfico de carga mayor que " + str(uSet),
                              "AREA:umbralGo#FF0000:Tráfico de carga mayor que " + str(uGo),  #
                              "HRULE:" + str(uReady) + "#00FF00:Umbral 1 - " + str(uReady) + "%",
                              "HRULE:" + str(uSet) + "#FFEC01:Umbral " + str(uReady + 1) + " - " + str(uSet) + "%",
                              "HRULE:" + str(uGo) + "#FF9F00:Umbral " + str(uSet + 1) + " - " + str(uGo) + "%",
                              "PRINT:cargaLAST:%6.2lf %S",
                              "GPRINT:cargaMIN:%6.2lf %SMIN",
                              "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                              "GPRINT:cargaLAST:%6.2lf %SLAST")
        HDD = float(ret1['print[0]'])
        # print(ret1)
        if (time.time() - 300) >= horaConsulta:
            horaConsulta = time.time() + 300
            if flagEnviado == True:
                flagEnviado = False

        if flagEnviado == False:
            if ultimo_valor_HDD > uReady or ultimo_valor_HDD > uSet or ultimo_valor_HDD > uGo:
                flagEnviado = True
                print("Sobrepasa Umbral línea base de la RAM, enviando correo")
                send_alert_attached("Sobrepasa Umbral línea base de la RAM ALONSO CARRILLO RUÍZ",
                                    pngpath + str(numAgente) + "hdd.png")
        time.sleep(10)


