numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista_primos = []

for numero in numeros:
    es_primo= True
    for divisor in range(2,numero):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        lista_primos.append(numero)
        
print(lista_primos)
