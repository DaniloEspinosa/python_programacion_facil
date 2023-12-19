# Pixabay  --> Conseguir imagenes
# Pinetools  --> Editar imagenes
# Importaciones
from tkinter import *
import os
# from os import * (tambien se puede importar de esta manera)
from PIL import ImageTk, ImageColor, Image
import getpass

# Creacion de usiario nuevo
usuario_creado = ()

while True:
    nuevo_usuario = input('Introduzca un nombre para el nuevo usuario.\n')
    nueva_contrasena = getpass.getpass('Introduzca una contraseña para el nuevo usuario.\n')

    repite_usuario = input('Introduzca el nombre para el nuevo usuario nuevamente.\n')
    repite_contrasena = input('Introduzca la contraseña para el nuevo usuario nuevamente.\n')
    
    if nuevo_usuario == repite_usuario and nueva_contrasena == repite_contrasena:
        usuario_creado = (nuevo_usuario, nueva_contrasena)
        print(f'Datos ingresados {usuario_creado}')
        break
    else:
        print('Los datos no coinciden, intentalo nuevamente')

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
imagen2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, 'imagen2.jpg')).resize((400, 225)))
etiqueta2 = Label(image=imagen2)

etiqueta2.pack()

# Usuario
Label(text='Usuario').pack()
usuario = Entry()
usuario.insert(0, "Nombre de usuario")
usuario.bind("<Button-1>", lambda e: usuario.delete(0, END))
usuario.pack()

# Contraseña
Label(text= 'Contraseña').pack()
contrasena = Entry()
contrasena.insert(0, "*"*7)
contrasena.bind("<Button-1>", lambda e: contrasena.delete(0, END))
contrasena.pack()

# Funcion para validar el login
def validar():
    obtener_usuario = usuario.get()
    obtener_contrasena = contrasena.get()
    if obtener_usuario == usuario_creado[0] and obtener_contrasena == usuario_creado[1]:
        Label(text="Accediendo").pack()
    else:
        Label(text="Datos incorrectos").pack()

Button(text='Enviar', command=validar).pack()

# Bucle de ejecución
root.mainloop()