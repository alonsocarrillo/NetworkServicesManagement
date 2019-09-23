from fpdf import FPDF
from Practica1.getSNMP import consultaSNMP

def generarReportePDF(comunidad,ip):
    so = str(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.1.0'))
    ubi = str(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.6.0'))
    numPuertos = str(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.2.1.0'))
    tiempoActivo = str(consultaSNMP(comunidad, ip, '1.3.6.6.1.2.1.1.3.0'))



    #so = str(consultaSNMP('aubuntu', '10.100.67.146', '1.3.6.1.2.1.1.1.0'))
    #ubi = str(consultaSNMP('aubuntu', '10.100.67.146', '1.3.6.1.2.1.1.6.0'))
    #numPuertos = str(consultaSNMP('aubuntu', '10.100.67.146', '1.3.6.1.2.1.2.1.0'))
    #tiempoActivo = str(consultaSNMP('aubuntu', '10.100.67.146', '1.3.6.6.1.2.1.1.3.0'))

    #Información
    # ricardovargassagrero 10.100.70.14

    #-packets con errores
    #consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.2.2.1.11")

    #Paquetes de entrada Unicast
    #consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.2.2.1.11")


    #Mensajes ICMP echo que ha enviado el agente
    #consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.5 ")

    #-Segmentos recibidos, incluyendo aquellos que se reciben con errores
    #consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.6.10.0")

    #-Datagramas entregados a usuarios UDP
    #consultaSNMP("acarrillo", "localhost", "1.3.6.1.2.1.7.1.0")

    pdf = FPDF(orientation='P', unit='mm', format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=32)
    pdf.cell(200, 10, txt="Practica 1: Adquisicion de informacion", ln=1, align="C")
    pdf.cell(200, 15, txt="Usando SNMP", ln=1, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 5, txt="Nombre y versión del sistema operativo: "+so, ln=1, align="L")
    pdf.cell(200, 5, txt="Ubicacion Geográfica: "+ubi, ln=1, align="L")
    pdf.cell(200, 5, txt="Numero de puertos: "+numPuertos, ln=1, align="L")
    pdf.cell(200, 5, txt="Tiempo de actividad desde el ultimo reinicio: "+tiempoActivo, ln=1, align="L")
    pdf.cell(200, 5, txt="Comunidad: ricardovargassagrero", ln=1, align="L")
    pdf.cell(200, 5, txt="Datagramas entregados a usuarios UDP", ln=1, align="R")
    pdf.image("mojave.png", x = 150, y = 35, w = 35, h = 25)
    pdf.image("datagramasUDP.png", x = 140, y = 100, w = 65, h = 45)
    pdf.image("segmentosrec.png", x = 140, y = 150, w = 65, h = 45)
    pdf.image("icmp.png", x = 40, y = 100, w = 65, h = 45)
    pdf.image("unicast.png", x = 40, y = 150, w = 65, h = 45)
    pdf.image("ipv4.png", x = 40, y = 200, w = 65, h = 45)
    pdf.output("reporteMacOs.pdf")
