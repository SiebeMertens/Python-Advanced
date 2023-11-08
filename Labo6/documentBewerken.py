import json
import os
def apparatenToevoegen():
    
    nogToeveogen = False
    
    while not nogToeveogen:
        
        hostname = input("Voer de hostname name in: ")
        ip = input("Voer het ip in: ")
        fabrikant = input("Voer de naam van een fabrikant in: ")
        
        nieuwApparaat = {
            "Hostname": hostname,
            "ip": ip,
            "Fabrikant": fabrikant
        },
        
        jsonPath = 'servers.json'
        with open(jsonPath, 'r') as jsonBestand:
            data = json.load(jsonBestand)
            data.append(nieuwApparaat)
        with open(jsonPath, 'w') as jsonBestand:
            json.dump(data, jsonBestand, indent=4)
            print("Nieuw object is toegevoegd aan het JSON-bestand.")
            
        tussentijdsAntwoord = input("Wilt u nog apparaten toevoegen? Y/N").upper()
        
        if tussentijdsAntwoord == 'Y':
            nogToeveogen = False 
        elif tussentijdsAntwoord == 'N':
            nogToeveogen = True
    
    json.loads('servers.json')
    

def apparatenVerwijderen():
    print("Apparaat verwijderen")
    apparatenTonen()
    path = 'servers.json'
    keyElement = input("Voer het ip in van het apparaat dat je wilt verwijderen")

    with open(path, 'r') as json_bestand:
        data = json.load(json_bestand)
    if keyElement in data:
        del data[keyElement]
        with open(path, 'w') as json_bestand:
            json.dump(data, json_bestand, indent=4)
            print(f"Dictionary-element met sleutel '{keyElement}' is verwijderd uit het JSON-bestand.")
    else:
        print(f"Dictionary-element met sleutel '{keyElement}' is niet gevonden in het JSON-bestand.")
    

    
    
def apparatenTonen():
    with open('servers.json', 'r') as fp:
        tijdelijk = json.load(fp)
    print(tijdelijk)