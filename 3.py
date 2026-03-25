#def saludar(nombre):
    #print(f'¡Hola, {nombre}! Bienvenido')

#saludar('Jose Pablo')
#saludar('Juan')
#saludar('Ana')


#def area_rectangulo(base, altura):
    #return base*altura

#resultado = area_rectangulo(5, 3)
#print(f'El área es: {resultado}')

def es_par(num):
    return num % 2 == 0




numeros = [4, 7, 2, 9, 14, 3, 8, 11, 6]

for num in numeros:
    if es_par(num):
        print(num)