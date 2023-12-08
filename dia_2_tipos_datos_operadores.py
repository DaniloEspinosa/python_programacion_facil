# construir una calculadora de exponentes

print("-- Calculadora de exponentes--")

numero_1 = input("Introduzca el número de base:\n")
numero_2 = input("Introduzca el valor del exponente:\n")

resultado = float(numero_1) ** float(numero_2)

print(f"El resultado de {numero_1} elevado a {numero_2} es {resultado}.")