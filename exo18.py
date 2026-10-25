def table(n):
    for i in range(11):
        print(f"{n} x {i} = {n*i}")
        
def list_table(n):
    liste = []
    for i in range(11):
        li = f"{n} x {i} = {n*i}"
        liste.append(li)
    print(liste)
        
table(7)
list_table(7)