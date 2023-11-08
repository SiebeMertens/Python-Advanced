import documentBewerken
import tools
import checker
def main():
    print("manager")
    print("**********************************************")
    print("1. Voeg netwerkapparaten toe aan de lijst \n2. Verwijder netwerkapparaten van de lijst \n3. Lijst met netwerkapparaten tonen\n4. Ping check naar apparaten")
    
    
    controlleur = False
    while not controlleur:
        try:
           keuze = input("\nVoer het cijfer in van het menu dat je wilt kiezen:")
           match keuze:
                case "1":
                    print("*** Hieronder kan u netwerkapparaten toevoegen ***")
                    controlleur = True
                    documentBewerken.apparatenToevoegen()
                case "2":
                    print("*** Hieronder kan u netwerkapparaten verwijderen *** ")
                    controlleur = True
                    documentBewerken.apparatenVerwijderen()
                case "3":
                    print("*** De lijst met netwerkapparaten worden hieronder getoond ***")
                    controlleur = True
                    documentBewerken.apparatenTonen()
                case "4":
                    print("*** Voer het ip of hostname van het apparaat in dat je wilt pingen ***")
                    controlleur = True
                    checker.main()
                    
        except ValueError:
            print("Waarde is ongeldig, probeer opnieuw")
        

   
    