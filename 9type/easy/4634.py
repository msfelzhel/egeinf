f = open('4634.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[2]*a[2] > a[0] * a[3] and a[0]*a[3] == a[1]*a[2]:
        k+=1
print(k)
