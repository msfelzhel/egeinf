f = open('2929.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if (a[0] + a[2])/2 <= a[1]:
        k+=1
print(k)
