import datetime

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
    else:
        print("No entiendo :(")