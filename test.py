def est_pair(n):
    return n % 2 == 0

print(est_pair(4))
print(est_pair(7))
print(est_pair(10))


def somme_pairs(liste):
    total = 0

    for nombre in liste:
        if nombre % 2 == 0:
            total += nombre

    return total


def compter(mot, lettre):
    total = 0

    for caractere in mot:
        if caractere == lettre:
            total += 1

    return total


for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
        
def maximum(liste):
    maxi = liste[0]

    for nombre in liste:
        if nombre > maxi:
            maxi = nombre

    return maxi

def minimum(liste):
    mini = liste[0]

    for nombre in liste:
        if nombre < mini:
            mini = nombre

    return mini