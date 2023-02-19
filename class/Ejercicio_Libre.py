# debes hacer un ejercicio donde por medio de un metodo, el vehiculo de marcha y haga un consumo de combustible a medida que este funcione, 
# cuando llegue a los niveles de combustible definidos en el mensaje anterior, muestre la advertencia y si esta llega a cero, detenga la marcha#
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
    def arrancar(self):
        if (self.nivel_combustible * 100) / self.max_combustible < 10:
            print('Nivel Bajo de Combustible')
        if (self.nivel_combustible * 100) / self.nivel_combustible < 1 :
            print('Se acabara la gasolina ')

    def marcha(self):
        print("Vehiculo en movimiento...", "Gasolina Inicial",self.nivel_combustible)
        while self.nivel_combustible > 0:
            self.nivel_combustible -= 1
            print("Gasolina",self.nivel_combustible)
            if self.nivel_combustible == 2 :
                print('🚧⚠⚠⚠🚧 vaya a tanquear')
        print('SE DETUVO! 🛑')

    def __str__(self):
        return "El {} Con Gasolina {} 🛺".format(self.marca, self.combustible)
carro = Vehiculo
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
      self.nivel_combustible = 3
carro = Carro('Toyota', 'corriente')
print(carro)
carro.arrancar()
carro.marcha()

moto = Moto('Honda', 'extra')
print(moto)
moto.arrancar()
moto.marcha()
