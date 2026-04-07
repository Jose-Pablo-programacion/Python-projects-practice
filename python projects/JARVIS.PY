import datetime
import random
import webbrowser

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
    JARVIS = input("Dile algo a JARVIS(escribir ayuda para poder ver comandos validos):").lower().strip()
    if JARVIS == "hola" or JARVIS == "hola jarvis":
        print("Hola bro")
    elif JARVIS == "como estas" or JARVIS == "como estas jarvis":
        print("Bien, gracias por preguntar")
    elif JARVIS == "adios" or JARVIS == "adios jarvis":
        print("Adios,hasta pronto")
        break
    elif JARVIS == "dame la hora" or JARVIS == "que hora es" or JARVIS == "Hora actual" or JARVIS == "hora" or JARVIS == "dame la hora jarvis" or JARVIS == "que hora es jarvis":
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
    elif JARVIS == "abre google" or JARVIS == "jarvis abre google" or JARVIS == "google" or JARVIS == "abrir google" or JARVIS == "jarvis abrir google":
        webbrowser.open("https://www.google.com/?hl=es")
    elif JARVIS == "abre youtube" or JARVIS == "jarvis abre youtube" or JARVIS == "youtube" or JARVIS == "abrir youtube" or JARVIS == "jarvis abrir youtube":
        webbrowser.open("https://www.youtube.com/")
    elif JARVIS == "abre facebook" or JARVIS == "jarvis abre facebook" or JARVIS == "facebook" or JARVIS == "abrir facebook" or JARVIS == "jarvis abrir facebook":
        webbrowser.open("https://www.facebook.com/")
    elif JARVIS == "abre whatsapp" or JARVIS == "jarvis abre whatsapp" or JARVIS == "whatsapp" or JARVIS == "abrir whatsapp" or JARVIS == "jarvis abrir whatsapp":
        webbrowser.open("https://www.whatsapp.com/?lang=es")
    elif JARVIS == "abre claude" or JARVIS == "jarvis abre claude" or JARVIS == "claude" or JARVIS == "abrir claude" or JARVIS == "jarvis abrir claude":
        webbrowser.open("https://claude.ai/new")
    elif JARVIS == "abre classroom" or JARVIS == "jarvis abre classroom" or JARVIS == "classroom" or JARVIS == "abrir classroom" or JARVIS == "jarvis abrir classroom":
        webbrowser.open("https://classroom.google.com/u/1/")
    elif JARVIS == "ayuda" or JARVIS == "comandos validos" or JARVIS == "comandos" or JARVIS == "comandos de ayuda" or JARVIS == "comandos de jarvis":
        print("decir hola->hola jarvis\ndecir como estas->como estas jarvis\ndecir adios->adios jarvis\nobtener la hora actual->jarvis dame la hora\ndecir buenos dias->buenos dias jarvis\ndecir buenos dias->buenos dias jarvis")
        print("decir buenas tardes->buenas tardes jarvis\ndecir buenas noches->buenas noches jarvis\nsuma->ejemplo(jarvis cuanto es 5+3)\nresta->ejemplo(jarvis cuanto es 5-3)\nmultiplicacion->ejemplo(jarvis cuanto es 5*3)\ndivision->ejemplo(jarvis cuanto es 5/3)")    
        print("obtener la fecha actual->jarvis dame la fecha actual\nfrase profunda->jarvis dame una frase\nabrir google->jarvis abre google\nabrir youtube->jarvis abre youtube\nabrir facebook->jarvis abre facebook\nabrir whatsapp->jarvis abre whatsapp")
        print("abrir claude->jarvis abre claude\nabrir classroom->jarvis abre classroom\n")
    else:
        print("No entiendo :(")

