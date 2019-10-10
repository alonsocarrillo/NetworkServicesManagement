from fpdf import FPDF
from getSNMP import consultaSNMP
from datetime import date

def generarReportePDF(comunidad,ip):
    #Obtener:
    #Fecha de elaboración
    fecha = str(date.today())
    #SO del servidor
    so = str(consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.1.0"))
    #Tiempo de actividad del servidor
    currentTime = str(consultaSNMP(comunidad, ip, "1.3.6.1.2.1.25.1.1.0"))
    #Num. de interfaces
    numPuertos = str(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.2.1.0'))



pdf = FPDF(orientation='P', unit='mm', format='letter')
pdf.add_page()
pdf.set_font("Arial", size=32)
pdf.cell(200, 10, txt="Practica 2: Administracion de rendimiento", ln=1, align="C")
pdf.cell(200, 15, txt="Usando SNMP", ln=1, align="C")
pdf.set_font("Arial", size=12)
pdf.cell(200, 6, txt="Número de equipo: 1", ln=1, align="L")
pdf.cell(200, 6, txt="Nombre y versión del sistema operativo: "+so, ln=1, align="L")
pdf.cell(200, 6, txt="Fecha de elaboración: "+fecha, ln=1, align="L")
pdf.cell(200, 6, txt="Ubicacion Geográfica: Mexico City", ln=1, align="L")
pdf.cell(200, 6, txt="Numero de interfaces: "+numPuertos, ln=1, align="L")
pdf.cell(200, 6, txt="Tiempo de actividad desde el ultimo reinicio: "+currentTime, ln=1, align="L")


pdf.image("ubuntu.png", x = 160, y = 35, w = 35, h = 25)
pdf.image("IMG/cpu.png", x=120, y=90, w=70, h=50)
pdf.image("IMG/ram.png", x=20, y=90, w=70, h=50)

pdf.output("IMG/reporte.pdf")
