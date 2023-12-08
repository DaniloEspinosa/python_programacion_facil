"""
# Importaciones - el signo de * lo importa todo.
from tkinter import *

# Creación de la ventana principal.
root =Tk()

# Título de la ventana.
root.title("Curso de Python")

# Tamaño de la ventana.
root.geometry("800x600+300+120") # 800 x 600 es el tamaño en px de la ventana, 560 es la distancia sobre el eje x (de izquierda a derecha), 240 es la distacia sobre el eje y (de arriba hacia abajo)


# Creación de las etiquetas.
mensaje = Label(root, text="Mi primer programa con Tkinter.")
mensaje_2 = Label(root, text="Esta es la segunda etiqueta.")

# Se muestran las etiquetas.
mensaje.grid(row=0, column=0)
mensaje_2.grid(row=1, column=0)

# Lo mismo de antes pero mas reducido.
mensaje = Label(root, text="Mi primer programa con Tkinter.").grid(row=0, column=0)
mensaje_2 = Label(root, text="Esta es la segunda etiqueta.").grid(row=1, column=0)


# Bucle de ejecución.
root.mainloop()
"""

from tkinter import *

root = Tk()

root.title("Curso Máster")
root.geometry("600x400+50+75")

mensaje = Label(root, text="Primer mensaje").grid(row=0, column=0)
mensaje_2 = Label(root, text="Segundo mensaje").grid(row=0, column=1)


root.mainloop()