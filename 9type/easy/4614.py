def odinak(a):
        if a[0] == a[1] and a[1] != a[2] and a[2] != a[3]: return True
        if a[0] != a[1] and a[1] == a[2] and a[2] != a[3]: return True
        if a[0] != a[1] and a[1] != a[2] and a[2] == a[3]: return True
        else:return False
f = open('4614.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[3] < a[0] + a[1] + a[2] and odinak(a):
        k+=1
print(k)    
