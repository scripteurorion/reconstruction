liste = [3,5,7,99,67]
liste.sort()
print(liste[-2])

db_liste = [3,5,7,99,67,3,5,7,99]

print(set(db_liste))

clear_set = []
for n in db_liste:
    if n in clear_set:
        print("existe")
    else:
        clear_set.append(n)
        
print(clear_set)

carre = [n * n for n in range(1, 11) if n % 2 == 0]
print(carre)

eleve = {"nom":"arafat", "age": 22, "notes":[17,18,16,12]}
moy = sum(eleve["notes"])/ len(eleve["notes"])
print(moy)

phrase = "le chat et le chien et le rat"
frequence = {}
for mot in phrase.split():
    frequence[mot] = frequence.get(mot, 0)+1
    
print(frequence)

def majeurs(dic):
    for i in dic:
        if i["age"] >= 18:
            print(i["nom"])
            
personne =  [
    {"nom": "Ali", "age": 20},
    {"nom": "Sara", "age": 16},
    {"nom": "Moussa", "age": 25}
]


majeurs(personne)

with open ("nombre.txt", "w") as f:
    for i in range(1,11):
        f.write(f"{i}\n")
        
with open("nombre.txt", "r") as f:
    somme = 0
    for ligne in f:
        somme += int(ligne.strip())
print("Somme :", somme)
#ia exemple
with open("nombres.txt", "w") as fichier:
    for i in range(1, 11):
        fichier.write(f"{i}\n")
somme = 0
with open("nombres.txt", "r") as fichier:
    for ligne in fichier:
        somme += int(ligne.strip())
print("Somme :", somme)

eleves =  [
    {"nom": "Ali", "age": 20},
    {"nom": "Sara", "age": 16},
    {"nom": "Moussa", "age": 25}
]

import json

with open ("eleves.json", "w") as fichier:
    json.dump(eleves,fichier, indent=2, ensure_ascii=False)
    
with open ("eleves.json", "r") as fichier:
    data = json.load(fichier)
    for i in data:
        print(i)
        
def lire_entier():
    entier = ""
    while True:
        try:
            entier = int(input("taper entier : "))
            print("entier",entier)
            break
        except:
            print("entrer un entier")

class Compte:
    def __init__(self, solde):
        self.solde = solde
    def deposer(self, montant):
        self.solde += montant
    def retirer(self, montant):
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant

c = Compte(100)
c.deposer(50)
print(c.solde)
c.retirer(30)
print(c.solde)


from math_utils import double, carre

print(double(5))
print(carre(5))