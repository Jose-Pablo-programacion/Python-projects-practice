#Manejo de errores con try/except
try:
    num1= int(input("Dame el primer numero: "))
    num2= int(input("Dame el segundo numero: "))

    division=num1 / num2
    print(division)

except ValueError:
    print("Error: Solo puedes escribir numeros")

except ZeroDivisionError:
    print("Error:No puedes dividir entre 0")
finally:
    print("Cerrando el programa")