#archivos
nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))

with open ("datos.txt","w") as archivo: #aqui podemos tambien usar append con "a"
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Edad: {edad}\n\n") #aqui pongo doble salto de lina por si se usa el append envez de write


with open ("datos.txt","r") as archivo: #Leemos lo que hay en nuestro archivo
    contenido = archivo.read()
    print(contenido)
