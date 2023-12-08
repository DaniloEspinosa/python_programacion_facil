print("---Calculadora 2.0---")

operador = input("Hola, elija una opción:\n1- Suma.\n2- Resta.\n3- Multiplicación\n4- División.\n5- Módulo.\n6- Exponente.\nTeclee un númwero y pulse ENTER:\n")

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
    case _:
        print("No ha seleccionado una opción válida.")
        continuar = False

if continuar:        
    operando_1 = float(input("Especifique el primer operando:\n"))
    operando_2 = float(input("Especifique el segundo operando:\n"))

    if operador == "1":
        resultado = operando_1 + operando_2
    elif operador == "2":
        resultado = operando_1 - operando_2
    elif operador == "3":
        resultado = operando_1 * operando_2
    elif operador == "4":
        resultado = operando_1 / operando_2
    if operador == "5":
        resultado = operando_1 % operando_2
    elif operador == "6":
        resultado = operando_1 ** operando_2
    else:
        print("Vuelva a ejecutar el programa y seleccione una opción válida")
        
    print(f"El resultado de la operacion {operador} es:\n{round(resultado, 2)}")
else:
    print("Por favor vuelva a ejecutar el programa")