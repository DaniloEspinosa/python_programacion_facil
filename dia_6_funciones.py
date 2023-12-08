"""
def saludar():
    nombre = input("Introduzca su nombre, por favor\n")
    print(f"¡Muy buenas, {nombre}!")
    
saludar()

def saludar(nombre): # ahora le estamos indicando un parametro dentro de la funcion, al llamar la funcion escribiremos este argumento
    print(f"¡Muy buenas, {nombre}!")
    
saludar("Danilo")


def saludar(nombre, edad):
    print(f"¡Muy buenas, {nombre} y tienes {edad} años!")
    
saludar("Denu", 28)
saludar(edad = 28, nombre ="Denu")   # argumento de clave, puedo alterar el orden de los argumentos

def suma(numero1,numero2):
    return numero1 + numero2

resultado = suma(20,40)
print(resultado)


colores = ["rojo", "verde", "amarillo"]

def agregar_color(color):
    return colores.append(color)

agregar_color("azul")

print(colores)

"""
def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    return a / b
def modulo(a,b):
    return a % b
def exponente(a,b):
    return a ** b

print("---Calculadora 3.0---")

operador = 1

while operador >= 1 and operador <=6:

    operador = input("Hola, elija una opción:\n1- Suma.\n2- Resta.\n3- Multiplicación\n4- División.\n5- Módulo.\n6- Exponente.\n7- SALIR -\nTeclee un número y pulse ENTER:\n")

    continuar = True

    match operador:
        case "1":
            print("Ha seleccionado SUMA")
        case "2":
            print("Ha seleccionado RESTA")
        case "3":
            print("Ha seleccionado MULTIPLICACIÓN")
        case "4":
            print("Ha seleccionado DIVISIÓN")
        case "5":
            print("Ha seleccionado MÓDULO")
        case "6":
            print("Ha seleccionado EXPONENTE")
        case "7":
            print("Gracias por utilizar nuestra calculadora, hasta la próxima!!\n\n")
            break
        case _:
            print("No ha seleccionado una opción válida.")
            continuar = False
            

    
    if continuar:        
        operando_1 = float(input("Especifique el primer operando:\n"))
        operando_2 = float(input("Especifique el segundo operando:\n"))

        operador =int(operador)
        
        if operador == 1:
            resultado = suma(operando_1,operando_2)
        elif operador == 2:
            resultado = resta(operando_1,operando_2)
        elif operador == 3:
            resultado = multiplicacion(operando_1,operando_2)
        elif operador == 4:
            resultado = division(operando_1,operando_2)
        if operador == 5:
            resultado = modulo(operando_1,operando_2)
        elif operador == 6:
            resultado = exponente(operando_1,operando_2)
            
        print(f"El resultado de la operacion {operador} es:\n{round(resultado, 2)}\n")
    else:
        operador = 1
        print("La opcion elejida no es correcta.\nPor favor elija una opcion valida entre los numeros 1 y 7\n")