calificaciones = [85, 92, 78, 95, 88, 72, 90, 65, 88, 79]
acumulador =0
menor = calificaciones[0]
mayor = calificaciones[0]

for calificacion in calificaciones:
    acumulador= acumulador + calificacion
    if calificacion < menor:
        menor = calificacion
    if calificacion > mayor:
        mayor = calificacion
         
print(f"Promedio de calificaciones = {acumulador/len(calificaciones)}")
print(f"Calificacion menor = {menor}")
print(f"Califiacion mayor = {mayor}")
