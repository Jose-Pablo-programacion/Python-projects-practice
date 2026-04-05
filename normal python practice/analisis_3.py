numeros = [4, -7, 2, -3, 9, -1, 5, -8, 3, -2, 6]

acumulador_positivos = 0
acumulador_negativos = 0

positivos = []
negativos = []


for numero in numeros:
        if numero < 0:
            acumulador_negativos += numero
            negativos.append(numero)
        else:
            acumulador_positivos += numero
            positivos.append(numero)

print(f"Positivos : {positivos}")
print(f"Suma positivos : {acumulador_positivos}")
print()
print(f"Negativos : {negativos}")
print(f"Suma negativos : {acumulador_negativos}")


            



