f = open('4669.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[3] + a[0] < a[2] + a[1]:
        k+=1
print(k)
