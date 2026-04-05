palabras = ["hola", "mundo", "python", "codigo"]

palabras_invertidas = []

for palabra in palabras:
    palabra_invertida = ""
    for letra in range(len(palabra)-1,-1,-1):
        palabra_invertida += palabra[letra]
    palabras_invertidas.append(palabra_invertida)

print(palabras_invertidas)