import tools
import documentBewerken
def main():
    print("1. Voer een nieuwe check uit\n2. Bekijk de gebeurde checks\n**** **** **** **** **** **** **** ****\n")
    keuze = input("Kies voor 1 of 2: ")
    if keuze == "1":
        print("**********************************************")
        keuze = input("1. Voer handtmatig een adress in \n2. Toon de lijst met apparaten\n")
        if keuze == "1":
            documentBewerken.ping()
        if keuze == "2":
            documentBewerken.apparatenTonen()
            tools.ping()
    elif keuze == "2":
        logs = open("pinglog.txt")
        
        
        
        