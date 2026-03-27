#Clases
class Coche:
    def __init__(self,marca,modelo,velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad = self.velocidad + 10
        print(f"La velocidad actual es {self.velocidad}")
    

mi_coche = Coche("Ford ","Escape",0)
mi_coche.acelerar()
mi_coche.acelerar()
mi_coche.acelerar()
