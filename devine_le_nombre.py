import random

def choisir_nombre():
    return random.randint(1, 50)

def demander_nombre():
    while True:
        valeur = input("Votre proposition : ")

        if valeur.isdigit():
            return int(valeur)

        print("Veuillez entrer un nombre.")

def jouer():
    secret = choisir_nombre()
    essais = 0
    max_essais = 7

    while essais < max_essais:
        proposition = demander_nombre()
        essais += 1

        if proposition < secret:
            print("Trop petit")
        elif proposition > secret:
            print("Trop grand")
        else:
            print(f"Gagné en {essais} essai(s) !")
            return

    print("Perdu !")
    print("Le nombre était", secret)

jouer()