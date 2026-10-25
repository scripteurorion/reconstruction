nombre = int(input("entrer un nombre entre 0 et 20 : "))

if nombre > 20:
    print("nombre invalide")
elif nombre <= 20 and nombre >= 10:
    print("Admis")
elif 8 > nombre < 10:
    print("Rattrapage")
else :
    print("refuse")