mot = input("Mot : ")

compteur = 0

for lettre in mot.lower():
    if lettre in "aeiouy":
        compteur += 1

print(compteur)