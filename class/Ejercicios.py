class Vehiculo:
    marca : str
    combustible : str  
    tipo : str
    nivel_combustible: float
    max_combustible: float
    def __init__(self,marca, combustible):
        self.marca = marca
        self.combustible = combustible    
    def encender(self):
        print('el vehiculo esta encendido')
        nivel

    def arrancar(self):
        if (self.nivel_combustible * 100) / self.max_combustible < 10:
            print('Nivel Bajo de Combustible')
        else:
            print('Nivel Normal')
    def __str__(self):
        return "para el {} se necesita {}".format(self.marca, self.combustible)
carro = Vehiculo('tesla','energia')
print(carro)



class Carro(Vehiculo):
    def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Moto'
      self.max_combustible = 10
      self.nivel_combustible = 4

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Carro'
      self.max_combustible = 10
      self.nivel_combustible = 0.9
carro = Carro('toyota', 'corriente')
print(carro)
carro.arrancar()


moto = Moto('honda', 'extra')
print(moto)
moto.arrancar()



# Ejercicio 1: Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; la clase también debe contener dos métodos encender y arrancar. 
# Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado
# Ejercicio 2: Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo.
# Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado
# Ejercicio 3: La clase Vehiculo, debe tener una propiedad llamada tipo (esta contendrá el tipo de vehiculo - Carro o Moto -),
# esta propiedad debe ser seteada al momento de instanciar la clase Carro o Moto y al momento de imprimir el objeto debe indicar el tipo 
# de vehiculo junto con el texto mostrado anteriormente 
# Ejercicio 4: Hacer control de encendido de los vehiculos, para esto al momento de usar el método encender, se debe validar el nivel de combustible del vehiculo
# (medida dada en galones) no este por debajo de un 10%, si este tiene un nivel muy bajo, mostrar la advertencia que necesita ir a la gasolinera. 
# Ejercicio 5: debes hacer un ejercicio donde por medio de un metodo, el vehiculo de marcha y haga un consumo de combustible a medida que este funcione, 
# cuando llegue a los niveles de combustible definidos en el mensaje anterior, muestre la advertencia y si esta llega a cero, detenga la marcha 
###Ejercicio_Libre.py###


