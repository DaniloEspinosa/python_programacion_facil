# dia de listas y tuplas
lista_numeros = [10, 45, 55, 76]
lista_colores = ["rojo", "azul", "verde", "amarillo"]
lista_colores2 = lista_colores
lista_colores3 = lista_colores2.copy()

print(lista_numeros[3])

print(f"El valor más pequeño en la lista es el {lista_numeros[0]}. El más grande es el {lista_numeros[3]}.")

print(lista_colores[1][2])  # Imprimir en consola el caracter u del color azul

print(lista_colores[-1],lista_colores[-2])  # imprimir en consola los ultimos 2 colores de la lista

lista_colores.insert(0, "gris")
print(lista_colores)

lista_colores.append("rosa")
print(lista_colores)

lista_colores.insert(3, "naranja")
print(lista_colores)

lista_colores.pop(1)
print(lista_colores)

lista_colores.pop(3)
print(lista_colores)

lista_colores.pop(-2)
print(lista_colores)

print(lista_colores3)

print(lista_numeros.count(10))

print(lista_colores.index("azul"))

print(len(lista_colores))