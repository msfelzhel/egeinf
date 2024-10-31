f = open('4636.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[3] - a[0] >= 50 and a[2] * a[1] <= 1000:
        k+=1
print(k)
