import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generar_pdf(tipo_bolsa, medida_bolsa, precio_total):
    # Crea un archivo PDF
    nombre_archivo = "remito_bolsas.pdf"
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)

    # Define el contenido del PDF
    story = []
    styles = getSampleStyleSheet()
    story.append(Paragraph(f"Tipo de Bolsas: {tipo_bolsa}", styles["Normal"]))
    story.append(Paragraph(f"Medida de Bolsas: {medida_bolsa}", styles["Normal"]))
    story.append(Paragraph(f"Precio Total: {precio_total}", styles["Normal"]))

    # Construye el PDF
    doc.build(story)

if __name__ == "__main__":
    # Ejemplo de uso para probar la generación del PDF
    tipo_bolsa = "Tipo de Bolsas de ejemplo"
    medida_bolsa = "Medida de Bolsas de ejemplo"
    precio_total = "Precio Total de ejemplo"
    generar_pdf(tipo_bolsa, medida_bolsa, precio_total)

    # Ruta al archivo PDF que deseas abrir
    pdf_file = 'remito_bolsas.pdf'

    # Abre el archivo PDF con el visor de PDF predeterminado del sistema
    subprocess.Popen([pdf_file], shell=True)
