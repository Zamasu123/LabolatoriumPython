def silnia_rek(n):
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)
print(silnia_rek(10))