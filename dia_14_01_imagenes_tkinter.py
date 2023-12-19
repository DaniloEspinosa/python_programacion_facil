# Pixabay  --> Conseguir imagenes
# Pinetools  --> Editar imagenes
# Importaciones
from tkinter import *
import os
# from os import * (tambien se puede importar de esta manera)
from PIL import ImageTk, ImageColor, Image


#  --Carga de directorios(carpetas)--
# Carpeta principal
carpeta_principal = os.path.dirname(__file__)

 # Carpeta de imágenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
#print(carpeta_imagenes)
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")

# Creación de la ventana principal
root = Tk()
# Título de la ventana
root.title("Aprendiendo con programación fácil")

# Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, 'favicon.ico'))

# Carga de imagen
imagen1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, 'imagen1.jpg')).resize((400, 225)))
etiqueta1 = Label(image=imagen1)
imagen2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, 'imagen2.jpg')).resize((400, 225)))
etiqueta2 = Label(image=imagen2)
imagen3 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, 'imagen3.jpg')).resize((400, 225)))
etiqueta3 = Label(image=imagen3)
imagen4 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, 'imagen4.jpg')).resize((400, 225)))
etiqueta4 = Label(image=imagen4)
etiqueta1.grid(row=0, column=0)
etiqueta2.grid(row=0, column=1)
etiqueta3.grid(row=1, column=0)
etiqueta4.grid(row=1, column=1)

  
# Bucle de ejecución
root.mainloop()