'''

p = "Programacion"
f = "fácil"
n = 10
d = 12.5
# Texto preformateado --> La variable al no tener nada inmediatamente 
# no adopta la triple comilla como comentario multilinea
texto = """Lorem Ipsum es simplemente el texto de relleno
de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las
industrias desde el año 1500,
cuando un impresor (N. del T. persona que se dedica a la imprenta)
desconocido usó una galería de textos y los mezcló de tal manera
que logró hacer un libro de textos especimen."""

print(p,f)
print(p + " " + f)
print(p, str(n))
print("%s %s" % (p,f)) # Otra forma de concatenar %s se refiere a STRING
print("%d %s" % (n,f)) # Otra forma de concatenar %d se refiere a
print("%i %s" % (d,f)) # Otra forma de concatenar %i se refiere a INT
print("%f %s" % (d,f)) # Otra forma de concatenar %f se refiere a FLOAT
print((p+" ") * 3)  # Multiplicación de string

# Concatenar con el método JOIN
print("".join([p,f]))
print(" ".join([p,f,str(n)]))

colores = ["rojo", "azul", "verde", "amarillo"]
separador = "*"
concatena = separador.join(colores)

print(concatena)

# Concatenar con el método FORMAT
print("{} {} {} {}".format(p, f, d, n))

# Formateo de string literales
print(f"{p} {f}")


# Iterar string
pf = "Programación fácil"

#forma óptima
for letra in pf:
    print(letra)

#Forma mas difícil:
for letra in range(len(pf)):
    print(pf[letra])
    
    
# Comprobar coincidencias en string
print("la" in "Hola")
print("sas" not in "Hola")

# Generar un diccionario a partir de un string. Tambien se pueden listas, tuplas, sets
lista_pf = dict(enumerate(pf))

print(lista_pf)
print(type(lista_pf))

'''
# Ejercicio 1
frase = ["Estoy", "aprendiendo", "Python", "con", "el", "curso", "de", "100", "dias", "de", "Programación", "Fácil."]
print(" ".join(frase))

# Ejercicio 2
colores = ["rojo", "azul", "verde", "amarillo"]
guion = "-"
punto = "."

for color in colores:
    print("{}{}{}".format(guion, color.capitalize(), punto))
    
# Ejercicio 3

numero_1 = 10
numero_2 = 34.50
resultado = numero_1 * numero_2

print("La multiplicacion de %i * %.2f da como resultado = %.2f." % (numero_1, numero_2, resultado))

# Ejercicio 4  Crear un contador de caracteres
texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum."""
texto_2 = "Anana"

def contar_caracteres(string):
    caracter = input("Introduce una letra\n")
    contador = 0
    for letra in string:
        if letra.lower() == caracter.lower():
            contador += 1
    print(f"Se ha encontrado la letra '{caracter}' {contador} veces.")

contar_caracteres(texto_2)

# Ejercicio 5

numero_1 = 10
numero_2 = 34.50
resultado = numero_1 * numero_2

print(f"La multiplicacion de {numero_1} * {numero_2:.3f} da como resultado = {resultado:.3f}.")