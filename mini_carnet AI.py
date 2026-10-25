import json


def charger():
    try:
        with open("carnet.json", "r", encoding="utf-8") as carnet:
            return json.load(carnet)

    except FileNotFoundError:
        return []

    finally:
        print("Chargement terminé")


def sauvegarder(data):
    with open("carnet.json", "w", encoding="utf-8") as carnet:
        json.dump(data, carnet, indent=4, ensure_ascii=False)


def ajouter(data):
    nom = input("Entrer le nom du contact : ")
    telephone = input("Entrer le numéro du contact : ")

    data.append({
        "nom": nom,
        "telephone": telephone
    })

    print("Contact ajouté.")


def lister(data):
    if not data:
        print("Aucun contact enregistré.")
        return

    for i, contact in enumerate(data, start=1):
        print(
            f"{i}. {contact['nom']} - {contact['telephone']}"
        )


def rechercher(data):
    nom_recherche = input("Entrer le nom à rechercher : ")

    trouve = False

    for contact in data:
        if nom_recherche.lower() in contact["nom"].lower():
            print(
                f"{contact['nom']} - {contact['telephone']}"
            )
            trouve = True

    if not trouve:
        print("Aucun contact trouvé.")


def supprimer(data):
    if not data:
        print("Aucun contact à supprimer.")
        return

    try:
        indice = int(input("Entrer le numéro du contact à supprimer : "))

        if 0 < indice <= len(data):
            supprime = data.pop(indice - 1)

            print(
                f"Contact supprimé : {supprime['nom']}"
            )
        else:
            print("Indice invalide.")

    except ValueError:
        print("Veuillez entrer un nombre.")


# Chargement des données
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
        ajouter(data)

    elif choix == 2:
        lister(data)

    elif choix == 3:
        rechercher(data)

    elif choix == 4:
        supprimer(data)

    elif choix == 0:
        sauvegarder(data)
        print("Au revoir.")
        break

    else:
        print("Choix invalide.")