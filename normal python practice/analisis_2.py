palabras = ["gato", "perro", "gato", "pez", "perro", "gato", "perro", "pez", "gato"]

conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

for palabra,cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")

    