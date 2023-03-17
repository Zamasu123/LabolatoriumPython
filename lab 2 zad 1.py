import random

def dind_min_elem(dane):
    min = dane(0)
    for i in dane:
        if i<min:
            min = i
    return min

def find_poz_min_elem(dane):
    min_poz=0
    for i in range(1, n):
        if dane(i)<dane[min_poz]:
            min_poz=i
        return min_poz



L = []
for i in range(20):
    lista.append(random.randint(10, 50))
print(L)
print("Najmniejszy element listy to: ",find_min_elem(L))
print("Pozycja tego elementu to: ",find_poz_min_elem(L)+1)

print(find_poz_min_elem(L))
print("Najmniejszy element listy to: ",L[poz])
print("Pozycja tego elementu to: ",poz+1)