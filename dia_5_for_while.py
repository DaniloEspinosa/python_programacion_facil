"""

for i in range(3, 6):
    print(f"Esta es la vuelta: {i + 1}.")

print("Fin deñ bucle for.\n")

colores = ["rojo", "azul", "verde", "amarillo"]

print("---LISTADO DE COLORES---")

for color in colores:
    if color == "azul" or color == "verde":
        print(f"Se ha saltado el color {color}.")
        continue
    elif color == "amarillo":
        print(f"El color {color} detiene la ejecucion del bucle")
        break
        
    print(f"- Color {color}.")
    
print("Esto se deberia imprimir de igual manera.")

# desde aqui vemos el bucle while

i = 1

while i <= 5:
    print(f"El valor del bucle es: {i}.")
    i += 1
    
while True:
    salida = input("Introduce 'salir' para finalizar.\n").lower()
    if salida == "salir":
        break
    print("Palabra mal introducida")

# mostrar los valores del 7 al 14 en bucles FOR y WHILE    
for i in range(7, 15):
    print(f"El valor del bucle FOR es: {i}.")
 
print("-----------")
   
i = 7
while i <= 14:
    print(f"El valor del bucle WHILE es: {i}.")
    i += 1


# mostrar valores del 0 al -5000 en decrementos de 500 con bucles FOR y WHILE
for i in range(0,-5001, -500):
    print(f"El valor del bucle FOR es: {i}.")
    
print("-----------")
    
i = 0
while i >= -5000:
    print(f"El valor del bucle WHILE es: {i}.")
    i -= 500
    
for i in colores:
    print(f"-> {i} <-")
    
i = 0

while i <= 3:
    print(f"-> {colores[i]} <- fucking while")
    i += 1
 
print("-----------LLL-----------") 
   
numeros = [10, 45, 356, 10, 10, 46, 67, 45, 10, 10, 43, 10, 65, 10, 10]

numeros.sort()



for i in numeros:
    if i == 10:
        continue
    elif i == 356:
        break
    else:
        print(f"EL valor del elemento es: {i}")
        
print("vvvv  Opcion mas corta  vvvv")
        
for i in numeros:
    if i >= 43 and i <= 67:
        print(f"EL valor del elemento es: {i}")

"""


dinero = float(input("Hola, indique el dinero que lleva:\n"))

print("-> Pizzería PF <-\n")

opcion_1 = ["Margarita", 7.85]
opcion_2 = ["Jamón y queso", 9.65]
opcion_3 = ["Cuatro quesos", 8.95]

extra_1 = ["Extra de queso", 1.25]
extra_2 = ["Champiñones", 0.85]
extra_3 = ["Albahaca", 0.5]

lista_pedido = []

opcion = input(f"1 - {opcion_1[0]} - {opcion_1[1]}$\n2 - {opcion_2[0]} - {opcion_2[1]}$\n3 - {opcion_3[0]} - {opcion_3[1]}$\nHola, por favor, seleccione su pizza con un número de opción.\n")

seguir = True

match opcion:
    case "1":
        print(f"Usted ha elegido la pizza {opcion_1[0]}.")
        pagar = opcion_1[1]
        print(f"Total a pagar {pagar}$")
        queda = dinero - pagar
        print(f"Le quedan {round(queda, 2)}$.")
        pizza_elegida = f"-{opcion_1[0]} - {opcion_1[1]}$."
    case "2":
        print(f"Usted ha elegido la pizza {opcion_2[0]}.")
        pagar = opcion_2[1]
        print(f"Total a pagar {pagar}$")
        queda = dinero - pagar
        print(f"Le quedan {round(queda, 2)}$.")
        pizza_elegida = f"-{opcion_2[0]} - {opcion_2[1]}$."
        
    case "3":
        print(f"Usted ha elegido la pizza {opcion_3[0]}.")
        pagar = opcion_3[1]
        print(f"Total a pagar {pagar}$")
        queda = dinero - pagar
        print(f"Le quedan {round(queda, 2)}$.")
        pizza_elegida = f"-{opcion_3[0]} - {opcion_3[1]}$."
    case _:
        print("La opcion elegida no es correcta")
        seguir = False
        
lista_pedido.append(pizza_elegida)
        
print("\n")
        
if seguir:
    
    extra = 1
    
    while extra >= 1 and extra <= 3: 
    
        extra = input(f"1 - {extra_1[0]} - {extra_1[1]}$\n2 - {extra_2[0]} - {extra_2[1]}$\n3 - {extra_3[0]} - {extra_3[1]}$\n4 - No añadir nada extra y pagar.\nSi desea algún extra seleccionelo:\n")
    
        extra = int(extra)
    
       
        match extra:
            case 1:
                print(f"Usted ha elegido {extra_1[0]}.")
                print(f"Extra a pagar {extra_1[1]}$")
                pagar += extra_1[1]
                print(f"Total a pagar {round(pagar, 2)}$.")
                queda = dinero - pagar
                print(f"Le quedan {round(queda, 2)}$.")
                extra_elegido = f"-{extra_1[0]} - {extra_1[1]}$."
                lista_pedido.append(extra_elegido)
            case 2:
                print(f"Usted ha elegido {extra_2[0]}.")
                print(f"Extra a pagar {extra_2[1]}$")
                pagar += extra_2[1]
                print(f"Total a pagar {round(pagar, 2)}$.")
                queda = dinero - pagar
                print(f"Le quedan {round(queda, 2)}$.")
                extra_elegido = f"-{extra_2[0]} - {extra_2[1]}$."
                lista_pedido.append(extra_elegido)
            case 3:
                print(f"Usted ha elegido {extra_3[0]}.")
                print(f"Extra a pagar {extra_3[1]}$")
                pagar += extra_3[1]
                print(f"Total a pagar {round(pagar, 2)}$.")
                queda = dinero - pagar
                print(f"Le quedan {round(queda, 2)}$.")
                extra_elegido = f"-{extra_3[0]} - {extra_3[1]}$."
                lista_pedido.append(extra_elegido)
            case 4:
                print("De acuerdo, no se añade nada extra.\n")
                print("--- SU PEDIDO ---")
                print(f"El total de su pedido es: {round(pagar, 2)}$")
                print(f"Su cambio: {round(queda, 2)}$\n")
                
                
                for i in lista_pedido:
                    print(i)
                    
                print("\n")               
                print("¡Buen provecho!")

            case _:
                print("La opcion elegida no es correcta")
        
    
else:
    print("Vuelva a iniciar el pedido desde el principio, gracias")