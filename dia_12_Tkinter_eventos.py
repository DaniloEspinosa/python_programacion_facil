'''
# Importaciones
from tkinter import *

# Creacion de la ventana principal
root = Tk()
# Título de la ventana
root.title("Curso de Tkinter de Programación fácil")

entrada = Entry(root)
entrada.insert(0,"Escriba su nombre.")
entrada.bind("<Button-1>", lambda d : entrada.delete(0, END))
entrada.pack()

# Evento para el botón
def pulsar_boton():
    nombre = entrada.get()
    Label(root, text=nombre).pack()

# Botón
Button(root, text="Enviar", command=pulsar_boton).pack()

# Bucle de ejecución
root.mainloop()


# Ejercicio, crear 4 botones con grid o pack
# Importar Tkinter
from tkinter import *

# Creacion de la ventana principal
root = Tk()

# Título de la ventana
root.title("Ejercicios dia 12 PYTHON")

# Botones solucion con PACK
# Button(root, text="Botón 1").pack()
# Button(root, text="Botón 2").pack()
# Button(root, text="Botón 3").pack()
# Button(root, text="Botón 4").pack()

# Solucion con grid
Button(root, text="Botón 1").grid(row=0, column=0)
Button(root, text="Botón 2").grid(row=0, column=1)
Button(root, text="Botón 3").grid(row=1, column=0)
Button(root, text="Botón 4").grid(row=1, column=1)

# Bucle de ejecución
root.mainloop()


# Ejercicio número 2, crear botones que impriman un mensaje en la ventana
# Importar Tkinter
from tkinter import *

# Creacion de la ventana principal
root = Tk()

# Título de la ventana
root.title("Ejercicios dia 12 PYTHON")

# Evento para el botón
def crear_etiqueta(numero_boton):
    etiqueta = Label(root, text=f"Botón {numero_boton} pulsado.")
    etiqueta.pack()
    
# Botones
boton_1 = Button(root, text="Botón 1", command= lambda : crear_etiqueta(1)).pack()
boton_2 = Button(root, text="Botón 2", command= lambda : crear_etiqueta(2)).pack()
boton_3 = Button(root, text="Botón 3", command= lambda : crear_etiqueta(3)).pack()
boton_4 = Button(root, text="Botón 4", command= lambda : crear_etiqueta(4)).pack()
    
# Bucle de ejecución
root.mainloop()
'''

# Crear una ventana que pida nombre, edad, y teng aun boton que al pulsarlo imprima un mensaje con
# con el nombre y la edad del usuario.
# Importar Tkinter
from tkinter import *

# Creacion de la ventana principal
root = Tk()

# Título de la ventana
root.title("Ejercicios dia 12 PYTHON")

# Entradad de datos
# Nombre
Label(root, text="Nombre: ").grid(row= 0, column= 0)
entrada_nombre = Entry(root)
entrada_nombre.grid(row=0, column= 1)

# Edad
Label(root, text="Edad: ").grid(row=1, column= 0)
entrada_edad = Entry(root)
entrada_edad.grid(row= 1, column= 1)

# Evento para el botón enviar
def pulsar_boton():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    Label(root, text=f"Hola {nombre}, tienes {edad} años.").grid(row= 3, column= 1)

# Botón de enviar
Button(root, text=" ENVIAR ", command=pulsar_boton).grid(row=2, column= 1)
    
# Bucle de ejecución
root.mainloop()