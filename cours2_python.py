# Écrire
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("première ligne\n")
    f.write("deuxième ligne\n")
 
# Ajouter
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("troisième ligne\n")
 
# Lire
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())

import json
 
contacts = [{"nom": "Awa", "tel": "90 00 00 01"}]
 
with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, indent=2, ensure_ascii=False)
 
with open("contacts.json", "r", encoding="utf-8") as f:
    donnees = json.load(f)
print(donnees[0]["nom"])


try:
    n = int(input("Un nombre : "))
    print(10 / n)
except ValueError:
    print("Ce n'est pas un nombre")
except ZeroDivisionError:
    print("Division par zéro impossible")
else:
    print("Tout s'est bien passé")
finally:
    print("Toujours exécuté")
def charger(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []           # premier lancement : pas encore de fichier
    
    
    
# utils.py
def double(x):
    return x * 2

class Contact:
    def __init__(self, nom, telephone):
        self.nom = nom
        self.telephone = telephone
 
    def afficher(self):
        return f"{self.nom} : {self.telephone}"
 
    def to_dict(self):
        return {"nom": self.nom, "telephone": self.telephone}
 
c = Contact("Awa", "90 00 00 01")
print(c.afficher())
print(c.to_dict())

# test_calcul.py
def moyenne(liste):
    return sum(liste) / len(liste)
 
def test_moyenne():
    assert moyenne([10, 20]) == 15
    assert moyenne([5]) == 5

