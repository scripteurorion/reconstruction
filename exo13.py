somme = 0
while True:
    i = int(input("entrer le nombre a additionner : "))
    somme += i
    if i == 0:
        print ("fin de l'addition ")
        print(f"la somme est : {somme}")
        break