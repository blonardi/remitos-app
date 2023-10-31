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
app.geometry("300x300")
app.config(background="black")
app.title("Remitos Bolsas ")


def enviar_datos():
    # Obtener datos del formulario

    valor_tipo_bolsa = campo_tipo_bolsa.get()

    valor_medida_bolsa = campo_medida_bolsa.get()

    valor_precio_total = campo_precio_total.get()

   # Llama a la función para generar el PDF
    generar_pdf2(valor_tipo_bolsa, valor_medida_bolsa, valor_precio_total)


def agregar_mas():
		nuevo_producto = Entry(app)
		nuevo_cantidad = Entry(app)
		nuevo_precio = Entry(app)

		nuevo_producto.grid(row=next_row, column=0)
		nuevo_cantidad.grid(row=next_row, column=1)
		nuevo_precio.grid(row=next_row, column=2)

		# Agrega los campos a la lista para su posterior procesamiento
		campos_productos.append(nuevo_producto)
		campos_cantidad.append(nuevo_cantidad)
		campos_precio.append(nuevo_precio)

    # Incrementa el contador de filas
    next_row += 1



# def show_name():
#     nuevo_nombre = name.get()

#     if nuevo_nombre:
#         print(f"My name is {nuevo_nombre}")
#     else:
#         print("I have no name, i am unnamed dea")


titulo = Label(app, text="Remito's App", font=(
    "Helvetica", 20, "bold"), bg="black", fg="white")
titulo.pack(pady=20)  # pady agrega espacio en la parte inferior del t

# Etiquetas y campos de entrada
etiqueta_tipo_bolsa = Label(
    app, text="Tipo de Bolsas", font=('Roboto', 12))
etiqueta_tipo_bolsa.pack(fill="both", expand=True)
campo_tipo_bolsa = Entry(app)
# textvariable=name
campo_tipo_bolsa.pack(fill="both", expand=True,)

etiqueta_medida_bolsa = Label(
    app, text="Medida de Bolsas", font=('Roboto', 12))
etiqueta_medida_bolsa.pack(fill="both", expand=True,)
campo_medida_bolsa = Entry(app)
campo_medida_bolsa.pack(fill="both", expand=True,)

etiqueta_precio_total = Label(app, text="Precio Total", font=('Roboto', 12))
etiqueta_precio_total.pack(fill="both", expand=True,)
campo_precio_total = Entry(app)
campo_precio_total.pack(fill="both", expand=True,)


boton_agregar_mas = Button(app, text="AGREGAR MAS", font=(
    'Roboto', 16), cursor="hand2", relief="flat", command=agregar_mas)
boton_agregar_mas.pack(fill="both", expand=True)


# Botón para generar el PDF
boton_generar_pdf = Button(
    app, text="GENERAR REMITO", font=('Roboto', 16), bg="#00a8e8", fg="white", cursor="hand2", relief="flat", command=enviar_datos)
boton_generar_pdf.pack(fill="both", expand=True)


# bootoon = Button(app, text="show name",
#                  command=show_name)
# bootoon.pack(fill="both")

# Iniciar la aplicación
app.mainloop()
