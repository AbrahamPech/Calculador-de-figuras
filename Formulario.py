import tkinter as tk  # tkinter para crear interfaces gráficas
from tkinter import messagebox  # Mostrar un cuadro de diálogo de error
from PIL import Image, ImageTk  # Importar Pillow para cargar imágenes JPEG

# Aquí importamos todas las figuras
from Rectangulo import Rectangulo
from Circulo import Circulo
from Triangulo import Triangulo
from Cuadrado import Cuadrado

# Función que se ejecuta al presionar el botón para calcular
def calcular():
    try:
        figura_seleccionada = tipo_figura.get()  # La figura seleccionada por el usuario

        if figura_seleccionada == "Rectángulo":
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            figura = Rectangulo(base, altura)
        elif figura_seleccionada == "Círculo":
            radio = float(entry_radio.get())
            figura = Circulo(radio)
        elif figura_seleccionada == "Triángulo":
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            figura = Triangulo(base, altura)
        elif figura_seleccionada == "Cuadrado":
            lado = float(entry_base.get())
            figura = Cuadrado(lado)
        else:
            raise ValueError("Selecciona una figura válida.")

        # Calcular el área y el perímetro
        area = figura.area()
        perimetro = figura.perimetro()

        # Mostrar los resultados en las etiquetas de área y perímetro
        label_area_resultado.config(text=f"Área: {area}")
        label_perimetro_resultado.config(text=f"Perímetro: {perimetro}")

    except ValueError as ve:
        messagebox.showerror("Error", f"Error de valor: {ve}")
    except TypeError as te:
        messagebox.showerror("Error", f"Error de tipo: {te}")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")  # Este es para cualquier otro error no contemplado

# Configuración de la ventana principal de Tkinter
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Figuras")

# Cargar imágenes para cada figura usando Pillow
img_rectangulo = ImageTk.PhotoImage(Image.open("Rectangulo.jpeg"))
img_circulo = ImageTk.PhotoImage(Image.open("Circulo.jpeg"))
img_triangulo = ImageTk.PhotoImage(Image.open("Triangulo.jpeg"))
img_cuadrado = ImageTk.PhotoImage(Image.open("Cuadrado.jpeg"))

# Selector de figura
label_seleccion_figura = tk.Label(ventana_principal, text="Selecciona la figura:")
label_seleccion_figura.grid(row=0, column=0)

tipo_figura = tk.StringVar(value="Rectángulo")  # por defecto la seleccionada será Rectángulo
figuras = [
    ("Rectángulo", img_rectangulo),
    ("Círculo", img_circulo),
    ("Triángulo", img_triangulo),
    ("Cuadrado", img_cuadrado)
]

# Crear los botones con imágenes para cada figura
for i, (figura, imagen) in enumerate(figuras):
    tk.Radiobutton(
        ventana_principal,
        text=figura,
        variable=tipo_figura,
        value=figura,
        image=imagen,  # Agregar la imagen
        compound="left"  # Muestra la imagen a la izquierda del texto
    ).grid(row=0, column=i + 1)

# Crear etiquetas y campos de entrada para las distintas figuras
label_base_o_lado = tk.Label(ventana_principal, text="Base / Lado:")
label_base_o_lado.grid(row=1, column=0)

entry_base = tk.Entry(ventana_principal)
entry_base.grid(row=1, column=1)

label_altura = tk.Label(ventana_principal, text="Altura:")
label_altura.grid(row=2, column=0)

entry_altura = tk.Entry(ventana_principal)
entry_altura.grid(row=2, column=1)

label_radio = tk.Label(ventana_principal, text="Radio:")
label_radio.grid(row=3, column=0)

entry_radio = tk.Entry(ventana_principal)
entry_radio.grid(row=3, column=1)

# Botón para calcular área y perímetro
button_calcular = tk.Button(ventana_principal, text="Calcular", command=calcular)
button_calcular.grid(row=4, columnspan=2)

# Etiquetas para mostrar los resultados
label_area_resultado = tk.Label(ventana_principal, text="Área: ")
label_area_resultado.grid(row=5, columnspan=2)

label_perimetro_resultado = tk.Label(ventana_principal, text="Perímetro: ")
label_perimetro_resultado.grid(row=6, columnspan=2)

# Iniciar el bucle principal de Tkinter
ventana_principal.mainloop()