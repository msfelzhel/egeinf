f = open('4633.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[0] + a[3] == a[1]+ a[2] and a[3] - a[0] < (a[1] + a[2]) - a[3]:
        k+=1
print(k)
