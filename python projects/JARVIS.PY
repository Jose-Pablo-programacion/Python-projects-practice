import datetime

def calculadora(cadena):
    numeros = []
    numero_actual = ""
    operador = ""
    for caracter in cadena:
        if caracter.isdigit():
            numero_actual += caracter
        if not caracter.isdigit() and numero_actual:
            a = numero_actual
            numeros.append(numero_actual)
            numero_actual = ""
        if caracter == "+" or caracter == "-" or caracter == "*" or caracter == "/":
            operador = caracter
            numero_actual = ""

    b = numero_actual

    if operador == "+":
        resultado =  int(a) + int(b)
    elif operador == "-":
        resultado = int(a) - int(b)
    elif operador == "*":
        resultado = int(a) * int(b)
    elif operador == "/":
        if b== "0":
            print("No se puede dividir entre 0")
            return None
        else:
            resultado = int(a) / int(b)
    else:
        print("No se pudo hacer la operacion")
    
    return resultado



while True:
    JARVIS = input("Dile algo a JARVIS:").lower().strip()
    if JARVIS == "hola":
        print("Hola bro")
    elif JARVIS == "como estas":
        print("Bien, gracias por preguntar")
    elif JARVIS == "adios":
        print("Adios,hasta pronto")
        break
    elif JARVIS == "dame la hora" or JARVIS == "que hora es" or JARVIS == "Hora actual" or JARVIS == "hora":
        print(datetime.datetime.now().strftime("%H:%M"))
    elif JARVIS == "buenos dias" or JARVIS == "buenos dias jarvis":
        print("Buenos dias")
    elif JARVIS == "buenas tardes" or JARVIS == "buenas tardes jarvis":
        print("Buenas tardes")
    elif JARVIS == "buenas noches" or JARVIS == "buenas noches jarvis":
        print("Buenas noches")
    elif "cuanto es" in JARVIS or "jarvis cuanto es" in JARVIS or "dame el resultado de" in JARVIS or "jarvis dame el resultado de" in JARVIS or "calcula" in JARVIS or "jarvis calcula" in JARVIS:
        resultado = calculadora(JARVIS)
        if resultado is not None:
            print(resultado)
    elif "+" in JARVIS or "-" in JARVIS or "*" in JARVIS or "/" in JARVIS:
        resultado = calculadora(JARVIS)
        if resultado is not None:
            print(resultado)
    else:
        print("No entiendo :(")

