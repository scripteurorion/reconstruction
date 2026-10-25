def moyenne(liste):
    somme = sum(liste)
    moy = somme/liste.__len__()
    return moy
    

liste = [3, 9, 4, 12, 7]

print(moyenne(liste))