import pdfkit
import jinja2
from datetime import datetime

today_date = datetime.today()
day = today_date.day
month = today_date.strftime('&b')
year = today_date.strftime('&y')


def generar_pdf2(tipo_bolsa, medida_bolsa, precio_total):
    context = {'tipo_bolsa': tipo_bolsa, 'medida_bolsa': medida_bolsa, 'precio_total': precio_total,
               'day': day, 'month': month, 'year': year}

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'plantilla1.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    output_pdf = 'remito.pdf'
    pdfkit.from_string(output_text, output_pdf,
                       configuration=config, css="styles.css")
