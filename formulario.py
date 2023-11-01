from generador_pdf import generar_pdf  # Importa la función para generar el PDF
from prueba import generar_pdf2
import sys

PYTHON_VERSION = sys.version_info.major

if PYTHON_VERSION < 3:
    try:
        print("menor a 3 version", + PYTHON_VERSION)
        from tkinter import Tk, Label, Entry, Button, StringVar
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        print("mayor a 3 version", + PYTHON_VERSION)
        from tkinter import Tk, Label, Entry, Button, StringVar

    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")


# Crear ventana principal
app = Tk()
name = StringVar()

# Tamano de ventana: anchura x altura
app.geometry("400x400")
app.config(background="black")
app.title("Remitos Bolsas ")


def enviar_datos():

    # Obtener datos del formulario
    print(datos_remito)
   # Llama a la función para generar el PDF
    generar_pdf2(datos_remito)


def agregar_mas():
    nuevo_conjunto = {
        'cantidad': campo_cantidad_value.get(),
        'tipo_bolsa': campo_tipo_bolsa_value.get(),
        'longitud_bolsa': campo_medida_bolsa_value.get(),
        'precio_bolsa': campo_precio_bolsa_value.get()
    }

    # Agrega el diccionario a la lista
    datos_remito.append(nuevo_conjunto)

    # Limpia los campos para el próximo conjunto
    campo_cantidad_value.set('')
    campo_tipo_bolsa_value.set('')
    campo_medida_bolsa_value.set('')
    campo_precio_bolsa_value.set('')

    print(datos_remito)


campo_cantidad_value = StringVar()
campo_tipo_bolsa_value = StringVar()
campo_medida_bolsa_value = StringVar()
campo_precio_bolsa_value = StringVar()

titulo = Label(app, text="Remito's App", font=(
    "Helvetica", 20, "bold"), bg="black", fg="white")
titulo.pack(pady=20)  # pady agrega espacio en la parte inferior del t

# Etiquetas y campos de entrada

etiqueta_cantidad = Label(
    app, text="Cantidad", font=('Roboto', 12))
etiqueta_cantidad.pack(fill="both", expand=True,)
campo_cantidad = Entry(app, textvariable=campo_cantidad_value)
campo_cantidad.pack(fill="both", expand=True,)


etiqueta_tipo_bolsa = Label(
    app, text="Tipo de Bolsas", font=('Roboto', 12))
etiqueta_tipo_bolsa.pack(fill="both", expand=True)
campo_tipo_bolsa = Entry(app, textvariable=campo_tipo_bolsa_value)
# textvariable=name
campo_tipo_bolsa.pack(fill="both", expand=True,)

etiqueta_medida_bolsa = Label(
    app, text="Medida de Bolsas", font=('Roboto', 12))
etiqueta_medida_bolsa.pack(fill="both", expand=True,)
campo_medida_bolsa = Entry(app, textvariable=campo_medida_bolsa_value)
campo_medida_bolsa.pack(fill="both", expand=True,)

etiqueta_precio_bolsa = Label(app, text="Precio bolsa", font=('Roboto', 12))
etiqueta_precio_bolsa.pack(fill="both", expand=True,)
campo_precio_bolsa = Entry(app, textvariable=campo_precio_bolsa_value)
campo_precio_bolsa.pack(fill="both", expand=True,)


boton_agregar_mas = Button(app, text="AGREGAR +", font=(
    'Roboto', 16), bg="#13B018", cursor="hand2", relief="flat", command=agregar_mas)
boton_agregar_mas.pack(fill="both", expand=True)


# Botón para generar el PDF
boton_generar_pdf = Button(
    app, text="GENERAR REMITO", font=('Roboto', 16), bg="#00a8e8", fg="white", cursor="hand2", relief="flat", command=enviar_datos)
boton_generar_pdf.pack(fill="both", expand=True)

datos_remito = []

# Iniciar la aplicación
app.mainloop()
