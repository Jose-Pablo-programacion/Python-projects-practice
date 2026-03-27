#Herencia en clases

class Vehiculo:
    def __init__(self,marca,velocidad_max):
        self.marca= marca
        self.velocidad_max = velocidad_max

    def describir(self):
        print(f"Marca: {self.marca} Velocidad maxima: {self.velocidad_max} km/h")

class Moto(Vehiculo):
    def hacerCaballito(self):
        print("La moto hizo un caballito")

class Camion(Vehiculo):
    def cargar(self,toneladas):
        print(f"El camion cargo {toneladas} tonenladas")

moto = Moto("Kawasaki",140)
camion = Camion("Volvo",100)

moto.describir()
moto.hacerCaballito()
camion.describir()
camion.cargar(10)
