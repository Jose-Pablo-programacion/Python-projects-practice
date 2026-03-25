#tabla = int(input('¿De qué número quieres la tabla?: '))

#for i in range(1,11):
    #resultado = tabla*i
    #print(f'{tabla} x {i} = {resultado}')

nombre = ['Jose','Juan','Jesus','Javier','Jared']
persona = len(nombre)
print(f'Hay {persona} personas')

for i,nombre_actual in enumerate(nombre,1):
    print(f'{i}. {nombre_actual}')