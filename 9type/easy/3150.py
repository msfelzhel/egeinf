f = open('3150.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a0 = a[0]
    a1 = a[1]
    a2 = a[2]
    if a2*a2 > 2*a0*a1:
        k+=1
print(k)
