nombre = input('¿Cómo te llamas?: ')
nacimiento = int(input('Dame tu año de nacimiento: '))

fecha_actual = 2026
edad = fecha_actual - nacimiento

print(f'Hola {nombre}, tienes aproximadamente {edad} años')

if edad < 18:
    print('Eres menor de edad')
if edad >= 18 and edad < 26:
    print('Eres joven')
if edad >= 26:
    print('Ya eres un adulto veterano 😂')