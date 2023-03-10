a = int(input())
b = input()
c = list(b.split())
e = 1
k = 0
for i in c:
    if int(i) != e:
        k += 1
    else:
        e += 1
print(k)