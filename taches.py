import json

# Gestionnaire de taches en ligne de commande
taches = []
def sauvegarder():
    with open("taches.json", "w") as f:
        json.dump(taches, f)
        
def charger():
    try:
        with open("taches.json", "r") as f:
            taches.extend(json.load(f))
    except FileNotFoundError :
        pass


def ajouter(titre, faite = False):
    taches.append({"titre":titre, "faite": faite})

def lister():
    numero = 1
    for tache in taches:
        if tache["faite"]:
            etat = "[x]"
        else:
            etat = "[ ]"
        print(numero, tache["titre"], etat)
        numero += 1

def terminer(numero):
    tache_a_finir = taches[numero-1]
    tache_a_finir["faite"] = True
    
def supprimer(numero):
    taches.pop(numero - 1)
    

def menu():
    charger()
    while True:
        print("===========MENU===========")
        print("1.Ajouter")
        print("2.lister")
        print("3.terminer")
        print("4.supprimer tache")
        print("5.Quitter")
        try:
            choix = int(input("enter votre choix : "))
        except ValueError:
            continue
        
        if choix == 1:
            tache = input("entrer votre tache : ")
            ajouter(tache)
            print("Tache ajouter avec succes")
            
        elif choix == 2:
            print("Liste des taches : ")
            lister()
            
        elif choix == 3:
            try:
                num_tache = int(input("Numero de la tache a finir : "))
            except ValueError:
                print("tapez un chiffre")
                continue
            if 0 < num_tache <= len(taches):
                terminer(num_tache)
                print(f"tache {num_tache} terminer")
            else:
                print("entrer un nombre valide")
        elif choix == 4:
            try:
                num_tache = int(input("Numero de la tache a supprimer : "))
            except ValueError:
                print("tapez un chiffre")
                continue
            if 0 < num_tache <= len(taches):
                supprimer(num_tache)
                print(f"tache {num_tache} supprimee avec succes")
            else:
                print("entrer un nombre valide")
        
        elif choix == 5:
            print("Au revoir")
            sauvegarder()
            break
        
        else:
            print("choix invalide reesayer")
       
menu()