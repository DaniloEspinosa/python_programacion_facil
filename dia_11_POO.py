'''
# Taza 1
taza_1_color = "blanco"
taza_1_mensaje = None
taza_1_material = "porcelana"
taza_1_limpia = True

# Taza 2
taza_2_color = "blanco y azul"
taza_2_mensaje = "Cookies and milk"
taza_2_material = "porcelana"
taza_2_limpia = False

# Por convención los nombres de las clases se escriben en pascal case (Primera letra en mayúsculas)

class Taza():
    color = "blanco"
    mensaje = None
    material = "porcelana"
    limpia = True
    
taza_1 = Taza()
taza_2 = Taza()

print(taza_1.color)
print(taza_2.color)

taza_2.color = "blanco y azul"

print(taza_1.color)
print(taza_2.color)


# Se declara la clase vehiculo

class Vehiculo():
    # Atributos
    color = None
    longitud_metros = None
    ruedas = 4
    
    # Metodos
    def arrancar(self):
        print("El vehiculo ha arrancado")
        
    def detener(self):
        print("El vehiculo se ha detenido")
        
vehiculo_1 = Vehiculo()
vehiculo_2 = Vehiculo()

vehiculo_2.material_aleron = "Fibra de carbono"

print(vehiculo_2.material_aleron)

# Llamadas a métodos
vehiculo_1.arrancar()
vehiculo_1.detener()



class Vehiculo():
    
    pais_origen = "Alemania"
    
    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas
    
    def arrancar(self):
        print("El vehiculo ha arrancado")
        
    def detener(self):
        print("El vehiculo se ha detenido")
        
    def mostrar_info(self):
        print(f"Vehiculo de color {self.color}. Con una longitud de {self.longitud_metros}m. Tiene {self.ruedas} ruedas.\n El pais de origne es {self.pais_origen}")
        
vehiculo_1 = Vehiculo("rojo", 4, 4)
vehiculo_2 = Vehiculo("negro", 8.25, 8)

print(vehiculo_1.pais_origen)
vehiculo_2.arrancar()

vehiculo_1.mostrar_info()


# Estructuras vacias
class Vehiculo():
    pass
'''

# Ejercicios

class Motocicleta():
    # Atributos de clase
    estado = "nueva"
    motor = False
    
    
    # Métodos
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta,peso,capacidad_tanque):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.capacidad_tanque = capacidad_tanque
    
    
    
    def arrancar(self):
        if self.motor:
            print("El motor ya esta en marcha")
        else:
            self.motor = True
            print("Se ha arrancado el motor")
    
    def detener(self):
        if self.motor:
            self.motor = False
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")
            
    def saber_precio(self):
        print(f"El precio de la motocicleta '{self.marca} {self.modelo}' es de {self.precio}€")
        
    def comprobar_tanque(self):
        print(f"--->Nivel de combustible de la {self.marca} {self.modelo}<--\n")
        print(f"Tiene {self.combustible_litros}litros en el tanque")
        print(f"La capacidad maxima es de {self.capacidad_tanque}")
        print(f"Puedes agregar hasta {self.capacidad_tanque - self.combustible_litros} litros para llenar el depósito.\n")
        
        
    def repostar(self):
        while True:
            litros_repostar = float(input("¿Que cantidad en litros desea repostar?\n"))
            tanque_repostado = litros_repostar + self.combustible_litros
            if tanque_repostado <= self.capacidad_tanque:
                print(f"La cantidad de combustible disponible es de {tanque_repostado} litros.")
                self.combustible_litros = tanque_repostado
                break
            elif tanque_repostado > self.capacidad_tanque:
                print(f"Lo siento, la cantidad supera el limite del tanque.\n Puedes cargar hasta {self.capacidad_tanque - self.combustible_litros}litros.")
        
        
        
        
            
motocicleta_1 = Motocicleta("negra", "leon-777", 10, 2, "honda", "wave", 2020, 145, 130, 20)
motocicleta_2 = Motocicleta(
    color = "rojo",
    matricula = "pez-123",
    combustible_litros = 0,
    numero_ruedas = 2,
    marca = "yamaha",
    modelo = "crypton",
    fecha_fabricacion = 2018,
    velocidad_punta = 155,
    peso = 125,
    capacidad_tanque = 20
    )


motocicleta_1.precio = 1650

# motocicleta_1.arrancar()
# motocicleta_1.arrancar()
# motocicleta_1.detener()

# print(f"El precio de la motocicleta '{motocicleta_1.marca} {motocicleta_1.modelo}' es de {motocicleta_1.precio}€")
# motocicleta_1.saber_precio()
# motocicleta_2.saber_precio()

motocicleta_1.comprobar_tanque()
motocicleta_1.repostar()
motocicleta_1.comprobar_tanque()
motocicleta_1.repostar()


