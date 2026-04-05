nombres = ["Ana", "Luis", "María", "Ana", "Carlos", "Luis", "María", "Ana", "José"]
acumulador = 0
unicos = []

for nombre in nombres:
        if nombre not in unicos:          
            unicos.append(nombre)
            acumulador +=1
                
print(f"Nombres unicos : {unicos}")
print(f"Total: {acumulador}")


#forma de hacerlo mas rapido pero puede que no se mantenga el orden  de la lista como va como del principio al final. Puede que muestre primero el ultimo y el de enmedio al final y el primero enmedio. 

#nombres = ["Ana", "Luis", "María", "Ana", "Carlos", "Luis", "María", "Ana", "José"]

#unicos = list(set(nombres))

#print(f"Nombres únicos: {unicos}")
#print(f"Total: {len(unicos)}")
