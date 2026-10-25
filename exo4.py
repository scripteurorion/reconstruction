nombre1 = int(input("entrer un nombre : "))
nombre2 = int(input("entrer un nombre : "))
nombre3 = int(input("entrer un nombre : "))

nombres = [nombre1, nombre2, nombre3]
n = 0
for i in nombres:
    if i > n:
        n = i
    
print(f"le plus grand est {n}")