import datetime
import random

def calculadora(cadena):
    numero_actual = ""
    operador = ""
    for caracter in cadena:
        if caracter.isdigit():
            numero_actual += caracter
        if not caracter.isdigit() and numero_actual:
            a = numero_actual
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


frases_jarvis = ["El ayer es historia, el mañana es un misterio, pero el hoy es un obsequio.","La mente es como un paracaídas, solo funciona si se abre.","No cuentes los días, haz que los días cuenten.",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.","Cae siete veces, levántate ocho.","La única forma de hacer un gran trabajo es amar lo que haces.",
    "El dolor es temporal, el orgullo es para siempre.","No esperes el momento perfecto, toma el momento y hazlo perfecto.","Las grandes mentes discuten ideas, las mentes mediocres discuten eventos, las mentes pequeñas discuten personas.",
    "La vida no se mide por las veces que respiras, sino por los momentos que te dejan sin aliento.","Si puedes soñarlo, puedes lograrlo.","El que no arriesga no gana.",
    "La disciplina es el puente entre las metas y los logros.","No importa qué tan lento vayas, siempre y cuando no te detengas.","El fracaso es simplemente la oportunidad de comenzar de nuevo con más inteligencia.",
    "Tu tiempo es limitado, no lo desperdicies viviendo la vida de alguien más.","La felicidad no es algo hecho, viene de tus propias acciones.",
    "El secreto del éxito es constancia en el propósito.","El talento sin trabajar duro es nada."]

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
    elif JARVIS == "fecha" or JARVIS == "dame la fecha" or JARVIS == "jarvis dame la fecha actual" or JARVIS == "jarvis dame la fecha" or JARVIS == "fecha actual":
        print(datetime.datetime.now().strftime("%d/%m/%Y"))
    elif JARVIS == "frase" or JARVIS == "dame una frase" or JARVIS == "jarvis dame una frase":
        frase_random = random.choice(frases_jarvis)
        print(frase_random)
    else:
        print("No entiendo :(")

