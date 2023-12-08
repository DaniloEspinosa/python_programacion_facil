"""
# DICCIONARIOS
microsoft_office = {
    "word" : "Editor de textos.",
    "excel" : "Editor de tablas y cálculos.",
    "power point" : "Editor de diapositivas y presentaciones."
}

print(microsoft_office)
print(microsoft_office["power point"])

diccionario = {
    1: "Hola",
    2: "Como estas",
    3: "Chau"
}

print(diccionario)

microsoft_office["Outlook"] = "Editor y gestor de correos/mails."   # Agregar nuevo elemento al diccionario, si el elemento ya existe se sobreescribe

print(microsoft_office)

vacio = {}  # esta es la manera de crear un diccionario vacio

for programa in microsoft_office:
    print(f"-{programa}")
    
for programa in microsoft_office:
    print(f"-{programa.capitalize()} : {microsoft_office[programa]}")
    
# SETS
animales = {"perro","iguana","gato","piton","chimpance"}
print(animales)  # el print devuelve los elementos pero en un orden aleatorio que cambia cada vez que se ejecuta el programa

animales = {"perro","iguana","gato","piton","chimpance","perro"}  # elimina los elementos duplicados
print(animales)
"""

colores = {
    1: "rojo",
    2: "azul",
    3: "verde",
    4: "amarillo"
}

print(colores)

for i in colores:
    print(f"{i} - {colores[i].capitalize()}")
    
colores[5] = "Magenta"

print(colores)