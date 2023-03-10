n = int(input())
p = input()
a = list(p.split())
maxskok = 0
ilep = 0
for i in a:
    if i == "1":
        ilep += 1
        if maxskok < ilep:
            maxskok = ilep
    else:
        ilep = 0
print(maxskok)