import pdfkit
import jinja2
from datetime import datetime
import subprocess  # Agrega esta importación

today_date = datetime.today()

fecha_context = {
    'day': today_date.day,
    'month': today_date.strftime('%b'),
    'year': today_date.strftime('%y')
}


def generar_pdf2(datos_remito):
    total_precio = sum(float(producto['precio_bolsa']) for producto in datos_remito)

    context = {'fecha': fecha_context,
               'productos': datos_remito,
               'total_precio': total_precio
               }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'plantilla1.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)
    options = {
        # Aquí puedes elegir el tamaño de página que desees, como 'Letter', 'Legal', 'A4', etc.
        'page-size': 'A4',
        # Otras opciones de configuración aquí...
    }
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    output_pdf = 'remito.pdf'
    pdfkit.from_string(output_text, output_pdf, options=options, configuration=config, css="styles.css")

    # Abre el archivo PDF con el visor de PDF predeterminado del sistema
    subprocess.Popen([output_pdf], shell=True)
