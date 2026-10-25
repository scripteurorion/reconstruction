import json

def charger():
    try:
        with open ("carnet.json", "r") as carnet:
            return json.load(carnet)
    except FileNotFoundError:
        return []
    finally:
        print("chragement terminer")
        
def sauvegarder():
    with open ("carnet.json", "w") as carnet:
        json.dump(data, carnet, indent=4, ensure_ascii=False)
        
def ajouter():
    nom = input("entrer le nom du contact : ")
    telephone = input("entrer le numero du contact : ")
    data.append({
        "nom": nom,
        "telephone": telephone
    })

    
def lister():
    for i,v in enumerate(data):
        print(i+1 ,":", v["nom"],"-",v["telephone"])

def rechercher():
    nom_rechercher = input("entrer le nom a rechercher : ")
    for i in data:
        if nom_rechercher.lower() == i["nom"].lower():
            print(i)   
            
def supprimer():
    indice = int(input("entrer l'index a supprimer : "))
    if 0 <= indice <= len(data):
        data.pop(indice-1)
    else:
        print("indice invslide")
        
data = charger()
while True:

    print("\n===== MENU =====")
    print("1. Ajouter")
    print("2. Lister")
    print("3. Rechercher")
    print("4. Supprimer")
    print("0. Quitter")

    try:
        choix = int(input("Faites votre choix : "))
    except ValueError:
        print("Veuillez entrer un nombre.")
        continue

    if choix == 1:
        ajouter()

    elif choix == 2:
        lister()

    elif choix == 3:
        rechercher()

    elif choix == 4:
        supprimer()

    elif choix == 0:
        sauvegarder()
        print("Au revoir.")
        break

    else:
        print("Choix invalide.")
    