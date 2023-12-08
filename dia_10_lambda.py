'''
def multiplicacion (numero1, numero2):
    return numero1 * numero2

multiplicar = lambda numero1, numero2 : numero1 * numero2

resultado_def = multiplicacion(217, 43)
resultado_lambda = multiplicar(217, 43)

print(resultado_def)
print(resultado_lambda)

(lambda numero1, numero2 : print(numero1 * numero2)) (217, 43)   #función que se ejecuta sin ser llamada


# Ejercicios

# Ejercicio 1
import math
pi = math.pi

area_circulo = lambda radio : pi * radio * radio

print(area_circulo(1))

# Ejercicio 2

(lambda nombre : print(f"Hola {nombre}")) (input("¿Como te llamas?\n"))
'''

# Ejercicio 3
colores = ["rojo", "azul", "verde", "amarillo"]
color_posicion = lambda color, posicion : print(f"El color {color} se encuentra en la posicion {posicion}.")

for color in colores:
    color_posicion(color, colores.index(color))
    
    